
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg
from kemeny import sc

rep = 3
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,594,497,549,580,512,606,548,537],
[406,0,475,484,478,423,479,496,467],
[503,525,0,535,583,494,532,533,501],
[451,516,465,0,524,539,482,563,537],
[420,522,417,476,0,411,443,454,462],
[488,577,506,461,589,0,470,567,544],
[394,521,468,518,557,530,0,499,524],
[452,504,467,437,546,433,501,0,455],
[463,533,499,463,538,456,476,545,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 1, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,513,544,499,522,529,572,527,485],
[487,0,494,480,517,483,502,465,463],
[456,506,0,515,544,472,522,547,476],
[501,520,485,0,547,473,513,504,454],
[478,483,456,453,0,460,474,457,411],
[471,517,528,527,540,0,517,504,470],
[428,498,478,487,526,483,0,452,471],
[473,535,453,496,543,496,548,0,507],
[515,537,524,546,589,530,529,493,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 2, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,521,492,561,505,570,568,535,540],
[479,0,503,531,484,529,510,582,564],
[508,497,0,505,474,523,520,550,502],
[439,469,495,0,439,542,488,521,469],
[495,516,526,561,0,508,546,530,510],
[430,471,477,458,492,0,476,498,483],
[432,490,480,512,454,524,0,540,505],
[465,418,450,479,470,502,460,0,504],
[460,436,498,531,490,517,495,496,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 3, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,490,483,480,473,461,491,484,480],
[510,0,490,495,474,478,506,523,503],
[517,510,0,518,486,523,490,527,509],
[520,505,482,0,493,490,502,534,516],
[527,526,514,507,0,500,504,522,482],
[539,522,477,510,500,0,496,524,506],
[509,494,510,498,496,504,0,517,503],
[516,477,473,466,478,476,483,0,513],
[520,497,491,484,518,494,497,487,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 4, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,496,475,452,506,515,496,492,483],
[504,0,466,483,462,484,505,498,468],
[525,534,0,510,571,502,513,548,469],
[548,517,490,0,517,546,538,527,509],
[494,538,429,483,0,498,490,478,456],
[485,516,498,454,502,0,502,478,470],
[504,495,487,462,510,498,0,506,467],
[508,502,452,473,522,522,494,0,489],
[517,532,531,491,544,530,533,511,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 5, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,503,496,508,493,524,511,499,509],
[497,0,483,487,494,513,474,498,478],
[504,517,0,504,473,536,489,502,516],
[492,513,496,0,494,516,500,514,492],
[507,506,527,506,0,519,490,512,505],
[476,487,464,484,481,0,487,495,491],
[489,526,511,500,510,513,0,533,512],
[501,502,498,486,488,505,467,0,496],
[491,522,484,508,495,509,488,504,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 6, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,499,515,492,488,504,518,490,507],
[501,0,497,515,491,524,516,506,511],
[485,503,0,498,500,523,511,500,503],
[508,485,502,0,503,522,513,498,472],
[512,509,500,497,0,522,531,516,498],
[496,476,477,478,478,0,483,485,489],
[482,484,489,487,469,517,0,480,464],
[510,494,500,502,484,515,520,0,499],
[493,489,497,528,502,511,536,501,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 7, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,521,507,501,513,540,515,521,498],
[479,0,467,495,473,506,494,477,486],
[493,533,0,503,469,491,514,488,474],
[499,505,497,0,513,519,517,527,494],
[487,527,531,487,0,530,504,498,508],
[460,494,509,481,470,0,496,496,474],
[485,506,486,483,496,504,0,501,497],
[479,523,512,473,502,504,499,0,494],
[502,514,526,506,492,526,503,506,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 8, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,496,474,513,493,470,475,538,511],
[504,0,482,509,455,480,481,548,524],
[526,518,0,574,474,534,501,547,527],
[487,491,426,0,470,479,494,502,511],
[507,545,526,530,0,503,515,540,492],
[530,520,466,521,497,0,528,525,477],
[525,519,499,506,485,472,0,521,560],
[462,452,453,498,460,475,479,0,532],
[489,476,473,489,508,523,440,468,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 9, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,531,443,458,548,523,565,532,535],
[469,0,505,520,526,556,539,556,520],
[557,495,0,511,599,521,510,649,554],
[542,480,489,0,588,533,581,517,506],
[452,474,401,412,0,436,489,496,511],
[477,444,479,467,564,0,542,494,468],
[435,461,490,419,511,458,0,489,448],
[468,444,351,483,504,506,511,0,452],
[465,480,446,494,489,532,552,548,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 10, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,510,512,519,515,500,503,511,512],
[490,0,500,511,513,509,485,491,486],
[488,500,0,482,500,505,500,506,498],
[481,489,518,0,510,485,503,518,496],
[485,487,500,490,0,493,486,496,466],
[500,491,495,515,507,0,504,517,504],
[497,515,500,497,514,496,0,508,509],
[489,509,494,482,504,483,492,0,494],
[488,514,502,504,534,496,491,506,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 11, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,544,515,486,525,505,480,500,501],
[456,0,485,428,534,478,443,475,443],
[485,515,0,462,506,522,541,470,502],
[514,572,538,0,510,518,524,458,511],
[475,466,494,490,0,528,470,473,492],
[495,522,478,482,472,0,477,439,523],
[520,557,459,476,530,523,0,473,548],
[500,525,530,542,527,561,527,0,504],
[499,557,498,489,508,477,452,496,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 12, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,461,483,494,493,438,485,457,447],
[539,0,542,496,562,497,525,537,498],
[517,458,0,476,492,488,482,437,467],
[506,504,524,0,504,480,498,490,492],
[507,438,508,496,0,454,482,501,465],
[562,503,512,520,546,0,508,489,530],
[515,475,518,502,518,492,0,506,477],
[543,463,563,510,499,511,494,0,458],
[553,502,533,508,535,470,523,542,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 13, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,449,482,458,494,471,478,441,462],
[551,0,529,487,512,475,500,468,543],
[518,471,0,478,498,490,477,492,482],
[542,513,522,0,524,488,514,507,535],
[506,488,502,476,0,462,501,473,460],
[529,525,510,512,538,0,542,527,495],
[522,500,523,486,499,458,0,478,460],
[559,532,508,493,527,473,522,0,518],
[538,457,518,465,540,505,540,482,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 14, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,523,513,520,495,500,524,536,485],
[477,0,509,530,507,484,498,506,457],
[487,491,0,499,459,454,489,492,435],
[480,470,501,0,454,475,497,508,472],
[505,493,541,546,0,477,531,535,498],
[500,516,546,525,523,0,540,510,517],
[476,502,511,503,469,460,0,516,472],
[464,494,508,492,465,490,484,0,421],
[515,543,565,528,502,483,528,579,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 15, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,525,527,487,518,502,506,472,468],
[475,0,550,470,545,498,508,502,518],
[473,450,0,449,527,443,464,483,440],
[513,530,551,0,523,496,501,446,527],
[482,455,473,477,0,480,507,479,468],
[498,502,557,504,520,0,520,469,486],
[494,492,536,499,493,480,0,451,496],
[528,498,517,554,521,531,549,0,508],
[532,482,560,473,532,514,504,492,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 16, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,482,475,450,452,488,505,466,467],
[518,0,491,465,481,469,489,481,460],
[525,509,0,480,483,483,515,474,503],
[550,535,520,0,495,513,543,476,497],
[548,519,517,505,0,493,513,509,488],
[512,531,517,487,507,0,563,510,497],
[495,511,485,457,487,437,0,497,478],
[534,519,526,524,491,490,503,0,493],
[533,540,497,503,512,503,522,507,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 17, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,484,512,517,501,537,467,500,508],
[516,0,498,519,501,554,487,513,498],
[488,502,0,505,506,535,511,488,498],
[483,481,495,0,485,505,468,470,493],
[499,499,494,515,0,547,505,506,490],
[463,446,465,495,453,0,457,474,454],
[533,513,489,532,495,543,0,488,510],
[500,487,512,530,494,526,512,0,502],
[492,502,502,507,510,546,490,498,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 18, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,552,391,478,524,564,529,650,530],
[448,0,521,494,500,529,545,616,453],
[609,479,0,553,557,579,543,603,413],
[522,506,447,0,452,585,529,591,472],
[476,500,443,548,0,563,583,584,488],
[436,471,421,415,437,0,438,554,437],
[471,455,457,471,417,562,0,530,479],
[350,384,397,409,416,446,470,0,383],
[470,547,587,528,512,563,521,617,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 19, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,486,499,504,539,520,526,521,496],
[514,0,485,517,508,497,504,506,520],
[501,515,0,510,533,523,516,530,492],
[496,483,490,0,517,485,494,492,505],
[461,492,467,483,0,482,479,493,486],
[480,503,477,515,518,0,507,508,502],
[474,496,484,506,521,493,0,512,490],
[479,494,470,508,507,492,488,0,506],
[504,480,508,495,514,498,510,494,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 20, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,492,500,486,532,475,477,538,468],
[508,0,555,492,523,475,516,558,466],
[500,445,0,488,511,477,504,538,499],
[514,508,512,0,507,481,500,562,511],
[468,477,489,493,0,465,476,517,476],
[525,525,523,519,535,0,538,555,480],
[523,484,496,500,524,462,0,530,492],
[462,442,462,438,483,445,470,0,461],
[532,534,501,489,524,520,508,539,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 21, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,495,494,526,522,526,520,521,502],
[505,0,479,527,519,523,504,524,517],
[506,521,0,537,527,545,497,514,523],
[474,473,463,0,505,510,500,518,485],
[478,481,473,495,0,506,483,501,499],
[474,477,455,490,494,0,485,470,463],
[480,496,503,500,517,515,0,507,505],
[479,476,486,482,499,530,493,0,488],
[498,483,477,515,501,537,495,512,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 22, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,431,333,468,439,546,465,544,481],
[569,0,403,613,403,614,536,538,474],
[667,597,0,712,492,644,615,653,537],
[532,387,288,0,638,540,451,534,419],
[561,597,508,362,0,637,514,543,571],
[454,386,356,460,363,0,530,447,444],
[535,464,385,549,486,470,0,543,497],
[456,462,347,466,457,553,457,0,402],
[519,526,463,581,429,556,503,598,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 23, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,497,502,506,504,519,523,522,522],
[503,0,502,497,513,511,505,498,508],
[498,498,0,524,509,515,521,509,504],
[494,503,476,0,485,509,483,477,479],
[496,487,491,515,0,494,497,481,488],
[481,489,485,491,506,0,512,498,493],
[477,495,479,517,503,488,0,485,501],
[478,502,491,523,519,502,515,0,522],
[478,492,496,521,512,507,499,478,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 24, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,521,526,486,509,492,502,483,496],
[479,0,457,434,460,535,460,495,446],
[474,543,0,461,484,499,463,452,448],
[514,566,539,0,489,537,505,501,501],
[491,540,516,511,0,536,482,510,511],
[508,465,501,463,464,0,489,483,495],
[498,540,537,495,518,511,0,501,507],
[517,505,548,499,490,517,499,0,478],
[504,554,552,499,489,505,493,522,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 25, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,488,499,498,498,466,470,502,499],
[512,0,487,505,526,501,500,524,518],
[501,513,0,511,515,495,469,511,486],
[502,495,489,0,535,475,470,503,496],
[502,474,485,465,0,458,482,494,507],
[534,499,505,525,542,0,502,531,542],
[530,500,531,530,518,498,0,510,538],
[498,476,489,497,506,469,490,0,489],
[501,482,514,504,493,458,462,511,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 26, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,494,479,531,487,484,527,507,496],
[506,0,484,502,471,497,508,492,418],
[521,516,0,541,498,527,536,528,518],
[469,498,459,0,439,427,501,511,424],
[513,529,502,561,0,505,511,540,483],
[516,503,473,573,495,0,506,496,491],
[473,492,464,499,489,494,0,537,442],
[493,508,472,489,460,504,463,0,468],
[504,582,482,576,517,509,558,532,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 27, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,536,503,519,526,514,505,520,498],
[464,0,484,506,487,489,491,476,489],
[497,516,0,496,509,502,500,497,465],
[481,494,504,0,510,518,515,512,506],
[474,513,491,490,0,499,504,498,515],
[486,511,498,482,501,0,507,494,479],
[495,509,500,485,496,493,0,485,499],
[480,524,503,488,502,506,515,0,464],
[502,511,535,494,485,521,501,536,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 28, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,479,487,492,475,438,471,492,418],
[521,0,488,508,489,458,474,474,443],
[513,512,0,509,524,457,438,450,454],
[508,492,491,0,518,462,482,471,475],
[525,511,476,482,0,507,479,477,465],
[562,542,543,538,493,0,509,528,495],
[529,526,562,518,521,491,0,512,504],
[508,526,550,529,523,472,488,0,484],
[582,557,546,525,535,505,496,516,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 29, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,514,547,497,514,555,538,502,472],
[486,0,521,495,546,528,506,525,486],
[453,479,0,493,472,539,516,495,490],
[503,505,507,0,483,547,487,498,503],
[486,454,528,517,0,583,539,507,501],
[445,472,461,453,417,0,461,460,439],
[462,494,484,513,461,539,0,507,492],
[498,475,505,502,493,540,493,0,476],
[528,514,510,497,499,561,508,524,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 30, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,476,498,537,536,519,534,517,529],
[524,0,526,500,530,490,525,552,516],
[502,474,0,498,517,514,504,515,495],
[463,500,502,0,514,493,490,523,504],
[464,470,483,486,0,473,531,513,471],
[481,510,486,507,527,0,542,510,499],
[466,475,496,510,469,458,0,483,499],
[483,448,485,477,487,490,517,0,500],
[471,484,505,496,529,501,501,500,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 31, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,534,519,494,447,483,512,472,500],
[466,0,477,484,481,503,463,480,513],
[481,523,0,530,486,515,503,516,473],
[506,516,470,0,451,513,493,466,500],
[553,519,514,549,0,525,523,495,535],
[517,497,485,487,475,0,498,471,513],
[488,537,497,507,477,502,0,493,531],
[528,520,484,534,505,529,507,0,530],
[500,487,527,500,465,487,469,470,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 32, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,503,513,486,495,502,491,502,503],
[497,0,538,518,491,548,499,525,517],
[487,462,0,486,479,484,478,512,496],
[514,482,514,0,510,523,505,509,518],
[505,509,521,490,0,509,521,518,509],
[498,452,516,477,491,0,474,510,493],
[509,501,522,495,479,526,0,511,510],
[498,475,488,491,482,490,489,0,491],
[497,483,504,482,491,507,490,509,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 33, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,481,511,476,499,476,550,499,517],
[519,0,512,491,489,506,529,477,485],
[489,488,0,514,523,485,538,495,491],
[524,509,486,0,526,519,526,494,507],
[501,511,477,474,0,509,515,477,479],
[524,494,515,481,491,0,544,484,488],
[450,471,462,474,485,456,0,459,468],
[501,523,505,506,523,516,541,0,498],
[483,515,509,493,521,512,532,502,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 34, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,452,486,449,467,469,474,498,472],
[548,0,502,493,490,499,503,508,507],
[514,498,0,476,468,479,489,470,503],
[551,507,524,0,512,515,540,543,488],
[533,510,532,488,0,506,508,521,512],
[531,501,521,485,494,0,490,503,507],
[526,497,511,460,492,510,0,505,494],
[502,492,530,457,479,497,495,0,487],
[528,493,497,512,488,493,506,513,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 35, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,488,477,509,495,509,519,504,505],
[512,0,510,502,476,494,517,511,497],
[523,490,0,474,508,498,540,523,489],
[491,498,526,0,496,497,535,516,534],
[505,524,492,504,0,526,511,498,504],
[491,506,502,503,474,0,525,506,512],
[481,483,460,465,489,475,0,495,484],
[496,489,477,484,502,494,505,0,502],
[495,503,511,466,496,488,516,498,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 36, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,468,482,488,465,487,483,500,480],
[532,0,518,526,496,527,523,542,540],
[518,482,0,512,496,486,522,533,488],
[512,474,488,0,435,476,465,511,489],
[535,504,504,565,0,486,516,551,530],
[513,473,514,524,514,0,476,522,491],
[517,477,478,535,484,524,0,522,521],
[500,458,467,489,449,478,478,0,485],
[520,460,512,511,470,509,479,515,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 37, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,507,564,607,489,543,534,467,489],
[493,0,518,565,588,517,500,500,524],
[436,482,0,540,495,466,465,499,473],
[393,435,460,0,496,447,453,458,494],
[511,412,505,504,0,470,489,410,431],
[457,483,534,553,530,0,517,477,481],
[466,500,535,547,511,483,0,473,506],
[533,500,501,542,590,523,527,0,533],
[511,476,527,506,569,519,494,467,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 38, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,536,521,533,473,474,514,538,524],
[464,0,506,501,502,494,478,506,472],
[479,494,0,514,483,541,530,528,544],
[467,499,486,0,500,530,460,526,492],
[527,498,517,500,0,556,475,518,560],
[526,506,459,470,444,0,457,485,470],
[486,522,470,540,525,543,0,484,529],
[462,494,472,474,482,515,516,0,543],
[476,528,456,508,440,530,471,457,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 39, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,468,492,507,432,470,464,470,476],
[532,0,562,526,505,498,510,540,523],
[508,438,0,524,474,511,488,504,501],
[493,474,476,0,460,458,415,510,492],
[568,495,526,540,0,473,476,518,485],
[530,502,489,542,527,0,484,505,540],
[536,490,512,585,524,516,0,520,532],
[530,460,496,490,482,495,480,0,512],
[524,477,499,508,515,460,468,488,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 40, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,475,497,471,504,505,476,469,472],
[525,0,485,503,505,508,504,493,502],
[503,515,0,500,527,510,493,506,465],
[529,497,500,0,513,510,496,502,494],
[496,495,473,487,0,497,487,484,484],
[495,492,490,490,503,0,495,485,479],
[524,496,507,504,513,505,0,508,486],
[531,507,494,498,516,515,492,0,512],
[528,498,535,506,516,521,514,488,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 41, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,558,507,534,491,515,513,514,495],
[442,0,489,471,494,497,478,517,501],
[493,511,0,531,504,496,504,515,488],
[466,529,469,0,514,502,532,518,498],
[509,506,496,486,0,494,492,526,512],
[485,503,504,498,506,0,502,515,486],
[487,522,496,468,508,498,0,544,481],
[486,483,485,482,474,485,456,0,445],
[505,499,512,502,488,514,519,555,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 42, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,390,480,506,483,503,538,536,559],
[610,0,647,539,561,717,645,545,472],
[520,353,0,442,465,517,488,431,516],
[494,461,558,0,452,533,600,532,509],
[517,439,535,548,0,489,594,428,592],
[497,283,483,467,511,0,560,445,502],
[462,355,512,400,406,440,0,436,504],
[464,455,569,468,572,555,564,0,482],
[441,528,484,491,408,498,496,518,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 43, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,472,470,493,526,503,478,511,504],
[528,0,509,473,528,519,523,525,496],
[530,491,0,519,554,536,525,522,533],
[507,527,481,0,539,515,487,499,517],
[474,472,446,461,0,478,481,487,480],
[497,481,464,485,522,0,473,513,513],
[522,477,475,513,519,527,0,498,528],
[489,475,478,501,513,487,502,0,521],
[496,504,467,483,520,487,472,479,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 44, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,511,512,493,482,459,484,491,492],
[489,0,523,497,504,492,493,492,492],
[488,477,0,489,488,483,484,483,486],
[507,503,511,0,512,511,502,498,502],
[518,496,512,488,0,471,498,502,478],
[541,508,517,489,529,0,524,502,513],
[516,507,516,498,502,476,0,505,478],
[509,508,517,502,498,498,495,0,495],
[508,508,514,498,522,487,522,505,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 45, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,491,509,502,517,503,489,483,472],
[509,0,511,510,499,499,504,468,509],
[491,489,0,505,501,493,496,487,476],
[498,490,495,0,479,495,481,477,486],
[483,501,499,521,0,503,487,476,485],
[497,501,507,505,497,0,512,495,503],
[511,496,504,519,513,488,0,483,507],
[517,532,513,523,524,505,517,0,499],
[528,491,524,514,515,497,493,501,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 46, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,379,377,407,505,501,486,469,411],
[621,0,525,421,664,540,588,577,562],
[623,475,0,435,525,579,590,494,559],
[593,579,565,0,619,651,641,623,498],
[495,336,475,381,0,542,521,548,434],
[499,460,421,349,458,0,478,501,393],
[514,412,410,359,479,522,0,484,373],
[531,423,506,377,452,499,516,0,402],
[589,438,441,502,566,607,627,598,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 47, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,509,526,564,515,481,513,522,514],
[491,0,489,514,516,516,505,533,476],
[474,511,0,539,536,513,484,485,516],
[436,486,461,0,492,476,479,493,502],
[485,484,464,508,0,522,478,454,506],
[519,484,487,524,478,0,520,505,486],
[487,495,516,521,522,480,0,492,477],
[478,467,515,507,546,495,508,0,562],
[486,524,484,498,494,514,523,438,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 48, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,554,574,495,552,579,545,574,566],
[446,0,506,472,491,486,461,522,476],
[426,494,0,455,483,502,446,514,466],
[505,528,545,0,563,528,473,539,514],
[448,509,517,437,0,455,425,526,485],
[421,514,498,472,545,0,449,486,479],
[455,539,554,527,575,551,0,550,534],
[426,478,486,461,474,514,450,0,464],
[434,524,534,486,515,521,466,536,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 49, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,487,496,519,474,476,494,475,480],
[513,0,505,522,466,462,494,477,501],
[504,495,0,517,441,475,462,481,451],
[481,478,483,0,443,406,473,455,439],
[526,534,559,557,0,527,543,477,509],
[524,538,525,594,473,0,520,518,527],
[506,506,538,527,457,480,0,512,471],
[525,523,519,545,523,482,488,0,495],
[520,499,549,561,491,473,529,505,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 50, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,474,502,519,492,500,509,510,486],
[526,0,502,515,519,490,537,498,496],
[498,498,0,506,521,503,520,491,479],
[481,485,494,0,493,487,492,495,467],
[508,481,479,507,0,489,516,488,474],
[500,510,497,513,511,0,518,502,483],
[491,463,480,508,484,482,0,473,478],
[490,502,509,505,512,498,527,0,504],
[514,504,521,533,526,517,522,496,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 51, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,534,501,515,487,493,525,509,532],
[466,0,496,491,526,512,520,507,522],
[499,504,0,499,538,467,498,497,510],
[485,509,501,0,497,490,506,492,494],
[513,474,462,503,0,501,505,514,507],
[507,488,533,510,499,0,519,474,514],
[475,480,502,494,495,481,0,493,485],
[491,493,503,508,486,526,507,0,507],
[468,478,490,506,493,486,515,493,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 52, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,521,531,519,501,497,481,489,501],
[479,0,469,478,430,474,467,473,488],
[469,531,0,507,479,490,494,481,480],
[481,522,493,0,475,478,481,475,482],
[499,570,521,525,0,509,513,520,512],
[503,526,510,522,491,0,518,482,510],
[519,533,506,519,487,482,0,494,488],
[511,527,519,525,480,518,506,0,491],
[499,512,520,518,488,490,512,509,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 53, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,508,512,518,505,492,522,521,491],
[492,0,504,529,505,494,491,518,503],
[488,496,0,483,505,491,481,479,492],
[482,471,517,0,502,493,502,502,504],
[495,495,495,498,0,501,484,491,498],
[508,506,509,507,499,0,504,517,515],
[478,509,519,498,516,496,0,520,494],
[479,482,521,498,509,483,480,0,481],
[509,497,508,496,502,485,506,519,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 54, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,479,532,483,553,541,490,495,537],
[521,0,509,530,598,552,558,477,547],
[468,491,0,469,537,547,498,487,540],
[517,470,531,0,560,519,510,521,524],
[447,402,463,440,0,463,465,459,486],
[459,448,453,481,537,0,501,480,489],
[510,442,502,490,535,499,0,515,553],
[505,523,513,479,541,520,485,0,507],
[463,453,460,476,514,511,447,493,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 55, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,454,475,482,535,460,468,453,429],
[546,0,529,542,528,508,524,519,480],
[525,471,0,521,492,482,495,512,470],
[518,458,479,0,479,484,502,470,466],
[465,472,508,521,0,449,493,465,476],
[540,492,518,516,551,0,533,501,486],
[532,476,505,498,507,467,0,501,509],
[547,481,488,530,535,499,499,0,469],
[571,520,530,534,524,514,491,531,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 56, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,500,611,549,588,614,525,499,560],
[500,0,537,487,528,528,567,543,567],
[389,463,0,418,534,497,457,477,513],
[451,513,582,0,586,541,552,483,541],
[412,472,466,414,0,527,477,470,495],
[386,472,503,459,473,0,487,437,513],
[475,433,543,448,523,513,0,495,520],
[501,457,523,517,530,563,505,0,603],
[440,433,487,459,505,487,480,397,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 57, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,495,503,488,521,505,506,524,515],
[505,0,479,494,512,503,500,517,515],
[497,521,0,500,510,512,494,530,533],
[512,506,500,0,525,525,510,529,518],
[479,488,490,475,0,494,495,515,504],
[495,497,488,475,506,0,511,508,518],
[494,500,506,490,505,489,0,500,481],
[476,483,470,471,485,492,500,0,501],
[485,485,467,482,496,482,519,499,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 58, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,476,518,564,470,529,503,503,520],
[524,0,530,501,474,535,496,478,518],
[482,470,0,505,468,511,489,498,500],
[436,499,495,0,437,474,489,489,461],
[530,526,532,563,0,486,533,546,516],
[471,465,489,526,514,0,484,506,488],
[497,504,511,511,467,516,0,534,496],
[497,522,502,511,454,494,466,0,520],
[480,482,500,539,484,512,504,480,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 59, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,509,529,501,514,474,513,456,516],
[491,0,480,453,464,459,438,474,473],
[471,520,0,474,472,479,476,483,472],
[499,547,526,0,517,480,492,495,511],
[486,536,528,483,0,504,470,464,444],
[526,541,521,520,496,0,527,512,514],
[487,562,524,508,530,473,0,519,513],
[544,526,517,505,536,488,481,0,500],
[484,527,528,489,556,486,487,500,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 60, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,505,438,545,458,499,561,501,583],
[495,0,438,530,472,501,522,479,553],
[562,562,0,523,541,490,557,554,605],
[455,470,477,0,499,519,488,478,583],
[542,528,459,501,0,503,500,442,564],
[501,499,510,481,497,0,570,486,607],
[439,478,443,512,500,430,0,448,604],
[499,521,446,522,558,514,552,0,589],
[417,447,395,417,436,393,396,411,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 61, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,489,492,514,497,526,502,483,524],
[511,0,499,530,507,547,508,505,501],
[508,501,0,525,483,523,496,500,537],
[486,470,475,0,492,479,499,479,513],
[503,493,517,508,0,542,516,488,535],
[474,453,477,521,458,0,478,479,497],
[498,492,504,501,484,522,0,488,508],
[517,495,500,521,512,521,512,0,506],
[476,499,463,487,465,503,492,494,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 62, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,539,506,512,486,471,582,597,577],
[461,0,519,497,481,518,536,543,531],
[494,481,0,460,476,521,581,510,508],
[488,503,540,0,518,512,545,537,510],
[514,519,524,482,0,527,552,545,562],
[529,482,479,488,473,0,516,529,502],
[418,464,419,455,448,484,0,492,512],
[403,457,490,463,455,471,508,0,458],
[423,469,492,490,438,498,488,542,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 63, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,567,502,410,528,487,581,515,585],
[433,0,482,534,515,563,470,540,539],
[498,518,0,409,580,404,413,462,505],
[590,466,591,0,579,567,494,503,538],
[472,485,420,421,0,401,415,431,508],
[513,437,596,433,599,0,420,482,488],
[419,530,587,506,585,580,0,540,599],
[485,460,538,497,569,518,460,0,493],
[415,461,495,462,492,512,401,507,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 64, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,490,517,456,478,478,518,512,482],
[510,0,463,478,456,499,457,474,460],
[483,537,0,509,526,516,458,483,473],
[544,522,491,0,475,516,506,536,504],
[522,544,474,525,0,477,482,495,502],
[522,501,484,484,523,0,489,530,481],
[482,543,542,494,518,511,0,491,489],
[488,526,517,464,505,470,509,0,453],
[518,540,527,496,498,519,511,547,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 65, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,483,496,497,485,480,502,491,496],
[517,0,523,502,507,494,509,490,504],
[504,477,0,483,468,509,507,509,492],
[503,498,517,0,466,492,488,508,490],
[515,493,532,534,0,507,528,504,500],
[520,506,491,508,493,0,509,496,508],
[498,491,493,512,472,491,0,508,477],
[509,510,491,492,496,504,492,0,508],
[504,496,508,510,500,492,523,492,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 66, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,479,497,511,496,487,486,494,502],
[521,0,515,506,525,489,520,553,498],
[503,485,0,469,495,482,500,518,483],
[489,494,531,0,505,527,508,563,498],
[504,475,505,495,0,492,490,525,491],
[513,511,518,473,508,0,482,524,510],
[514,480,500,492,510,518,0,544,497],
[506,447,482,437,475,476,456,0,479],
[498,502,517,502,509,490,503,521,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 67, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,489,499,501,483,517,460,531,499],
[511,0,474,501,482,503,440,524,505],
[501,526,0,529,489,526,485,505,514],
[499,499,471,0,479,492,486,510,505],
[517,518,511,521,0,515,500,529,534],
[483,497,474,508,485,0,487,526,486],
[540,560,515,514,500,513,0,544,510],
[469,476,495,490,471,474,456,0,508],
[501,495,486,495,466,514,490,492,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 68, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,506,482,518,494,522,498,496,506],
[494,0,500,524,511,533,540,535,512],
[518,500,0,531,510,516,500,525,539],
[482,476,469,0,480,492,492,506,489],
[506,489,490,520,0,518,510,501,485],
[478,467,484,508,482,0,499,494,482],
[502,460,500,508,490,501,0,510,482],
[504,465,475,494,499,506,490,0,472],
[494,488,461,511,515,518,518,528,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 69, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,494,494,510,526,505,498,526,492],
[506,0,527,495,525,495,513,512,498],
[506,473,0,515,515,506,522,534,511],
[490,505,485,0,515,500,497,517,496],
[474,475,485,485,0,479,487,503,479],
[495,505,494,500,521,0,514,515,506],
[502,487,478,503,513,486,0,534,494],
[474,488,466,483,497,485,466,0,499],
[508,502,489,504,521,494,506,501,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 70, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,507,510,530,517,497,585,508,522],
[493,0,485,530,498,473,552,461,489],
[490,515,0,514,528,500,549,530,507],
[470,470,486,0,500,456,525,476,471],
[483,502,472,500,0,491,527,476,476],
[503,527,500,544,509,0,538,499,520],
[415,448,451,475,473,462,0,468,472],
[492,539,470,524,524,501,532,0,501],
[478,511,493,529,524,480,528,499,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 71, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,485,504,483,479,505,546,479,529],
[515,0,506,491,479,531,508,494,521],
[496,494,0,473,489,485,505,508,514],
[517,509,527,0,467,510,531,505,512],
[521,521,511,533,0,539,483,519,515],
[495,469,515,490,461,0,505,439,500],
[454,492,495,469,517,495,0,471,489],
[521,506,492,495,481,561,529,0,530],
[471,479,486,488,485,500,511,470,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 72, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,479,497,488,521,490,526,529,463],
[521,0,511,477,550,483,549,573,482],
[503,489,0,488,523,510,537,507,445],
[512,523,512,0,552,483,541,566,506],
[479,450,477,448,0,442,502,528,518],
[510,517,490,517,558,0,583,546,514],
[474,451,463,459,498,417,0,510,453],
[471,427,493,434,472,454,490,0,465],
[537,518,555,494,482,486,547,535,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 73, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,523,451,467,412,518,447,434,552],
[477,0,497,459,426,537,450,478,547],
[549,503,0,451,450,548,467,500,627],
[533,541,549,0,516,534,491,515,575],
[588,574,550,484,0,577,495,495,537],
[482,463,452,466,423,0,365,457,519],
[553,550,533,509,505,635,0,495,630],
[566,522,500,485,505,543,505,0,495],
[448,453,373,425,463,481,370,505,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 74, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,490,523,524,509,495,490,507,506],
[510,0,511,510,489,482,478,477,509],
[477,489,0,487,491,465,479,503,480],
[476,490,513,0,491,489,475,480,488],
[491,511,509,509,0,506,505,495,499],
[505,518,535,511,494,0,503,515,511],
[510,522,521,525,495,497,0,517,525],
[493,523,497,520,505,485,483,0,513],
[494,491,520,512,501,489,475,487,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 75, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,466,449,486,477,496,486,492,503],
[534,0,505,473,511,489,524,490,511],
[551,495,0,528,520,522,502,520,511],
[514,527,472,0,517,537,505,514,517],
[523,489,480,483,0,509,495,500,491],
[504,511,478,463,491,0,496,502,539],
[514,476,498,495,505,504,0,499,497],
[508,510,480,486,500,498,501,0,513],
[497,489,489,483,509,461,503,487,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 76, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,501,501,505,505,524,519,501,492],
[499,0,517,504,511,507,497,507,504],
[499,483,0,498,512,510,505,503,511],
[495,496,502,0,483,496,482,501,481],
[495,489,488,517,0,510,501,504,511],
[476,493,490,504,490,0,502,494,492],
[481,503,495,518,499,498,0,486,487],
[499,493,497,499,496,506,514,0,492],
[508,496,489,519,489,508,513,508,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 77, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,490,512,503,503,485,501,514,521],
[510,0,527,514,507,497,516,524,502],
[488,473,0,493,490,465,475,489,501],
[497,486,507,0,519,490,510,492,509],
[497,493,510,481,0,481,482,494,510],
[515,503,535,510,519,0,517,496,535],
[499,484,525,490,518,483,0,508,509],
[486,476,511,508,506,504,492,0,509],
[479,498,499,491,490,465,491,491,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 78, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,490,502,489,520,494,503,517,481],
[510,0,487,481,490,494,473,505,479],
[498,513,0,497,544,485,501,518,488],
[511,519,503,0,529,506,515,510,482],
[480,510,456,471,0,451,468,479,465],
[506,506,515,494,549,0,499,501,511],
[497,527,499,485,532,501,0,519,498],
[483,495,482,490,521,499,481,0,511],
[519,521,512,518,535,489,502,489,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 79, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,509,509,500,487,508,527,521,503],
[491,0,502,509,495,505,544,508,502],
[491,498,0,482,481,496,527,521,513],
[500,491,518,0,484,483,519,503,499],
[513,505,519,516,0,507,542,514,500],
[492,495,504,517,493,0,520,499,495],
[473,456,473,481,458,480,0,485,487],
[479,492,479,497,486,501,515,0,494],
[497,498,487,501,500,505,513,506,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 80, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,504,497,489,501,510,497,506,510],
[496,0,490,478,508,492,489,482,482],
[503,510,0,492,503,496,507,517,510],
[511,522,508,0,513,496,501,504,494],
[499,492,497,487,0,472,483,501,484],
[490,508,504,504,528,0,501,503,491],
[503,511,493,499,517,499,0,531,515],
[494,518,483,496,499,497,469,0,496],
[490,518,490,506,516,509,485,504,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 81, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,507,508,509,508,500,487,502,504],
[493,0,493,510,470,519,483,523,503],
[492,507,0,519,512,512,506,523,492],
[491,490,481,0,490,503,484,482,511],
[492,530,488,510,0,521,495,495,491],
[500,481,488,497,479,0,504,522,489],
[513,517,494,516,505,496,0,519,510],
[498,477,477,518,505,478,481,0,500],
[496,497,508,489,509,511,490,500,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 82, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,432,482,473,471,464,487,465,496],
[568,0,495,559,518,535,514,506,515],
[518,505,0,488,482,511,512,485,497],
[527,441,512,0,474,518,533,464,510],
[529,482,518,526,0,487,511,524,509],
[536,465,489,482,513,0,491,488,491],
[513,486,488,467,489,509,0,466,507],
[535,494,515,536,476,512,534,0,528],
[504,485,503,490,491,509,493,472,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 83, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,544,573,564,528,515,588,484,556],
[456,0,518,497,476,539,521,490,497],
[427,482,0,529,464,470,546,457,449],
[436,503,471,0,462,451,546,492,547],
[472,524,536,538,0,541,532,466,589],
[485,461,530,549,459,0,553,479,504],
[412,479,454,454,468,447,0,441,478],
[516,510,543,508,534,521,559,0,482],
[444,503,551,453,411,496,522,518,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 84, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,498,620,585,577,581,566,600,551],
[502,0,503,540,482,487,555,524,580],
[380,497,0,544,443,434,462,478,478],
[415,460,456,0,460,435,448,486,464],
[423,518,557,540,0,552,474,552,541],
[419,513,566,565,448,0,510,516,577],
[434,445,538,552,526,490,0,538,566],
[400,476,522,514,448,484,462,0,517],
[449,420,522,536,459,423,434,483,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 85, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,492,506,509,496,503,505,484,491],
[508,0,499,488,472,499,498,496,489],
[494,501,0,498,489,498,514,484,493],
[491,512,502,0,504,498,491,480,528],
[504,528,511,496,0,512,494,516,505],
[497,501,502,502,488,0,499,506,499],
[495,502,486,509,506,501,0,485,521],
[516,504,516,520,484,494,515,0,499],
[509,511,507,472,495,501,479,501,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 86, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,608,572,523,488,547,509,550,537],
[392,0,513,406,454,451,510,448,513],
[428,487,0,446,462,459,516,453,548],
[477,594,554,0,517,521,564,537,549],
[512,546,538,483,0,514,538,536,491],
[453,549,541,479,486,0,475,532,549],
[491,490,484,436,462,525,0,493,534],
[450,552,547,463,464,468,507,0,507],
[463,487,452,451,509,451,466,493,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 87, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,505,510,507,478,489,487,490,478],
[495,0,487,519,505,523,538,517,502],
[490,513,0,515,488,492,515,512,502],
[493,481,485,0,497,455,487,505,463],
[522,495,512,503,0,479,555,514,515],
[511,477,508,545,521,0,504,511,528],
[513,462,485,513,445,496,0,498,466],
[510,483,488,495,486,489,502,0,473],
[522,498,498,537,485,472,534,527,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 88, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,533,505,513,499,532,531,513,533],
[467,0,498,499,506,473,502,518,487],
[495,502,0,498,504,482,513,490,521],
[487,501,502,0,487,493,511,483,520],
[501,494,496,513,0,510,520,488,523],
[468,527,518,507,490,0,533,509,531],
[469,498,487,489,480,467,0,493,507],
[487,482,510,517,512,491,507,0,514],
[467,513,479,480,477,469,493,486,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 89, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,489,499,507,501,502,498,486,495],
[511,0,477,498,472,504,492,490,480],
[501,523,0,520,499,514,497,515,505],
[493,502,480,0,479,524,494,502,502],
[499,528,501,521,0,514,520,495,490],
[498,496,486,476,486,0,493,500,495],
[502,508,503,506,480,507,0,524,504],
[514,510,485,498,505,500,476,0,528],
[505,520,495,498,510,505,496,472,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 90, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,512,539,507,514,493,518,531,533],
[488,0,514,519,511,507,527,489,517],
[461,486,0,491,526,456,512,475,510],
[493,481,509,0,518,449,494,519,495],
[486,489,474,482,0,468,490,517,509],
[507,493,544,551,532,0,527,536,533],
[482,473,488,506,510,473,0,474,497],
[469,511,525,481,483,464,526,0,507],
[467,483,490,505,491,467,503,493,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 91, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,480,515,536,472,530,498,478,487],
[520,0,529,532,513,518,517,495,501],
[485,471,0,528,470,506,463,490,487],
[464,468,472,0,481,512,502,475,495],
[528,487,530,519,0,510,484,502,505],
[470,482,494,488,490,0,476,481,476],
[502,483,537,498,516,524,0,506,504],
[522,505,510,525,498,519,494,0,514],
[513,499,513,505,495,524,496,486,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 92, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,511,527,512,498,520,525,529,536],
[489,0,513,513,511,526,500,497,487],
[473,487,0,501,508,511,521,511,504],
[488,487,499,0,516,474,505,535,489],
[502,489,492,484,0,504,501,494,517],
[480,474,489,526,496,0,514,507,493],
[475,500,479,495,499,486,0,487,479],
[471,503,489,465,506,493,513,0,483],
[464,513,496,511,483,507,521,517,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 93, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,515,452,520,503,507,501,531,500],
[485,0,434,514,492,488,484,493,475],
[548,566,0,575,544,578,499,557,569],
[480,486,425,0,456,477,428,477,439],
[497,508,456,544,0,525,498,504,504],
[493,512,422,523,475,0,463,518,468],
[499,516,501,572,502,537,0,528,517],
[469,507,443,523,496,482,472,0,495],
[500,525,431,561,496,532,483,505,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 94, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,510,491,491,483,510,480,467,494],
[490,0,490,484,492,490,517,501,497],
[509,510,0,477,481,496,484,507,515],
[509,516,523,0,545,524,516,498,520],
[517,508,519,455,0,521,472,516,501],
[490,510,504,476,479,0,482,511,486],
[520,483,516,484,528,518,0,508,494],
[533,499,493,502,484,489,492,0,471],
[506,503,485,480,499,514,506,529,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 95, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,530,534,514,488,493,512,527,502],
[470,0,494,490,466,449,451,491,478],
[466,506,0,488,472,467,512,500,485],
[486,510,512,0,494,480,505,532,499],
[512,534,528,506,0,504,479,544,522],
[507,551,533,520,496,0,517,506,514],
[488,549,488,495,521,483,0,502,493],
[473,509,500,468,456,494,498,0,509],
[498,522,515,501,478,486,507,491,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 96, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,459,503,499,500,498,455,461,475],
[541,0,521,532,509,496,504,477,494],
[497,479,0,524,494,512,493,527,505],
[501,468,476,0,496,522,492,500,489],
[500,491,506,504,0,533,504,476,450],
[502,504,488,478,467,0,484,512,440],
[545,496,507,508,496,516,0,500,436],
[539,523,473,500,524,488,500,0,512],
[525,506,495,511,550,560,564,488,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 97, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,589,564,501,565,537,515,589,497],
[411,0,509,449,529,485,444,523,465],
[436,491,0,482,506,447,436,486,489],
[499,551,518,0,527,491,500,544,484],
[435,471,494,473,0,446,458,464,468],
[463,515,553,509,554,0,525,539,487],
[485,556,564,500,542,475,0,589,522],
[411,477,514,456,536,461,411,0,493],
[503,535,511,516,532,513,478,507,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 98, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,517,493,496,479,480,498,488,491],
[483,0,485,456,477,478,478,497,458],
[507,515,0,474,507,489,522,517,478],
[504,544,526,0,505,498,524,506,488],
[521,523,493,495,0,475,514,519,480],
[520,522,511,502,525,0,535,520,497],
[502,522,478,476,486,465,0,504,500],
[512,503,483,494,481,480,496,0,469],
[509,542,522,512,520,503,500,531,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 99, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,536,515,490,496,512,511,455,467],
[464,0,463,480,429,451,459,429,464],
[485,537,0,525,507,494,521,486,482],
[510,520,475,0,553,505,527,505,483],
[504,571,493,447,0,530,513,500,485],
[488,549,506,495,470,0,519,462,478],
[489,541,479,473,487,481,0,460,461],
[545,571,514,495,500,538,540,0,517],
[533,536,518,517,515,522,539,483,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 100, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,479,538,509,498,499,504,517,493],
[521,0,533,529,502,532,494,515,490],
[462,467,0,510,469,515,454,514,495],
[491,471,490,0,481,498,487,492,459],
[502,498,531,519,0,523,504,534,491],
[501,468,485,502,477,0,486,509,465],
[496,506,546,513,496,514,0,534,543],
[483,485,486,508,466,491,466,0,470],
[507,510,505,541,509,535,457,530,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 101, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,511,501,522,507,520,518,523,484],
[489,0,518,527,508,503,487,491,507],
[499,482,0,517,520,503,500,486,499],
[478,473,483,0,462,501,483,484,500],
[493,492,480,538,0,514,499,495,479],
[480,497,497,499,486,0,496,490,475],
[482,513,500,517,501,504,0,500,498],
[477,509,514,516,505,510,500,0,473],
[516,493,501,500,521,525,502,527,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 102, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,503,500,509,438,485,563,566,488],
[497,0,500,485,512,485,502,561,489],
[500,500,0,535,481,515,516,545,491],
[491,515,465,0,490,486,508,552,498],
[562,488,519,510,0,491,536,575,537],
[515,515,485,514,509,0,569,574,481],
[437,498,484,492,464,431,0,502,452],
[434,439,455,448,425,426,498,0,430],
[512,511,509,502,463,519,548,570,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 103, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,458,501,512,487,430,462,501,464],
[542,0,494,566,515,492,479,530,514],
[499,506,0,544,487,482,519,518,500],
[488,434,456,0,475,446,465,463,481],
[513,485,513,525,0,498,535,520,500],
[570,508,518,554,502,0,498,538,524],
[538,521,481,535,465,502,0,504,501],
[499,470,482,537,480,462,496,0,470],
[536,486,500,519,500,476,499,530,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 104, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,496,579,542,583,587,509,517,428],
[504,0,504,539,500,524,437,527,395],
[421,496,0,525,565,493,434,470,500],
[458,461,475,0,493,481,463,492,469],
[417,500,435,507,0,556,398,419,442],
[413,476,507,519,444,0,390,422,436],
[491,563,566,537,602,610,0,576,504],
[483,473,530,508,581,578,424,0,448],
[572,605,500,531,558,564,496,552,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 105, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,482,445,486,526,488,525,522,481],
[518,0,468,502,534,473,500,507,510],
[555,532,0,507,511,547,535,513,497],
[514,498,493,0,511,514,529,495,490],
[474,466,489,489,0,489,519,509,495],
[512,527,453,486,511,0,490,512,485],
[475,500,465,471,481,510,0,478,492],
[478,493,487,505,491,488,522,0,462],
[519,490,503,510,505,515,508,538,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 106, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,506,472,463,485,455,510,498,507],
[494,0,513,505,502,491,534,535,538],
[528,487,0,484,475,485,509,492,539],
[537,495,516,0,536,501,529,517,547],
[515,498,525,464,0,470,500,519,514],
[545,509,515,499,530,0,534,514,541],
[490,466,491,471,500,466,0,490,528],
[502,465,508,483,481,486,510,0,527],
[493,462,461,453,486,459,472,473,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 107, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,517,438,456,475,461,488,522,461],
[483,0,448,452,432,465,450,528,432],
[562,552,0,523,512,503,483,531,509],
[544,548,477,0,530,524,511,540,508],
[525,568,488,470,0,513,497,534,490],
[539,535,497,476,487,0,513,531,485],
[512,550,517,489,503,487,0,548,457],
[478,472,469,460,466,469,452,0,432],
[539,568,491,492,510,515,543,568,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 108, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,555,495,590,604,535,526,562,518],
[445,0,508,532,526,466,467,499,466],
[505,492,0,550,501,524,483,546,490],
[410,468,450,0,427,471,439,438,481],
[396,474,499,573,0,512,503,473,522],
[465,534,476,529,488,0,486,553,489],
[474,533,517,561,497,514,0,529,513],
[438,501,454,562,527,447,471,0,456],
[482,534,510,519,478,511,487,544,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 109, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,491,509,501,497,486,484,511,514],
[509,0,494,486,488,516,476,498,498],
[491,506,0,496,468,495,488,506,492],
[499,514,504,0,501,498,468,500,489],
[503,512,532,499,0,495,502,526,517],
[514,484,505,502,505,0,496,493,505],
[516,524,512,532,498,504,0,510,509],
[489,502,494,500,474,507,490,0,497],
[486,502,508,511,483,495,491,503,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 110, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,555,526,517,481,522,533,522,557],
[445,0,495,492,483,555,477,518,507],
[474,505,0,510,492,536,473,489,501],
[483,508,490,0,503,513,491,499,501],
[519,517,508,497,0,554,484,515,546],
[478,445,464,487,446,0,469,485,518],
[467,523,527,509,516,531,0,532,533],
[478,482,511,501,485,515,468,0,521],
[443,493,499,499,454,482,467,479,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 111, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,496,519,520,496,479,494,472,492],
[504,0,510,518,475,499,486,468,482],
[481,490,0,472,459,467,464,451,477],
[480,482,528,0,476,492,478,481,474],
[504,525,541,524,0,498,496,498,533],
[521,501,533,508,502,0,503,504,499],
[506,514,536,522,504,497,0,492,520],
[528,532,549,519,502,496,508,0,520],
[508,518,523,526,467,501,480,480,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 112, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,529,506,519,494,547,539,534,540],
[471,0,474,502,443,504,482,487,524],
[494,526,0,489,500,489,487,510,548],
[481,498,511,0,509,522,519,542,547],
[506,557,500,491,0,530,526,524,561],
[453,496,511,478,470,0,505,496,530],
[461,518,513,481,474,495,0,496,519],
[466,513,490,458,476,504,504,0,516],
[460,476,452,453,439,470,481,484,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 113, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,494,511,546,510,513,505,483,510],
[506,0,512,517,506,523,488,478,526],
[489,488,0,538,493,511,499,508,504],
[454,483,462,0,468,507,464,442,468],
[490,494,507,532,0,512,480,470,474],
[487,477,489,493,488,0,510,489,488],
[495,512,501,536,520,490,0,467,538],
[517,522,492,558,530,511,533,0,534],
[490,474,496,532,526,512,462,466,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 114, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,491,480,509,495,513,483,521,503],
[509,0,517,509,501,530,506,470,529],
[520,483,0,510,483,522,497,496,485],
[491,491,490,0,478,528,485,500,505],
[505,499,517,522,0,537,506,503,507],
[487,470,478,472,463,0,492,467,475],
[517,494,503,515,494,508,0,492,495],
[479,530,504,500,497,533,508,0,511],
[497,471,515,495,493,525,505,489,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 115, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,494,526,520,491,480,486,541,514],
[506,0,506,540,487,478,507,501,513],
[474,494,0,516,482,500,464,543,494],
[480,460,484,0,463,460,501,526,482],
[509,513,518,537,0,491,514,561,525],
[520,522,500,540,509,0,516,544,506],
[514,493,536,499,486,484,0,526,524],
[459,499,457,474,439,456,474,0,482],
[486,487,506,518,475,494,476,518,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 116, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,492,495,509,511,514,514,520,520],
[508,0,495,520,540,552,517,511,539],
[505,505,0,479,497,519,509,487,503],
[491,480,521,0,500,543,511,523,511],
[489,460,503,500,0,520,504,502,515],
[486,448,481,457,480,0,480,455,466],
[486,483,491,489,496,520,0,493,530],
[480,489,513,477,498,545,507,0,498],
[480,461,497,489,485,534,470,502,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 117, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,484,503,478,470,507,496,510,500],
[516,0,499,474,502,463,476,490,464],
[497,501,0,482,507,526,486,528,484],
[522,526,518,0,522,526,509,534,492],
[530,498,493,478,0,493,504,519,512],
[493,537,474,474,507,0,492,509,483],
[504,524,514,491,496,508,0,517,500],
[490,510,472,466,481,491,483,0,459],
[500,536,516,508,488,517,500,541,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 118, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,498,494,492,522,522,513,515,504],
[502,0,513,484,517,527,497,479,488],
[506,487,0,509,507,520,508,518,513],
[508,516,491,0,510,525,511,504,529],
[478,483,493,490,0,510,483,489,490],
[478,473,480,475,490,0,485,491,493],
[487,503,492,489,517,515,0,518,493],
[485,521,482,496,511,509,482,0,516],
[496,512,487,471,510,507,507,484,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 119, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,477,514,502,486,491,496,512,476],
[523,0,532,493,524,545,488,538,524],
[486,468,0,456,466,514,472,511,483],
[498,507,544,0,477,541,504,519,500],
[514,476,534,523,0,505,485,522,475],
[509,455,486,459,495,0,463,520,485],
[504,512,528,496,515,537,0,499,487],
[488,462,489,481,478,480,501,0,451],
[524,476,517,500,525,515,513,549,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 120, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,470,503,521,517,516,497,461,515],
[530,0,517,515,525,516,488,502,509],
[497,483,0,482,487,477,467,463,476],
[479,485,518,0,487,481,502,466,490],
[483,475,513,513,0,520,527,498,502],
[484,484,523,519,480,0,500,491,498],
[503,512,533,498,473,500,0,480,490],
[539,498,537,534,502,509,520,0,517],
[485,491,524,510,498,502,510,483,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 121, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,487,503,502,495,472,487,508,490],
[513,0,535,517,484,498,507,529,480],
[497,465,0,509,483,471,470,484,484],
[498,483,491,0,491,488,504,500,495],
[505,516,517,509,0,489,482,505,497],
[528,502,529,512,511,0,496,513,489],
[513,493,530,496,518,504,0,489,500],
[492,471,516,500,495,487,511,0,480],
[510,520,516,505,503,511,500,520,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 122, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,496,482,514,498,474,492,516,483],
[504,0,516,501,512,494,506,527,484],
[518,484,0,511,504,470,491,483,493],
[486,499,489,0,473,475,511,485,499],
[502,488,496,527,0,509,488,498,491],
[526,506,530,525,491,0,521,512,511],
[508,494,509,489,512,479,0,499,482],
[484,473,517,515,502,488,501,0,500],
[517,516,507,501,509,489,518,500,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 123, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,483,494,450,438,480,462,486,500],
[517,0,520,474,475,521,500,486,515],
[506,480,0,501,491,467,447,437,490],
[550,526,499,0,520,546,545,516,517],
[562,525,509,480,0,524,522,484,493],
[520,479,533,454,476,0,487,478,497],
[538,500,553,455,478,513,0,477,523],
[514,514,563,484,516,522,523,0,496],
[500,485,510,483,507,503,477,504,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 124, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,392,584,445,634,477,649,527,578],
[608,0,629,486,664,608,527,504,523],
[416,371,0,388,415,484,316,404,329],
[555,514,612,0,621,458,620,490,606],
[366,336,585,379,0,584,615,528,453],
[523,392,516,542,416,0,500,737,514],
[351,473,684,380,385,500,0,559,574],
[473,496,596,510,472,263,441,0,504],
[422,477,671,394,547,486,426,496,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 125, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,501,545,509,497,542,494,552,486],
[499,0,494,502,509,476,471,498,496],
[455,506,0,469,498,464,468,494,499],
[491,498,531,0,470,491,534,525,459],
[503,491,502,530,0,523,499,526,541],
[458,524,536,509,477,0,479,488,520],
[506,529,532,466,501,521,0,553,490],
[448,502,506,475,474,512,447,0,498],
[514,504,501,541,459,480,510,502,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 126, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,485,471,496,524,479,485,512,492],
[515,0,505,534,532,500,539,523,530],
[529,495,0,527,535,508,503,507,509],
[504,466,473,0,507,503,488,502,497],
[476,468,465,493,0,479,507,507,492],
[521,500,492,497,521,0,520,513,487],
[515,461,497,512,493,480,0,514,486],
[488,477,493,498,493,487,486,0,501],
[508,470,491,503,508,513,514,499,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 127, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,523,577,493,536,541,502,494,552],
[477,0,495,504,501,534,489,506,532],
[423,505,0,465,421,463,470,442,466],
[507,496,535,0,525,526,502,486,522],
[464,499,579,475,0,528,515,514,500],
[459,466,537,474,472,0,494,477,467],
[498,511,530,498,485,506,0,470,515],
[506,494,558,514,486,523,530,0,528],
[448,468,534,478,500,533,485,472,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 128, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,474,495,502,509,485,488,494,480],
[526,0,510,534,528,509,490,493,501],
[505,490,0,502,521,507,444,521,484],
[498,466,498,0,484,487,468,471,480],
[491,472,479,516,0,492,465,486,474],
[515,491,493,513,508,0,504,517,499],
[512,510,556,532,535,496,0,521,506],
[506,507,479,529,514,483,479,0,486],
[520,499,516,520,526,501,494,514,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 129, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,481,443,370,432,466,421,429,581],
[519,0,573,348,552,649,577,391,618],
[557,427,0,522,490,538,527,579,505],
[630,652,478,0,689,682,570,595,685],
[568,448,510,311,0,616,493,547,550],
[534,351,462,318,384,0,506,393,622],
[579,423,473,430,507,494,0,452,529],
[571,609,421,405,453,607,548,0,635],
[419,382,495,315,450,378,471,365,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 130, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,474,495,502,489,489,474,490,518],
[526,0,501,525,508,518,477,518,516],
[505,499,0,519,503,479,501,504,493],
[498,475,481,0,472,478,462,503,480],
[511,492,497,528,0,479,482,510,495],
[511,482,521,522,521,0,490,516,509],
[526,523,499,538,518,510,0,526,504],
[510,482,496,497,490,484,474,0,492],
[482,484,507,520,505,491,496,508,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 131, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,484,497,471,465,509,476,486,488],
[516,0,506,522,489,557,507,528,532],
[503,494,0,490,479,527,479,494,500],
[529,478,510,0,523,533,509,532,535],
[535,511,521,477,0,542,522,497,521],
[491,443,473,467,458,0,464,496,467],
[524,493,521,491,478,536,0,510,494],
[514,472,506,468,503,504,490,0,513],
[512,468,500,465,479,533,506,487,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 132, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,544,520,624,539,533,520,514,469],
[456,0,538,542,508,448,481,460,504],
[480,462,0,595,513,446,519,459,560],
[376,458,405,0,484,411,445,428,425],
[461,492,487,516,0,453,455,512,395],
[467,552,554,589,547,0,511,512,521],
[480,519,481,555,545,489,0,526,531],
[486,540,541,572,488,488,474,0,478],
[531,496,440,575,605,479,469,522,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 133, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,528,509,496,501,506,488,529,528],
[472,0,516,487,497,494,493,515,509],
[491,484,0,502,501,498,508,499,540],
[504,513,498,0,493,506,478,504,515],
[499,503,499,507,0,493,489,504,517],
[494,506,502,494,507,0,484,513,526],
[512,507,492,522,511,516,0,527,520],
[471,485,501,496,496,487,473,0,499],
[472,491,460,485,483,474,480,501,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 134, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,495,479,480,480,491,508,518,517],
[505,0,462,492,499,486,522,551,516],
[521,538,0,500,505,500,537,530,530],
[520,508,500,0,525,484,542,542,534],
[520,501,495,475,0,489,514,543,511],
[509,514,500,516,511,0,496,510,526],
[492,478,463,458,486,504,0,516,515],
[482,449,470,458,457,490,484,0,495],
[483,484,470,466,489,474,485,505,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 135, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,487,481,490,455,518,538,454,495],
[513,0,436,520,463,575,534,563,647],
[519,564,0,614,502,556,561,498,628],
[510,480,386,0,432,530,521,427,579],
[545,537,498,568,0,511,589,491,602],
[482,425,444,470,489,0,602,509,592],
[462,466,439,479,411,398,0,463,502],
[546,437,502,573,509,491,537,0,484],
[505,353,372,421,398,408,498,516,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 136, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,489,485,479,483,493,506,518,504],
[511,0,510,492,533,521,552,501,519],
[515,490,0,495,495,483,517,486,505],
[521,508,505,0,520,508,512,499,522],
[517,467,505,480,0,492,487,509,487],
[507,479,517,492,508,0,521,512,511],
[494,448,483,488,513,479,0,460,488],
[482,499,514,501,491,488,540,0,522],
[496,481,495,478,513,489,512,478,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 137, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,541,492,700,332,235,556,466,603],
[459,0,503,606,550,348,551,456,565],
[508,497,0,540,284,287,591,502,442],
[300,394,460,0,274,200,354,259,361],
[668,450,716,726,0,548,431,589,512],
[765,652,713,800,452,0,487,547,490],
[444,449,409,646,569,513,0,455,450],
[534,544,498,741,411,453,545,0,491],
[397,435,558,639,488,510,550,509,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 138, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,433,339,424,372,427,416,393,580],
[567,0,471,552,557,544,478,481,659],
[661,529,0,473,561,552,547,548,740],
[576,448,527,0,541,583,481,468,639],
[628,443,439,459,0,597,486,458,674],
[573,456,448,417,403,0,470,434,586],
[584,522,453,519,514,530,0,573,690],
[607,519,452,532,542,566,427,0,696],
[420,341,260,361,326,414,310,304,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 139, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,532,539,535,551,537,499,527,504],
[468,0,539,534,551,572,538,501,544],
[461,461,0,498,503,479,467,506,479],
[465,466,502,0,533,539,551,475,514],
[449,449,497,467,0,507,456,489,476],
[463,428,521,461,493,0,486,495,496],
[501,462,533,449,544,514,0,498,492],
[473,499,494,525,511,505,502,0,487],
[496,456,521,486,524,504,508,513,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 140, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,470,472,499,532,448,503,498,465],
[530,0,498,516,533,518,518,513,472],
[528,502,0,512,522,505,489,514,487],
[501,484,488,0,507,487,500,505,485],
[468,467,478,493,0,432,459,497,483],
[552,482,495,513,568,0,506,519,506],
[497,482,511,500,541,494,0,508,498],
[502,487,486,495,503,481,492,0,463],
[535,528,513,515,517,494,502,537,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 141, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,582,531,493,520,542,560,580,564],
[418,0,477,489,495,517,495,508,550],
[469,523,0,491,486,544,530,515,546],
[507,511,509,0,471,528,524,518,536],
[480,505,514,529,0,548,507,550,546],
[458,483,456,472,452,0,455,524,465],
[440,505,470,476,493,545,0,497,537],
[420,492,485,482,450,476,503,0,497],
[436,450,454,464,454,535,463,503,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 142, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,531,497,506,491,491,499,500,523],
[469,0,481,485,467,488,497,477,486],
[503,519,0,504,505,494,484,491,502],
[494,515,496,0,502,488,488,487,526],
[509,533,495,498,0,539,480,506,511],
[509,512,506,512,461,0,492,498,538],
[501,503,516,512,520,508,0,484,549],
[500,523,509,513,494,502,516,0,555],
[477,514,498,474,489,462,451,445,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 143, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,513,503,502,491,500,486,505,491],
[487,0,489,504,493,492,484,479,501],
[497,511,0,501,508,486,516,483,496],
[498,496,499,0,506,508,494,499,500],
[509,507,492,494,0,494,495,492,504],
[500,508,514,492,506,0,503,493,500],
[514,516,484,506,505,497,0,488,490],
[495,521,517,501,508,507,512,0,496],
[509,499,504,500,496,500,510,504,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 144, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,501,546,496,529,505,511,512,523],
[499,0,514,481,502,496,505,488,479],
[454,486,0,453,492,491,500,484,472],
[504,519,547,0,515,525,517,524,488],
[471,498,508,485,0,504,488,491,482],
[495,504,509,475,496,0,501,498,480],
[489,495,500,483,512,499,0,501,503],
[488,512,516,476,509,502,499,0,499],
[477,521,528,512,518,520,497,501,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 145, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,510,505,488,494,512,499,521,525],
[490,0,518,490,469,511,483,510,485],
[495,482,0,499,437,480,486,495,511],
[512,510,501,0,507,526,471,520,506],
[506,531,563,493,0,517,507,502,527],
[488,489,520,474,483,0,473,500,477],
[501,517,514,529,493,527,0,526,497],
[479,490,505,480,498,500,474,0,490],
[475,515,489,494,473,523,503,510,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 146, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,549,539,504,505,517,496,538,499],
[451,0,495,475,455,499,473,499,496],
[461,505,0,460,478,484,487,493,497],
[496,525,540,0,493,509,517,508,519],
[495,545,522,507,0,512,530,527,518],
[483,501,516,491,488,0,500,512,510],
[504,527,513,483,470,500,0,505,489],
[462,501,507,492,473,488,495,0,508],
[501,504,503,481,482,490,511,492,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 147, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,499,483,509,499,510,516,517,518],
[501,0,503,525,490,508,499,518,520],
[517,497,0,503,517,517,512,516,532],
[491,475,497,0,475,490,500,492,514],
[501,510,483,525,0,502,515,507,505],
[490,492,483,510,498,0,510,514,498],
[484,501,488,500,485,490,0,495,520],
[483,482,484,508,493,486,505,0,494],
[482,480,468,486,495,502,480,506,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 148, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,511,453,479,477,483,515,453,503],
[489,0,472,478,456,474,468,471,478],
[547,528,0,534,483,530,536,524,548],
[521,522,466,0,521,516,530,502,547],
[523,544,517,479,0,481,519,522,543],
[517,526,470,484,519,0,498,524,576],
[485,532,464,470,481,502,0,479,505],
[547,529,476,498,478,476,521,0,537],
[497,522,452,453,457,424,495,463,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 149, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,469,460,490,501,486,477,488,476],
[531,0,518,514,509,514,493,508,496],
[540,482,0,537,506,478,512,510,515],
[510,486,463,0,485,468,482,491,479],
[499,491,494,515,0,490,481,517,485],
[514,486,522,532,510,0,488,516,496],
[523,507,488,518,519,512,0,511,516],
[512,492,490,509,483,484,489,0,478],
[524,504,485,521,515,504,484,522,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 150, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,496,487,544,525,479,514,502,505],
[504,0,492,531,518,472,489,520,485],
[513,508,0,515,517,482,508,509,518],
[456,469,485,0,502,468,502,458,491],
[475,482,483,498,0,466,490,455,459],
[521,528,518,532,534,0,498,473,500],
[486,511,492,498,510,502,0,510,510],
[498,480,491,542,545,527,490,0,502],
[495,515,482,509,541,500,490,498,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 151, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,498,517,492,498,494,465,511,488],
[502,0,495,534,510,486,463,504,466],
[483,505,0,529,516,533,495,519,505],
[508,466,471,0,501,513,455,501,456],
[502,490,484,499,0,515,473,508,501],
[506,514,467,487,485,0,459,507,516],
[535,537,505,545,527,541,0,532,500],
[489,496,481,499,492,493,468,0,465],
[512,534,495,544,499,484,500,535,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 152, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,496,505,491,495,483,475,509,505],
[504,0,499,523,535,523,525,503,519],
[495,501,0,511,496,494,494,490,491],
[509,477,489,0,509,506,502,499,507],
[505,465,504,491,0,485,491,488,500],
[517,477,506,494,515,0,494,516,520],
[525,475,506,498,509,506,0,504,503],
[491,497,510,501,512,484,496,0,509],
[495,481,509,493,500,480,497,491,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 153, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,479,498,501,531,508,522,516,484],
[521,0,500,534,518,516,539,524,509],
[502,500,0,529,544,528,525,491,496],
[499,466,471,0,513,499,529,482,481],
[469,482,456,487,0,493,482,487,460],
[492,484,472,501,507,0,512,474,466],
[478,461,475,471,518,488,0,492,489],
[484,476,509,518,513,526,508,0,498],
[516,491,504,519,540,534,511,502,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 154, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,523,493,479,506,474,483,484,481],
[477,0,457,475,487,491,460,463,458],
[507,543,0,540,502,518,474,489,501],
[521,525,460,0,505,503,481,487,479],
[494,513,498,495,0,482,495,508,486],
[526,509,482,497,518,0,501,501,485],
[517,540,526,519,505,499,0,524,500],
[516,537,511,513,492,499,476,0,503],
[519,542,499,521,514,515,500,497,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 155, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,541,468,475,525,502,494,547,488],
[459,0,451,465,511,488,482,493,455],
[532,549,0,516,547,559,519,505,500],
[525,535,484,0,531,510,493,508,440],
[475,489,453,469,0,478,481,523,483],
[498,512,441,490,522,0,501,489,472],
[506,518,481,507,519,499,0,506,496],
[453,507,495,492,477,511,494,0,471],
[512,545,500,560,517,528,504,529,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 156, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,519,523,523,499,495,527,497,512],
[481,0,503,504,479,496,501,500,497],
[477,497,0,500,480,496,501,494,495],
[477,496,500,0,503,511,497,509,498],
[501,521,520,497,0,490,523,507,516],
[505,504,504,489,510,0,516,483,502],
[473,499,499,503,477,484,0,497,476],
[503,500,506,491,493,517,503,0,495],
[488,503,505,502,484,498,524,505,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 157, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,455,486,439,451,455,448,462,500],
[545,0,502,495,536,491,535,506,534],
[514,498,0,463,487,453,486,490,503],
[561,505,537,0,518,484,541,500,515],
[549,464,513,482,0,472,514,475,497],
[545,509,547,516,528,0,525,491,502],
[552,465,514,459,486,475,0,518,498],
[538,494,510,500,525,509,482,0,507],
[500,466,497,485,503,498,502,493,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 158, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,375,579,371,419,687,542,630,353],
[625,0,715,503,495,759,619,699,659],
[421,285,0,589,497,561,543,640,301],
[629,497,411,0,434,552,603,539,390],
[581,505,503,566,0,608,520,739,481],
[313,241,439,448,392,0,489,542,355],
[458,381,457,397,480,511,0,526,332],
[370,301,360,461,261,458,474,0,400],
[647,341,699,610,519,645,668,600,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 159, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,511,551,488,487,504,494,522,490],
[489,0,515,478,461,459,483,485,466],
[449,485,0,463,482,452,494,451,459],
[512,522,537,0,512,509,514,504,490],
[513,539,518,488,0,506,513,473,470],
[496,541,548,491,494,0,509,536,488],
[506,517,506,486,487,491,0,499,482],
[478,515,549,496,527,464,501,0,505],
[510,534,541,510,530,512,518,495,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 160, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,541,588,538,537,502,471,540,535],
[459,0,500,490,548,490,504,528,484],
[412,500,0,475,477,458,470,523,463],
[462,510,525,0,458,488,463,542,470],
[463,452,523,542,0,465,501,547,514],
[498,510,542,512,535,0,497,564,515],
[529,496,530,537,499,503,0,526,499],
[460,472,477,458,453,436,474,0,456],
[465,516,537,530,486,485,501,544,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 161, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,495,497,498,523,534,515,504,520],
[505,0,499,527,518,520,515,538,537],
[503,501,0,539,503,519,488,528,493],
[502,473,461,0,473,497,447,481,519],
[477,482,497,527,0,495,502,548,523],
[466,480,481,503,505,0,480,479,489],
[485,485,512,553,498,520,0,511,516],
[496,462,472,519,452,521,489,0,499],
[480,463,507,481,477,511,484,501,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 162, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,503,477,499,501,509,498,478,492],
[497,0,513,501,514,505,505,494,493],
[523,487,0,505,494,492,511,491,497],
[501,499,495,0,510,510,515,501,499],
[499,486,506,490,0,508,525,494,501],
[491,495,508,490,492,0,528,473,506],
[502,495,489,485,475,472,0,483,487],
[522,506,509,499,506,527,517,0,533],
[508,507,503,501,499,494,513,467,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 163, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,490,487,489,500,475,485,495,498],
[510,0,492,498,499,493,491,508,486],
[513,508,0,527,500,494,509,494,492],
[511,502,473,0,499,477,497,499,493],
[500,501,500,501,0,491,514,497,502],
[525,507,506,523,509,0,508,486,490],
[515,509,491,503,486,492,0,494,483],
[505,492,506,501,503,514,506,0,494],
[502,514,508,507,498,510,517,506,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 164, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,551,511,557,499,479,514,470,491],
[449,0,477,510,446,516,478,462,463],
[489,523,0,558,472,531,523,474,520],
[443,490,442,0,451,441,453,451,411],
[501,554,528,549,0,556,514,518,445],
[521,484,469,559,444,0,510,476,489],
[486,522,477,547,486,490,0,489,508],
[530,538,526,549,482,524,511,0,474],
[509,537,480,589,555,511,492,526,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 165, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,518,453,423,430,468,443,481,429],
[482,0,464,479,471,483,481,492,471],
[547,536,0,492,502,547,511,554,523],
[577,521,508,0,565,531,446,491,453],
[570,529,498,435,0,539,498,547,502],
[532,517,453,469,461,0,418,446,444],
[557,519,489,554,502,582,0,508,487],
[519,508,446,509,453,554,492,0,519],
[571,529,477,547,498,556,513,481,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 166, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,481,497,471,493,511,498,494,502],
[519,0,509,480,512,545,500,549,532],
[503,491,0,499,513,527,498,536,507],
[529,520,501,0,502,512,486,569,500],
[507,488,487,498,0,521,483,506,493],
[489,455,473,488,479,0,469,514,504],
[502,500,502,514,517,531,0,515,528],
[506,451,464,431,494,486,485,0,463],
[498,468,493,500,507,496,472,537,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 167, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,530,509,503,510,495,534,526,531],
[470,0,489,485,485,476,510,471,474],
[491,511,0,514,510,518,542,487,535],
[497,515,486,0,494,483,504,471,503],
[490,515,490,506,0,499,485,493,482],
[505,524,482,517,501,0,508,512,508],
[466,490,458,496,515,492,0,491,487],
[474,529,513,529,507,488,509,0,515],
[469,526,465,497,518,492,513,485,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 168, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,521,532,534,530,551,496,530,519],
[479,0,527,508,544,528,489,493,493],
[468,473,0,506,511,494,475,497,488],
[466,492,494,0,528,502,500,489,476],
[470,456,489,472,0,494,487,480,480],
[449,472,506,498,506,0,494,477,492],
[504,511,525,500,513,506,0,519,514],
[470,507,503,511,520,523,481,0,493],
[481,507,512,524,520,508,486,507,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 169, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,523,494,508,490,506,511,521,514],
[477,0,479,505,507,500,502,494,497],
[506,521,0,528,487,515,515,515,527],
[492,495,472,0,481,496,497,495,484],
[510,493,513,519,0,515,510,532,503],
[494,500,485,504,485,0,478,512,494],
[489,498,485,503,490,522,0,525,500],
[479,506,485,505,468,488,475,0,483],
[486,503,473,516,497,506,500,517,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 170, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,553,529,515,555,564,524,493,548],
[447,0,516,497,503,543,474,496,477],
[471,484,0,497,471,527,456,475,524],
[485,503,503,0,495,533,496,497,531],
[445,497,529,505,0,543,493,514,487],
[436,457,473,467,457,0,471,498,487],
[476,526,544,504,507,529,0,504,499],
[507,504,525,503,486,502,496,0,515],
[452,523,476,469,513,513,501,485,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 171, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,520,521,517,523,506,487,514,514],
[480,0,501,494,511,497,484,475,491],
[479,499,0,492,513,462,480,492,515],
[483,506,508,0,500,484,488,485,478],
[477,489,487,500,0,516,495,491,489],
[494,503,538,516,484,0,496,494,508],
[513,516,520,512,505,504,0,488,498],
[486,525,508,515,509,506,512,0,490],
[486,509,485,522,511,492,502,510,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 172, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,514,505,527,532,493,520,463,517],
[486,0,482,492,544,461,500,507,485],
[495,518,0,508,529,492,487,486,510],
[473,508,492,0,526,474,473,445,472],
[468,456,471,474,0,451,492,473,485],
[507,539,508,526,549,0,487,486,503],
[480,500,513,527,508,513,0,467,511],
[537,493,514,555,527,514,533,0,515],
[483,515,490,528,515,497,489,485,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 173, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,488,483,518,448,478,480,479,468],
[512,0,496,512,459,512,470,489,504],
[517,504,0,559,505,482,512,455,494],
[482,488,441,0,422,441,480,425,502],
[552,541,495,578,0,517,537,493,533],
[522,488,518,559,483,0,488,516,516],
[520,530,488,520,463,512,0,477,508],
[521,511,545,575,507,484,523,0,503],
[532,496,506,498,467,484,492,497,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 174, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,489,476,501,513,485,513,538,524],
[511,0,456,508,511,519,498,515,491],
[524,544,0,505,541,485,553,514,552],
[499,492,495,0,532,492,483,502,482],
[487,489,459,468,0,490,486,521,497],
[515,481,515,508,510,0,498,499,504],
[487,502,447,517,514,502,0,478,503],
[462,485,486,498,479,501,522,0,480],
[476,509,448,518,503,496,497,520,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 175, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,520,545,511,537,493,527,526,519],
[480,0,511,510,494,481,486,494,476],
[455,489,0,501,478,497,472,493,474],
[489,490,499,0,488,494,475,501,487],
[463,506,522,512,0,490,477,506,497],
[507,519,503,506,510,0,496,495,485],
[473,514,528,525,523,504,0,499,493],
[474,506,507,499,494,505,501,0,499],
[481,524,526,513,503,515,507,501,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 176, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,550,463,490,485,539,507,514,513],
[450,0,465,500,470,465,516,495,440],
[537,535,0,509,524,538,490,553,525],
[510,500,491,0,473,530,518,515,464],
[515,530,476,527,0,524,544,524,544],
[461,535,462,470,476,0,465,469,424],
[493,484,510,482,456,535,0,513,470],
[486,505,447,485,476,531,487,0,488],
[487,560,475,536,456,576,530,512,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 177, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,498,466,488,495,514,470,477,480],
[502,0,468,511,518,467,480,507,521],
[534,532,0,526,494,547,562,474,539],
[512,489,474,0,528,515,494,473,482],
[505,482,506,472,0,489,516,505,534],
[486,533,453,485,511,0,513,512,497],
[530,520,438,506,484,487,0,488,509],
[523,493,526,527,495,488,512,0,498],
[520,479,461,518,466,503,491,502,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 178, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,478,482,502,507,505,496,513,508],
[522,0,488,522,514,493,514,518,509],
[518,512,0,512,502,497,502,517,502],
[498,478,488,0,496,487,496,508,503],
[493,486,498,504,0,491,476,501,507],
[495,507,503,513,509,0,502,530,499],
[504,486,498,504,524,498,0,499,511],
[487,482,483,492,499,470,501,0,492],
[492,491,498,497,493,501,489,508,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 179, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,357,405,530,638,680,649,770,429],
[643,0,446,598,619,724,557,501,441],
[595,554,0,503,803,499,632,776,563],
[470,402,497,0,654,502,440,759,417],
[362,381,197,346,0,567,420,589,393],
[320,276,501,498,433,0,402,556,392],
[351,443,368,560,580,598,0,521,489],
[230,499,224,241,411,444,479,0,394],
[571,559,437,583,607,608,511,606,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 180, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,530,526,540,515,496,509,511,512],
[470,0,484,504,492,467,500,500,482],
[474,516,0,527,494,477,493,493,485],
[460,496,473,0,486,471,480,499,501],
[485,508,506,514,0,500,504,497,513],
[504,533,523,529,500,0,519,517,507],
[491,500,507,520,496,481,0,498,504],
[489,500,507,501,503,483,502,0,483],
[488,518,515,499,487,493,496,517,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 181, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,505,514,501,440,494,481,488,478],
[495,0,501,465,488,497,497,473,515],
[486,499,0,468,467,507,505,470,488],
[499,535,532,0,506,528,501,508,516],
[560,512,533,494,0,510,542,497,528],
[506,503,493,472,490,0,457,488,487],
[519,503,495,499,458,543,0,472,485],
[512,527,530,492,503,512,528,0,524],
[522,485,512,484,472,513,515,476,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 182, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,462,511,521,499,481,507,500,487],
[538,0,544,512,520,509,535,521,500],
[489,456,0,465,477,489,519,465,484],
[479,488,535,0,485,492,487,488,476],
[501,480,523,515,0,495,509,504,493],
[519,491,511,508,505,0,495,475,485],
[493,465,481,513,491,505,0,470,466],
[500,479,535,512,496,525,530,0,488],
[513,500,516,524,507,515,534,512,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 183, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,527,516,527,500,502,512,486,469],
[473,0,472,482,493,459,527,500,459],
[484,528,0,495,532,480,513,493,470],
[473,518,505,0,526,490,522,504,483],
[500,507,468,474,0,465,503,493,454],
[498,541,520,510,535,0,548,503,506],
[488,473,487,478,497,452,0,496,451],
[514,500,507,496,507,497,504,0,482],
[531,541,530,517,546,494,549,518,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 184, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,511,467,493,492,563,505,463,517],
[489,0,528,485,510,536,501,542,499],
[533,472,0,527,474,527,525,569,508],
[507,515,473,0,507,563,495,483,505],
[508,490,526,493,0,562,544,533,476],
[437,464,473,437,438,0,507,531,512],
[495,499,475,505,456,493,0,557,525],
[537,458,431,517,467,469,443,0,450],
[483,501,492,495,524,488,475,550,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 185, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,493,487,466,484,508,480,483,481],
[507,0,519,499,493,503,501,502,492],
[513,481,0,482,507,510,485,485,490],
[534,501,518,0,493,516,524,514,496],
[516,507,493,507,0,489,503,521,507],
[492,497,490,484,511,0,498,490,489],
[520,499,515,476,497,502,0,501,497],
[517,498,515,486,479,510,499,0,514],
[519,508,510,504,493,511,503,486,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 186, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,517,526,508,527,494,502,519,503],
[483,0,519,527,497,511,510,499,470],
[474,481,0,463,486,502,469,491,464],
[492,473,537,0,486,499,483,511,471],
[473,503,514,514,0,485,513,501,457],
[506,489,498,501,515,0,523,498,512],
[498,490,531,517,487,477,0,521,500],
[481,501,509,489,499,502,479,0,484],
[497,530,536,529,543,488,500,516,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 187, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,521,494,501,486,508,481,480,496],
[479,0,484,497,487,489,464,461,491],
[506,516,0,514,475,488,478,475,504],
[499,503,486,0,472,489,467,484,494],
[514,513,525,528,0,494,485,491,505],
[492,511,512,511,506,0,481,503,490],
[519,536,522,533,515,519,0,492,534],
[520,539,525,516,509,497,508,0,510],
[504,509,496,506,495,510,466,490,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 188, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,491,448,526,409,482,423,505,460],
[509,0,455,559,460,489,505,509,547],
[552,545,0,612,469,526,480,534,576],
[474,441,388,0,408,458,403,424,462],
[591,540,531,592,0,500,532,560,567],
[518,511,474,542,500,0,452,514,557],
[577,495,520,597,468,548,0,515,564],
[495,491,466,576,440,486,485,0,540],
[540,453,424,538,433,443,436,460,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 189, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,497,492,497,490,495,494,506,504],
[503,0,474,510,519,498,499,502,507],
[508,526,0,518,480,496,518,499,520],
[503,490,482,0,470,492,493,506,497],
[510,481,520,530,0,509,513,513,529],
[505,502,504,508,491,0,482,510,520],
[506,501,482,507,487,518,0,506,473],
[494,498,501,494,487,490,494,0,501],
[496,493,480,503,471,480,527,499,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 190, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,442,468,458,451,463,495,450,491],
[558,0,518,509,478,558,607,476,544],
[532,482,0,470,517,521,554,498,504],
[542,491,530,0,539,505,602,505,544],
[549,522,483,461,0,546,536,517,522],
[537,442,479,495,454,0,528,472,506],
[505,393,446,398,464,472,0,417,432],
[550,524,502,495,483,528,583,0,559],
[509,456,496,456,478,494,568,441,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 191, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,507,491,525,509,503,500,494,540],
[493,0,463,530,500,451,490,507,530],
[509,537,0,536,502,527,490,517,546],
[475,470,464,0,479,486,493,481,506],
[491,500,498,521,0,475,498,484,527],
[497,549,473,514,525,0,509,519,540],
[500,510,510,507,502,491,0,491,531],
[506,493,483,519,516,481,509,0,528],
[460,470,454,494,473,460,469,472,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 192, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,522,520,542,525,506,539,491,562],
[478,0,563,517,520,507,526,534,536],
[480,437,0,491,480,404,499,516,544],
[458,483,509,0,539,445,531,492,578],
[475,480,520,461,0,482,499,524,527],
[494,493,596,555,518,0,526,507,559],
[461,474,501,469,501,474,0,522,559],
[509,466,484,508,476,493,478,0,540],
[438,464,456,422,473,441,441,460,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 193, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,532,603,501,464,462,467,524,492],
[468,0,476,491,463,474,449,545,467],
[397,524,0,522,450,495,424,511,476],
[499,509,478,0,453,430,487,524,461],
[536,537,550,547,0,493,514,602,516],
[538,526,505,570,507,0,564,572,493],
[533,551,576,513,486,436,0,548,491],
[476,455,489,476,398,428,452,0,444],
[508,533,524,539,484,507,509,556,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 194, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,607,471,515,503,506,548,469,621],
[393,0,452,462,432,479,498,395,481],
[529,548,0,535,542,547,462,445,553],
[485,538,465,0,506,460,497,502,524],
[497,568,458,494,0,524,489,491,499],
[494,521,453,540,476,0,497,431,524],
[452,502,538,503,511,503,0,466,509],
[531,605,555,498,509,569,534,0,557],
[379,519,447,476,501,476,491,443,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 195, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,495,189,343,497,294,396,191,393],
[505,0,266,343,105,454,279,240,72],
[811,734,0,546,497,657,651,734,309],
[657,657,454,0,483,451,669,395,461],
[503,895,503,517,0,691,514,497,616],
[706,546,343,549,309,0,649,549,310],
[604,721,349,331,486,351,0,632,393],
[809,760,266,605,503,451,368,0,481],
[607,928,691,539,384,690,607,519,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 196, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,483,481,515,494,478,500,506,504],
[517,0,499,519,485,489,515,483,496],
[519,501,0,524,506,498,515,493,490],
[485,481,476,0,475,467,472,498,489],
[506,515,494,525,0,506,503,481,509],
[522,511,502,533,494,0,524,533,512],
[500,485,485,528,497,476,0,507,501],
[494,517,507,502,519,467,493,0,526],
[496,504,510,511,491,488,499,474,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 197, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,557,535,508,519,540,551,523,492],
[443,0,492,491,509,514,495,494,502],
[465,508,0,469,493,532,491,503,487],
[492,509,531,0,532,517,525,509,513],
[481,491,507,468,0,481,505,504,463],
[460,486,468,483,519,0,483,470,479],
[449,505,509,475,495,517,0,496,474],
[477,506,497,491,496,530,504,0,461],
[508,498,513,487,537,521,526,539,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 198, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,508,480,495,496,495,504,473,479],
[492,0,508,494,486,508,509,481,504],
[520,492,0,495,507,534,502,517,505],
[505,506,505,0,500,505,509,491,481],
[504,514,493,500,0,520,520,520,488],
[505,492,466,495,480,0,517,493,489],
[496,491,498,491,480,483,0,485,483],
[527,519,483,509,480,507,515,0,494],
[521,496,495,519,512,511,517,506,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 199, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,416,374,294,293,275,420,401,287],
[584,0,446,491,532,559,638,531,443],
[626,554,0,334,439,450,448,523,412],
[706,509,666,0,594,519,588,573,475],
[707,468,561,406,0,431,545,507,432],
[725,441,550,481,569,0,500,513,505],
[580,362,552,412,455,500,0,638,262],
[599,469,477,427,493,487,362,0,428],
[713,557,588,525,568,495,738,572,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 1000, 200, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/mebbd/mebbd_9_1000.csv", index=False, header=False)