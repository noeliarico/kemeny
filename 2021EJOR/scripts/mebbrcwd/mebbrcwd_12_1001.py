
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg
from kemeny import sc

rep = 1
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,531,537,494,524,475,513,532,501,515,495,511],
[470,0,523,482,478,489,487,513,500,457,482,491],
[464,478,0,455,459,463,478,483,449,465,449,481],
[507,519,546,0,520,497,550,499,491,501,490,511],
[477,523,542,481,0,457,508,526,477,481,479,514],
[526,512,538,504,544,0,523,513,485,524,509,535],
[488,514,523,451,493,478,0,497,491,495,451,470],
[469,488,518,502,475,488,504,0,470,504,466,495],
[500,501,552,510,524,516,510,531,0,525,488,514],
[486,544,536,500,520,477,506,497,476,0,450,482],
[506,519,552,511,522,492,550,535,513,551,0,526],
[490,510,520,490,487,466,531,506,487,519,475,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 1, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,454,482,453,440,432,439,470,448,458,451,428],
[547,0,484,479,477,437,480,481,490,515,466,478],
[519,517,0,479,440,473,496,498,475,514,463,477],
[548,522,522,0,459,489,516,530,530,511,486,473],
[561,524,561,542,0,460,486,504,535,539,476,491],
[569,564,528,512,541,0,521,517,536,534,499,496],
[562,521,505,485,515,480,0,495,499,495,450,502],
[531,520,503,471,497,484,506,0,521,540,475,494],
[553,511,526,471,466,465,502,480,0,501,467,470],
[543,486,487,490,462,467,506,461,500,0,503,479],
[550,535,538,515,525,502,551,526,534,498,0,499],
[573,523,524,528,510,505,499,507,531,522,502,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 2, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,506,495,493,475,488,496,463,496,507,477,500],
[495,0,489,496,512,502,492,502,485,517,503,486],
[506,512,0,529,510,508,507,520,504,515,497,494],
[508,505,472,0,506,499,475,495,484,485,483,493],
[526,489,491,495,0,503,488,482,502,488,488,482],
[513,499,493,502,498,0,494,477,512,501,503,504],
[505,509,494,526,513,507,0,477,471,515,490,487],
[538,499,481,506,519,524,524,0,498,519,497,504],
[505,516,497,517,499,489,530,503,0,516,514,505],
[494,484,486,516,513,500,486,482,485,0,490,494],
[524,498,504,518,513,498,511,504,487,511,0,496],
[501,515,507,508,519,497,514,497,496,507,505,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 3, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,500,512,486,483,487,486,502,496,480,484,501],
[501,0,526,470,495,488,499,467,477,478,488,479],
[489,475,0,510,478,508,499,503,474,495,458,498],
[515,531,491,0,508,531,520,509,505,520,531,524],
[518,506,523,493,0,511,515,505,521,520,501,510],
[514,513,493,470,490,0,475,461,479,466,481,475],
[515,502,502,481,486,526,0,509,500,511,511,508],
[499,534,498,492,496,540,492,0,522,501,492,501],
[505,524,527,496,480,522,501,479,0,475,482,480],
[521,523,506,481,481,535,490,500,526,0,499,510],
[517,513,543,470,500,520,490,509,519,502,0,493],
[500,522,503,477,491,526,493,500,521,491,508,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 4, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,504,455,415,475,534,628,279,397,433,380,596],
[497,0,422,370,413,525,477,405,396,503,445,451],
[546,579,0,395,511,533,527,364,632,537,453,525],
[586,631,606,0,465,630,543,584,592,489,515,562],
[526,588,490,536,0,576,565,440,448,605,519,634],
[467,476,468,371,425,0,502,405,482,310,410,487],
[373,524,474,458,436,499,0,356,612,545,495,472],
[722,596,637,417,561,596,645,0,666,585,645,531],
[604,605,369,409,553,519,389,335,0,612,456,508],
[568,498,464,512,396,691,456,416,389,0,504,595],
[621,556,548,486,482,591,506,356,545,497,0,590],
[405,550,476,439,367,514,529,470,493,406,411,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 5, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,481,504,526,532,481,537,542,505,535,509,524],
[520,0,492,545,548,477,534,578,505,562,535,542],
[497,509,0,529,561,525,510,553,439,564,518,528],
[475,456,472,0,543,472,494,511,488,549,520,515],
[469,453,440,458,0,441,487,514,429,516,468,488],
[520,524,476,529,560,0,532,575,500,536,533,538],
[464,467,491,507,514,469,0,489,421,490,486,496],
[459,423,448,490,487,426,512,0,428,498,475,468],
[496,496,562,513,572,501,580,573,0,569,554,524],
[466,439,437,452,485,465,511,503,432,0,493,477],
[492,466,483,481,533,468,515,526,447,508,0,477],
[477,459,473,486,513,463,505,533,477,524,524,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 6, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,515,499,525,506,488,505,497,505,496,499,478],
[486,0,495,479,494,481,441,472,497,462,465,497],
[502,506,0,476,496,456,476,488,521,451,504,456],
[476,522,525,0,496,504,502,456,499,492,489,487],
[495,507,505,505,0,505,465,443,457,449,465,504],
[513,520,545,497,496,0,492,491,515,478,538,508],
[496,560,525,499,536,509,0,523,544,481,506,523],
[504,529,513,545,558,510,478,0,508,487,516,515],
[496,504,480,502,544,486,457,493,0,469,481,474],
[505,539,550,509,552,523,520,514,532,0,545,492],
[502,536,497,512,536,463,495,485,520,456,0,507],
[523,504,545,514,497,493,478,486,527,509,494,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 7, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,448,498,481,523,496,503,506,488,491,502,548],
[553,0,508,536,574,517,563,542,492,539,513,569],
[503,493,0,506,504,524,542,500,443,506,509,537],
[520,465,495,0,527,480,491,497,502,470,474,522],
[478,427,497,474,0,469,472,493,459,466,429,483],
[505,484,477,521,532,0,514,492,466,470,478,502],
[498,438,459,510,529,487,0,488,469,475,481,532],
[495,459,501,504,508,509,513,0,469,465,465,519],
[513,509,558,499,542,535,532,532,0,497,518,561],
[510,462,495,531,535,531,526,536,504,0,489,555],
[499,488,492,527,572,523,520,536,483,512,0,546],
[453,432,464,479,518,499,469,482,440,446,455,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 8, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,479,499,492,479,483,505,499,507,477,482,496],
[522,0,512,477,505,485,502,501,530,489,499,509],
[502,489,0,477,492,488,474,463,512,491,482,459],
[509,524,524,0,503,522,520,507,526,500,510,497],
[522,496,509,498,0,515,530,508,512,496,504,508],
[518,516,513,479,486,0,514,463,511,494,490,483],
[496,499,527,481,471,487,0,484,518,490,478,515],
[502,500,538,494,493,538,517,0,519,498,509,485],
[494,471,489,475,489,490,483,482,0,490,483,479],
[524,512,510,501,505,507,511,503,511,0,507,491],
[519,502,519,491,497,511,523,492,518,494,0,494],
[505,492,542,504,493,518,486,516,522,510,507,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 9, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,512,518,514,515,532,505,480,549,513,543,489],
[489,0,513,500,513,516,484,469,530,503,508,492],
[483,488,0,456,503,480,501,495,503,463,528,475],
[487,501,545,0,509,507,482,492,524,503,531,492],
[486,488,498,492,0,496,488,476,514,477,521,456],
[469,485,521,494,505,0,489,470,532,504,511,491],
[496,517,500,519,513,512,0,478,530,492,519,496],
[521,532,506,509,525,531,523,0,540,489,547,522],
[452,471,498,477,487,469,471,461,0,471,517,464],
[488,498,538,498,524,497,509,512,530,0,528,505],
[458,493,473,470,480,490,482,454,484,473,0,488],
[512,509,526,509,545,510,505,479,537,496,513,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 10, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,477,475,451,500,489,501,469,497,486,514,486],
[524,0,496,506,498,513,519,511,520,525,523,497],
[526,505,0,482,510,523,505,508,497,506,523,492],
[550,495,519,0,504,528,514,520,517,520,513,485],
[501,503,491,497,0,495,503,490,478,467,503,462],
[512,488,478,473,506,0,483,474,495,476,498,489],
[500,482,496,487,498,518,0,478,489,469,494,466],
[532,490,493,481,511,527,523,0,508,509,506,496],
[504,481,504,484,523,506,512,493,0,497,514,501],
[515,476,495,481,534,525,532,492,504,0,522,482],
[487,478,478,488,498,503,507,495,487,479,0,469],
[515,504,509,516,539,512,535,505,500,519,532,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 11, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,492,498,559,564,550,532,474,523,566,555,580],
[509,0,520,563,533,559,521,490,505,520,531,539],
[503,481,0,547,534,509,528,507,500,517,526,555],
[442,438,454,0,517,482,488,460,475,515,490,523],
[437,468,467,484,0,484,459,486,481,500,501,503],
[451,442,492,519,517,0,466,487,522,521,493,532],
[469,480,473,513,542,535,0,493,528,544,555,516],
[527,511,494,541,515,514,508,0,489,529,536,529],
[478,496,501,526,520,479,473,512,0,500,534,520],
[435,481,484,486,501,480,457,472,501,0,481,535],
[446,470,475,511,500,508,446,465,467,520,0,520],
[421,462,446,478,498,469,485,472,481,466,481,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 12, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,515,494,583,499,471,476,505,481,471,506,568],
[486,0,477,523,514,531,466,501,491,469,443,542],
[507,524,0,547,466,464,476,472,480,478,474,510],
[418,478,454,0,434,456,433,449,465,413,428,493],
[502,487,535,567,0,499,494,485,482,483,520,528],
[530,470,537,545,502,0,472,497,419,473,498,467],
[525,535,525,568,507,529,0,533,480,508,505,540],
[496,500,529,552,516,504,468,0,493,474,477,550],
[520,510,521,536,519,582,521,508,0,496,500,545],
[530,532,523,588,518,528,493,527,505,0,502,534],
[495,558,527,573,481,503,496,524,501,499,0,557],
[433,459,491,508,473,534,461,451,456,467,444,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 13, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,511,499,498,500,504,489,516,514,498,538,495],
[490,0,490,492,493,522,509,493,501,505,534,496],
[502,511,0,514,476,510,492,500,503,518,521,478],
[503,509,487,0,490,520,496,509,502,521,541,487],
[501,508,525,511,0,526,482,511,492,516,517,499],
[497,479,491,481,475,0,477,501,490,499,524,487],
[512,492,509,505,519,524,0,500,519,539,524,511],
[485,508,501,492,490,500,501,0,480,495,542,495],
[487,500,498,499,509,511,482,521,0,498,533,493],
[503,496,483,480,485,502,462,506,503,0,520,483],
[463,467,480,460,484,477,477,459,468,481,0,469],
[506,505,523,514,502,514,490,506,508,518,532,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 14, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,479,511,501,490,483,511,491,504,476,499,481],
[522,0,509,485,496,490,522,518,511,489,531,473],
[490,492,0,510,497,503,519,513,474,480,515,499],
[500,516,491,0,533,498,525,519,496,513,528,467],
[511,505,504,468,0,493,531,507,509,485,507,504],
[518,511,498,503,508,0,527,504,505,492,535,491],
[490,479,482,476,470,474,0,473,471,477,499,459],
[510,483,488,482,494,497,528,0,510,510,522,480],
[497,490,527,505,492,496,530,491,0,504,526,490],
[525,512,521,488,516,509,524,491,497,0,530,489],
[502,470,486,473,494,466,502,479,475,471,0,463],
[520,528,502,534,497,510,542,521,511,512,538,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 15, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,509,521,495,489,525,539,529,489,495,502,516],
[492,0,510,507,492,555,493,513,490,516,470,523],
[480,491,0,484,496,531,485,523,489,512,494,474],
[506,494,517,0,478,566,508,504,508,499,486,493],
[512,509,505,523,0,560,522,515,519,543,512,497],
[476,446,470,435,441,0,465,498,464,494,459,468],
[462,508,516,493,479,536,0,512,486,517,452,474],
[472,488,478,497,486,503,489,0,467,508,483,462],
[512,511,512,493,482,537,515,534,0,526,523,502],
[506,485,489,502,458,507,484,493,475,0,458,517],
[499,531,507,515,489,542,549,518,478,543,0,521],
[485,478,527,508,504,533,527,539,499,484,480,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 16, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,501,522,506,500,530,524,486,489,507,514,488],
[500,0,485,490,498,502,540,484,506,519,521,488],
[479,516,0,512,517,521,528,487,494,522,525,512],
[495,511,489,0,508,496,536,495,493,509,502,508],
[501,503,484,493,0,498,529,511,500,504,517,533],
[471,499,480,505,503,0,525,477,502,496,511,502],
[477,461,473,465,472,476,0,457,457,488,464,465],
[515,517,514,506,490,524,544,0,529,507,526,516],
[512,495,507,508,501,499,544,472,0,487,502,474],
[494,482,479,492,497,505,513,494,514,0,524,504],
[487,480,476,499,484,490,537,475,499,477,0,495],
[513,513,489,493,468,499,536,485,527,497,506,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 17, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,475,467,533,509,537,509,541,572,540,474,493],
[526,0,458,494,411,384,396,453,583,553,513,583],
[534,543,0,438,481,487,530,488,514,544,417,654],
[468,507,563,0,512,449,533,500,570,612,527,583],
[492,590,520,489,0,524,503,565,606,619,515,575],
[464,617,514,552,477,0,477,523,647,593,534,514],
[492,605,471,468,498,524,0,527,557,581,470,617],
[460,548,513,501,436,478,474,0,595,578,532,536],
[429,418,487,431,395,354,444,406,0,532,450,497],
[461,448,457,389,382,408,420,423,469,0,448,485],
[527,488,584,474,486,467,531,469,551,553,0,615],
[508,418,347,418,426,487,384,465,504,516,386,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 18, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,513,504,503,506,486,496,496,498,514,504,514],
[488,0,503,493,494,495,483,502,490,521,495,520],
[497,498,0,500,512,504,494,498,489,528,500,504],
[498,508,501,0,504,504,504,496,499,527,474,502],
[495,507,489,497,0,495,494,496,511,527,480,495],
[515,506,497,497,506,0,513,499,483,516,502,505],
[505,518,507,497,507,488,0,507,502,544,519,500],
[505,499,503,505,505,502,494,0,519,550,508,506],
[503,511,512,502,490,518,499,482,0,525,509,499],
[487,480,473,474,474,485,457,451,476,0,474,474],
[497,506,501,527,521,499,482,493,492,527,0,496],
[487,481,497,499,506,496,501,495,502,527,505,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 19, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,503,512,519,495,478,518,494,521,493,490,490],
[498,0,516,493,475,486,502,508,508,474,512,503],
[489,485,0,499,468,490,495,501,479,494,485,497],
[482,508,502,0,493,468,495,497,479,483,488,489],
[506,526,533,508,0,503,510,528,520,500,512,507],
[523,515,511,533,498,0,502,534,510,512,518,512],
[483,499,506,506,491,499,0,508,497,470,512,498],
[507,493,500,504,473,467,493,0,482,464,480,486],
[480,493,522,522,481,491,504,519,0,484,502,494],
[508,527,507,518,501,489,531,537,517,0,500,526],
[511,489,516,513,489,483,489,521,499,501,0,496],
[511,498,504,512,494,489,503,515,507,475,505,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 20, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,495,498,536,511,520,513,508,500,553,514,533],
[506,0,505,462,473,487,507,505,499,539,496,494],
[503,496,0,459,471,490,475,484,485,521,467,503],
[465,539,542,0,520,513,515,505,505,536,499,525],
[490,528,530,481,0,486,491,509,493,530,487,517],
[481,514,511,488,515,0,527,500,493,528,494,521],
[488,494,526,486,510,474,0,500,483,525,515,523],
[493,496,517,496,492,501,501,0,515,541,467,501],
[501,502,516,496,508,508,518,486,0,533,502,512],
[448,462,480,465,471,473,476,460,468,0,459,476],
[487,505,534,502,514,507,486,534,499,542,0,508],
[468,507,498,476,484,480,478,500,489,525,493,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 21, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,509,493,501,486,489,516,504,501,506,487,482],
[492,0,483,514,506,503,536,488,485,527,503,494],
[508,518,0,511,496,506,517,522,511,508,525,516],
[500,487,490,0,484,492,494,511,492,499,493,479],
[515,495,505,517,0,506,526,526,503,516,508,535],
[512,498,495,509,495,0,541,510,513,522,522,501],
[485,465,484,507,475,460,0,484,486,472,492,462],
[497,513,479,490,475,491,517,0,492,495,491,483],
[500,516,490,509,498,488,515,509,0,516,495,490],
[495,474,493,502,485,479,529,506,485,0,507,490],
[514,498,476,508,493,479,509,510,506,494,0,498],
[519,507,485,522,466,500,539,518,511,511,503,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 22, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,474,480,527,510,459,502,487,507,524,502,523],
[527,0,500,502,515,464,513,530,507,489,482,531],
[521,501,0,507,540,519,527,493,532,487,518,539],
[474,499,494,0,477,482,522,513,492,508,506,521],
[491,486,461,524,0,454,499,476,495,484,512,550],
[542,537,482,519,547,0,525,509,539,499,486,547],
[499,488,474,479,502,476,0,481,506,502,496,535],
[514,471,508,488,525,492,520,0,510,486,475,527],
[494,494,469,509,506,462,495,491,0,510,482,500],
[477,512,514,493,517,502,499,515,491,0,489,512],
[499,519,483,495,489,515,505,526,519,512,0,553],
[478,470,462,480,451,454,466,474,501,489,448,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 23, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,503,491,506,469,455,522,520,491,491,503,450],
[498,0,513,496,460,447,506,470,501,471,518,470],
[510,488,0,455,501,490,538,475,480,493,494,488],
[495,505,546,0,497,423,533,491,491,525,536,488],
[532,541,500,504,0,505,501,479,512,480,517,520],
[546,554,511,578,496,0,584,553,539,492,558,522],
[479,495,463,468,500,417,0,459,482,486,476,453],
[481,531,526,510,522,448,542,0,537,503,490,536],
[510,500,521,510,489,462,519,464,0,483,499,470],
[510,530,508,476,521,509,515,498,518,0,530,476],
[498,483,507,465,484,443,525,511,502,471,0,469],
[551,531,513,513,481,479,548,465,531,525,532,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 24, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,486,482,505,504,490,515,504,501,506,533,480],
[515,0,476,500,518,488,509,501,483,488,519,502],
[519,525,0,516,518,494,524,504,507,495,525,505],
[496,501,485,0,505,476,498,479,471,489,491,475],
[497,483,483,496,0,497,501,505,506,478,509,470],
[511,513,507,525,504,0,542,516,494,507,540,486],
[486,492,477,503,500,459,0,471,485,484,503,470],
[497,500,497,522,496,485,530,0,480,506,496,492],
[500,518,494,530,495,507,516,521,0,509,523,490],
[495,513,506,512,523,494,517,495,492,0,512,492],
[468,482,476,510,492,461,498,505,478,489,0,468],
[521,499,496,526,531,515,531,509,511,509,533,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 25, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,534,516,510,544,504,508,526,546,531,499,534],
[467,0,456,495,502,519,486,508,496,518,484,503],
[485,545,0,537,529,486,524,515,491,515,511,513],
[491,506,464,0,511,480,477,525,460,496,470,513],
[457,499,472,490,0,481,483,483,501,495,501,462],
[497,482,515,521,520,0,462,499,501,525,489,476],
[493,515,477,524,518,539,0,509,518,526,491,511],
[475,493,486,476,518,502,492,0,470,479,465,495],
[455,505,510,541,500,500,483,531,0,516,431,497],
[470,483,486,505,506,476,475,522,485,0,525,516],
[502,517,490,531,500,512,510,536,570,476,0,554],
[467,498,488,488,539,525,490,506,504,485,447,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 26, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,481,509,537,504,482,557,462,483,531,532,508],
[520,0,501,508,514,467,511,484,464,525,501,485],
[492,500,0,508,516,505,549,511,451,473,532,483],
[464,493,493,0,489,499,519,490,493,503,525,496],
[497,487,485,512,0,488,532,480,495,520,495,490],
[519,534,496,502,513,0,530,496,476,497,531,509],
[444,490,452,482,469,471,0,455,424,468,484,461],
[539,517,490,511,521,505,546,0,515,532,517,517],
[518,537,550,508,506,525,577,486,0,544,541,511],
[470,476,528,498,481,504,533,469,457,0,492,471],
[469,500,469,476,506,470,517,484,460,509,0,505],
[493,516,518,505,511,492,540,484,490,530,496,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 27, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,432,530,446,528,444,536,438,489,563,465,571],
[569,0,584,507,525,437,487,564,515,576,489,558],
[471,417,0,539,508,468,468,436,423,596,538,561],
[555,494,462,0,479,470,545,476,450,586,489,549],
[473,476,493,522,0,530,476,480,459,599,512,604],
[557,564,533,531,471,0,528,465,515,568,479,512],
[465,514,533,456,525,473,0,490,465,615,428,594],
[563,437,565,525,521,536,511,0,553,598,530,543],
[512,486,578,551,542,486,536,448,0,650,567,522],
[438,425,405,415,402,433,386,403,351,0,446,454],
[536,512,463,512,489,522,573,471,434,555,0,527],
[430,443,440,452,397,489,407,458,479,547,474,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 28, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,609,512,504,730,662,520,585,567,539,470,640],
[392,0,462,374,558,566,449,492,587,413,328,463],
[489,539,0,432,585,576,571,643,682,443,542,560],
[497,627,569,0,582,658,601,706,765,563,452,549],
[271,443,416,419,0,434,359,406,597,244,312,337],
[339,435,425,343,567,0,523,359,488,406,402,339],
[481,552,430,400,642,478,0,549,483,475,330,453],
[416,509,358,295,595,642,452,0,331,495,287,430],
[434,414,319,236,404,513,518,670,0,384,214,563],
[462,588,558,438,757,595,526,506,617,0,555,639],
[531,673,459,549,689,599,671,714,787,446,0,685],
[361,538,441,452,664,662,548,571,438,362,316,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 29, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,492,499,493,481,485,512,514,508,485,502,510],
[509,0,481,480,528,511,512,533,522,523,516,502],
[502,520,0,500,509,508,510,516,541,528,511,498],
[508,521,501,0,500,472,483,522,518,512,526,520],
[520,473,492,501,0,508,511,547,510,501,515,505],
[516,490,493,529,493,0,506,485,510,509,478,512],
[489,489,491,518,490,495,0,516,511,517,506,497],
[487,468,485,479,454,516,485,0,517,468,496,447],
[493,479,460,483,491,491,490,484,0,475,477,481],
[516,478,473,489,500,492,484,533,526,0,499,502],
[499,485,490,475,486,523,495,505,524,502,0,501],
[491,499,503,481,496,489,504,554,520,499,500,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 30, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,508,515,517,510,513,497,500,507,479,514,497],
[493,0,497,483,495,481,494,485,477,484,500,476],
[486,504,0,500,506,468,492,464,491,460,491,487],
[484,518,501,0,510,474,496,500,496,473,495,485],
[491,506,495,491,0,450,513,497,486,454,490,466],
[488,520,533,527,551,0,528,529,520,515,531,506],
[504,507,509,505,488,473,0,513,498,453,495,492],
[501,516,537,501,504,472,488,0,522,512,492,495],
[494,524,510,505,515,481,503,479,0,500,505,483],
[522,517,541,528,547,486,548,489,501,0,515,520],
[487,501,510,506,511,470,506,509,496,486,0,478],
[504,525,514,516,535,495,509,506,518,481,523,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 31, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,514,477,552,539,553,470,565,526,532,523,521],
[487,0,487,508,481,510,461,547,499,472,471,473],
[524,514,0,535,512,554,488,581,570,532,516,528],
[449,493,466,0,496,499,469,514,538,474,469,526],
[462,520,489,505,0,522,501,530,549,504,509,486],
[448,491,447,502,479,0,447,523,534,471,453,462],
[531,540,513,532,500,554,0,568,568,548,523,497],
[436,454,420,487,471,478,433,0,488,482,460,462],
[475,502,431,463,452,467,433,513,0,459,461,470],
[469,529,469,527,497,530,453,519,542,0,479,508],
[478,530,485,532,492,548,478,541,540,522,0,496],
[480,528,473,475,515,539,504,539,531,493,505,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 32, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,522,487,514,528,494,535,467,544,502,506,508],
[479,0,483,511,506,511,511,524,525,495,511,498],
[514,518,0,530,499,552,519,525,584,454,530,551],
[487,490,471,0,522,509,500,497,544,502,484,516],
[473,495,502,479,0,485,508,458,547,460,495,503],
[507,490,449,492,516,0,513,484,532,481,492,490],
[466,490,482,501,493,488,0,496,538,515,497,517],
[534,477,476,504,543,517,505,0,551,511,504,495],
[457,476,417,457,454,469,463,450,0,483,465,476],
[499,506,547,499,541,520,486,490,518,0,517,504],
[495,490,471,517,506,509,504,497,536,484,0,506],
[493,503,450,485,498,511,484,506,525,497,495,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 33, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,552,543,567,555,526,586,531,539,541,556,499],
[449,0,511,526,484,445,536,502,492,497,490,536],
[458,490,0,513,512,482,527,471,470,509,535,506],
[434,475,488,0,489,496,501,517,480,521,503,541],
[446,517,489,512,0,482,511,471,488,520,507,497],
[475,556,519,505,519,0,530,517,494,534,491,557],
[415,465,474,500,490,471,0,511,469,471,449,476],
[470,499,530,484,530,484,490,0,497,509,526,523],
[462,509,531,521,513,507,532,504,0,538,554,524],
[460,504,492,480,481,467,530,492,463,0,463,511],
[445,511,466,498,494,510,552,475,447,538,0,509],
[502,465,495,460,504,444,525,478,477,490,492,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 34, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,495,538,539,550,517,527,503,533,541,472,496],
[506,0,525,522,500,551,560,463,501,530,517,451],
[463,476,0,486,513,498,486,455,449,539,431,472],
[462,479,515,0,474,471,524,483,510,536,475,484],
[451,501,488,527,0,476,472,446,518,576,529,499],
[484,450,503,530,525,0,514,488,516,503,489,444],
[474,441,515,477,529,487,0,481,502,502,455,492],
[498,538,546,518,555,513,520,0,473,542,465,533],
[468,500,552,491,483,485,499,528,0,520,529,471],
[460,471,462,465,425,498,499,459,481,0,478,481],
[529,484,570,526,472,512,546,536,472,523,0,498],
[505,550,529,517,502,557,509,468,530,520,503,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 35, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,486,476,505,502,477,522,506,487,485,517,490],
[515,0,492,548,504,496,532,538,508,526,507,504],
[525,509,0,537,516,483,558,516,496,520,520,505],
[496,453,464,0,512,471,509,491,453,487,475,485],
[499,497,485,489,0,471,521,499,486,511,493,457],
[524,505,518,530,530,0,551,538,537,506,517,499],
[479,469,443,492,480,450,0,489,477,484,470,461],
[495,463,485,510,502,463,512,0,473,476,489,479],
[514,493,505,548,515,464,524,528,0,523,526,481],
[516,475,481,514,490,495,517,525,478,0,488,489],
[484,494,481,526,508,484,531,512,475,513,0,496],
[511,497,496,516,544,502,540,522,520,512,505,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 36, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,536,497,523,533,561,478,556,533,568,467,511],
[465,0,474,507,473,524,519,472,488,501,482,500],
[504,527,0,553,531,511,491,529,561,528,547,511],
[478,494,448,0,478,477,476,472,494,519,504,449],
[468,528,470,523,0,526,504,505,540,547,539,489],
[440,477,490,524,475,0,445,472,527,503,502,469],
[523,482,510,525,497,556,0,498,491,527,520,527],
[445,529,472,529,496,529,503,0,534,532,496,507],
[468,513,440,507,461,474,510,467,0,510,500,463],
[433,500,473,482,454,498,474,469,491,0,487,468],
[534,519,454,497,462,499,481,505,501,514,0,496],
[490,501,490,552,512,532,474,494,538,533,505,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 37, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,450,613,520,538,585,434,566,627,498,489,535],
[551,0,543,468,664,585,528,593,641,463,441,477],
[388,458,0,529,515,473,490,556,602,430,431,474],
[481,533,472,0,507,581,429,543,743,431,390,468],
[463,337,486,494,0,586,350,424,614,537,485,539],
[416,416,528,420,415,0,368,401,529,460,257,509],
[567,473,511,572,651,633,0,605,674,489,609,627],
[435,408,445,458,577,600,396,0,602,492,401,336],
[374,360,399,258,387,472,327,399,0,290,322,421],
[503,538,571,570,464,541,512,509,711,0,417,441],
[512,560,570,611,516,744,392,600,679,584,0,605],
[466,524,527,533,462,492,374,665,580,560,396,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 38, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,416,539,438,477,566,362,535,501,488,372,523],
[585,0,504,524,569,512,521,599,522,459,527,552],
[462,497,0,453,419,557,417,455,537,418,422,511],
[563,477,548,0,644,529,449,495,531,497,545,527],
[524,432,582,357,0,549,471,524,521,482,579,541],
[435,489,444,472,452,0,413,458,462,421,440,512],
[639,480,584,552,530,588,0,569,537,560,485,622],
[466,402,546,506,477,543,432,0,488,436,487,546],
[500,479,464,470,480,539,464,513,0,486,461,533],
[513,542,583,504,519,580,441,565,515,0,525,628],
[629,474,579,456,422,561,516,514,540,476,0,548],
[478,449,490,474,460,489,379,455,468,373,453,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 39, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,460,526,501,459,502,505,515,507,480,501,474],
[541,0,511,533,486,496,498,512,504,489,517,500],
[475,490,0,507,464,491,528,475,483,453,503,476],
[500,468,494,0,448,472,496,462,472,439,452,462],
[542,515,537,553,0,531,561,526,538,537,536,498],
[499,505,510,529,470,0,472,486,503,496,480,488],
[496,503,473,505,440,529,0,470,466,470,459,509],
[486,489,526,539,475,515,531,0,489,466,497,488],
[494,497,518,529,463,498,535,512,0,472,498,500],
[521,512,548,562,464,505,531,535,529,0,525,530],
[500,484,498,549,465,521,542,504,503,476,0,463],
[527,501,525,539,503,513,492,513,501,471,538,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 40, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,509,470,452,491,481,491,513,460,466,485,474],
[492,0,489,453,509,480,492,523,462,471,471,487],
[531,512,0,462,517,496,484,502,497,484,489,499],
[549,548,539,0,529,525,516,524,506,496,530,513],
[510,492,484,472,0,495,485,507,489,483,481,478],
[520,521,505,476,506,0,492,521,488,483,512,475],
[510,509,517,485,516,509,0,522,486,527,527,510],
[488,478,499,477,494,480,479,0,449,475,507,462],
[541,539,504,495,512,513,515,552,0,507,522,500],
[535,530,517,505,518,518,474,526,494,0,502,505],
[516,530,512,471,520,489,474,494,479,499,0,507],
[527,514,502,488,523,526,491,539,501,496,494,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 41, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,453,532,537,495,511,472,453,491,484,428,508],
[548,0,536,484,495,496,486,454,544,517,500,543],
[469,465,0,478,479,471,515,452,504,493,490,479],
[464,517,523,0,519,540,473,458,497,472,472,487],
[506,506,522,482,0,495,483,507,484,483,452,458],
[490,505,530,461,506,0,510,473,506,476,454,475],
[529,515,486,528,518,491,0,485,522,510,508,494],
[548,547,549,543,494,528,516,0,552,562,542,544],
[510,457,497,504,517,495,479,449,0,512,454,481],
[517,484,508,529,518,525,491,439,489,0,483,482],
[573,501,511,529,549,547,493,459,547,518,0,495],
[493,458,522,514,543,526,507,457,520,519,506,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 42, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,524,516,530,518,520,539,499,524,526,528,514],
[477,0,469,499,521,484,493,508,526,494,488,486],
[485,532,0,536,516,454,506,499,508,513,499,512],
[471,502,465,0,483,470,461,511,470,472,463,452],
[483,480,485,518,0,489,483,515,518,477,497,490],
[481,517,547,531,512,0,484,474,513,496,501,507],
[462,508,495,540,518,517,0,513,510,505,538,536],
[502,493,502,490,486,527,488,0,541,484,529,488],
[477,475,493,531,483,488,491,460,0,481,504,474],
[475,507,488,529,524,505,496,517,520,0,509,503],
[473,513,502,538,504,500,463,472,497,492,0,467],
[487,515,489,549,511,494,465,513,527,498,534,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 43, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,288,188,254,121,357,298,121,220,535,358,121],
[713,0,391,536,613,613,580,233,646,647,503,476],
[813,610,0,743,513,613,480,577,743,646,710,573],
[747,465,258,0,447,683,480,577,813,380,467,474],
[880,388,488,554,0,487,468,251,554,665,554,451],
[644,388,388,318,514,0,347,267,533,665,367,695],
[703,421,521,521,533,654,0,396,566,554,400,484],
[880,768,424,424,750,734,605,0,810,634,303,831],
[781,355,258,188,447,468,435,191,0,535,237,595],
[466,354,355,621,336,336,447,367,466,0,670,484],
[643,498,291,534,447,634,601,698,764,331,0,628],
[880,525,428,527,550,306,517,170,406,517,373,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 44, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,453,497,479,474,507,492,452,464,497,508,488],
[548,0,540,536,496,535,522,519,512,526,523,507],
[504,461,0,478,444,511,469,464,470,484,478,454],
[522,465,523,0,470,512,508,472,476,494,502,484],
[527,505,557,531,0,519,511,492,509,513,531,502],
[494,466,490,489,482,0,470,467,481,488,478,471],
[509,479,532,493,490,531,0,488,488,499,501,494],
[549,482,537,529,509,534,513,0,524,523,532,514],
[537,489,531,525,492,520,513,477,0,491,516,509],
[504,475,517,507,488,513,502,478,510,0,492,497],
[493,478,523,499,470,523,500,469,485,509,0,475],
[513,494,547,517,499,530,507,487,492,504,526,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 45, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,489,510,499,516,480,501,465,512,526,491,509],
[512,0,517,526,513,511,522,489,532,520,532,511],
[491,484,0,496,491,513,482,485,495,490,484,483],
[502,475,505,0,498,501,527,496,531,503,508,501],
[485,488,510,503,0,508,514,508,532,509,495,510],
[521,490,488,500,493,0,529,502,513,524,520,491],
[500,479,519,474,487,472,0,491,516,512,501,502],
[536,512,516,505,493,499,510,0,506,526,513,502],
[489,469,506,470,469,488,485,495,0,515,500,502],
[475,481,511,498,492,477,489,475,486,0,484,483],
[510,469,517,493,506,481,500,488,501,517,0,502],
[492,490,518,500,491,510,499,499,499,518,499,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 46, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,499,516,527,486,493,513,519,546,488,531,520],
[502,0,493,503,495,468,513,484,538,526,529,531],
[485,508,0,519,496,513,533,525,534,520,522,526],
[474,498,482,0,480,491,493,494,520,509,512,508],
[515,506,505,521,0,460,509,525,503,490,503,529],
[508,533,488,510,541,0,533,521,556,526,536,535],
[488,488,468,508,492,468,0,512,515,486,530,508],
[482,517,476,507,476,480,489,0,502,510,528,502],
[455,463,467,481,498,445,486,499,0,494,518,493],
[513,475,481,492,511,475,515,491,507,0,497,493],
[470,472,479,489,498,465,471,473,483,504,0,500],
[481,470,475,493,472,466,493,499,508,508,501,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 47, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,507,527,481,506,506,516,504,522,520,540,514],
[494,0,521,491,482,475,503,486,493,488,536,520],
[474,480,0,476,476,460,472,473,494,487,490,486],
[520,510,525,0,539,511,526,485,522,502,509,526],
[495,519,525,462,0,499,524,487,499,483,520,525],
[495,526,541,490,502,0,527,514,518,526,541,516],
[485,498,529,475,477,474,0,462,518,487,548,502],
[497,515,528,516,514,487,539,0,514,520,521,500],
[479,508,507,479,502,483,483,487,0,491,532,511],
[481,513,514,499,518,475,514,481,510,0,525,512],
[461,465,511,492,481,460,453,480,469,476,0,483],
[487,481,515,475,476,485,499,501,490,489,518,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 48, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,513,495,490,503,505,498,491,524,500,489,474],
[488,0,476,487,476,525,486,459,502,481,484,480],
[506,525,0,516,502,522,518,514,519,487,486,498],
[511,514,485,0,502,544,506,474,501,501,479,516],
[498,525,499,499,0,520,477,475,493,496,471,477],
[496,476,479,457,481,0,470,464,514,454,488,463],
[503,515,483,495,524,531,0,482,503,494,515,500],
[510,542,487,527,526,537,519,0,537,497,517,532],
[477,499,482,500,508,487,498,464,0,476,495,494],
[501,520,514,500,505,547,507,504,525,0,507,491],
[512,517,515,522,530,513,486,484,506,494,0,503],
[527,521,503,485,524,538,501,469,507,510,498,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 49, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,558,554,544,524,580,485,530,506,536,544,528],
[443,0,495,417,468,488,469,455,443,506,472,481],
[447,506,0,425,463,448,436,452,376,446,440,403],
[457,584,576,0,533,550,519,478,451,541,506,483],
[477,533,538,468,0,507,501,499,482,520,524,452],
[421,513,553,451,494,0,455,438,452,472,490,499],
[516,532,565,482,500,546,0,542,481,525,519,573],
[471,546,549,523,502,563,459,0,490,510,512,496],
[495,558,625,550,519,549,520,511,0,523,567,521],
[465,495,555,460,481,529,476,491,478,0,495,486],
[457,529,561,495,477,511,482,489,434,506,0,457],
[473,520,598,518,549,502,428,505,480,515,544,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 50, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,533,497,517,495,545,480,498,509,499,534,484],
[468,0,490,490,475,523,478,467,461,504,487,505],
[504,511,0,543,527,534,511,502,469,548,535,512],
[484,511,458,0,489,482,458,481,479,494,499,449],
[506,526,474,512,0,571,498,513,491,530,518,479],
[456,478,467,519,430,0,491,490,470,484,532,528],
[521,523,490,543,503,510,0,491,498,529,523,503],
[503,534,499,520,488,511,510,0,511,515,537,511],
[492,540,532,522,510,531,503,490,0,528,526,489],
[502,497,453,507,471,517,472,486,473,0,481,495],
[467,514,466,502,483,469,478,464,475,520,0,459],
[517,496,489,552,522,473,498,490,512,506,542,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 51, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,574,435,462,511,484,468,394,580,553,508,507],
[427,0,411,423,501,447,460,461,520,552,416,441],
[566,590,0,486,497,568,589,571,518,595,475,455],
[539,578,515,0,556,526,622,554,517,595,456,487],
[490,500,504,445,0,479,527,474,524,525,349,419],
[517,554,433,475,522,0,596,483,592,531,498,437],
[533,541,412,379,474,405,0,530,495,490,375,455],
[607,540,430,447,527,518,471,0,599,677,498,506],
[421,481,483,484,477,409,506,402,0,512,492,498],
[448,449,406,406,476,470,511,324,489,0,412,396],
[493,585,526,545,652,503,626,503,509,589,0,411],
[494,560,546,514,582,564,546,495,503,605,590,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 52, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,502,515,506,512,524,535,500,504,527,470,515],
[499,0,505,491,517,519,533,507,543,499,473,474],
[486,496,0,475,499,495,492,500,540,495,453,484],
[495,510,526,0,510,481,525,508,510,516,506,505],
[489,484,502,491,0,490,494,474,498,502,459,491],
[477,482,506,520,511,0,507,489,482,508,463,491],
[466,468,509,476,507,494,0,501,500,490,477,493],
[501,494,501,493,527,512,500,0,515,511,486,495],
[497,458,461,491,503,519,501,486,0,503,474,481],
[474,502,506,485,499,493,511,490,498,0,512,471],
[531,528,548,495,542,538,524,515,527,489,0,505],
[486,527,517,496,510,510,508,506,520,530,496,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 53, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,504,513,473,496,512,498,495,520,513,490,499],
[497,0,488,501,513,518,506,477,493,495,506,518],
[488,513,0,498,505,534,503,483,495,512,482,474],
[528,500,503,0,507,503,503,518,527,502,516,517],
[505,488,496,494,0,522,496,488,499,490,491,504],
[489,483,467,498,479,0,462,468,494,476,479,468],
[503,495,498,498,505,539,0,506,502,506,513,527],
[506,524,518,483,513,533,495,0,506,490,514,520],
[481,508,506,474,502,507,499,495,0,484,502,502],
[488,506,489,499,511,525,495,511,517,0,496,500],
[511,495,519,485,510,522,488,487,499,505,0,514],
[502,483,527,484,497,533,474,481,499,501,487,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 54, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,515,478,479,457,484,505,521,470,514,467,448],
[486,0,469,472,442,487,498,489,459,454,474,464],
[523,532,0,510,473,503,519,525,463,507,505,482],
[522,529,491,0,481,513,505,491,458,478,497,491],
[544,559,528,520,0,532,549,531,529,495,511,498],
[517,514,498,488,469,0,525,480,469,478,480,477],
[496,503,482,496,452,476,0,511,444,509,465,477],
[480,512,476,510,470,521,490,0,475,486,465,479],
[531,542,538,543,472,532,557,526,0,501,520,500],
[487,547,494,523,506,523,492,515,500,0,502,512],
[534,527,496,504,490,521,536,536,481,499,0,505],
[553,537,519,510,503,524,524,522,501,489,496,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 55, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,446,526,513,464,456,540,454,582,473,549,453],
[555,0,544,542,507,487,479,478,485,429,455,540],
[475,457,0,462,462,413,420,458,421,336,438,511],
[488,459,539,0,475,407,462,491,463,471,454,506],
[537,494,539,526,0,354,488,437,455,481,466,491],
[545,514,588,594,647,0,456,503,570,494,507,546],
[461,522,581,539,513,545,0,467,475,501,411,556],
[547,523,543,510,564,498,534,0,528,489,507,498],
[419,516,580,538,546,431,526,473,0,421,375,467],
[528,572,665,530,520,507,500,512,580,0,526,628],
[452,546,563,547,535,494,590,494,626,475,0,534],
[548,461,490,495,510,455,445,503,534,373,467,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 56, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,535,516,504,525,509,516,481,506,500,541,505],
[466,0,501,469,489,466,472,450,462,486,507,478],
[485,500,0,497,488,467,480,474,483,501,499,494],
[497,532,504,0,499,476,498,491,489,473,499,504],
[476,512,513,502,0,448,488,458,466,468,500,508],
[492,535,534,525,553,0,514,520,520,508,539,502],
[485,529,521,503,513,487,0,454,482,466,524,509],
[520,551,527,510,543,481,547,0,509,492,524,528],
[495,539,518,512,535,481,519,492,0,532,511,503],
[501,515,500,528,533,493,535,509,469,0,509,508],
[460,494,502,502,501,462,477,477,490,492,0,494],
[496,523,507,497,493,499,492,473,498,493,507,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 57, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,485,479,507,491,477,463,454,449,515,528,476],
[516,0,518,519,508,513,476,526,452,533,536,553],
[522,483,0,552,472,527,471,502,475,528,534,471],
[494,482,449,0,469,472,490,481,475,513,520,492],
[510,493,529,532,0,520,494,490,472,524,534,467],
[524,488,474,529,481,0,520,524,473,531,537,520],
[538,525,530,511,507,481,0,528,481,516,565,547],
[547,475,499,520,511,477,473,0,511,526,550,491],
[552,549,526,526,529,528,520,490,0,546,522,508],
[486,468,473,488,477,470,485,475,455,0,474,437],
[473,465,467,481,467,464,436,451,479,527,0,490],
[525,448,530,509,534,481,454,510,493,564,511,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 58, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,509,538,491,501,499,481,516,483,515,494,513],
[492,0,501,487,491,518,487,510,489,497,483,490],
[463,500,0,503,501,483,480,526,497,500,503,494],
[510,514,498,0,519,485,488,529,483,506,494,473],
[500,510,500,482,0,488,489,516,487,501,520,484],
[502,483,518,516,513,0,484,499,493,497,487,498],
[520,514,521,513,512,517,0,538,502,504,512,496],
[485,491,475,472,485,502,463,0,487,485,471,474],
[518,512,504,518,514,508,499,514,0,519,498,498],
[486,504,501,495,500,504,497,516,482,0,486,494],
[507,518,498,507,481,514,489,530,503,515,0,497],
[488,511,507,528,517,503,505,527,503,507,504,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 59, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,505,464,523,522,514,520,520,508,534,490,510],
[496,0,485,502,508,498,486,510,502,510,495,525],
[537,516,0,512,537,519,499,522,505,551,522,535],
[478,499,489,0,504,482,492,510,489,499,487,515],
[479,493,464,497,0,491,498,511,467,516,492,508],
[487,503,482,519,510,0,485,516,482,492,471,516],
[481,515,502,509,503,516,0,533,494,509,499,526],
[481,491,479,491,490,485,468,0,480,494,484,501],
[493,499,496,512,534,519,507,521,0,505,505,519],
[467,491,450,502,485,509,492,507,496,0,471,505],
[511,506,479,514,509,530,502,517,496,530,0,519],
[491,476,466,486,493,485,475,500,482,496,482,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 60, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,488,522,543,545,558,554,555,465,507,611,549],
[513,0,535,561,569,587,498,541,513,531,578,518],
[479,466,0,545,536,543,515,554,528,526,599,539],
[458,440,456,0,501,488,494,508,412,449,551,382],
[456,432,465,500,0,482,427,478,430,423,544,371],
[443,414,458,513,519,0,489,454,447,450,506,464],
[447,503,486,507,574,512,0,513,493,509,597,451],
[446,460,447,493,523,547,488,0,430,483,563,424],
[536,488,473,589,571,554,508,571,0,492,568,514],
[494,470,475,552,578,551,492,518,509,0,617,505],
[390,423,402,450,457,495,404,438,433,384,0,389],
[452,483,462,619,630,537,550,577,487,496,612,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 61, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,521,497,513,517,533,482,513,538,497,524,491],
[480,0,496,505,529,512,504,509,505,486,515,494],
[504,505,0,493,505,502,479,515,485,492,510,493],
[488,496,508,0,501,509,492,522,513,514,526,494],
[484,472,496,500,0,497,480,519,498,492,525,485],
[468,489,499,492,504,0,478,504,501,492,520,509],
[519,497,522,509,521,523,0,540,530,506,533,502],
[488,492,486,479,482,497,461,0,488,499,504,462],
[463,496,516,488,503,500,471,513,0,484,513,487],
[504,515,509,487,509,509,495,502,517,0,523,489],
[477,486,491,475,476,481,468,497,488,478,0,477],
[510,507,508,507,516,492,499,539,514,512,524,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 62, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,537,488,498,532,517,506,502,509,513,531,527],
[464,0,498,524,514,485,499,475,506,474,521,478],
[513,503,0,533,520,509,534,498,529,525,563,523],
[503,477,468,0,500,497,482,498,500,495,520,512],
[469,487,481,501,0,484,483,478,486,475,527,514],
[484,516,492,504,517,0,526,513,506,493,542,505],
[495,502,467,519,518,475,0,504,501,508,544,504],
[499,526,503,503,523,488,497,0,480,471,501,505],
[492,495,472,501,515,495,500,521,0,530,523,511],
[488,527,476,506,526,508,493,530,471,0,544,461],
[470,480,438,481,474,459,457,500,478,457,0,509],
[474,523,478,489,487,496,497,496,490,540,492,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 63, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,517,514,516,503,526,486,490,486,493,514,536],
[484,0,461,502,470,505,490,509,456,467,509,483],
[487,540,0,492,504,505,526,485,463,505,529,493],
[485,499,509,0,521,490,529,477,515,491,525,501],
[498,531,497,480,0,474,468,464,480,472,482,462],
[475,496,496,511,527,0,495,486,480,500,510,509],
[515,511,475,472,533,506,0,506,447,471,503,485],
[511,492,516,524,537,515,495,0,501,483,510,515],
[515,545,538,486,521,521,554,500,0,510,515,523],
[508,534,496,510,529,501,530,518,491,0,528,515],
[487,492,472,476,519,491,498,491,486,473,0,479],
[465,518,508,500,539,492,516,486,478,486,522,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 64, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,466,516,488,605,471,493,441,515,492,453,465],
[535,0,520,499,609,496,514,454,570,477,519,493],
[485,481,0,448,510,463,435,451,494,443,447,505],
[513,502,553,0,566,472,463,454,552,433,480,448],
[396,392,491,435,0,410,435,396,482,365,428,419],
[530,505,538,529,591,0,539,471,582,488,413,523],
[508,487,566,538,566,462,0,504,560,473,468,510],
[560,547,550,547,605,530,497,0,533,485,521,514],
[486,431,507,449,519,419,441,468,0,458,479,431],
[509,524,558,568,636,513,528,516,543,0,489,508],
[548,482,554,521,573,588,533,480,522,512,0,528],
[536,508,496,553,582,478,491,487,570,493,473,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 65, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,498,476,487,587,508,518,501,508,523,548,550],
[503,0,511,498,553,513,482,502,473,552,583,519],
[525,490,0,474,484,428,513,499,555,476,526,476],
[514,503,527,0,503,500,506,518,458,525,610,511],
[414,448,517,498,0,514,535,485,497,558,585,519],
[493,488,573,501,487,0,539,515,445,445,553,484],
[483,519,488,495,466,462,0,452,450,471,540,485],
[500,499,502,483,516,486,549,0,443,525,557,530],
[493,528,446,543,504,556,551,558,0,503,568,571],
[478,449,525,476,443,556,530,476,498,0,572,453],
[453,418,475,391,416,448,461,444,433,429,0,465],
[451,482,525,490,482,517,516,471,430,548,536,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 66, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,523,505,526,481,529,504,499,491,514,514,519],
[478,0,489,477,473,479,488,460,448,492,484,467],
[496,512,0,487,466,495,503,480,468,487,470,448],
[475,524,514,0,490,527,496,511,491,497,493,515],
[520,528,535,511,0,499,538,508,509,535,466,531],
[472,522,506,474,502,0,506,487,472,504,480,471],
[497,513,498,505,463,495,0,465,503,523,513,508],
[502,541,521,490,493,514,536,0,489,520,508,520],
[510,553,533,510,492,529,498,512,0,543,521,515],
[487,509,514,504,466,497,478,481,458,0,502,500],
[487,517,531,508,535,521,488,493,480,499,0,504],
[482,534,553,486,470,530,493,481,486,501,497,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 67, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,474,495,498,518,490,517,504,506,494,529,501],
[527,0,509,504,506,492,490,513,512,491,521,503],
[506,492,0,496,510,486,498,526,515,496,528,497],
[503,497,505,0,521,504,519,522,535,522,531,494],
[483,495,491,480,0,473,501,510,490,479,514,461],
[511,509,515,497,528,0,501,526,539,509,543,505],
[484,511,503,482,500,500,0,499,514,487,522,514],
[497,488,475,479,491,475,502,0,494,495,507,498],
[495,489,486,466,511,462,487,507,0,472,521,497],
[507,510,505,479,522,492,514,506,529,0,523,495],
[472,480,473,470,487,458,479,494,480,478,0,468],
[500,498,504,507,540,496,487,503,504,506,533,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 68, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,502,516,534,541,482,430,559,501,456,528,513],
[499,0,455,452,462,504,439,475,493,436,466,481],
[485,546,0,537,534,507,585,510,542,508,520,499],
[467,549,464,0,468,500,539,510,496,480,541,448],
[460,539,467,533,0,458,517,531,483,467,568,519],
[519,497,494,501,543,0,539,514,514,464,534,520],
[571,562,416,462,484,462,0,498,469,527,493,514],
[442,526,491,491,470,487,503,0,489,502,520,445],
[500,508,459,505,518,487,532,512,0,476,489,500],
[545,565,493,521,534,537,474,499,525,0,540,515],
[473,535,481,460,433,467,508,481,512,461,0,417],
[488,520,502,553,482,481,487,556,501,486,584,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 69, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,519,498,507,503,502,500,499,534,529,484,483],
[482,0,500,479,486,474,493,487,495,499,489,482],
[503,501,0,493,487,477,517,487,496,519,489,491],
[494,522,508,0,490,505,509,497,517,500,490,510],
[498,515,514,511,0,511,526,512,510,499,498,494],
[499,527,524,496,490,0,520,506,524,518,497,484],
[501,508,484,492,475,481,0,472,492,497,461,461],
[502,514,514,504,489,495,529,0,510,520,506,480],
[467,506,505,484,491,477,509,491,0,515,489,494],
[472,502,482,501,502,483,504,481,486,0,473,470],
[517,512,512,511,503,504,540,495,512,528,0,506],
[518,519,510,491,507,517,540,521,507,531,495,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 70, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,502,545,452,486,425,593,497,529,616,471,437],
[499,0,508,520,562,580,542,559,590,690,463,531],
[456,493,0,526,428,532,518,567,523,612,486,411],
[549,481,475,0,533,520,592,537,608,671,451,538],
[515,439,573,468,0,482,542,589,528,659,461,520],
[576,421,469,481,519,0,541,510,561,723,530,493],
[408,459,483,409,459,460,0,472,443,603,427,351],
[504,442,434,464,412,491,529,0,514,659,468,453],
[472,411,478,393,473,440,558,487,0,562,409,426],
[385,311,389,330,342,278,398,342,439,0,356,278],
[530,538,515,550,540,471,574,533,592,645,0,453],
[564,470,590,463,481,508,650,548,575,723,548,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 71, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,469,360,402,332,403,534,501,438,578,338,414],
[532,0,532,487,581,426,675,569,675,582,714,501],
[641,469,0,573,663,518,583,774,553,401,755,746],
[599,514,428,0,483,335,605,714,598,616,517,462],
[669,420,338,518,0,570,484,442,398,369,302,451],
[598,575,483,666,431,0,539,706,511,526,467,553],
[467,326,418,396,517,462,0,435,371,473,348,467],
[500,432,227,287,559,295,566,0,387,337,396,366],
[563,326,448,403,603,490,630,614,0,455,576,496],
[423,419,600,385,632,475,528,664,546,0,519,640],
[663,287,246,484,699,534,653,605,425,482,0,544],
[587,500,255,539,550,448,534,635,505,361,457,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 72, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,530,490,480,530,517,552,513,548,499,521,528],
[471,0,456,476,470,485,492,484,506,501,502,480],
[511,545,0,493,526,523,520,508,548,511,525,507],
[521,525,508,0,530,529,526,498,513,522,504,492],
[471,531,475,471,0,514,521,514,515,503,502,505],
[484,516,478,472,487,0,505,489,519,511,526,494],
[449,509,481,475,480,496,0,502,477,486,494,476],
[488,517,493,503,487,512,499,0,535,487,515,528],
[453,495,453,488,486,482,524,466,0,483,501,472],
[502,500,490,479,498,490,515,514,518,0,499,509],
[480,499,476,497,499,475,507,486,500,502,0,488],
[473,521,494,509,496,507,525,473,529,492,513,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 73, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,571,490,523,557,531,511,570,551,521,506,583],
[430,0,435,455,503,515,459,526,532,481,503,468],
[511,566,0,490,585,524,533,533,548,474,557,519],
[478,546,511,0,605,532,514,522,556,541,521,491],
[444,498,416,396,0,478,487,500,413,434,436,450],
[470,486,477,469,523,0,485,538,473,481,499,485],
[490,542,468,487,514,516,0,520,503,518,514,473],
[431,475,468,479,501,463,481,0,509,453,467,471],
[450,469,453,445,588,528,498,492,0,515,497,439],
[480,520,527,460,567,520,483,548,486,0,533,484],
[495,498,444,480,565,502,487,534,504,468,0,442],
[418,533,482,510,551,516,528,530,562,517,559,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 74, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,518,489,482,482,482,491,519,468,511,477,507],
[483,0,444,475,462,461,454,513,466,488,495,455],
[512,557,0,508,496,527,488,537,490,527,494,499],
[519,526,493,0,482,513,479,548,501,534,488,517],
[519,539,505,519,0,519,457,517,505,519,519,522],
[519,540,474,488,482,0,499,550,529,522,510,525],
[510,547,513,522,544,502,0,570,497,506,532,499],
[482,488,464,453,484,451,431,0,473,515,493,477],
[533,535,511,500,496,472,504,528,0,522,500,497],
[490,513,474,467,482,479,495,486,479,0,479,499],
[524,506,507,513,482,491,469,508,501,522,0,534],
[494,546,502,484,479,476,502,524,504,502,467,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 75, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,475,501,476,478,497,486,502,477,485,473,486],
[526,0,538,518,507,523,514,519,505,519,498,509],
[500,463,0,503,496,505,489,499,500,505,501,491],
[525,483,498,0,494,492,505,498,491,513,487,505],
[523,494,505,507,0,493,501,517,501,507,508,510],
[504,478,496,509,508,0,491,499,496,499,490,492],
[515,487,512,496,500,510,0,510,484,496,514,494],
[499,482,502,503,484,502,491,0,486,487,486,485],
[524,496,501,510,500,505,517,515,0,500,501,489],
[516,482,496,488,494,502,505,514,501,0,501,476],
[528,503,500,514,493,511,487,515,500,500,0,499],
[515,492,510,496,491,509,507,516,512,525,502,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 76, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,525,536,522,540,506,524,527,500,523,529,508],
[476,0,504,499,527,497,500,515,519,524,515,495],
[465,497,0,489,518,486,493,493,504,499,507,491],
[479,502,512,0,494,510,520,516,508,511,528,514],
[461,474,483,507,0,475,482,486,486,477,495,492],
[495,504,515,491,526,0,503,527,512,516,508,515],
[477,501,508,481,519,498,0,490,491,501,497,495],
[474,486,508,485,515,474,511,0,491,510,515,487],
[501,482,497,493,515,489,510,510,0,509,499,494],
[478,477,502,490,524,485,500,491,492,0,476,486],
[472,486,494,473,506,493,504,486,502,525,0,463],
[493,506,510,487,509,486,506,514,507,515,538,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 77, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,485,470,447,406,495,496,464,482,443,511,423],
[516,0,463,486,452,511,493,478,503,457,470,451],
[531,538,0,527,533,575,502,529,560,527,538,443],
[554,515,474,0,523,534,525,523,532,467,512,456],
[595,549,468,478,0,584,501,543,553,525,512,430],
[506,490,426,467,417,0,493,492,494,493,380,413],
[505,508,499,476,500,508,0,550,505,488,460,438],
[537,523,472,478,458,509,451,0,439,446,446,444],
[519,498,441,469,448,507,496,562,0,497,465,446],
[558,544,474,534,476,508,513,555,504,0,495,469],
[490,531,463,489,489,621,541,555,536,506,0,523],
[578,550,558,545,571,588,563,557,555,532,478,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 78, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,513,392,572,609,389,599,525,489,572,567,573],
[488,0,455,533,675,348,551,573,508,593,522,497],
[609,546,0,517,574,483,572,581,467,613,589,607],
[429,468,484,0,561,412,528,576,498,571,508,557],
[392,326,427,440,0,199,422,339,380,433,457,383],
[612,653,518,589,802,0,729,615,523,631,487,639],
[402,450,429,473,579,272,0,555,468,474,417,439],
[476,428,420,425,662,386,446,0,428,549,469,405],
[512,493,534,503,621,478,533,573,0,626,607,600],
[429,408,388,430,568,370,527,452,375,0,385,413],
[434,479,412,493,544,514,584,532,394,616,0,475],
[428,504,394,444,618,362,562,596,401,588,526,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 79, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,512,507,502,516,518,513,496,513,516,530,514],
[489,0,494,531,495,522,498,503,509,499,506,505],
[494,507,0,500,499,525,500,494,528,512,524,507],
[499,470,501,0,491,528,512,486,503,494,497,502],
[485,506,502,510,0,526,495,486,520,507,514,537],
[483,479,476,473,475,0,493,478,467,482,512,492],
[488,503,501,489,506,508,0,492,523,502,502,517],
[505,498,507,515,515,523,509,0,496,504,528,532],
[488,492,473,498,481,534,478,505,0,489,516,513],
[485,502,489,507,494,519,499,497,512,0,509,523],
[471,495,477,504,487,489,499,473,485,492,0,496],
[487,496,494,499,464,509,484,469,488,478,505,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 80, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,482,476,537,584,571,550,515,495,624,488,474],
[519,0,464,469,506,595,482,550,474,525,549,441],
[525,537,0,602,533,604,563,552,539,630,608,499],
[464,532,399,0,545,488,447,465,453,520,424,508],
[417,495,468,456,0,527,513,527,423,525,461,490],
[430,406,397,513,474,0,489,431,416,499,436,503],
[451,519,438,554,488,512,0,511,520,613,430,528],
[486,451,449,536,474,570,490,0,530,526,491,421],
[506,527,462,548,578,585,481,471,0,578,531,550],
[377,476,371,481,476,502,388,475,423,0,459,517],
[513,452,393,577,540,565,571,510,470,542,0,561],
[527,560,502,493,511,498,473,580,451,484,440,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 81, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,524,497,481,509,488,487,483,474,489,499,492],
[477,0,485,480,487,496,485,489,490,483,496,482],
[504,516,0,494,502,498,502,483,494,476,479,481],
[520,521,507,0,512,503,523,499,496,500,516,514],
[492,514,499,489,0,483,484,504,498,476,497,504],
[513,505,503,498,518,0,508,524,503,499,509,518],
[514,516,499,478,517,493,0,507,502,485,504,507],
[518,512,518,502,497,477,494,0,491,496,481,490],
[527,511,507,505,503,498,499,510,0,501,497,508],
[512,518,525,501,525,502,516,505,500,0,501,515],
[502,505,522,485,504,492,497,520,504,500,0,496],
[509,519,520,487,497,483,494,511,493,486,505,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 82, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,485,516,482,513,491,489,477,510,512,473,513],
[516,0,490,454,493,484,533,471,506,512,488,502],
[485,511,0,503,494,514,522,487,503,503,489,525],
[519,547,498,0,520,522,518,517,520,532,493,524],
[488,508,507,481,0,519,538,496,513,512,485,509],
[510,517,487,479,482,0,490,484,513,505,485,506],
[512,468,479,483,463,511,0,463,489,467,477,504],
[524,530,514,484,505,517,538,0,503,515,520,515],
[491,495,498,481,488,488,512,498,0,494,511,522],
[489,489,498,469,489,496,534,486,507,0,492,497],
[528,513,512,508,516,516,524,481,490,509,0,521],
[488,499,476,477,492,495,497,486,479,504,480,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 83, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,476,503,492,481,507,476,490,501,492,512,482],
[525,0,510,521,500,509,513,533,534,526,533,533],
[498,491,0,488,504,497,481,484,498,489,513,486],
[509,480,513,0,486,525,483,519,516,523,522,506],
[520,501,497,515,0,522,466,503,522,509,520,519],
[494,492,504,476,479,0,450,484,487,511,515,501],
[525,488,520,518,535,551,0,515,518,527,542,523],
[511,468,517,482,498,517,486,0,519,517,518,502],
[500,467,503,485,479,514,483,482,0,491,511,508],
[509,475,512,478,492,490,474,484,510,0,534,501],
[489,468,488,479,481,486,459,483,490,467,0,499],
[519,468,515,495,482,500,478,499,493,500,502,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 84, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,450,457,460,458,467,497,488,468,468,445,479],
[551,0,495,518,531,529,515,512,527,525,555,541],
[544,506,0,497,518,528,503,504,489,494,511,505],
[541,483,504,0,495,504,492,504,496,484,493,499],
[543,470,483,506,0,500,537,505,485,506,509,524],
[534,472,473,497,501,0,508,519,515,483,466,516],
[504,486,498,509,464,493,0,488,509,499,471,478],
[513,489,497,497,496,482,513,0,514,520,505,510],
[533,474,512,505,516,486,492,487,0,482,502,493],
[533,476,507,517,495,518,502,481,519,0,485,505],
[556,446,490,508,492,535,530,496,499,516,0,507],
[522,460,496,502,477,485,523,491,508,496,494,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 85, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,482,509,483,476,513,473,501,497,522,522,483],
[519,0,549,491,522,489,455,535,512,514,513,460],
[492,452,0,463,484,481,464,501,482,459,482,465],
[518,510,538,0,530,530,488,573,537,533,533,525],
[525,479,517,471,0,516,478,501,476,491,494,504],
[488,512,520,471,485,0,489,524,506,492,486,454],
[528,546,537,513,523,512,0,564,534,540,530,496],
[500,466,500,428,500,477,437,0,481,466,488,463],
[504,489,519,464,525,495,467,520,0,505,504,492],
[479,487,542,468,510,509,461,535,496,0,506,430],
[479,488,519,468,507,515,471,513,497,495,0,494],
[518,541,536,476,497,547,505,538,509,571,507,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 86, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,492,503,469,522,510,511,465,534,529,517,549],
[509,0,517,502,468,515,510,504,560,530,545,536],
[498,484,0,488,503,518,509,515,522,515,511,485],
[532,499,513,0,495,513,533,494,551,516,562,493],
[479,533,498,506,0,535,531,501,563,553,529,512],
[491,486,483,488,466,0,533,509,510,475,520,502],
[490,491,492,468,470,468,0,501,510,494,487,493],
[536,497,486,507,500,492,500,0,523,520,539,538],
[467,441,479,450,438,491,491,478,0,517,520,497],
[472,471,486,485,448,526,507,481,484,0,522,497],
[484,456,490,439,472,481,514,462,481,479,0,494],
[452,465,516,508,489,499,508,463,504,504,507,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 87, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,497,516,510,500,519,513,524,507,517,523,527],
[504,0,510,479,519,504,509,512,502,501,530,507],
[485,491,0,492,515,500,503,509,499,493,526,522],
[491,522,509,0,509,510,505,515,501,513,523,526],
[501,482,486,492,0,487,489,516,486,488,518,488],
[482,497,501,491,514,0,510,505,518,485,534,498],
[488,492,498,496,512,491,0,510,479,495,515,517],
[477,489,492,486,485,496,491,0,481,495,520,497],
[494,499,502,500,515,483,522,520,0,501,532,497],
[484,500,508,488,513,516,506,506,500,0,526,512],
[478,471,475,478,483,467,486,481,469,475,0,482],
[474,494,479,475,513,503,484,504,504,489,519,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 88, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,490,508,500,520,546,497,498,533,523,496,501],
[511,0,504,478,478,513,492,498,490,478,463,481],
[493,497,0,495,514,521,507,518,500,507,498,477],
[501,523,506,0,494,515,489,518,511,504,492,487],
[481,523,487,507,0,496,519,505,489,512,477,503],
[455,488,480,486,505,0,476,512,520,497,479,473],
[504,509,494,512,482,525,0,528,535,490,497,499],
[503,503,483,483,496,489,473,0,490,492,475,510],
[468,511,501,490,512,481,466,511,0,457,479,493],
[478,523,494,497,489,504,511,509,544,0,486,497],
[505,538,503,509,524,522,504,526,522,515,0,485],
[500,520,524,514,498,528,502,491,508,504,516,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 89, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,483,536,510,501,494,495,519,512,495,534,494],
[518,0,520,505,519,508,508,494,519,520,513,510],
[465,481,0,481,499,495,470,475,463,479,481,476],
[491,496,520,0,493,509,485,483,517,509,530,509],
[500,482,502,508,0,514,493,491,490,517,510,480],
[507,493,506,492,487,0,496,505,485,494,485,490],
[506,493,531,516,508,505,0,494,520,521,529,485],
[482,507,526,518,510,496,507,0,488,490,516,482],
[489,482,538,484,511,516,481,513,0,499,507,499],
[506,481,522,492,484,507,480,511,502,0,503,483],
[467,488,520,471,491,516,472,485,494,498,0,487],
[507,491,525,492,521,511,516,519,502,518,514,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 90, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,499,529,500,483,444,505,527,492,484,519,536],
[502,0,554,524,527,440,544,570,519,504,554,583],
[472,447,0,484,461,397,441,504,451,457,441,508],
[501,477,517,0,518,388,510,500,506,542,478,538],
[518,474,540,483,0,440,482,546,574,577,539,558],
[557,561,604,613,561,0,490,521,580,560,573,627],
[496,457,560,491,519,511,0,563,553,552,535,569],
[474,431,497,501,455,480,438,0,462,461,486,518],
[509,482,550,495,427,421,448,539,0,514,455,529],
[517,497,544,459,424,441,449,540,487,0,482,592],
[482,447,560,523,462,428,466,515,546,519,0,572],
[465,418,493,463,443,374,432,483,472,409,429,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 91, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,473,490,501,520,511,469,453,509,444,489,490],
[528,0,496,494,535,544,493,458,516,479,506,475],
[511,505,0,485,498,535,474,434,496,462,470,463],
[500,507,516,0,526,573,510,467,491,448,512,464],
[481,466,503,475,0,531,509,466,484,470,499,476],
[490,457,466,428,470,0,482,424,475,445,451,446],
[532,508,527,491,492,519,0,503,515,468,536,526],
[548,543,567,534,535,577,498,0,531,465,530,507],
[492,485,505,510,517,526,486,470,0,471,496,501],
[557,522,539,553,531,556,533,536,530,0,552,499],
[512,495,531,489,502,550,465,471,505,449,0,506],
[511,526,538,537,525,555,475,494,500,502,495,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 92, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,515,503,481,485,527,566,515,520,495,530,502],
[486,0,481,454,443,466,513,493,508,462,482,485],
[498,520,0,464,472,504,516,512,475,483,479,488],
[520,547,537,0,462,516,551,518,523,507,515,520],
[516,558,529,539,0,536,556,529,535,489,533,511],
[474,535,497,485,465,0,524,512,500,451,512,475],
[435,488,485,450,445,477,0,487,474,456,493,506],
[486,508,489,483,472,489,514,0,500,464,503,512],
[481,493,526,478,466,501,527,501,0,453,492,500],
[506,539,518,494,512,550,545,537,548,0,519,545],
[471,519,522,486,468,489,508,498,509,482,0,516],
[499,516,513,481,490,526,495,489,501,456,485,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 93, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,496,512,520,508,495,510,502,509,491,525,506],
[505,0,506,519,521,496,524,503,489,496,519,525],
[489,495,0,501,501,481,510,487,478,476,505,505],
[481,482,500,0,513,474,500,480,499,506,500,516],
[493,480,500,488,0,481,503,482,503,488,504,510],
[506,505,520,527,520,0,539,508,521,500,519,543],
[491,477,491,501,498,462,0,483,503,500,496,518],
[499,498,514,521,519,493,518,0,509,508,512,522],
[492,512,523,502,498,480,498,492,0,489,524,512],
[510,505,525,495,513,501,501,493,512,0,532,516],
[476,482,496,501,497,482,505,489,477,469,0,509],
[495,476,496,485,491,458,483,479,489,485,492,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 94, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,486,497,503,497,533,451,506,497,499,513,462],
[515,0,519,546,498,520,505,537,520,496,520,462],
[504,482,0,504,530,529,479,501,482,505,523,454],
[498,455,497,0,488,523,504,512,510,512,488,505],
[504,503,471,513,0,510,497,512,499,484,506,473],
[468,481,472,478,491,0,464,479,502,471,513,467],
[550,496,522,497,504,537,0,536,521,508,543,480],
[495,464,500,489,489,522,465,0,489,519,510,460],
[504,481,519,491,502,499,480,512,0,499,503,494],
[502,505,496,489,517,530,493,482,502,0,513,467],
[488,481,478,513,495,488,458,491,498,488,0,452],
[539,539,547,496,528,534,521,541,507,534,549,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 95, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,408,430,430,468,501,429,492,506,459,501,426],
[593,0,430,484,502,566,493,416,465,541,516,517],
[571,571,0,507,574,472,457,470,616,474,540,542],
[571,517,494,0,530,596,491,562,475,484,511,550],
[533,499,427,471,0,460,422,497,453,504,480,531],
[500,435,529,405,541,0,390,451,517,503,554,460],
[572,508,544,510,579,611,0,528,546,477,512,543],
[509,585,531,439,504,550,473,0,522,478,467,413],
[495,536,385,526,548,484,455,479,0,492,484,438],
[542,460,527,517,497,498,524,523,509,0,491,458],
[500,485,461,490,521,447,489,534,517,510,0,485],
[575,484,459,451,470,541,458,588,563,543,516,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 96, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,489,534,507,511,487,489,575,556,489,572,462],
[512,0,525,488,533,495,516,535,563,472,530,474],
[467,476,0,431,474,477,477,457,528,539,452,451],
[494,513,570,0,472,534,518,525,589,504,516,515],
[490,468,527,529,0,531,518,490,538,555,484,449],
[514,506,524,467,470,0,505,522,543,495,525,466],
[512,485,524,483,483,496,0,516,554,525,538,476],
[426,466,544,476,511,479,485,0,568,464,509,490],
[445,438,473,412,463,458,447,433,0,476,453,458],
[512,529,462,497,446,506,476,537,525,0,501,451],
[429,471,549,485,517,476,463,492,548,500,0,440],
[539,527,550,486,552,535,525,511,543,550,561,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 97, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,496,495,469,505,506,456,476,481,482,468,491],
[505,0,514,504,532,551,481,457,510,534,494,554],
[506,487,0,501,518,544,475,466,495,522,491,521],
[532,497,500,0,501,527,494,478,465,489,501,519],
[496,469,483,500,0,508,479,462,489,509,485,511],
[495,450,457,474,493,0,453,463,473,488,465,504],
[545,520,526,507,522,548,0,486,516,519,509,528],
[525,544,535,523,539,538,515,0,505,524,491,542],
[520,491,506,536,512,528,485,496,0,519,518,520],
[519,467,479,512,492,513,482,477,482,0,476,501],
[533,507,510,500,516,536,492,510,483,525,0,550],
[510,447,480,482,490,497,473,459,481,500,451,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 98, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,438,512,524,460,467,473,425,465,486,479,460],
[563,0,559,552,513,485,509,505,499,586,548,512],
[489,442,0,505,464,480,451,395,464,489,497,442],
[477,449,496,0,466,476,442,447,431,485,459,461],
[541,488,537,535,0,508,496,473,465,512,523,499],
[534,516,521,525,493,0,479,463,494,507,504,472],
[528,492,550,559,505,522,0,483,524,536,555,506],
[576,496,606,554,528,538,518,0,500,554,546,531],
[536,502,537,570,536,507,477,501,0,535,538,535],
[515,415,512,516,489,494,465,447,466,0,508,451],
[522,453,504,542,478,497,446,455,463,493,0,472],
[541,489,559,540,502,529,495,470,466,550,529,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 99, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,554,531,523,330,479,396,448,470,390,439,381],
[447,0,383,555,350,386,393,310,235,334,239,404],
[470,618,0,530,281,423,513,426,416,434,391,378],
[478,446,471,0,392,457,373,384,472,416,315,423],
[671,651,720,609,0,451,528,453,451,568,530,478],
[522,615,578,544,550,0,495,440,359,518,545,495],
[605,608,488,628,473,506,0,449,443,488,583,468],
[553,691,575,617,548,561,552,0,603,528,549,446],
[531,766,585,529,550,642,558,398,0,652,570,463],
[611,667,567,585,433,483,513,473,349,0,497,602],
[562,762,610,686,471,456,418,452,431,504,0,479],
[620,597,623,578,523,506,533,555,538,399,522,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 100, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,446,480,512,458,485,488,477,503,518,534,521],
[555,0,487,510,514,518,534,502,500,546,515,557],
[521,514,0,513,484,483,481,531,507,557,569,554],
[489,491,488,0,494,497,498,520,483,492,532,496],
[543,487,517,507,0,517,479,527,494,510,526,542],
[516,483,518,504,484,0,525,520,497,528,516,550],
[513,467,520,503,522,476,0,512,494,513,498,550],
[524,499,470,481,474,481,489,0,502,526,547,520],
[498,501,494,518,507,504,507,499,0,523,514,548],
[483,455,444,509,491,473,488,475,478,0,504,516],
[467,486,432,469,475,485,503,454,487,497,0,506],
[480,444,447,505,459,451,451,481,453,485,495,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 101, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,475,586,498,533,580,565,559,491,355,438,539],
[526,0,653,562,604,575,660,582,616,475,621,496],
[415,348,0,445,330,486,446,497,509,394,411,338],
[503,439,556,0,445,589,602,530,505,493,414,489],
[468,397,671,556,0,563,533,512,555,512,458,497],
[421,426,515,412,438,0,484,481,501,391,445,421],
[436,341,555,399,468,517,0,435,522,392,374,394],
[442,419,504,471,489,520,566,0,510,448,429,517],
[510,385,492,496,446,500,479,491,0,323,435,472],
[646,526,607,508,489,610,609,553,678,0,499,549],
[563,380,590,587,543,556,627,572,566,502,0,559],
[462,505,663,512,504,580,607,484,529,452,442,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 102, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,498,508,499,529,487,490,498,505,519,500,518],
[503,0,525,508,523,511,493,523,530,522,507,524],
[493,476,0,482,497,468,470,490,492,494,484,505],
[502,493,519,0,513,502,499,506,535,511,517,534],
[472,478,504,488,0,468,496,486,489,505,481,505],
[514,490,533,499,533,0,513,520,517,525,502,521],
[511,508,531,502,505,488,0,504,516,515,511,517],
[503,478,511,495,515,481,497,0,506,493,482,519],
[496,471,509,466,512,484,485,495,0,476,485,516],
[482,479,507,490,496,476,486,508,525,0,495,494],
[501,494,517,484,520,499,490,519,516,506,0,514],
[483,477,496,467,496,480,484,482,485,507,487,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 103, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,493,385,523,351,475,500,510,438,424,526,396],
[508,0,471,505,436,503,445,608,486,468,506,453],
[616,530,0,563,465,567,574,620,573,558,605,521],
[478,496,438,0,382,479,406,575,438,463,555,473],
[650,565,536,619,0,640,578,624,562,585,569,466],
[526,498,434,522,361,0,487,625,467,489,533,451],
[501,556,427,595,423,514,0,634,559,538,476,471],
[491,393,381,426,377,376,367,0,385,466,445,416],
[563,515,428,563,439,534,442,616,0,540,529,470],
[577,533,443,538,416,512,463,535,461,0,454,452],
[475,495,396,446,432,468,525,556,472,547,0,482],
[605,548,480,528,535,550,530,585,531,549,519,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 104, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,500,499,502,531,505,552,476,532,521,538,504],
[501,0,507,511,532,483,542,511,566,529,528,522],
[502,494,0,491,509,471,542,479,516,490,506,488],
[499,490,510,0,513,485,530,467,521,507,510,482],
[470,469,492,488,0,471,499,499,515,509,495,487],
[496,518,530,516,530,0,525,515,529,504,492,506],
[449,459,459,471,502,476,0,425,499,509,486,457],
[525,490,522,534,502,486,576,0,535,528,525,529],
[469,435,485,480,486,472,502,466,0,491,482,491],
[480,472,511,494,492,497,492,473,510,0,508,496],
[463,473,495,491,506,509,515,476,519,493,0,484],
[497,479,513,519,514,495,544,472,510,505,517,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 105, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,502,495,481,494,514,505,502,461,512,506,472],
[499,0,504,488,504,479,495,520,481,527,500,478],
[506,497,0,459,477,449,478,510,471,498,511,453],
[520,513,542,0,478,485,534,521,488,537,490,494],
[507,497,524,523,0,498,518,521,508,555,527,495],
[487,522,552,516,503,0,552,522,504,539,523,512],
[496,506,523,467,483,449,0,510,460,490,494,457],
[499,481,491,480,480,479,491,0,449,515,489,457],
[540,520,530,513,493,497,541,552,0,517,518,480],
[489,474,503,464,446,462,511,486,484,0,491,472],
[495,501,490,511,474,478,507,512,483,510,0,492],
[529,523,548,507,506,489,544,544,521,529,509,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 106, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,456,462,496,493,472,509,471,490,506,515,510],
[545,0,506,525,525,459,549,510,508,531,543,501],
[539,495,0,514,523,507,557,482,520,560,526,513],
[505,476,487,0,504,465,514,475,467,484,506,474],
[508,476,478,497,0,524,518,506,448,501,504,509],
[529,542,494,536,477,0,540,511,513,520,543,519],
[492,452,444,487,483,461,0,456,494,477,500,512],
[530,491,519,526,495,490,545,0,498,533,514,500],
[511,493,481,534,553,488,507,503,0,523,531,499],
[495,470,441,517,500,481,524,468,478,0,502,480],
[486,458,475,495,497,458,501,487,470,499,0,500],
[491,500,488,527,492,482,489,501,502,521,501,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 107, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,453,493,512,479,513,507,505,481,475,451,501],
[548,0,494,542,511,517,492,569,559,464,502,525],
[508,507,0,541,520,521,512,541,532,484,474,512],
[489,459,460,0,460,540,475,512,499,463,455,486],
[522,490,481,541,0,516,503,536,523,495,478,521],
[488,484,480,461,485,0,472,518,507,473,468,499],
[494,509,489,526,498,529,0,549,523,464,479,486],
[496,432,460,489,465,483,452,0,484,445,483,472],
[520,442,469,502,478,494,478,517,0,475,461,498],
[526,537,517,538,506,528,537,556,526,0,487,508],
[550,499,527,546,523,533,522,518,540,514,0,507],
[500,476,489,515,480,502,515,529,503,493,494,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 108, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,503,497,480,512,515,552,502,523,493,527,490],
[498,0,492,490,507,505,547,494,518,478,500,490],
[504,509,0,485,535,512,537,505,519,509,533,478],
[521,511,516,0,513,487,543,528,559,510,538,501],
[489,494,466,488,0,494,547,498,514,471,487,483],
[486,496,489,514,507,0,545,483,534,492,504,513],
[449,454,464,458,454,456,0,456,469,477,480,485],
[499,507,496,473,503,518,545,0,545,513,505,474],
[478,483,482,442,487,467,532,456,0,450,491,514],
[508,523,492,491,530,509,524,488,551,0,538,510],
[474,501,468,463,514,497,521,496,510,463,0,471],
[511,511,523,500,518,488,516,527,487,491,530,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 109, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,507,506,518,500,533,525,496,505,498,515,510],
[494,0,504,536,514,529,544,525,516,521,480,516],
[495,497,0,527,520,524,513,503,524,526,482,522],
[483,465,474,0,503,500,507,483,496,477,472,498],
[501,487,481,498,0,527,503,501,501,493,481,488],
[468,472,477,501,474,0,500,471,487,492,483,483],
[476,457,488,494,498,501,0,494,502,496,471,500],
[505,476,498,518,500,530,507,0,489,510,496,500],
[496,485,477,505,500,514,499,512,0,488,501,495],
[503,480,475,524,508,509,505,491,513,0,497,494],
[486,521,519,529,520,518,530,505,500,504,0,525],
[491,485,479,503,513,518,501,501,506,507,476,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 110, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,505,437,448,464,504,462,446,502,408,467,452],
[496,0,478,513,482,572,470,460,483,467,556,547],
[564,523,0,473,545,585,511,522,478,485,503,539],
[553,488,528,0,482,502,504,486,523,536,507,548],
[537,519,456,519,0,531,502,495,528,469,483,564],
[497,429,416,499,470,0,416,437,453,446,417,451],
[539,531,490,497,499,585,0,499,502,453,573,540],
[555,541,479,515,506,564,502,0,542,461,505,551],
[499,518,523,478,473,548,499,459,0,462,495,530],
[593,534,516,465,532,555,548,540,539,0,502,555],
[534,445,498,494,518,584,428,496,506,499,0,475],
[549,454,462,453,437,550,461,450,471,446,526,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 111, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,459,519,496,453,495,483,482,497,472,471,465],
[542,0,532,502,466,495,524,509,510,516,548,474],
[482,469,0,456,453,481,492,478,470,457,472,470],
[505,499,545,0,502,497,518,478,514,503,512,499],
[548,535,548,499,0,531,549,532,524,497,519,517],
[506,506,520,504,470,0,489,479,494,457,465,471],
[518,477,509,483,452,512,0,527,518,507,507,486],
[519,492,523,523,469,522,474,0,522,489,508,494],
[504,491,531,487,477,507,483,479,0,477,489,464],
[529,485,544,498,504,544,494,512,524,0,517,489],
[530,453,529,489,482,536,494,493,512,484,0,473],
[536,527,531,502,484,530,515,507,537,512,528,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 112, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,484,499,489,492,457,507,491,506,514,497,470],
[517,0,514,504,489,490,537,493,538,519,515,509],
[502,487,0,525,501,501,507,487,513,507,482,491],
[512,497,476,0,507,485,509,502,518,500,506,501],
[509,512,500,494,0,473,517,505,522,498,492,491],
[544,511,500,516,528,0,553,508,522,521,517,513],
[494,464,494,492,484,448,0,476,489,509,471,521],
[510,508,514,499,496,493,525,0,506,513,499,518],
[495,463,488,483,479,479,512,495,0,498,495,511],
[487,482,494,501,503,480,492,488,503,0,501,497],
[504,486,519,495,509,484,530,502,506,500,0,499],
[531,492,510,500,510,488,480,483,490,504,502,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 113, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,500,487,489,497,486,496,506,492,482,464,485],
[501,0,482,495,513,485,492,491,497,503,478,512],
[514,519,0,499,508,503,491,519,502,497,487,495],
[512,506,502,0,497,499,492,489,508,503,501,495],
[504,488,493,504,0,487,503,503,502,528,502,521],
[515,516,498,502,514,0,502,509,491,497,490,496],
[505,509,510,509,498,499,0,489,489,495,486,512],
[495,510,482,512,498,492,512,0,521,496,484,489],
[509,504,499,493,499,510,512,480,0,497,483,481],
[519,498,504,498,473,504,506,505,504,0,490,499],
[537,523,514,500,499,511,515,517,518,511,0,536],
[516,489,506,506,480,505,489,512,520,502,465,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 114, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,489,473,501,467,478,496,471,459,485,461,470],
[512,0,500,529,537,525,511,493,513,519,505,479],
[528,501,0,510,532,512,533,529,549,522,524,468],
[500,472,491,0,493,479,460,488,485,488,470,458],
[534,464,469,508,0,465,503,479,506,492,472,466],
[523,476,489,522,536,0,506,481,499,505,475,471],
[505,490,468,541,498,495,0,496,484,501,483,469],
[530,508,472,513,522,520,505,0,486,494,492,491],
[542,488,452,516,495,502,517,515,0,491,465,469],
[516,482,479,513,509,496,500,507,510,0,484,486],
[540,496,477,531,529,526,518,509,536,517,0,504],
[531,522,533,543,535,530,532,510,532,515,497,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 115, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,478,514,500,535,463,453,487,524,513,472,469],
[523,0,510,532,537,514,489,486,588,525,505,482],
[487,491,0,489,545,491,470,478,550,482,516,498],
[501,469,512,0,542,449,469,505,544,453,491,493],
[466,464,456,459,0,419,427,434,498,443,442,435],
[538,487,510,552,582,0,530,512,548,524,531,498],
[548,512,531,532,574,471,0,501,562,519,545,495],
[514,515,523,496,567,489,500,0,569,498,473,540],
[477,413,451,457,503,453,439,432,0,441,454,430],
[488,476,519,548,558,477,482,503,560,0,501,475],
[529,496,485,510,559,470,456,528,547,500,0,496],
[532,519,503,508,566,503,506,461,571,526,505,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 116, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,557,582,510,575,527,571,571,498,542,517,523],
[444,0,529,495,521,473,517,481,467,450,488,497],
[419,472,0,486,515,505,489,504,482,515,479,481],
[491,506,515,0,551,486,535,534,507,503,518,499],
[426,480,486,450,0,444,461,458,470,459,447,474],
[474,528,496,515,557,0,528,499,474,487,491,539],
[430,484,512,466,540,473,0,476,497,511,497,483],
[430,520,497,467,543,502,525,0,484,492,478,463],
[503,534,519,494,531,527,504,517,0,479,485,520],
[459,551,486,498,542,514,490,509,522,0,495,526],
[484,513,522,483,554,510,504,523,516,506,0,539],
[478,504,520,502,527,462,518,538,481,475,462,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 117, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,512,530,513,518,521,505,482,495,510,541,484],
[489,0,507,523,526,490,542,514,520,509,515,516],
[471,494,0,481,507,451,499,486,500,495,526,494],
[488,478,520,0,500,472,496,477,500,495,512,465],
[483,475,494,501,0,469,495,473,500,499,486,491],
[480,511,550,529,532,0,530,496,535,513,535,517],
[496,459,502,505,506,471,0,492,478,494,508,484],
[519,487,515,524,528,505,509,0,527,525,546,502],
[506,481,501,501,501,466,523,474,0,486,510,488],
[491,492,506,506,502,488,507,476,515,0,528,493],
[460,486,475,489,515,466,493,455,491,473,0,474],
[517,485,507,536,510,484,517,499,513,508,527,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 118, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,496,496,536,519,497,524,505,526,487,498,527],
[505,0,514,532,517,498,537,523,558,520,506,556],
[505,487,0,537,500,504,508,517,523,496,494,517],
[465,469,464,0,477,474,479,491,514,475,464,477],
[482,484,501,524,0,487,497,484,514,494,495,515],
[504,503,497,527,514,0,517,486,557,503,510,517],
[477,464,493,522,504,484,0,503,525,499,453,500],
[496,478,484,510,517,515,498,0,541,483,502,530],
[475,443,478,487,487,444,476,460,0,468,463,483],
[514,481,505,526,507,498,502,518,533,0,501,508],
[503,495,507,537,506,491,548,499,538,500,0,525],
[474,445,484,524,486,484,501,471,518,493,476,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 119, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,476,516,464,474,492,462,512,491,500,471,454],
[525,0,512,485,463,510,483,480,488,510,469,456],
[485,489,0,488,441,501,492,480,486,496,459,450],
[537,516,513,0,457,506,515,485,500,492,449,470],
[527,538,560,544,0,557,524,521,538,531,486,507],
[509,491,500,495,444,0,497,503,477,500,463,476],
[539,518,509,486,477,504,0,501,516,503,519,455],
[489,521,521,516,480,498,500,0,488,523,467,454],
[510,513,515,501,463,524,485,513,0,515,451,447],
[501,491,505,509,470,501,498,478,486,0,475,452],
[530,532,542,552,515,538,482,534,550,526,0,508],
[547,545,551,531,494,525,546,547,554,549,493,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 120, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,534,509,517,528,540,536,573,460,457,430,420],
[467,0,497,418,427,431,368,497,379,425,391,420],
[492,504,0,571,607,587,514,578,501,511,459,520],
[484,583,430,0,505,452,501,529,502,453,492,399],
[473,574,394,496,0,556,410,475,468,368,445,386],
[461,570,414,549,445,0,467,483,388,387,502,410],
[465,633,487,500,591,534,0,533,531,427,454,456],
[428,504,423,472,526,518,468,0,468,412,396,468],
[541,622,500,499,533,613,470,533,0,483,472,512],
[544,576,490,548,633,614,574,589,518,0,504,492],
[571,610,542,509,556,499,547,605,529,497,0,445],
[581,581,481,602,615,591,545,533,489,509,556,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 121, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,503,538,537,516,544,522,500,507,526,512,530],
[498,0,495,507,511,516,486,495,462,522,481,517],
[463,506,0,526,518,521,515,490,480,532,490,514],
[464,494,475,0,475,510,468,472,482,516,485,487],
[485,490,483,526,0,515,506,495,491,517,491,499],
[457,485,480,491,486,0,482,493,502,519,483,516],
[479,515,486,533,495,519,0,494,494,526,504,513],
[501,506,511,529,506,508,507,0,496,538,500,508],
[494,539,521,519,510,499,507,505,0,533,519,518],
[475,479,469,485,484,482,475,463,468,0,470,491],
[489,520,511,516,510,518,497,501,482,531,0,530],
[471,484,487,514,502,485,488,493,483,510,471,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 122, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,535,503,515,463,523,457,469,499,433,454,559],
[466,0,538,518,493,488,450,501,441,488,505,478],
[498,463,0,499,482,488,504,473,456,452,460,486],
[486,483,502,0,463,455,467,490,492,449,448,501],
[538,508,519,538,0,540,460,497,525,515,547,567],
[478,513,513,546,461,0,509,520,503,497,487,519],
[544,551,497,534,541,492,0,497,526,486,557,543],
[532,500,528,511,504,481,504,0,535,497,509,558],
[502,560,545,509,476,498,475,466,0,485,489,543],
[568,513,549,552,486,504,515,504,516,0,491,553],
[547,496,541,553,454,514,444,492,512,510,0,521],
[442,523,515,500,434,482,458,443,458,448,480,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 123, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,505,486,471,494,481,486,524,500,490,533,489],
[496,0,498,461,504,474,487,472,501,477,550,482],
[515,503,0,484,513,490,510,504,516,475,529,502],
[530,540,517,0,528,470,507,522,529,559,531,507],
[507,497,488,473,0,474,471,479,503,469,515,446],
[520,527,511,531,527,0,483,521,547,525,538,502],
[515,514,491,494,530,518,0,527,497,494,537,469],
[477,529,497,479,522,480,474,0,525,455,512,491],
[501,500,485,472,498,454,504,476,0,493,524,473],
[511,524,526,442,532,476,507,546,508,0,532,480],
[468,451,472,470,486,463,464,489,477,469,0,443],
[512,519,499,494,555,499,532,510,528,521,558,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 124, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,489,526,499,524,500,484,486,492,503,508,532],
[512,0,538,508,511,516,497,493,505,527,488,527],
[475,463,0,467,483,472,453,472,480,457,466,493],
[502,493,534,0,522,518,504,527,512,528,533,560],
[477,490,518,479,0,509,490,477,484,483,492,523],
[501,485,529,483,492,0,473,500,506,470,483,538],
[517,504,548,497,511,528,0,516,527,498,519,544],
[515,508,529,474,524,501,485,0,513,501,519,529],
[509,496,521,489,517,495,474,488,0,510,480,524],
[498,474,544,473,518,531,503,500,491,0,493,526],
[493,513,535,468,509,518,482,482,521,508,0,543],
[469,474,508,441,478,463,457,472,477,475,458,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 125, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,493,564,558,486,606,404,456,463,570,543,527],
[508,0,513,583,459,558,496,488,470,511,559,572],
[437,488,0,479,361,451,394,454,379,437,456,439],
[443,418,522,0,384,512,449,540,440,467,507,536],
[515,542,640,617,0,633,471,514,522,553,547,620],
[395,443,550,489,368,0,444,466,401,419,470,537],
[597,505,607,552,530,557,0,523,468,588,596,578],
[545,513,547,461,487,535,478,0,491,514,555,487],
[538,531,622,561,479,600,533,510,0,567,606,627],
[431,490,564,534,448,582,413,487,434,0,455,537],
[458,442,545,494,454,531,405,446,395,546,0,502],
[474,429,562,465,381,464,423,514,374,464,499,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 126, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,520,497,523,491,504,485,522,554,501,504,498],
[481,0,502,476,497,465,489,513,515,489,494,471],
[504,499,0,512,473,485,481,513,494,504,479,516],
[478,525,489,0,517,467,479,503,499,464,520,514],
[510,504,528,484,0,500,503,546,498,497,501,519],
[497,536,516,534,501,0,504,517,529,531,520,525],
[516,512,520,522,498,497,0,539,546,498,541,514],
[479,488,488,498,455,484,462,0,492,487,485,478],
[447,486,507,502,503,472,455,509,0,480,509,477],
[500,512,497,537,504,470,503,514,521,0,491,510],
[497,507,522,481,500,481,460,516,492,510,0,488],
[503,530,485,487,482,476,487,523,524,491,513,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 127, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,497,486,487,488,492,481,505,502,464,507,480],
[504,0,477,481,483,502,486,490,502,494,506,497],
[515,524,0,503,521,488,510,510,520,512,523,509],
[514,520,498,0,508,501,501,535,522,506,535,504],
[513,518,480,493,0,487,501,471,518,481,528,503],
[509,499,513,500,514,0,511,511,523,499,526,497],
[520,515,491,500,500,490,0,513,518,483,528,500],
[496,511,491,466,530,490,488,0,506,470,505,504],
[499,499,481,479,483,478,483,495,0,450,529,482],
[537,507,489,495,520,502,518,531,551,0,526,507],
[494,495,478,466,473,475,473,496,472,475,0,455],
[521,504,492,497,498,504,501,497,519,494,546,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 128, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,480,487,448,424,469,432,496,498,484,501,466],
[521,0,514,484,525,535,454,494,526,525,538,488],
[514,487,0,503,473,489,488,498,492,448,510,469],
[553,517,498,0,475,568,508,529,514,509,502,556],
[577,476,528,526,0,542,504,505,497,536,547,516],
[532,466,512,433,459,0,437,475,506,493,532,530],
[569,547,513,493,497,564,0,550,527,502,542,590],
[505,507,503,472,496,526,451,0,528,502,529,514],
[503,475,509,487,504,495,474,473,0,502,514,496],
[517,476,553,492,465,508,499,499,499,0,512,529],
[500,463,491,499,454,469,459,472,487,489,0,468],
[535,513,532,445,485,471,411,487,505,472,533,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 129, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,539,532,527,538,490,491,560,523,515,518,488],
[462,0,504,437,422,414,404,427,404,482,432,432],
[469,497,0,539,414,416,488,511,410,430,470,480],
[474,564,462,0,417,435,428,438,442,430,452,457],
[463,579,587,584,0,572,500,575,509,517,453,467],
[511,587,585,566,429,0,513,552,592,536,549,527],
[510,597,513,573,501,488,0,552,516,511,461,446],
[441,574,490,563,426,449,449,0,483,510,444,452],
[478,597,591,559,492,409,485,518,0,565,428,457],
[486,519,571,571,484,465,490,491,436,0,468,541],
[483,569,531,549,548,452,540,557,573,533,0,515],
[513,569,521,544,534,474,555,549,544,460,486,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 130, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,500,492,504,515,503,539,516,516,512,495,509],
[501,0,524,521,512,509,539,515,524,525,500,508],
[509,477,0,497,507,496,535,482,510,497,505,509],
[497,480,504,0,497,497,542,503,527,509,491,504],
[486,489,494,504,0,499,553,489,508,515,486,492],
[498,492,505,504,502,0,533,504,528,516,484,512],
[462,462,466,459,448,468,0,467,491,480,471,467],
[485,486,519,498,512,497,534,0,503,516,495,512],
[485,477,491,474,493,473,510,498,0,516,482,484],
[489,476,504,492,486,485,521,485,485,0,496,491],
[506,501,496,510,515,517,530,506,519,505,0,524],
[492,493,492,497,509,489,534,489,517,510,477,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 131, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,504,496,512,522,546,482,505,502,512,522,491],
[497,0,491,488,496,502,485,519,487,499,487,483],
[505,510,0,497,515,512,511,511,501,497,516,488],
[489,513,504,0,489,505,503,511,502,520,485,489],
[479,505,486,512,0,497,495,493,479,509,502,496],
[455,499,489,496,504,0,486,496,460,480,494,481],
[519,516,490,498,506,515,0,481,508,499,501,473],
[496,482,490,490,508,505,520,0,497,489,504,474],
[499,514,500,499,522,541,493,504,0,500,502,492],
[489,502,504,481,492,521,502,512,501,0,507,509],
[479,514,485,516,499,507,500,497,499,494,0,494],
[510,518,513,512,505,520,528,527,509,492,507,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 132, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,512,520,504,519,509,495,506,521,497,496,512],
[489,0,521,499,518,510,512,504,517,492,508,532],
[481,480,0,483,499,492,477,473,508,471,481,490],
[497,502,518,0,514,502,489,508,529,500,497,526],
[482,483,502,487,0,484,487,459,486,501,485,477],
[492,491,509,499,517,0,485,495,517,501,486,524],
[506,489,524,512,514,516,0,502,485,512,498,517],
[495,497,528,493,542,506,499,0,516,501,508,510],
[480,484,493,472,515,484,516,485,0,490,481,514],
[504,509,530,501,500,500,489,500,511,0,496,493],
[505,493,520,504,516,515,503,493,520,505,0,541],
[489,469,511,475,524,477,484,491,487,508,460,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 133, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,508,488,472,491,496,478,472,478,455,484,512],
[493,0,472,482,506,466,473,496,476,489,483,504],
[513,529,0,497,554,502,533,501,514,515,542,517],
[529,519,504,0,522,537,495,510,519,482,524,526],
[510,495,447,479,0,524,472,464,520,461,516,489],
[505,535,499,464,477,0,494,507,519,447,503,486],
[523,528,468,506,529,507,0,496,538,480,529,515],
[529,505,500,491,537,494,505,0,503,473,495,490],
[523,525,487,482,481,482,463,498,0,494,515,485],
[546,512,486,519,540,554,521,528,507,0,521,512],
[517,518,459,477,485,498,472,506,486,480,0,495],
[489,497,484,475,512,515,486,511,516,489,506,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 134, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,494,495,520,498,501,565,494,505,514,504,508],
[507,0,484,512,503,489,536,496,486,519,501,513],
[506,517,0,526,501,495,524,540,519,516,483,524],
[481,489,475,0,525,468,527,477,498,507,484,500],
[503,498,500,476,0,491,514,530,489,510,486,515],
[500,512,506,533,510,0,543,503,508,555,505,508],
[436,465,477,474,487,458,0,488,444,472,450,469],
[507,505,461,524,471,498,513,0,486,512,506,506],
[496,515,482,503,512,493,557,515,0,521,491,513],
[487,482,485,494,491,446,529,489,480,0,485,505],
[497,500,518,517,515,496,551,495,510,516,0,516],
[493,488,477,501,486,493,532,495,488,496,485,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 135, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,514,504,507,496,491,511,512,493,524,497,472],
[487,0,482,485,489,509,473,504,522,473,494,473],
[497,519,0,519,515,540,504,496,513,504,532,453],
[494,516,482,0,503,498,517,486,520,487,492,487],
[505,512,486,498,0,504,460,494,499,497,493,471],
[510,492,461,503,497,0,485,497,513,466,508,494],
[490,528,497,484,541,516,0,522,511,509,491,492],
[489,497,505,515,507,504,479,0,501,522,513,511],
[508,479,488,481,502,488,490,500,0,467,479,474],
[477,528,497,514,504,535,492,479,534,0,516,496],
[504,507,469,509,508,493,510,488,522,485,0,475],
[529,528,548,514,530,507,509,490,527,505,526,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 136, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,527,500,504,456,483,468,491,497,498,470,494],
[474,0,490,504,463,485,479,496,502,508,498,504],
[501,511,0,494,482,496,499,520,515,500,514,501],
[497,497,507,0,471,489,484,524,509,489,512,498],
[545,538,519,530,0,491,505,539,520,511,508,519],
[518,516,505,512,510,0,501,526,533,505,495,531],
[533,522,502,517,496,500,0,524,491,527,485,509],
[510,505,481,477,462,475,477,0,500,503,473,484],
[504,499,486,492,481,468,510,501,0,496,497,488],
[503,493,501,512,490,496,474,498,505,0,497,511],
[531,503,487,489,493,506,516,528,504,504,0,517],
[507,497,500,503,482,470,492,517,513,490,484,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 137, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,504,496,480,474,488,477,478,491,507,497,473],
[497,0,495,494,495,507,500,461,515,497,481,481],
[505,506,0,499,493,518,512,482,535,504,516,500],
[521,507,502,0,511,499,524,481,538,538,494,498],
[527,506,508,490,0,515,511,517,533,520,512,501],
[513,494,483,502,486,0,497,487,501,490,491,473],
[524,501,489,477,490,504,0,479,520,497,500,514],
[523,540,519,520,484,514,522,0,543,511,518,517],
[510,486,466,463,468,500,481,458,0,481,480,458],
[494,504,497,463,481,511,504,490,520,0,487,473],
[504,520,485,507,489,510,501,483,521,514,0,506],
[528,520,501,503,500,528,487,484,543,528,495,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 138, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,489,495,497,470,495,500,497,484,459,505,470],
[512,0,488,530,493,505,517,494,486,485,487,477],
[506,513,0,523,468,510,501,469,504,453,489,488],
[504,471,478,0,469,486,503,486,471,476,486,458],
[531,508,533,532,0,539,521,514,502,497,533,490],
[506,496,491,515,462,0,522,489,489,477,491,471],
[501,484,500,498,480,479,0,481,496,477,487,475],
[504,507,532,515,487,512,520,0,508,489,535,503],
[517,515,497,530,499,512,505,493,0,487,498,484],
[542,516,548,525,504,524,524,512,514,0,512,479],
[496,514,512,515,468,510,514,466,503,489,0,492],
[531,524,513,543,511,530,526,498,517,522,509,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 139, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,513,465,488,490,508,442,441,478,490,467,503],
[488,0,477,477,506,490,472,483,496,454,472,500],
[536,524,0,502,535,506,507,474,513,513,500,505],
[513,524,499,0,538,526,486,506,499,491,491,518],
[511,495,466,463,0,471,524,462,510,471,470,455],
[493,511,495,475,530,0,444,514,529,489,494,475],
[559,529,494,515,477,557,0,507,496,521,503,528],
[560,518,527,495,539,487,494,0,519,502,502,529],
[523,505,488,502,491,472,505,482,0,489,485,468],
[511,547,488,510,530,512,480,499,512,0,527,537],
[534,529,501,510,531,507,498,499,516,474,0,507],
[498,501,496,483,546,526,473,472,533,464,494,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 140, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,463,458,661,114,525,405,525,512,688,456,245],
[538,0,476,563,456,751,497,471,703,574,695,391],
[543,525,0,576,322,777,690,437,574,733,733,450],
[340,438,425,0,196,708,572,689,487,585,427,376],
[887,545,679,805,0,702,615,898,556,849,484,849],
[476,250,224,293,299,0,443,501,443,248,394,335],
[596,504,311,429,386,558,0,588,430,384,530,442],
[476,530,564,312,103,500,413,0,443,603,456,456],
[489,298,427,514,445,558,571,558,0,481,633,530],
[313,427,268,416,152,753,617,398,520,0,476,136],
[545,306,268,574,517,607,471,545,368,525,0,378],
[756,610,551,625,152,666,559,545,471,865,623,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 141, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,477,508,513,505,461,502,505,500,537,488,476],
[524,0,488,522,516,457,553,511,508,524,487,495],
[493,513,0,543,510,480,484,580,527,539,513,473],
[488,479,458,0,449,445,464,528,447,498,454,388],
[496,485,491,552,0,461,521,527,464,453,487,467],
[540,544,521,556,540,0,575,569,536,528,538,493],
[499,448,517,537,480,426,0,521,457,488,488,439],
[496,490,421,473,474,432,480,0,469,493,441,442],
[501,493,474,554,537,465,544,532,0,543,498,509],
[464,477,462,503,548,473,513,508,458,0,505,458],
[513,514,488,547,514,463,513,560,503,496,0,486],
[525,506,528,613,534,508,562,559,492,543,515,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 142, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,474,472,505,512,474,490,514,504,498,516,525],
[527,0,511,496,511,501,534,541,517,499,531,516],
[529,490,0,511,527,509,532,534,533,510,515,526],
[496,505,490,0,500,491,509,511,490,486,493,506],
[489,490,474,501,0,494,520,523,503,512,505,482],
[527,500,492,510,507,0,522,550,519,502,513,526],
[511,467,469,492,481,479,0,498,505,471,487,515],
[487,460,467,490,478,451,503,0,488,468,468,463],
[497,484,468,511,498,482,496,513,0,472,500,512],
[503,502,491,515,489,499,530,533,529,0,495,521],
[485,470,486,508,496,488,514,533,501,506,0,477],
[476,485,475,495,519,475,486,538,489,480,524,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 143, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,492,458,474,479,509,494,482,487,467,486,513],
[509,0,463,464,502,486,465,494,497,465,509,520],
[543,538,0,504,509,508,501,502,523,489,519,525],
[527,537,497,0,497,516,483,491,504,488,502,522],
[522,499,492,504,0,493,484,541,505,494,502,531],
[492,515,493,485,508,0,497,500,505,487,496,512],
[507,536,500,518,517,504,0,530,534,489,516,525],
[519,507,499,510,460,501,471,0,514,484,488,536],
[514,504,478,497,496,496,467,487,0,484,490,502],
[534,536,512,513,507,514,512,517,517,0,499,540],
[515,492,482,499,499,505,485,513,511,502,0,512],
[488,481,476,479,470,489,476,465,499,461,489,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 144, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,502,529,524,531,518,543,513,528,513,493,499],
[499,0,519,497,536,543,566,537,549,528,520,526],
[472,482,0,495,489,463,521,502,504,485,519,480],
[477,504,506,0,513,531,518,514,512,508,501,512],
[470,465,512,488,0,470,504,494,517,493,458,471],
[483,458,538,470,531,0,542,482,521,482,487,506],
[458,435,480,483,497,459,0,488,493,482,462,444],
[488,464,499,487,507,519,513,0,493,509,477,504],
[473,452,497,489,484,480,508,508,0,481,479,504],
[488,473,516,493,508,519,519,492,520,0,475,490],
[508,481,482,500,543,514,539,524,522,526,0,512],
[502,475,521,489,530,495,557,497,497,511,489,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 145, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,318,462,641,435,460,516,437,507,476,380,434],
[683,0,418,658,330,354,687,434,620,547,621,494],
[539,583,0,756,497,554,668,557,575,614,464,469],
[360,343,245,0,300,235,474,334,245,336,304,215],
[566,671,504,701,0,451,622,379,561,553,588,411],
[541,647,447,766,550,0,693,572,643,632,581,510],
[485,314,333,527,379,308,0,387,548,425,395,379],
[564,567,444,667,622,429,614,0,450,497,505,455],
[494,381,426,756,440,358,453,551,0,516,406,368],
[525,454,387,665,448,369,576,504,485,0,499,484],
[621,380,537,697,413,420,606,496,595,502,0,409],
[567,507,532,786,590,491,622,546,633,517,592,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 146, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,502,498,511,541,505,546,515,540,490,560,553],
[499,0,481,462,503,529,528,508,517,485,530,510],
[503,520,0,500,515,509,542,518,526,516,558,506],
[490,539,501,0,491,516,532,508,490,491,511,524],
[460,498,486,510,0,488,527,514,504,474,512,522],
[496,472,492,485,513,0,534,495,503,485,526,496],
[455,473,459,469,474,467,0,466,515,440,501,479],
[486,493,483,493,487,506,535,0,495,496,523,507],
[461,484,475,511,497,498,486,506,0,476,492,477],
[511,516,485,510,527,516,561,505,525,0,529,540],
[441,471,443,490,489,475,500,478,509,472,0,490],
[448,491,495,477,479,505,522,494,524,461,511,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 147, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,521,486,514,544,593,509,575,543,518,537,518],
[480,0,477,437,500,490,475,443,463,479,457,469],
[515,524,0,574,566,575,452,556,498,506,520,456],
[487,564,427,0,527,498,579,523,520,487,496,530],
[457,501,435,474,0,495,453,538,426,485,478,492],
[408,511,426,503,506,0,469,505,456,456,471,456],
[492,526,549,422,548,532,0,558,477,461,475,441],
[426,558,445,478,463,496,443,0,421,448,475,448],
[458,538,503,481,575,545,524,580,0,499,541,514],
[483,522,495,514,516,545,540,553,502,0,508,461],
[464,544,481,505,523,530,526,526,460,493,0,489],
[483,532,545,471,509,545,560,553,487,540,512,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 148, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,511,500,528,526,510,508,525,511,527,535,503],
[490,0,470,500,521,481,499,490,515,487,495,511],
[501,531,0,541,517,486,497,536,519,518,525,509],
[473,501,460,0,507,473,483,508,500,479,498,493],
[475,480,484,494,0,479,504,492,503,508,499,470],
[491,520,515,528,522,0,540,519,514,514,513,513],
[493,502,504,518,497,461,0,494,500,505,503,506],
[476,511,465,493,509,482,507,0,499,502,503,520],
[490,486,482,501,498,487,501,502,0,478,500,482],
[474,514,483,522,493,487,496,499,523,0,508,508],
[466,506,476,503,502,488,498,498,501,493,0,486],
[498,490,492,508,531,488,495,481,519,493,515,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 149, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,498,503,506,464,499,437,488,486,470,478,537],
[503,0,517,487,478,486,508,476,445,487,518,525],
[498,484,0,480,452,523,463,476,454,498,484,534],
[495,514,521,0,501,532,488,509,475,507,470,526],
[537,523,549,500,0,567,508,519,525,525,535,562],
[502,515,478,469,434,0,460,475,477,472,422,531],
[564,493,538,513,493,541,0,510,512,508,500,560],
[513,525,525,492,482,526,491,0,482,510,488,543],
[515,556,547,526,476,524,489,519,0,515,502,598],
[531,514,503,494,476,529,493,491,486,0,505,525],
[523,483,517,531,466,579,501,513,499,496,0,521],
[464,476,467,475,439,470,441,458,403,476,480,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 150, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,537,501,539,473,484,496,519,515,502,519,523],
[464,0,482,470,432,475,460,473,459,470,472,484],
[500,519,0,525,512,505,468,491,502,463,489,521],
[462,531,476,0,430,475,506,450,467,453,522,502],
[528,569,489,571,0,559,516,523,494,525,532,512],
[517,526,496,526,442,0,524,487,487,477,493,525],
[505,541,533,495,485,477,0,523,497,489,535,526],
[482,528,510,551,478,514,478,0,497,527,536,507],
[486,542,499,534,507,514,504,504,0,482,535,526],
[499,531,538,548,476,524,512,474,519,0,562,537],
[482,529,512,479,469,508,466,465,466,439,0,497],
[478,517,480,499,489,476,475,494,475,464,504,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 151, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,484,508,483,493,467,540,525,397,469,462,512],
[517,0,526,477,500,479,457,507,454,482,567,479],
[493,475,0,476,447,451,459,518,437,519,531,445],
[518,524,525,0,504,471,496,562,484,530,555,496],
[508,501,554,497,0,463,473,472,452,522,519,472],
[534,522,550,530,538,0,503,533,523,558,572,490],
[461,544,542,505,528,498,0,564,459,521,574,512],
[476,494,483,439,529,468,437,0,445,527,483,440],
[604,547,564,517,549,478,542,556,0,567,558,523],
[532,519,482,471,479,443,480,474,434,0,559,453],
[539,434,470,446,482,429,427,518,443,442,0,490],
[489,522,556,505,529,511,489,561,478,548,511,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 152, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,510,464,486,463,539,458,482,512,464,448,506],
[491,0,513,508,491,567,476,489,503,509,479,489],
[537,488,0,533,491,614,509,518,542,478,480,551],
[515,493,468,0,479,537,467,492,535,482,450,523],
[538,510,510,522,0,574,483,490,497,485,492,513],
[462,434,387,464,427,0,411,428,435,443,402,461],
[543,525,492,534,518,590,0,468,530,531,508,528],
[519,512,483,509,511,573,533,0,504,539,471,531],
[489,498,459,466,504,566,471,497,0,506,474,520],
[537,492,523,519,516,558,470,462,495,0,471,538],
[553,522,521,551,509,599,493,530,527,530,0,534],
[495,512,450,478,488,540,473,470,481,463,467,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 153, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,507,515,536,501,534,499,536,525,522,504,516],
[494,0,503,521,496,527,503,518,507,487,498,515],
[486,498,0,517,502,517,504,502,498,507,522,494],
[465,480,484,0,493,507,476,490,478,495,478,490],
[500,505,499,508,0,501,486,500,506,507,489,502],
[467,474,484,494,500,0,493,486,504,487,467,494],
[502,498,497,525,515,508,0,504,512,512,496,525],
[465,483,499,511,501,515,497,0,527,505,514,490],
[476,494,503,523,495,497,489,474,0,518,513,492],
[479,514,494,506,494,514,489,496,483,0,479,483],
[497,503,479,523,512,534,505,487,488,522,0,502],
[485,486,507,511,499,507,476,511,509,518,499,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 154, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,506,494,505,532,535,500,525,506,502,495,483],
[495,0,488,485,493,514,494,501,495,501,482,467],
[507,513,0,495,504,508,514,527,499,497,500,495],
[496,516,506,0,501,528,515,527,532,513,505,507],
[469,508,497,500,0,529,493,523,495,506,493,484],
[466,487,493,473,472,0,472,510,493,488,454,481],
[501,507,487,486,508,529,0,541,512,513,499,509],
[476,500,474,474,478,491,460,0,481,492,462,487],
[495,506,502,469,506,508,489,520,0,513,492,496],
[499,500,504,488,495,513,488,509,488,0,506,508],
[506,519,501,496,508,547,502,539,509,495,0,503],
[518,534,506,494,517,520,492,514,505,493,498,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 155, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,470,458,491,431,425,471,411,518,543,467,506],
[531,0,447,515,449,437,487,501,513,557,527,565],
[543,554,0,576,506,453,472,526,521,558,574,615],
[510,486,425,0,424,470,512,546,537,548,498,534],
[570,552,495,577,0,503,545,486,527,593,571,560],
[576,564,548,531,498,0,535,522,532,617,558,603],
[530,514,529,489,456,466,0,493,554,597,544,526],
[590,500,475,455,515,479,508,0,522,598,605,552],
[483,488,480,464,474,469,447,479,0,562,598,546],
[458,444,443,453,408,384,404,403,439,0,504,460],
[534,474,427,503,430,443,457,396,403,497,0,467],
[495,436,386,467,441,398,475,449,455,541,534,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 156, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,479,486,492,518,453,494,475,493,480,482,464],
[522,0,509,520,532,488,510,498,500,508,484,454],
[515,492,0,512,520,470,504,500,488,501,493,475],
[509,481,489,0,478,461,491,515,499,521,490,475],
[483,469,481,523,0,439,520,512,481,493,480,460],
[548,513,531,540,562,0,558,524,529,510,539,500],
[507,491,497,510,481,443,0,477,479,480,459,461],
[526,503,501,486,489,477,524,0,485,489,482,435],
[508,501,513,502,520,472,522,516,0,518,499,514],
[521,493,500,480,508,491,521,512,483,0,483,460],
[519,517,508,511,521,462,542,519,502,518,0,506],
[537,547,526,526,541,501,540,566,487,541,495,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 157, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,446,448,453,443,424,447,539,519,478,487,466],
[555,0,479,522,494,468,463,610,561,489,544,500],
[553,522,0,492,597,521,548,628,587,524,568,504],
[548,479,509,0,494,490,506,595,514,505,535,462],
[558,507,404,507,0,438,440,590,509,442,521,506],
[577,533,480,511,563,0,479,592,535,488,574,487],
[554,538,453,495,561,522,0,607,596,499,572,512],
[462,391,373,406,411,409,394,0,474,437,486,456],
[482,440,414,487,492,466,405,527,0,446,431,412],
[523,512,477,496,559,513,502,564,555,0,559,507],
[514,457,433,466,480,427,429,515,570,442,0,467],
[535,501,497,539,495,514,489,545,589,494,534,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 158, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,502,492,485,480,497,494,475,511,508,520,484],
[499,0,485,483,477,488,496,482,494,486,507,492],
[509,516,0,520,500,503,490,506,524,494,519,508],
[516,518,481,0,484,497,489,506,507,516,511,492],
[521,524,501,517,0,530,499,514,519,505,523,518],
[504,513,498,504,471,0,504,488,497,497,502,486],
[507,505,511,512,502,497,0,505,505,519,512,496],
[526,519,495,495,487,513,496,0,518,516,516,512],
[490,507,477,494,482,504,496,483,0,511,505,477],
[493,515,507,485,496,504,482,485,490,0,508,503],
[481,494,482,490,478,499,489,485,496,493,0,481],
[517,509,493,509,483,515,505,489,524,498,520,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 159, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,480,490,508,467,467,492,491,497,496,445,461],
[521,0,455,539,480,508,482,475,526,507,477,506],
[511,546,0,552,543,523,528,526,509,511,484,473],
[493,462,449,0,474,499,469,489,487,491,469,422],
[534,521,458,527,0,537,496,504,513,535,485,486],
[534,493,478,502,464,0,497,512,511,518,490,482],
[509,519,473,532,505,504,0,525,509,555,532,497],
[510,526,475,512,497,489,476,0,502,551,485,473],
[504,475,492,514,488,490,492,499,0,523,472,488],
[505,494,490,510,466,483,446,450,478,0,446,477],
[556,524,517,532,516,511,469,516,529,555,0,469],
[540,495,528,579,515,519,504,528,513,524,532,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 160, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,494,497,529,503,548,501,483,531,530,529,527],
[507,0,456,510,516,519,467,472,506,528,470,513],
[504,545,0,510,506,527,505,519,505,526,499,481],
[472,491,491,0,473,521,492,478,475,488,490,498],
[498,485,495,528,0,516,474,482,512,501,517,526],
[453,482,474,480,485,0,462,488,475,491,484,511],
[500,534,496,509,527,539,0,509,512,501,490,529],
[518,529,482,523,519,513,492,0,529,546,494,555],
[470,495,496,526,489,526,489,472,0,477,478,492],
[471,473,475,513,500,510,500,455,524,0,494,512],
[472,531,502,511,484,517,511,507,523,507,0,506],
[474,488,520,503,475,490,472,446,509,489,495,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 161, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,506,539,518,512,553,525,553,556,464,553,500],
[495,0,518,512,531,509,527,517,537,473,517,489],
[462,483,0,500,488,492,527,555,520,478,496,450],
[483,489,501,0,510,502,494,541,555,502,507,478],
[489,470,513,491,0,517,531,553,545,476,511,504],
[448,492,509,499,484,0,520,493,571,506,499,478],
[476,474,474,507,470,481,0,500,498,471,473,438],
[448,484,446,460,448,508,501,0,512,439,499,426],
[445,464,481,446,456,430,503,489,0,427,475,440],
[537,528,523,499,525,495,530,562,574,0,527,499],
[448,484,505,494,490,502,528,502,526,474,0,457],
[501,512,551,523,497,523,563,575,561,502,544,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 162, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,513,484,496,483,511,493,507,465,478,496,490],
[488,0,468,493,496,499,490,514,502,484,491,494],
[517,533,0,512,496,495,526,514,509,530,505,524],
[505,508,489,0,498,502,491,512,484,517,514,512],
[518,505,505,503,0,499,520,515,501,522,525,533],
[490,502,506,499,502,0,492,511,483,502,501,509],
[508,511,475,510,481,509,0,505,504,506,504,506],
[494,487,487,489,486,490,496,0,492,498,490,507],
[536,499,492,517,500,518,497,509,0,518,517,517],
[523,517,471,484,479,499,495,503,483,0,495,506],
[505,510,496,487,476,500,497,511,484,506,0,496],
[511,507,477,489,468,492,495,494,484,495,505,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 163, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,519,489,492,496,493,478,502,494,519,519,516],
[482,0,493,464,489,488,456,480,454,492,472,464],
[512,508,0,486,504,476,487,506,501,497,503,502],
[509,537,515,0,506,510,488,527,468,517,509,483],
[505,512,497,495,0,499,482,513,494,546,501,519],
[508,513,525,491,502,0,484,497,473,542,524,485],
[523,545,514,513,519,517,0,513,519,534,534,498],
[499,521,495,474,488,504,488,0,487,502,530,507],
[507,547,500,533,507,528,482,514,0,536,517,514],
[482,509,504,484,455,459,467,499,465,0,498,475],
[482,529,498,492,500,477,467,471,484,503,0,457],
[485,537,499,518,482,516,503,494,487,526,544,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 164, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,478,490,464,501,509,479,491,542,509,468,479],
[523,0,507,512,503,535,535,515,529,510,500,491],
[511,494,0,509,523,525,525,516,531,468,486,500],
[537,489,492,0,491,508,506,507,542,504,511,488],
[500,498,478,510,0,526,493,497,533,497,514,483],
[492,466,476,493,475,0,493,494,525,469,467,501],
[522,466,476,495,508,508,0,482,534,485,496,511],
[510,486,485,494,504,507,519,0,503,486,475,507],
[459,472,470,459,468,476,467,498,0,479,457,466],
[492,491,533,497,504,532,516,515,522,0,505,507],
[533,501,515,490,487,534,505,526,544,496,0,510],
[522,510,501,513,518,500,490,494,535,494,491,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 165, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,596,533,477,596,591,660,540,528,552,529,667],
[405,0,564,525,489,533,512,560,530,546,521,519],
[468,437,0,527,370,522,563,517,382,399,340,473],
[524,476,474,0,364,644,608,626,604,520,397,601],
[405,512,631,637,0,618,391,501,523,569,551,483],
[410,468,479,357,383,0,484,439,448,482,495,403],
[341,489,438,393,610,517,0,589,485,586,475,535],
[461,441,484,375,500,562,412,0,401,534,524,517],
[473,471,619,397,478,553,516,600,0,490,506,568],
[449,455,602,481,432,519,415,467,511,0,589,635],
[472,480,661,604,450,506,526,477,495,412,0,591],
[334,482,528,400,518,598,466,484,433,366,410,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 166, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,504,504,512,530,528,511,506,555,508,542,489],
[497,0,479,467,481,494,490,470,510,475,482,487],
[497,522,0,524,508,508,513,477,510,540,515,511],
[489,534,477,0,511,510,519,498,489,533,507,493],
[471,520,493,490,0,510,510,495,489,471,523,481],
[473,507,493,491,491,0,485,471,510,517,501,487],
[490,511,488,482,491,516,0,477,516,495,505,503],
[495,531,524,503,506,530,524,0,527,526,530,507],
[446,491,491,512,512,491,485,474,0,494,510,479],
[493,526,461,468,530,484,506,475,507,0,496,492],
[459,519,486,494,478,500,496,471,491,505,0,460],
[512,514,490,508,520,514,498,494,522,509,541,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 167, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,493,488,522,538,534,520,540,460,511,487,459],
[508,0,469,539,477,477,543,529,471,503,511,469],
[513,532,0,545,509,587,497,546,501,529,506,495],
[479,462,456,0,472,507,482,527,451,461,486,444],
[463,524,492,529,0,484,488,558,464,489,472,451],
[467,524,414,494,517,0,576,525,447,463,504,424],
[481,458,504,519,513,425,0,463,408,448,448,472],
[461,472,455,474,443,476,538,0,388,445,494,449],
[541,530,500,550,537,554,593,613,0,518,592,529],
[490,498,472,540,512,538,553,556,483,0,545,488],
[514,490,495,515,529,497,553,507,409,456,0,421],
[542,532,506,557,550,577,529,552,472,513,580,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 168, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,560,508,505,512,488,526,529,506,530,508,502],
[441,0,491,458,485,471,463,486,454,490,480,457],
[493,510,0,474,473,494,515,501,493,527,481,467],
[496,543,527,0,493,508,482,515,491,526,491,484],
[489,516,528,508,0,506,496,507,504,540,470,478],
[513,530,507,493,495,0,498,517,495,530,491,517],
[475,538,486,519,505,503,0,505,518,538,495,498],
[472,515,500,486,494,484,496,0,517,512,485,480],
[495,547,508,510,497,506,483,484,0,524,493,479],
[471,511,474,475,461,471,463,489,477,0,474,483],
[493,521,520,510,531,510,506,516,508,527,0,496],
[499,544,534,517,523,484,503,521,522,518,505,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 169, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,487,494,509,498,458,459,473,458,508,513,491],
[514,0,497,517,544,500,476,459,487,495,522,529],
[507,504,0,498,547,480,486,489,481,482,519,504],
[492,484,503,0,496,476,467,458,452,509,494,503],
[503,457,454,505,0,468,449,488,476,501,488,494],
[543,501,521,525,533,0,501,509,504,500,547,527],
[542,525,515,534,552,500,0,499,506,535,536,550],
[528,542,512,543,513,492,502,0,497,522,501,523],
[543,514,520,549,525,497,495,504,0,509,553,539],
[493,506,519,492,500,501,466,479,492,0,515,522],
[488,479,482,507,513,454,465,500,448,486,0,500],
[510,472,497,498,507,474,451,478,462,479,501,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 170, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,552,490,496,505,501,498,509,544,511,500,518],
[449,0,493,492,464,469,471,456,497,477,486,484],
[511,508,0,493,480,474,469,490,520,501,492,475],
[505,509,508,0,484,481,501,482,516,513,515,511],
[496,537,521,517,0,482,471,480,529,507,532,525],
[500,532,527,520,519,0,531,502,547,511,519,517],
[503,530,532,500,530,470,0,503,534,493,516,505],
[492,545,511,519,521,499,498,0,537,540,515,534],
[457,504,481,485,472,454,467,464,0,458,468,483],
[490,524,500,488,494,490,508,461,543,0,507,502],
[501,515,509,486,469,482,485,486,533,494,0,526],
[483,517,526,490,476,484,496,467,518,499,475,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 171, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,463,492,533,497,493,501,481,485,494,499,523],
[538,0,519,560,541,545,490,508,519,560,521,505],
[509,482,0,555,529,530,484,494,543,548,540,530],
[468,441,446,0,509,510,463,462,463,499,507,469],
[504,460,472,492,0,459,467,453,485,492,531,491],
[508,456,471,491,542,0,461,451,512,487,485,474],
[500,511,517,538,534,540,0,494,515,546,520,520],
[520,493,507,539,548,550,507,0,523,569,524,526],
[516,482,458,538,516,489,486,478,0,511,517,503],
[507,441,453,502,509,514,455,432,490,0,502,476],
[502,480,461,494,470,516,481,477,484,499,0,472],
[478,496,471,532,510,527,481,475,498,525,529,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 172, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,467,429,426,647,487,494,290,832,559,422,660],
[534,0,161,292,411,439,416,165,674,535,319,567],
[572,840,0,555,480,793,558,552,806,657,493,823],
[575,709,446,0,502,464,381,240,477,418,359,662],
[354,590,521,499,0,515,456,509,480,659,406,732],
[514,562,208,537,486,0,338,350,552,408,340,756],
[507,585,443,620,545,663,0,405,717,678,491,821],
[711,836,449,761,492,651,596,0,755,627,652,618],
[169,327,195,524,521,449,284,246,0,468,298,568],
[442,466,344,583,342,593,323,374,533,0,295,699],
[579,682,508,642,595,661,510,349,703,706,0,682],
[341,434,178,339,269,245,180,383,433,302,319,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 173, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,574,534,514,507,524,458,517,541,514,544,506],
[427,0,496,460,447,486,439,499,500,468,491,466],
[467,505,0,459,447,460,454,502,475,445,468,463],
[487,541,542,0,510,531,505,532,507,501,527,477],
[494,554,554,491,0,525,471,507,511,493,547,491],
[477,515,541,470,476,0,475,518,521,507,516,488],
[543,562,547,496,530,526,0,529,550,507,521,519],
[484,502,499,469,494,483,472,0,512,498,491,465],
[460,501,526,494,490,480,451,489,0,482,501,450],
[487,533,556,500,508,494,494,503,519,0,525,478],
[457,510,533,474,454,485,480,510,500,476,0,451],
[495,535,538,524,510,513,482,536,551,523,550,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 174, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,486,515,494,487,424,476,452,495,439,493,459],
[515,0,492,508,498,471,481,483,511,480,481,487],
[486,509,0,510,517,470,498,468,480,462,502,487],
[507,493,491,0,501,475,490,450,475,441,495,495],
[514,503,484,500,0,462,480,478,474,476,484,483],
[577,530,531,526,539,0,485,530,542,505,534,520],
[525,520,503,511,521,516,0,483,499,497,522,508],
[549,518,533,551,523,471,518,0,519,505,530,502],
[506,490,521,526,527,459,502,482,0,479,505,497],
[562,521,539,560,525,496,504,496,522,0,537,504],
[508,520,499,506,517,467,479,471,496,464,0,469],
[542,514,514,506,518,481,493,499,504,497,532,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 175, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,504,418,455,461,492,514,494,463,458,481,468],
[497,0,447,456,475,471,480,473,495,476,410,450],
[583,554,0,505,518,544,533,520,516,499,511,511],
[546,545,496,0,523,512,553,519,483,517,485,521],
[540,526,483,478,0,482,528,529,490,529,508,478],
[509,530,457,489,519,0,518,481,489,508,463,501],
[487,521,468,448,473,483,0,483,495,467,449,492],
[507,528,481,482,472,520,518,0,475,521,440,497],
[538,506,485,518,511,512,506,526,0,538,476,489],
[543,525,502,484,472,493,534,480,463,0,449,482],
[520,591,490,516,493,538,552,561,525,552,0,506],
[533,551,490,480,523,500,509,504,512,519,495,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 176, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,496,511,484,480,454,478,481,519,523,515,489],
[505,0,568,545,529,515,498,509,537,548,531,525],
[490,433,0,487,482,459,459,444,485,499,501,468],
[517,456,514,0,471,441,454,484,492,502,499,488],
[521,472,519,530,0,476,498,497,546,506,516,504],
[547,486,542,560,525,0,509,507,546,546,559,519],
[523,503,542,547,503,492,0,529,527,531,516,507],
[520,492,557,517,504,494,472,0,558,547,533,525],
[482,464,516,509,455,455,474,443,0,490,507,455],
[478,453,502,499,495,455,470,454,511,0,499,460],
[486,470,500,502,485,442,485,468,494,502,0,499],
[512,476,533,513,497,482,494,476,546,541,502,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 177, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,483,455,498,488,468,511,483,471,495,500,465],
[518,0,473,507,513,504,520,495,498,522,503,504],
[546,528,0,556,509,538,516,540,511,525,490,524],
[503,494,445,0,498,487,504,493,476,495,495,492],
[513,488,492,503,0,500,505,510,461,513,528,488],
[533,497,463,514,501,0,513,507,478,528,511,487],
[490,481,485,497,496,488,0,523,470,503,506,496],
[518,506,461,508,491,494,478,0,450,515,522,503],
[530,503,490,525,540,523,531,551,0,537,545,521],
[506,479,476,506,488,473,498,486,464,0,496,495],
[501,498,511,506,473,490,495,479,456,505,0,492],
[536,497,477,509,513,514,505,498,480,506,509,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 178, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,506,471,524,501,511,504,513,518,549,504,450],
[495,0,485,563,484,481,503,478,527,542,484,495],
[530,516,0,538,481,481,517,534,502,508,518,563],
[477,438,463,0,482,446,502,445,517,522,441,470],
[500,517,520,519,0,464,506,497,555,524,491,526],
[490,520,520,555,537,0,518,481,534,559,487,498],
[497,498,484,499,495,483,0,536,521,505,511,519],
[488,523,467,556,504,520,465,0,503,514,484,496],
[483,474,499,484,446,467,480,498,0,480,495,453],
[452,459,493,479,477,442,496,487,521,0,466,475],
[497,517,483,560,510,514,490,517,506,535,0,515],
[551,506,438,531,475,503,482,505,548,526,486,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 179, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,512,513,518,487,538,573,492,522,549,515,505],
[489,0,494,474,464,498,513,459,495,490,499,477],
[488,507,0,512,466,509,524,459,490,492,483,478],
[483,527,489,0,464,501,534,500,502,509,491,499],
[514,537,535,537,0,528,543,493,509,513,531,493],
[463,503,492,500,473,0,500,483,480,496,496,488],
[428,488,477,467,458,501,0,446,472,482,478,431],
[509,542,542,501,508,518,555,0,521,548,520,494],
[479,506,511,499,492,521,529,480,0,507,491,485],
[452,511,509,492,488,505,519,453,494,0,501,460],
[486,502,518,510,470,505,523,481,510,500,0,501],
[496,524,523,502,508,513,570,507,516,541,500,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 180, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,441,456,449,443,476,480,483,458,495,488,459],
[560,0,500,504,498,529,510,541,477,528,520,467],
[545,501,0,491,502,513,509,520,489,540,507,485],
[552,497,510,0,524,556,523,557,505,553,533,500],
[558,503,499,477,0,518,502,505,499,546,500,485],
[525,472,488,445,483,0,469,482,466,516,492,469],
[521,491,492,478,499,532,0,525,446,524,507,461],
[518,460,481,444,496,519,476,0,462,508,484,467],
[543,524,512,496,502,535,555,539,0,541,522,501],
[506,473,461,448,455,485,477,493,460,0,518,436],
[513,481,494,468,501,509,494,517,479,483,0,464],
[542,534,516,501,516,532,540,534,500,565,537,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 181, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,533,519,525,489,519,511,521,516,535,512,510],
[468,0,470,504,472,510,504,497,493,506,505,475],
[482,531,0,521,488,507,528,505,496,530,499,496],
[476,497,480,0,473,508,502,478,475,505,505,467],
[512,529,513,528,0,516,508,484,506,530,532,509],
[482,491,494,493,485,0,505,484,476,499,482,482],
[490,497,473,499,493,496,0,474,488,526,504,481],
[480,504,496,523,517,517,527,0,501,513,510,483],
[485,508,505,526,495,525,513,500,0,530,504,514],
[466,495,471,496,471,502,475,488,471,0,496,482],
[489,496,502,496,469,519,497,491,497,505,0,480],
[491,526,505,534,492,519,520,518,487,519,521,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 182, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,514,509,482,513,512,497,520,510,517,498,498],
[487,0,476,473,483,480,490,499,503,473,504,515],
[492,525,0,503,508,504,504,544,527,484,503,525],
[519,528,498,0,514,515,508,544,540,488,517,543],
[488,518,493,487,0,489,479,502,518,482,513,521],
[489,521,497,486,512,0,492,514,508,497,513,505],
[504,511,497,493,522,509,0,515,515,496,488,537],
[481,502,457,457,499,487,486,0,489,487,499,491],
[491,498,474,461,483,493,486,512,0,489,507,506],
[484,528,517,513,519,504,505,514,512,0,501,522],
[503,497,498,484,488,488,513,502,494,500,0,511],
[503,486,476,458,480,496,464,510,495,479,490,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 183, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,511,500,504,500,504,483,515,493,489,485,479],
[490,0,501,472,498,506,465,496,522,470,503,501],
[501,500,0,467,476,487,466,486,498,456,467,473],
[497,529,534,0,510,496,485,521,512,481,486,493],
[501,503,525,491,0,492,464,508,500,506,486,474],
[497,495,514,505,509,0,473,511,504,495,491,496],
[518,536,535,516,537,528,0,521,514,529,525,495],
[486,505,515,480,493,490,480,0,511,484,500,504],
[508,479,503,489,501,497,487,490,0,470,480,461],
[512,531,545,520,495,506,472,517,531,0,490,508],
[516,498,534,515,515,510,476,501,521,511,0,491],
[522,500,528,508,527,505,506,497,540,493,510,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 184, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,473,509,542,476,457,490,475,496,508,508,536],
[528,0,524,531,509,482,483,485,514,530,543,536],
[492,477,0,518,484,455,478,473,479,485,508,503],
[459,470,483,0,447,457,449,417,433,489,454,508],
[525,492,517,554,0,493,475,500,516,528,522,535],
[544,519,546,544,508,0,542,483,487,517,493,532],
[511,518,523,552,526,459,0,473,465,509,533,509],
[526,516,528,584,501,518,528,0,499,539,542,562],
[505,487,522,568,485,514,536,502,0,532,522,534],
[493,471,516,512,473,484,492,462,469,0,486,523],
[493,458,493,547,479,508,468,459,479,515,0,519],
[465,465,498,493,466,469,492,439,467,478,482,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 185, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,452,409,609,432,516,511,536,511,511,576,384],
[549,0,547,584,498,551,545,492,644,596,597,544],
[592,454,0,591,456,461,451,462,571,430,516,453],
[392,417,410,0,408,462,505,406,420,456,442,395],
[569,503,545,593,0,592,528,497,507,562,524,466],
[485,450,540,539,409,0,481,461,558,536,507,519],
[490,456,550,496,473,520,0,413,505,491,505,493],
[465,509,539,595,504,540,588,0,537,588,545,437],
[490,357,430,581,494,443,496,464,0,538,480,417],
[490,405,571,545,439,465,510,413,463,0,507,471],
[425,404,485,559,477,494,496,456,521,494,0,469],
[617,457,548,606,535,482,508,564,584,530,532,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 186, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,458,484,519,526,501,477,526,509,550,557,571],
[543,0,492,452,572,465,484,498,493,471,547,606],
[517,509,0,464,547,442,470,494,461,531,536,536],
[482,549,537,0,532,525,546,558,579,508,567,570],
[475,429,454,469,0,429,466,544,462,500,525,537],
[500,536,559,476,572,0,540,544,534,571,531,577],
[524,517,531,455,535,461,0,491,537,462,507,529],
[475,503,507,443,457,457,510,0,501,462,507,514],
[492,508,540,422,539,467,464,500,0,528,595,580],
[451,530,470,493,501,430,539,539,473,0,578,603],
[444,454,465,434,476,470,494,494,406,423,0,522],
[430,395,465,431,464,424,472,487,421,398,479,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 187, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,519,538,497,511,479,472,515,470,525,519,543],
[482,0,523,491,478,504,483,507,485,527,490,490],
[463,478,0,474,531,470,484,492,465,496,507,483],
[504,510,527,0,550,530,497,541,522,529,484,527],
[490,523,470,451,0,450,470,500,500,505,509,489],
[522,497,531,471,551,0,518,521,506,518,539,514],
[529,518,517,504,531,483,0,543,473,552,515,532],
[486,494,509,460,501,480,458,0,476,501,481,476],
[531,516,536,479,501,495,528,525,0,523,507,505],
[476,474,505,472,496,483,449,500,478,0,484,474],
[482,511,494,517,492,462,486,520,494,517,0,505],
[458,511,518,474,512,487,469,525,496,527,496,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 188, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,516,497,492,486,493,529,531,460,504,521,496],
[485,0,488,495,466,518,517,503,475,497,494,480],
[504,513,0,478,470,508,514,532,506,499,497,499],
[509,506,523,0,515,493,515,510,446,497,510,489],
[515,535,531,486,0,517,533,535,489,532,546,554],
[508,483,493,508,484,0,543,525,441,512,486,502],
[472,484,487,486,468,458,0,490,446,466,471,457],
[470,498,469,491,466,476,511,0,453,494,481,489],
[541,526,495,555,512,560,555,548,0,523,553,553],
[497,504,502,504,469,489,535,507,478,0,519,504],
[480,507,504,491,455,515,530,520,448,482,0,511],
[505,521,502,512,447,499,544,512,448,497,490,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 189, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,479,469,449,462,482,459,399,431,485,445,444],
[522,0,544,448,557,501,450,538,491,554,558,512],
[532,457,0,517,482,503,420,525,431,520,492,459],
[552,553,484,0,511,515,509,543,480,572,557,488],
[539,444,519,490,0,470,469,523,502,484,466,439],
[519,500,498,486,531,0,528,550,483,555,518,519],
[542,551,581,492,532,473,0,566,504,543,562,439],
[602,463,476,458,478,451,435,0,418,487,464,452],
[570,510,570,521,499,518,497,583,0,525,549,515],
[516,447,481,429,517,446,458,514,476,0,467,478],
[556,443,509,444,535,483,439,537,452,534,0,448],
[557,489,542,513,562,482,562,549,486,523,553,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 190, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,463,473,466,485,468,517,454,470,462,461,476],
[538,0,559,554,525,505,522,511,460,546,503,537],
[528,442,0,499,514,492,500,467,454,445,452,495],
[535,447,502,0,514,496,501,467,422,472,473,470],
[516,476,487,487,0,502,522,443,451,494,430,500],
[533,496,509,505,499,0,517,503,463,512,424,465],
[484,479,501,500,479,484,0,450,419,466,464,466],
[547,490,534,534,558,498,551,0,465,519,447,469],
[531,541,547,579,550,538,582,536,0,528,500,538],
[539,455,556,529,507,489,535,482,473,0,470,471],
[540,498,549,528,571,577,537,554,501,531,0,531],
[525,464,506,531,501,536,535,532,463,530,470,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 191, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,464,433,429,558,484,447,465,504,465,485,467],
[537,0,503,406,490,449,459,491,479,521,562,541],
[568,498,0,501,592,527,565,529,532,568,617,474],
[572,595,500,0,567,499,499,474,538,614,470,475],
[443,511,409,434,0,414,454,434,442,519,514,413],
[517,552,474,502,587,0,480,448,498,549,517,544],
[554,542,436,502,547,521,0,531,509,594,518,453],
[536,510,472,527,567,553,470,0,560,559,518,512],
[497,522,469,463,559,503,492,441,0,566,480,497],
[536,480,433,387,482,452,407,442,435,0,460,446],
[516,439,384,531,487,484,483,483,521,541,0,474],
[534,460,527,526,588,457,548,489,504,555,527,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 192, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,500,488,471,505,483,499,509,505,493,490,462],
[501,0,486,499,509,481,505,510,516,497,479,482],
[513,515,0,490,511,505,523,512,510,488,483,514],
[530,502,511,0,522,513,533,519,510,509,481,516],
[496,492,490,479,0,499,503,493,498,482,466,481],
[518,520,496,488,502,0,519,514,520,510,511,466],
[502,496,478,468,498,482,0,520,510,458,464,472],
[492,491,489,482,508,487,481,0,517,501,480,483],
[496,485,491,491,503,481,491,484,0,493,474,498],
[508,504,513,492,519,491,543,500,508,0,487,492],
[511,522,518,520,535,490,537,521,527,514,0,496],
[539,519,487,485,520,535,529,518,503,509,505,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 193, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,551,449,562,543,495,593,526,477,485,578,548],
[450,0,424,440,430,564,420,448,453,469,541,508],
[552,577,0,579,461,582,479,406,429,520,526,488],
[439,561,422,0,455,442,498,423,421,434,500,481],
[458,571,540,546,0,593,498,460,496,479,607,559],
[506,437,419,559,408,0,475,415,386,426,424,432],
[408,581,522,503,503,526,0,517,463,496,559,577],
[475,553,595,578,541,586,484,0,472,513,479,563],
[524,548,572,580,505,615,538,529,0,473,566,624],
[516,532,481,567,522,575,505,488,528,0,564,534],
[423,460,475,501,394,577,442,522,435,437,0,471],
[453,493,513,520,442,569,424,438,377,467,530,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 194, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,512,521,497,539,541,504,510,502,511,486,498],
[489,0,515,497,530,502,489,503,517,512,501,502],
[480,486,0,476,519,489,514,479,504,494,508,470],
[504,504,525,0,521,530,498,527,492,530,493,511],
[462,471,482,480,0,456,490,481,454,459,462,478],
[460,499,512,471,545,0,469,520,451,483,463,508],
[497,512,487,503,511,532,0,521,538,512,494,484],
[491,498,522,474,520,481,480,0,512,503,515,514],
[499,484,497,509,547,550,463,489,0,496,495,491],
[490,489,507,471,542,518,489,498,505,0,482,475],
[515,500,493,508,539,538,507,486,506,519,0,492],
[503,499,531,490,523,493,517,487,510,526,509,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 195, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,525,512,540,534,497,488,585,527,509,536,502],
[476,0,537,554,541,500,513,544,557,502,534,507],
[489,464,0,446,472,454,431,508,480,457,501,492],
[461,447,555,0,473,462,484,528,502,460,483,489],
[467,460,529,528,0,473,433,468,505,456,511,514],
[504,501,547,539,528,0,476,525,523,508,502,514],
[513,488,570,517,568,525,0,532,517,501,552,552],
[416,457,493,473,533,476,469,0,531,452,498,521],
[474,444,521,499,496,478,484,470,0,479,486,527],
[492,499,544,541,545,493,500,549,522,0,548,553],
[465,467,500,518,490,499,449,503,515,453,0,503],
[499,494,509,512,487,487,449,480,474,448,498,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 196, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,568,461,500,514,552,500,456,469,556,535,473],
[433,0,408,430,461,501,473,425,452,442,456,452],
[540,593,0,527,549,537,521,526,470,565,511,530],
[501,571,474,0,550,571,522,436,513,522,437,494],
[487,540,452,451,0,537,509,473,475,532,511,450],
[449,500,464,430,464,0,488,419,479,445,439,452],
[501,528,480,479,492,513,0,412,480,503,435,442],
[545,576,475,565,528,582,589,0,526,543,480,531],
[532,549,531,488,526,522,521,475,0,530,489,470],
[445,559,436,479,469,556,498,458,471,0,496,480],
[466,545,490,564,490,562,566,521,512,505,0,480],
[528,549,471,507,551,549,559,470,531,521,521,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 197, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,515,484,522,487,525,490,505,522,501,498,469],
[486,0,504,521,492,532,518,481,516,494,510,502],
[517,497,0,519,529,541,529,483,522,487,471,489],
[479,480,482,0,481,500,459,463,504,482,474,481],
[514,509,472,520,0,518,516,479,500,480,510,482],
[476,469,460,501,483,0,513,473,480,480,454,472],
[511,483,472,542,485,488,0,472,493,503,470,482],
[496,520,518,538,522,528,529,0,529,526,485,503],
[479,485,479,497,501,521,508,472,0,472,467,479],
[500,507,514,519,521,521,498,475,529,0,496,483],
[503,491,530,527,491,547,531,516,534,505,0,514],
[532,499,512,520,519,529,519,498,522,518,487,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 198, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,498,504,529,511,508,512,512,512,480,525,500],
[503,0,522,544,532,509,520,519,497,495,533,511],
[497,479,0,527,492,491,490,493,525,481,503,506],
[472,457,474,0,512,506,507,491,501,491,501,492],
[490,469,509,489,0,497,531,534,538,497,507,495],
[493,492,510,495,504,0,518,515,522,459,535,502],
[489,481,511,494,470,483,0,517,514,503,490,481],
[489,482,508,510,467,486,484,0,493,474,487,516],
[489,504,476,500,463,479,487,508,0,470,513,475],
[521,506,520,510,504,542,498,527,531,0,551,482],
[476,468,498,500,494,466,511,514,488,450,0,484],
[501,490,495,509,506,499,520,485,526,519,517,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 199, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,502,517,534,496,512,457,527,490,514,505,472],
[499,0,497,502,515,490,481,520,508,528,503,478],
[484,504,0,501,496,481,470,498,492,524,503,473],
[467,499,500,0,470,473,466,491,479,469,472,471],
[505,486,505,531,0,484,507,526,502,515,494,501],
[489,511,520,528,517,0,477,512,506,530,490,491],
[544,520,531,535,494,524,0,529,525,534,518,514],
[474,481,503,510,475,489,472,0,489,510,491,468],
[511,493,509,522,499,495,476,512,0,495,516,481],
[487,473,477,532,486,471,467,491,506,0,488,478],
[496,498,498,529,507,511,483,510,485,513,0,484],
[529,523,528,530,500,510,487,533,520,523,517,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([12, 1001, 200, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/mebbrcwd/mebbrcwd_12_1001.csv", index=False, header=False)