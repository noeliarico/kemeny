
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg

rep = 3
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,515,530,520,500,479,506,504,534,498],
[486,0,514,467,463,486,479,521,520,497],
[471,487,0,458,503,462,431,464,509,484],
[481,534,543,0,481,503,501,515,544,482],
[501,538,498,520,0,499,527,517,548,503],
[522,515,539,498,502,0,490,517,513,489],
[495,522,570,500,474,511,0,492,490,518],
[497,480,537,486,484,484,509,0,514,516],
[467,481,492,457,453,488,511,487,0,457],
[503,504,517,519,498,512,483,485,544,0]])



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
result = np.append(np.array([10, 1001, 1, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,498,478,509,513,484,505,478,479,500],
[503,0,499,508,493,494,468,498,503,508],
[523,502,0,531,534,464,496,510,520,494],
[492,493,470,0,532,501,506,503,474,503],
[488,508,467,469,0,493,477,507,478,499],
[517,507,537,500,508,0,539,503,506,504],
[496,533,505,495,524,462,0,505,508,504],
[523,503,491,498,494,498,496,0,490,493],
[522,498,481,527,523,495,493,511,0,529],
[501,493,507,498,502,497,497,508,472,0]])



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
result = np.append(np.array([10, 1001, 2, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,511,502,507,491,532,522,507,496,516],
[490,0,473,490,503,526,539,531,502,524],
[499,528,0,487,485,522,522,484,494,505],
[494,511,514,0,489,548,551,516,505,515],
[510,498,516,512,0,509,526,516,493,519],
[469,475,479,453,492,0,499,493,480,488],
[479,462,479,450,475,502,0,496,476,482],
[494,470,517,485,485,508,505,0,469,490],
[505,499,507,496,508,521,525,532,0,521],
[485,477,496,486,482,513,519,511,480,0]])



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
result = np.append(np.array([10, 1001, 3, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,511,493,536,496,497,468,463,448,521],
[490,0,521,484,496,444,425,477,430,501],
[508,480,0,502,483,480,452,490,412,470],
[465,517,499,0,488,489,478,471,458,521],
[505,505,518,513,0,490,459,480,420,475],
[504,557,521,512,511,0,499,496,517,557],
[533,576,549,523,542,502,0,483,507,551],
[538,524,511,530,521,505,518,0,477,498],
[553,571,589,543,581,484,494,524,0,534],
[480,500,531,480,526,444,450,503,467,0]])



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
result = np.append(np.array([10, 1001, 4, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,482,454,487,482,499,492,505,488,493],
[519,0,517,498,522,539,513,503,527,518],
[547,484,0,521,554,541,523,510,559,545],
[514,503,480,0,542,531,532,515,535,535],
[519,479,447,459,0,523,498,499,477,508],
[502,462,460,470,478,0,481,500,468,483],
[509,488,478,469,503,520,0,522,502,481],
[496,498,491,486,502,501,479,0,527,508],
[513,474,442,466,524,533,499,474,0,509],
[508,483,456,466,493,518,520,493,492,0]])



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
result = np.append(np.array([10, 1001, 5, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,429,465,532,509,414,515,448,457,558],
[572,0,454,588,507,535,574,538,468,592],
[536,547,0,522,569,503,539,544,485,502],
[469,413,479,0,470,436,453,449,524,597],
[492,494,432,531,0,477,529,552,501,566],
[587,466,498,565,524,0,528,521,535,525],
[486,427,462,548,472,473,0,468,485,548],
[553,463,457,552,449,480,533,0,466,536],
[544,533,516,477,500,466,516,535,0,506],
[443,409,499,404,435,476,453,465,495,0]])



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
result = np.append(np.array([10, 1001, 6, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,474,493,513,518,512,494,512,522,498],
[527,0,552,521,508,520,508,491,514,497],
[508,449,0,475,512,492,469,487,483,512],
[488,480,526,0,468,480,472,504,510,478],
[483,493,489,533,0,495,500,518,529,513],
[489,481,509,521,506,0,470,489,534,500],
[507,493,532,529,501,531,0,519,525,537],
[489,510,514,497,483,512,482,0,503,496],
[479,487,518,491,472,467,476,498,0,466],
[503,504,489,523,488,501,464,505,535,0]])



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
result = np.append(np.array([10, 1001, 7, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,454,456,485,483,565,490,469,455,470],
[547,0,475,515,513,527,529,540,503,509],
[545,526,0,520,504,529,539,537,549,495],
[516,486,481,0,507,524,506,508,505,498],
[518,488,497,494,0,551,527,515,528,488],
[436,474,472,477,450,0,482,468,476,456],
[511,472,462,495,474,519,0,484,467,450],
[532,461,464,493,486,533,517,0,511,502],
[546,498,452,496,473,525,534,490,0,493],
[531,492,506,503,513,545,551,499,508,0]])



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
result = np.append(np.array([10, 1001, 8, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,465,476,497,483,478,535,525,438,490],
[536,0,488,530,508,513,564,565,476,532],
[525,513,0,468,483,479,525,533,497,537],
[504,471,533,0,501,506,514,532,467,531],
[518,493,518,500,0,482,472,576,509,518],
[523,488,522,495,519,0,524,543,494,514],
[466,437,476,487,529,477,0,528,446,478],
[476,436,468,469,425,458,473,0,445,491],
[563,525,504,534,492,507,555,556,0,551],
[511,469,464,470,483,487,523,510,450,0]])



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
result = np.append(np.array([10, 1001, 9, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,481,585,433,446,454,455,452,508,521],
[520,0,522,468,385,453,529,437,557,512],
[416,479,0,455,362,417,499,432,480,469],
[568,533,546,0,478,429,504,478,508,506],
[555,616,639,523,0,534,566,493,599,630],
[547,548,584,572,467,0,508,534,584,557],
[546,472,502,497,435,493,0,435,493,470],
[549,564,569,523,508,467,566,0,509,516],
[493,444,521,493,402,417,508,492,0,511],
[480,489,532,495,371,444,531,485,490,0]])



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
result = np.append(np.array([10, 1001, 10, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,470,471,586,589,535,478,496,468,602],
[531,0,588,538,542,528,532,488,524,527],
[530,413,0,657,534,470,541,488,458,610],
[415,463,344,0,486,446,313,462,362,437],
[412,459,467,515,0,537,436,533,393,518],
[466,473,531,555,464,0,515,554,459,542],
[523,469,460,688,565,486,0,495,374,533],
[505,513,513,539,468,447,506,0,409,537],
[533,477,543,639,608,542,627,592,0,617],
[399,474,391,564,483,459,468,464,384,0]])



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
result = np.append(np.array([10, 1001, 11, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,462,474,501,439,508,451,462,436,461],
[539,0,553,529,515,551,492,509,528,491],
[527,448,0,533,485,546,465,481,457,501],
[500,472,468,0,479,516,475,458,439,452],
[562,486,516,522,0,558,503,508,521,501],
[493,450,455,485,443,0,462,471,431,452],
[550,509,536,526,498,539,0,523,488,530],
[539,492,520,543,493,530,478,0,521,499],
[565,473,544,562,480,570,513,480,0,514],
[540,510,500,549,500,549,471,502,487,0]])



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
result = np.append(np.array([10, 1001, 12, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,500,597,489,544,494,486,490,582,566],
[501,0,540,465,465,511,440,421,471,565],
[404,461,0,467,417,381,422,392,480,549],
[512,536,534,0,435,471,495,503,547,522],
[457,536,584,566,0,535,515,532,569,631],
[507,490,620,530,466,0,508,485,497,532],
[515,561,579,506,486,493,0,508,598,579],
[511,580,609,498,469,516,493,0,496,588],
[419,530,521,454,432,504,403,505,0,609],
[435,436,452,479,370,469,422,413,392,0]])



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
result = np.append(np.array([10, 1001, 13, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,458,471,510,475,463,452,447,491,528],
[543,0,468,487,445,480,485,443,533,520],
[530,533,0,556,486,453,470,480,489,522],
[491,514,445,0,457,442,431,451,494,479],
[526,556,515,544,0,502,489,497,498,553],
[538,521,548,559,499,0,548,542,528,524],
[549,516,531,570,512,453,0,463,484,513],
[554,558,521,550,504,459,538,0,554,539],
[510,468,512,507,503,473,517,447,0,542],
[473,481,479,522,448,477,488,462,459,0]])



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
result = np.append(np.array([10, 1001, 14, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,489,532,512,523,537,508,524,503,530],
[512,0,483,454,508,531,512,499,470,527],
[469,518,0,475,497,504,496,479,423,482],
[489,547,526,0,504,523,540,518,517,521],
[478,493,504,497,0,511,487,489,467,482],
[464,470,497,478,490,0,500,483,473,477],
[493,489,505,461,514,501,0,467,482,506],
[477,502,522,483,512,518,534,0,458,532],
[498,531,578,484,534,528,519,543,0,523],
[471,474,519,480,519,524,495,469,478,0]])



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
result = np.append(np.array([10, 1001, 15, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,528,503,523,521,491,513,504,467,541],
[473,0,478,524,468,469,474,464,479,477],
[498,523,0,531,534,540,525,529,519,533],
[478,477,470,0,537,496,427,457,485,475],
[480,533,467,464,0,467,491,454,509,480],
[510,532,461,505,534,0,460,454,453,482],
[488,527,476,574,510,541,0,494,513,531],
[497,537,472,544,547,547,507,0,506,476],
[534,522,482,516,492,548,488,495,0,534],
[460,524,468,526,521,519,470,525,467,0]])



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
result = np.append(np.array([10, 1001, 16, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,522,511,507,530,478,533,494,529,494],
[479,0,462,477,493,476,501,480,492,466],
[490,539,0,524,524,495,540,518,502,508],
[494,524,477,0,514,480,524,476,503,504],
[471,508,477,487,0,462,498,481,487,485],
[523,525,506,521,539,0,528,505,496,518],
[468,500,461,477,503,473,0,467,490,458],
[507,521,483,525,520,496,534,0,498,504],
[472,509,499,498,514,505,511,503,0,491],
[507,535,493,497,516,483,543,497,510,0]])



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
result = np.append(np.array([10, 1001, 17, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,545,505,460,545,525,505,466,498,524],
[456,0,478,440,594,436,491,493,516,491],
[496,523,0,502,524,425,404,537,485,500],
[541,561,499,0,556,629,509,515,501,525],
[456,407,477,445,0,517,395,455,487,523],
[476,565,576,372,484,0,487,527,505,490],
[496,510,597,492,606,514,0,509,472,506],
[535,508,464,486,546,474,492,0,462,510],
[503,485,516,500,514,496,529,539,0,514],
[477,510,501,476,478,511,495,491,487,0]])



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
result = np.append(np.array([10, 1001, 18, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,503,528,506,529,521,487,555,486,508],
[498,0,516,486,495,493,489,534,460,495],
[473,485,0,503,504,477,481,539,479,506],
[495,515,498,0,530,502,493,562,472,515],
[472,506,497,471,0,507,498,559,452,507],
[480,508,524,499,494,0,506,565,506,532],
[514,512,520,508,503,495,0,541,491,503],
[446,467,462,439,442,436,460,0,436,473],
[515,541,522,529,549,495,510,565,0,544],
[493,506,495,486,494,469,498,528,457,0]])



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
result = np.append(np.array([10, 1001, 19, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,478,513,513,519,508,510,541,544,506],
[523,0,513,490,519,543,503,550,509,503],
[488,488,0,515,519,529,482,528,506,515],
[488,511,486,0,527,518,525,553,485,527],
[482,482,482,474,0,485,502,512,490,481],
[493,458,472,483,516,0,496,513,493,497],
[491,498,519,476,499,505,0,535,508,500],
[460,451,473,448,489,488,466,0,461,466],
[457,492,495,516,511,508,493,540,0,533],
[495,498,486,474,520,504,501,535,468,0]])



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
result = np.append(np.array([10, 1001, 20, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,517,523,569,494,484,521,515,452,543],
[484,0,504,556,504,496,506,574,466,515],
[478,497,0,526,534,502,533,532,503,428],
[432,445,475,0,451,402,423,493,412,463],
[507,497,467,550,0,379,468,434,410,474],
[517,505,499,599,622,0,481,472,514,500],
[480,495,468,578,533,520,0,492,443,487],
[486,427,469,508,567,529,509,0,457,477],
[549,535,498,589,591,487,558,544,0,523],
[458,486,573,538,527,501,514,524,478,0]])



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
result = np.append(np.array([10, 1001, 21, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,486,496,500,526,469,501,523,510,496],
[515,0,500,528,518,534,536,558,521,522],
[505,501,0,506,512,511,503,525,505,485],
[501,473,495,0,516,517,524,553,503,521],
[475,483,489,485,0,498,529,528,494,499],
[532,467,490,484,503,0,515,534,513,491],
[500,465,498,477,472,486,0,509,486,496],
[478,443,476,448,473,467,492,0,477,474],
[491,480,496,498,507,488,515,524,0,490],
[505,479,516,480,502,510,505,527,511,0]])



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
result = np.append(np.array([10, 1001, 22, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,505,540,522,507,502,498,477,521,527],
[496,0,498,520,491,497,489,501,514,513],
[461,503,0,481,474,478,464,481,494,484],
[479,481,520,0,511,484,487,498,495,504],
[494,510,527,490,0,488,484,509,532,509],
[499,504,523,517,513,0,509,508,522,525],
[503,512,537,514,517,492,0,506,518,531],
[524,500,520,503,492,493,495,0,523,528],
[480,487,507,506,469,479,483,478,0,503],
[474,488,517,497,492,476,470,473,498,0]])



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
result = np.append(np.array([10, 1001, 23, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,504,521,491,517,522,517,491,536,508],
[497,0,544,497,522,511,539,512,541,536],
[480,457,0,474,506,486,486,507,505,512],
[510,504,527,0,496,507,517,510,528,519],
[484,479,495,505,0,483,528,500,513,541],
[479,490,515,494,518,0,515,503,513,498],
[484,462,515,484,473,486,0,476,499,496],
[510,489,494,491,501,498,525,0,532,513],
[465,460,496,473,488,488,502,469,0,482],
[493,465,489,482,460,503,505,488,519,0]])



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
result = np.append(np.array([10, 1001, 24, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,481,505,474,489,480,481,490,523,509],
[520,0,495,499,516,520,513,525,532,520],
[496,506,0,517,499,488,499,501,508,505],
[527,502,484,0,488,496,511,482,534,499],
[512,485,502,513,0,499,488,523,520,496],
[521,481,513,505,502,0,507,527,525,520],
[520,488,502,490,513,494,0,510,520,502],
[511,476,500,519,478,474,491,0,533,516],
[478,469,493,467,481,476,481,468,0,484],
[492,481,496,502,505,481,499,485,517,0]])



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
result = np.append(np.array([10, 1001, 25, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,516,482,507,464,478,502,490,537,491],
[485,0,471,466,485,466,470,467,521,467],
[519,530,0,515,519,515,536,490,561,510],
[494,535,486,0,473,484,504,497,523,507],
[537,516,482,528,0,497,534,513,559,510],
[523,535,486,517,504,0,506,489,544,522],
[499,531,465,497,467,495,0,473,513,503],
[511,534,511,504,488,512,528,0,571,509],
[464,480,440,478,442,457,488,430,0,459],
[510,534,491,494,491,479,498,492,542,0]])



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
result = np.append(np.array([10, 1001, 26, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,488,527,539,492,555,536,518,560,507],
[513,0,511,493,498,534,538,477,531,503],
[474,490,0,497,475,504,517,473,523,508],
[462,508,504,0,495,522,506,457,537,498],
[509,503,526,506,0,536,524,504,519,498],
[446,467,497,479,465,0,496,473,523,479],
[465,463,484,495,477,505,0,479,531,476],
[483,524,528,544,497,528,522,0,524,526],
[441,470,478,464,482,478,470,477,0,462],
[494,498,493,503,503,522,525,475,539,0]])



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
result = np.append(np.array([10, 1001, 27, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,505,466,506,476,501,520,529,521,502],
[496,0,516,494,488,498,521,532,517,538],
[535,485,0,514,497,500,503,513,512,519],
[495,507,487,0,498,487,518,525,517,509],
[525,513,504,503,0,486,527,528,534,531],
[500,503,501,514,515,0,517,529,536,533],
[481,480,498,483,474,484,0,487,502,488],
[472,469,488,476,473,472,514,0,526,507],
[480,484,489,484,467,465,499,475,0,489],
[499,463,482,492,470,468,513,494,512,0]])



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
result = np.append(np.array([10, 1001, 28, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,480,490,504,507,500,504,481,501,532],
[521,0,533,477,493,502,473,492,507,552],
[511,468,0,472,499,484,475,475,484,523],
[497,524,529,0,515,499,499,513,525,527],
[494,508,502,486,0,507,495,498,508,542],
[501,499,517,502,494,0,486,472,495,500],
[497,528,526,502,506,515,0,501,514,533],
[520,509,526,488,503,529,500,0,500,536],
[500,494,517,476,493,506,487,501,0,528],
[469,449,478,474,459,501,468,465,473,0]])



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
result = np.append(np.array([10, 1001, 29, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,498,511,507,497,490,541,503,507,509],
[503,0,480,483,470,468,489,469,462,485],
[490,521,0,474,495,476,496,476,481,542],
[494,518,527,0,533,502,507,517,503,533],
[504,531,506,468,0,491,503,516,495,507],
[511,533,525,499,510,0,520,519,516,554],
[460,512,505,494,498,481,0,497,505,536],
[498,532,525,484,485,482,504,0,530,513],
[494,539,520,498,506,485,496,471,0,480],
[492,516,459,468,494,447,465,488,521,0]])



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
result = np.append(np.array([10, 1001, 30, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,545,491,550,499,516,526,529,533,537],
[456,0,459,460,472,429,497,475,468,463],
[510,542,0,504,503,518,516,539,505,500],
[451,541,497,0,474,499,479,523,483,526],
[502,529,498,527,0,466,507,525,513,505],
[485,572,483,502,535,0,512,553,499,505],
[475,504,485,522,494,489,0,520,457,508],
[472,526,462,478,476,448,481,0,452,482],
[468,533,496,518,488,502,544,549,0,518],
[464,538,501,475,496,496,493,519,483,0]])



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
result = np.append(np.array([10, 1001, 31, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,479,468,500,373,409,551,429,539,498],
[522,0,535,490,461,489,523,489,580,535],
[533,466,0,530,549,442,554,500,551,553],
[501,511,471,0,469,509,560,568,553,588],
[628,540,452,532,0,483,497,542,535,518],
[592,512,559,492,518,0,557,517,649,590],
[450,478,447,441,504,444,0,508,510,449],
[572,512,501,433,459,484,493,0,553,589],
[462,421,450,448,466,352,491,448,0,531],
[503,466,448,413,483,411,552,412,470,0]])



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
result = np.append(np.array([10, 1001, 32, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,475,513,478,519,501,504,470,517,486],
[526,0,506,497,532,532,503,505,492,484],
[488,495,0,491,529,497,514,487,507,496],
[523,504,510,0,510,538,495,481,493,493],
[482,469,472,491,0,471,453,462,462,483],
[500,469,504,463,530,0,485,482,484,517],
[497,498,487,506,548,516,0,478,499,509],
[531,496,514,520,539,519,523,0,518,496],
[484,509,494,508,539,517,502,483,0,519],
[515,517,505,508,518,484,492,505,482,0]])



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
result = np.append(np.array([10, 1001, 33, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,477,477,394,459,465,491,570,464,481],
[524,0,507,503,519,525,509,525,581,436],
[524,494,0,478,457,490,512,539,525,415],
[607,498,523,0,506,457,525,611,542,546],
[542,482,544,495,0,439,441,638,566,485],
[536,476,511,544,562,0,481,639,455,433],
[510,492,489,476,560,520,0,593,464,459],
[431,476,462,390,363,362,408,0,392,385],
[537,420,476,459,435,546,537,609,0,467],
[520,565,586,455,516,568,542,616,534,0]])



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
result = np.append(np.array([10, 1001, 34, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,525,495,516,525,492,562,475,515,509],
[476,0,492,513,514,491,488,474,522,508],
[506,509,0,506,505,503,492,471,524,514],
[485,488,495,0,555,464,461,476,495,504],
[476,487,496,446,0,464,463,463,486,455],
[509,510,498,537,537,0,497,502,527,510],
[439,513,509,540,538,504,0,478,499,503],
[526,527,530,525,538,499,523,0,511,490],
[486,479,477,506,515,474,502,490,0,457],
[492,493,487,497,546,491,498,511,544,0]])



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
result = np.append(np.array([10, 1001, 35, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,494,500,477,528,471,492,474,451,481],
[507,0,526,514,503,519,483,515,492,518],
[501,475,0,478,513,482,490,507,471,470],
[524,487,523,0,510,495,488,488,489,508],
[473,498,488,491,0,484,492,488,464,483],
[530,482,519,506,517,0,479,510,502,473],
[509,518,511,513,509,522,0,493,487,504],
[527,486,494,513,513,491,508,0,487,486],
[550,509,530,512,537,499,514,514,0,500],
[520,483,531,493,518,528,497,515,501,0]])



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
result = np.append(np.array([10, 1001, 36, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,531,515,507,502,504,505,474,535,519],
[470,0,513,507,506,507,498,501,516,470],
[486,488,0,505,492,496,518,475,515,492],
[494,494,496,0,467,483,497,472,546,483],
[499,495,509,534,0,486,523,493,530,493],
[497,494,505,518,515,0,503,491,512,496],
[496,503,483,504,478,498,0,500,518,485],
[527,500,526,529,508,510,501,0,542,525],
[466,485,486,455,471,489,483,459,0,445],
[482,531,509,518,508,505,516,476,556,0]])



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
result = np.append(np.array([10, 1001, 37, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,511,522,502,529,508,490,503,493,513],
[490,0,486,490,526,500,493,490,484,505],
[479,515,0,515,518,510,499,492,504,521],
[499,511,486,0,522,500,486,501,474,513],
[472,475,483,479,0,487,446,461,466,492],
[493,501,491,501,514,0,513,499,507,530],
[511,508,502,515,555,488,0,516,500,516],
[498,511,509,500,540,502,485,0,504,503],
[508,517,497,527,535,494,501,497,0,507],
[488,496,480,488,509,471,485,498,494,0]])



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
result = np.append(np.array([10, 1001, 38, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,473,544,488,492,478,498,470,476,499],
[528,0,522,524,492,480,523,501,501,512],
[457,479,0,485,490,479,500,493,479,484],
[513,477,516,0,486,488,511,464,473,460],
[509,509,511,515,0,513,504,526,480,510],
[523,521,522,513,488,0,492,523,482,514],
[503,478,501,490,497,509,0,505,474,495],
[531,500,508,537,475,478,496,0,479,510],
[525,500,522,528,521,519,527,522,0,519],
[502,489,517,541,491,487,506,491,482,0]])



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
result = np.append(np.array([10, 1001, 39, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,492,518,538,520,500,548,515,509,533],
[509,0,536,522,500,510,536,510,510,541],
[483,465,0,529,514,475,538,502,521,513],
[463,479,472,0,494,475,516,496,490,531],
[481,501,487,507,0,494,521,504,499,538],
[501,491,526,526,507,0,518,495,500,537],
[453,465,463,485,480,483,0,500,492,517],
[486,491,499,505,497,506,501,0,512,499],
[492,491,480,511,502,501,509,489,0,521],
[468,460,488,470,463,464,484,502,480,0]])



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
result = np.append(np.array([10, 1001, 40, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,368,472,540,467,463,431,501,506,469],
[633,0,519,568,479,529,503,600,438,452],
[529,482,0,575,537,542,501,559,523,472],
[461,433,426,0,517,400,480,525,476,447],
[534,522,464,484,0,470,494,541,507,486],
[538,472,459,601,531,0,524,607,504,530],
[570,498,500,521,507,477,0,558,500,512],
[500,401,442,476,460,394,443,0,482,498],
[495,563,478,525,494,497,501,519,0,531],
[532,549,529,554,515,471,489,503,470,0]])



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
result = np.append(np.array([10, 1001, 41, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,516,521,513,507,522,512,502,495,502],
[485,0,505,515,513,500,497,500,527,519],
[480,496,0,499,510,505,493,511,515,512],
[488,486,502,0,501,526,488,512,496,495],
[494,488,491,500,0,521,495,513,511,486],
[479,501,496,475,480,0,476,485,475,475],
[489,504,508,513,506,525,0,509,534,511],
[499,501,490,489,488,516,492,0,493,506],
[506,474,486,505,490,526,467,508,0,507],
[499,482,489,506,515,526,490,495,494,0]])



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
result = np.append(np.array([10, 1001, 42, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,471,509,519,492,541,487,494,523,519],
[530,0,499,519,538,544,500,502,542,531],
[492,502,0,483,458,513,496,478,523,501],
[482,482,518,0,479,522,518,483,479,487],
[509,463,543,522,0,534,497,486,523,553],
[460,457,488,479,467,0,469,462,502,451],
[514,501,505,483,504,532,0,501,547,514],
[507,499,523,518,515,539,500,0,515,509],
[478,459,478,522,478,499,454,486,0,500],
[482,470,500,514,448,550,487,492,501,0]])



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
result = np.append(np.array([10, 1001, 43, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,479,524,628,418,439,443,490,469,513],
[522,0,463,523,399,502,335,535,407,451],
[477,538,0,588,448,553,431,577,436,514],
[373,478,413,0,430,500,419,584,441,406],
[583,602,553,571,0,505,558,595,492,571],
[562,499,448,501,496,0,424,555,461,475],
[558,666,570,582,443,577,0,628,603,533],
[511,466,424,417,406,446,373,0,423,414],
[532,594,565,560,509,540,398,578,0,488],
[488,550,487,595,430,526,468,587,513,0]])



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
result = np.append(np.array([10, 1001, 44, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,522,510,481,512,516,486,562,502,508],
[479,0,535,517,510,484,515,542,511,490],
[491,466,0,483,506,474,500,504,489,497],
[520,484,518,0,503,510,525,514,522,551],
[489,491,495,498,0,472,504,498,492,503],
[485,517,527,491,529,0,498,516,508,510],
[515,486,501,476,497,503,0,506,502,518],
[439,459,497,487,503,485,495,0,464,486],
[499,490,512,479,509,493,499,537,0,501],
[493,511,504,450,498,491,483,515,500,0]])



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
result = np.append(np.array([10, 1001, 45, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,511,511,501,505,490,501,523,509,502],
[490,0,496,499,498,473,486,499,489,504],
[490,505,0,500,509,502,513,521,512,507],
[500,502,501,0,498,487,498,517,508,500],
[496,503,492,503,0,475,499,480,497,484],
[511,528,499,514,526,0,499,525,510,507],
[500,515,488,503,502,502,0,509,491,505],
[478,502,480,484,521,476,492,0,497,501],
[492,512,489,493,504,491,510,504,0,495],
[499,497,494,501,517,494,496,500,506,0]])



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
result = np.append(np.array([10, 1001, 46, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,466,481,516,466,474,448,509,483,471],
[535,0,489,496,519,532,476,537,481,519],
[520,512,0,475,483,517,477,517,512,477],
[485,505,526,0,522,555,481,550,526,504],
[535,482,518,479,0,531,449,537,516,482],
[527,469,484,446,470,0,438,516,483,478],
[553,525,524,520,552,563,0,580,509,499],
[492,464,484,451,464,485,421,0,444,448],
[518,520,489,475,485,518,492,557,0,498],
[530,482,524,497,519,523,502,553,503,0]])



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
result = np.append(np.array([10, 1001, 47, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,473,463,510,455,479,515,490,477,454],
[528,0,527,552,467,505,487,519,489,496],
[538,474,0,541,508,533,469,495,475,460],
[491,449,460,0,479,462,453,501,475,451],
[546,534,493,522,0,500,478,511,492,502],
[522,496,468,539,501,0,499,525,507,496],
[486,514,532,548,523,502,0,512,511,524],
[511,482,506,500,490,476,489,0,494,479],
[524,512,526,526,509,494,490,507,0,469],
[547,505,541,550,499,505,477,522,532,0]])



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
result = np.append(np.array([10, 1001, 48, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,514,480,514,464,486,501,512,484,513],
[487,0,475,495,494,493,481,497,501,517],
[521,526,0,523,526,524,508,495,498,509],
[487,506,478,0,506,503,514,509,475,516],
[537,507,475,495,0,494,509,520,499,528],
[515,508,477,498,507,0,522,516,493,536],
[500,520,493,487,492,479,0,503,499,535],
[489,504,506,492,481,485,498,0,468,503],
[517,500,503,526,502,508,502,533,0,531],
[488,484,492,485,473,465,466,498,470,0]])



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
result = np.append(np.array([10, 1001, 49, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,507,487,525,502,502,520,465,500,520],
[494,0,493,489,520,508,496,489,494,498],
[514,508,0,499,514,520,506,507,495,540],
[476,512,502,0,489,503,514,516,499,513],
[499,481,487,512,0,520,493,491,499,521],
[499,493,481,498,481,0,488,483,488,509],
[481,505,495,487,508,513,0,491,512,517],
[536,512,494,485,510,518,510,0,504,520],
[501,507,506,502,502,513,489,497,0,508],
[481,503,461,488,480,492,484,481,493,0]])



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
result = np.append(np.array([10, 1001, 50, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,495,497,429,450,495,463,490,495,509],
[506,0,506,484,483,507,485,529,516,546],
[504,495,0,465,478,450,473,474,491,491],
[572,517,536,0,480,524,512,542,492,530],
[551,518,523,521,0,531,480,495,512,569],
[506,494,551,477,470,0,482,531,493,497],
[538,516,528,489,521,519,0,514,487,563],
[511,472,527,459,506,470,487,0,481,471],
[506,485,510,509,489,508,514,520,0,542],
[492,455,510,471,432,504,438,530,459,0]])



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
result = np.append(np.array([10, 1001, 51, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,468,478,452,488,435,501,537,513,487],
[533,0,529,495,472,511,536,471,502,538],
[523,472,0,456,480,475,509,510,475,430],
[549,506,545,0,515,544,536,564,569,487],
[513,529,521,486,0,501,484,497,545,501],
[566,490,526,457,500,0,506,533,518,440],
[500,465,492,465,517,495,0,578,569,524],
[464,530,491,437,504,468,423,0,507,451],
[488,499,526,432,456,483,432,494,0,454],
[514,463,571,514,500,561,477,550,547,0]])



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
result = np.append(np.array([10, 1001, 52, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,495,503,467,533,498,486,491,472,489],
[506,0,509,503,559,532,469,495,481,519],
[498,492,0,502,531,543,489,452,487,510],
[534,498,499,0,516,560,502,515,491,532],
[468,442,470,485,0,510,448,449,425,460],
[503,469,458,441,491,0,442,453,435,448],
[515,532,512,499,553,559,0,501,516,531],
[510,506,549,486,552,548,500,0,526,524],
[529,520,514,510,576,566,485,475,0,524],
[512,482,491,469,541,553,470,477,477,0]])



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
result = np.append(np.array([10, 1001, 53, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,460,490,485,438,558,476,530,487,441],
[541,0,486,559,486,519,461,520,530,536],
[511,515,0,545,484,556,529,556,477,532],
[516,442,456,0,479,532,506,541,490,453],
[563,515,517,522,0,546,540,556,546,484],
[443,482,445,469,455,0,451,462,461,449],
[525,540,472,495,461,550,0,537,511,499],
[471,481,445,460,445,539,464,0,532,457],
[514,471,524,511,455,540,490,469,0,492],
[560,465,469,548,517,552,502,544,509,0]])



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
result = np.append(np.array([10, 1001, 54, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,480,476,498,511,502,463,510,563,487],
[521,0,514,496,523,546,497,541,562,517],
[525,487,0,555,530,537,511,565,557,512],
[503,505,446,0,497,526,492,541,526,494],
[490,478,471,504,0,529,500,493,517,443],
[499,455,464,475,472,0,461,504,526,496],
[538,504,490,509,501,540,0,545,526,499],
[491,460,436,460,508,497,456,0,520,511],
[438,439,444,475,484,475,475,481,0,466],
[514,484,489,507,558,505,502,490,535,0]])



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
result = np.append(np.array([10, 1001, 55, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,445,445,484,499,480,528,523,553,477],
[556,0,545,572,604,597,619,562,575,499],
[556,456,0,556,572,499,563,548,532,511],
[517,429,445,0,527,510,517,538,524,436],
[502,397,429,474,0,488,523,515,542,377],
[521,404,502,491,513,0,495,533,571,393],
[473,382,438,484,478,506,0,471,526,373],
[478,439,453,463,486,468,530,0,513,443],
[448,426,469,477,459,430,475,488,0,445],
[524,502,490,565,624,608,628,558,556,0]])



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
result = np.append(np.array([10, 1001, 56, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,513,443,518,468,488,479,447,489,535],
[488,0,515,525,455,497,481,499,504,544],
[558,486,0,518,534,520,576,509,579,576],
[483,476,483,0,464,546,503,452,559,546],
[533,546,467,537,0,557,497,586,528,520],
[513,504,481,455,444,0,481,484,488,553],
[522,520,425,498,504,520,0,481,558,501],
[554,502,492,549,415,517,520,0,509,541],
[512,497,422,442,473,513,443,492,0,481],
[466,457,425,455,481,448,500,460,520,0]])



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
result = np.append(np.array([10, 1001, 57, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,643,345,491,574,409,542,548,450,428],
[358,0,385,453,484,358,428,507,468,500],
[656,616,0,624,559,480,632,619,455,570],
[510,548,377,0,562,435,577,605,474,486],
[427,517,442,439,0,423,555,570,495,481],
[592,643,521,566,578,0,709,670,554,473],
[459,573,369,424,446,292,0,499,363,408],
[453,494,382,396,431,331,502,0,408,483],
[551,533,546,527,506,447,638,593,0,481],
[573,501,431,515,520,528,593,518,520,0]])



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
result = np.append(np.array([10, 1001, 58, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,484,450,476,447,505,525,454,498,463],
[517,0,498,481,487,529,587,451,515,517],
[551,503,0,529,495,529,595,550,568,547],
[525,520,472,0,491,500,526,463,527,487],
[554,514,506,510,0,540,585,544,506,473],
[496,472,472,501,461,0,555,419,504,450],
[476,414,406,475,416,446,0,441,456,397],
[547,550,451,538,457,582,560,0,535,500],
[503,486,433,474,495,497,545,466,0,502],
[538,484,454,514,528,551,604,501,499,0]])



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
result = np.append(np.array([10, 1001, 59, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,533,521,527,526,539,500,499,526,525],
[468,0,464,499,491,500,489,463,490,490],
[480,537,0,514,501,545,511,502,496,527],
[474,502,487,0,518,485,473,498,527,511],
[475,510,500,483,0,480,481,464,470,486],
[462,501,456,516,521,0,491,481,475,504],
[501,512,490,528,520,510,0,519,509,519],
[502,538,499,503,537,520,482,0,510,532],
[475,511,505,474,531,526,492,491,0,502],
[476,511,474,490,515,497,482,469,499,0]])



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
result = np.append(np.array([10, 1001, 60, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,554,476,522,510,539,484,492,520,527],
[447,0,431,467,479,499,462,456,428,463],
[525,570,0,541,555,560,496,553,533,524],
[479,534,460,0,490,474,469,471,457,475],
[491,522,446,511,0,512,486,470,516,533],
[462,502,441,527,489,0,436,493,465,498],
[517,539,505,532,515,565,0,516,494,514],
[509,545,448,530,531,508,485,0,493,510],
[481,573,468,544,485,536,507,508,0,498],
[474,538,477,526,468,503,487,491,503,0]])



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
result = np.append(np.array([10, 1001, 61, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,479,502,503,500,516,489,636,546,607],
[522,0,557,492,530,535,447,593,562,611],
[499,444,0,559,513,523,493,543,467,587],
[498,509,442,0,505,488,491,567,531,553],
[501,471,488,496,0,502,521,612,476,545],
[485,466,478,513,499,0,569,645,529,546],
[512,554,508,510,480,432,0,582,523,530],
[365,408,458,434,389,356,419,0,476,514],
[455,439,534,470,525,472,478,525,0,597],
[394,390,414,448,456,455,471,487,404,0]])



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
result = np.append(np.array([10, 1001, 62, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,525,557,498,496,531,484,466,512,534],
[476,0,545,537,496,532,481,517,543,544],
[444,456,0,498,481,507,459,439,446,498],
[503,464,503,0,485,546,440,471,488,537],
[505,505,520,516,0,553,438,524,528,532],
[470,469,494,455,448,0,422,440,477,495],
[517,520,542,561,563,579,0,519,481,536],
[535,484,562,530,477,561,482,0,515,492],
[489,458,555,513,473,524,520,486,0,518],
[467,457,503,464,469,506,465,509,483,0]])



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
result = np.append(np.array([10, 1001, 63, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,480,535,469,467,511,500,507,554,479],
[521,0,576,511,531,535,538,511,580,499],
[466,425,0,459,460,489,497,476,519,455],
[532,490,542,0,488,488,507,512,555,495],
[534,470,541,513,0,522,496,504,559,508],
[490,466,512,513,479,0,512,510,532,476],
[501,463,504,494,505,489,0,500,539,486],
[494,490,525,489,497,491,501,0,539,506],
[447,421,482,446,442,469,462,462,0,424],
[522,502,546,506,493,525,515,495,577,0]])



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
result = np.append(np.array([10, 1001, 64, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,485,533,512,528,509,494,494,484,505],
[516,0,541,512,536,515,504,522,521,486],
[468,460,0,448,476,475,473,485,445,448],
[489,489,553,0,500,506,499,498,475,485],
[473,465,525,501,0,527,474,496,492,475],
[492,486,526,495,474,0,500,480,477,486],
[507,497,528,502,527,501,0,497,483,495],
[507,479,516,503,505,521,504,0,485,502],
[517,480,556,526,509,524,518,516,0,495],
[496,515,553,516,526,515,506,499,506,0]])



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
result = np.append(np.array([10, 1001, 65, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,491,489,522,466,513,486,487,497,514],
[510,0,496,549,511,513,527,511,541,534],
[512,505,0,517,518,485,507,491,502,503],
[479,452,484,0,468,488,482,504,477,485],
[535,490,483,533,0,518,502,532,539,524],
[488,488,516,513,483,0,499,466,495,507],
[515,474,494,519,499,502,0,501,520,503],
[514,490,510,497,469,535,500,0,524,531],
[504,460,499,524,462,506,481,477,0,491],
[487,467,498,516,477,494,498,470,510,0]])



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
result = np.append(np.array([10, 1001, 66, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,498,503,500,496,507,529,492,506,495],
[503,0,503,521,515,499,511,519,502,506],
[498,498,0,518,539,522,535,526,513,531],
[501,480,483,0,519,478,523,508,502,524],
[505,486,462,482,0,497,515,513,492,492],
[494,502,479,523,504,0,528,514,522,510],
[472,490,466,478,486,473,0,479,482,489],
[509,482,475,493,488,487,522,0,505,519],
[495,499,488,499,509,479,519,496,0,505],
[506,495,470,477,509,491,512,482,496,0]])



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
result = np.append(np.array([10, 1001, 67, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,600,639,579,689,509,577,573,580,496],
[401,0,453,344,484,369,358,364,329,353],
[362,548,0,428,561,367,435,482,346,476],
[422,657,573,0,540,497,461,428,444,397],
[312,517,440,461,0,393,529,465,430,482],
[492,632,634,504,608,0,544,514,549,599],
[424,643,566,540,472,457,0,505,479,511],
[428,637,519,573,536,487,496,0,521,466],
[421,672,655,557,571,452,522,480,0,515],
[505,648,525,604,519,402,490,535,486,0]])



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
result = np.append(np.array([10, 1001, 68, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,490,465,453,464,485,490,463,502,507],
[511,0,499,502,460,492,485,496,494,514],
[536,502,0,490,485,512,514,494,501,525],
[548,499,511,0,510,512,508,534,509,533],
[537,541,516,491,0,515,526,530,489,532],
[516,509,489,489,486,0,502,518,499,544],
[511,516,487,493,475,499,0,535,493,552],
[538,505,507,467,471,483,466,0,480,518],
[499,507,500,492,512,502,508,521,0,526],
[494,487,476,468,469,457,449,483,475,0]])



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
result = np.append(np.array([10, 1001, 69, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,447,528,498,484,485,451,504,461,480],
[554,0,530,520,478,506,529,520,514,499],
[473,471,0,448,456,447,450,489,424,459],
[503,481,553,0,483,498,467,490,484,517],
[517,523,545,518,0,543,491,521,552,519],
[516,495,554,503,458,0,498,500,523,508],
[550,472,551,534,510,503,0,498,515,532],
[497,481,512,511,480,501,503,0,527,516],
[540,487,577,517,449,478,486,474,0,497],
[521,502,542,484,482,493,469,485,504,0]])



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
result = np.append(np.array([10, 1001, 70, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,512,485,471,480,483,531,459,458,460],
[489,0,500,499,506,487,545,496,502,503],
[516,501,0,513,524,505,504,498,539,497],
[530,502,488,0,504,506,534,519,514,488],
[521,495,477,497,0,526,536,511,496,489],
[518,514,496,495,475,0,538,466,515,481],
[470,456,497,467,465,463,0,513,486,451],
[542,505,503,482,490,535,488,0,477,494],
[543,499,462,487,505,486,515,524,0,442],
[541,498,504,513,512,520,550,507,559,0]])



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
result = np.append(np.array([10, 1001, 71, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,529,523,548,496,510,538,531,465,513],
[472,0,471,518,506,449,540,501,471,493],
[478,530,0,511,520,486,537,531,513,550],
[453,483,490,0,476,512,524,518,461,487],
[505,495,481,525,0,504,515,567,494,493],
[491,552,515,489,497,0,540,558,484,506],
[463,461,464,477,486,461,0,522,454,502],
[470,500,470,483,434,443,479,0,428,468],
[536,530,488,540,507,517,547,573,0,495],
[488,508,451,514,508,495,499,533,506,0]])



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
result = np.append(np.array([10, 1001, 72, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,505,492,497,543,500,526,507,518,513],
[496,0,478,483,508,477,491,494,509,497],
[509,523,0,508,535,495,517,522,522,522],
[504,518,493,0,537,525,520,533,521,495],
[458,493,466,464,0,474,507,465,488,471],
[501,524,506,476,527,0,517,501,524,516],
[475,510,484,481,494,484,0,474,499,487],
[494,507,479,468,536,500,527,0,501,501],
[483,492,479,480,513,477,502,500,0,507],
[488,504,479,506,530,485,514,500,494,0]])



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
result = np.append(np.array([10, 1001, 73, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,493,517,511,498,516,496,494,507,472],
[508,0,510,515,510,498,537,496,528,491],
[484,491,0,501,488,494,520,500,495,490],
[490,486,500,0,476,508,529,497,505,489],
[503,491,513,525,0,488,508,516,511,470],
[485,503,507,493,513,0,510,517,491,475],
[505,464,481,472,493,491,0,482,472,460],
[507,505,501,504,485,484,519,0,497,507],
[494,473,506,496,490,510,529,504,0,476],
[529,510,511,512,531,526,541,494,525,0]])



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
result = np.append(np.array([10, 1001, 74, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,482,482,474,488,523,507,482,487,474],
[519,0,502,482,486,507,503,505,497,508],
[519,499,0,504,516,510,500,495,509,512],
[527,519,497,0,501,518,523,496,531,516],
[513,515,485,500,0,526,513,490,516,504],
[478,494,491,483,475,0,479,479,496,479],
[494,498,501,478,488,522,0,492,512,488],
[519,496,506,505,511,522,509,0,524,538],
[514,504,492,470,485,505,489,477,0,497],
[527,493,489,485,497,522,513,463,504,0]])



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
result = np.append(np.array([10, 1001, 75, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,530,476,539,564,501,546,504,528,549],
[471,0,490,528,529,483,540,507,523,550],
[525,511,0,528,543,496,543,529,550,540],
[462,473,473,0,490,473,508,485,490,510],
[437,472,458,511,0,503,492,455,477,538],
[500,518,505,528,498,0,529,518,534,562],
[455,461,458,493,509,472,0,498,489,493],
[497,494,472,516,546,483,503,0,509,551],
[473,478,451,511,524,467,512,492,0,520],
[452,451,461,491,463,439,508,450,481,0]])



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
result = np.append(np.array([10, 1001, 76, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,560,452,494,485,475,459,522,522,538],
[441,0,476,499,488,471,456,492,439,506],
[549,525,0,612,588,555,521,504,500,543],
[507,502,389,0,488,498,468,531,486,528],
[516,513,413,513,0,524,488,620,462,526],
[526,530,446,503,477,0,520,505,486,583],
[542,545,480,533,513,481,0,534,477,546],
[479,509,497,470,381,496,467,0,441,537],
[479,562,501,515,539,515,524,560,0,565],
[463,495,458,473,475,418,455,464,436,0]])



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
result = np.append(np.array([10, 1001, 77, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,384,524,555,475,515,428,682,401,774],
[617,0,449,573,569,620,585,791,559,826],
[477,552,0,385,533,522,380,567,367,513],
[446,428,616,0,553,341,594,479,380,602],
[526,432,468,448,0,556,387,756,393,565],
[486,381,479,660,445,0,413,642,441,539],
[573,416,621,407,614,588,0,627,291,637],
[319,210,434,522,245,359,374,0,421,592],
[600,442,634,621,608,560,710,580,0,779],
[227,175,488,399,436,462,364,409,222,0]])



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
result = np.append(np.array([10, 1001, 78, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,489,485,531,496,506,483,494,526,474],
[512,0,467,504,472,456,474,451,479,423],
[516,534,0,526,515,462,528,523,525,496],
[470,497,475,0,471,451,444,475,503,443],
[505,529,486,530,0,457,475,463,507,468],
[495,545,539,550,544,0,511,535,531,543],
[518,527,473,557,526,490,0,498,557,488],
[507,550,478,526,538,466,503,0,526,446],
[475,522,476,498,494,470,444,475,0,481],
[527,578,505,558,533,458,513,555,520,0]])



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
result = np.append(np.array([10, 1001, 79, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,516,527,508,516,521,499,491,503,489],
[485,0,509,479,494,501,478,491,505,473],
[474,492,0,496,493,526,484,476,488,482],
[493,522,505,0,495,487,505,488,516,476],
[485,507,508,506,0,493,502,475,489,473],
[480,500,475,514,508,0,497,477,483,481],
[502,523,517,496,499,504,0,520,504,510],
[510,510,525,513,526,524,481,0,517,487],
[498,496,513,485,512,518,497,484,0,472],
[512,528,519,525,528,520,491,514,529,0]])



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
result = np.append(np.array([10, 1001, 80, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,472,492,478,489,524,541,482,527,504],
[529,0,510,514,495,533,550,468,545,482],
[509,491,0,489,480,512,529,465,521,511],
[523,487,512,0,520,524,547,487,537,503],
[512,506,521,481,0,518,548,512,541,498],
[477,468,489,477,483,0,512,461,498,481],
[460,451,472,454,453,489,0,461,497,464],
[519,533,536,514,489,540,540,0,531,513],
[474,456,480,464,460,503,504,470,0,465],
[497,519,490,498,503,520,537,488,536,0]])



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
result = np.append(np.array([10, 1001, 81, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,481,467,521,551,462,478,548,509,533],
[520,0,526,563,544,511,505,584,514,462],
[534,475,0,543,484,514,441,506,550,495],
[480,438,458,0,470,491,477,513,542,490],
[450,457,517,531,0,573,510,573,542,496],
[539,490,487,510,428,0,498,487,506,471],
[523,496,560,524,491,503,0,550,554,542],
[453,417,495,488,428,514,451,0,507,450],
[492,487,451,459,459,495,447,494,0,511],
[468,539,506,511,505,530,459,551,490,0]])



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
result = np.append(np.array([10, 1001, 82, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,538,532,518,516,519,515,530,517,487],
[463,0,485,483,499,519,471,500,484,464],
[469,516,0,506,510,509,478,496,507,466],
[483,518,495,0,501,513,510,485,447,502],
[485,502,491,500,0,537,503,515,474,492],
[482,482,492,488,464,0,526,492,491,474],
[486,530,523,491,498,475,0,528,517,510],
[471,501,505,516,486,509,473,0,493,483],
[484,517,494,554,527,510,484,508,0,507],
[514,537,535,499,509,527,491,518,494,0]])



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
result = np.append(np.array([10, 1001, 83, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,494,505,503,502,510,510,506,498,512],
[507,0,525,498,512,532,521,509,529,515],
[496,476,0,501,512,530,509,506,515,517],
[498,503,500,0,507,527,514,510,524,499],
[499,489,489,494,0,525,508,500,511,498],
[491,469,471,474,476,0,474,505,457,490],
[491,480,492,487,493,527,0,515,478,508],
[495,492,495,491,501,496,486,0,502,487],
[503,472,486,477,490,544,523,499,0,499],
[489,486,484,502,503,511,493,514,502,0]])



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
result = np.append(np.array([10, 1001, 84, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,488,453,467,460,480,470,503,501,509],
[513,0,518,465,538,460,517,535,504,498],
[548,483,0,520,510,504,522,525,517,540],
[534,536,481,0,544,497,501,529,518,471],
[541,463,491,457,0,486,478,484,482,502],
[521,541,497,504,515,0,556,514,527,479],
[531,484,479,500,523,445,0,506,504,484],
[498,466,476,472,517,487,495,0,504,463],
[500,497,484,483,519,474,497,497,0,483],
[492,503,461,530,499,522,517,538,518,0]])



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
result = np.append(np.array([10, 1001, 85, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,450,428,464,444,453,444,451,475,468],
[551,0,473,517,483,518,513,532,536,543],
[573,528,0,505,518,493,503,539,521,529],
[537,484,496,0,493,464,474,476,479,515],
[557,518,483,508,0,522,492,523,506,544],
[548,483,508,537,479,0,523,509,467,473],
[557,488,498,527,509,478,0,516,483,496],
[550,469,462,525,478,492,485,0,483,506],
[526,465,480,522,495,534,518,518,0,489],
[533,458,472,486,457,528,505,495,512,0]])



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
result = np.append(np.array([10, 1001, 86, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,531,495,502,507,512,509,505,523,536],
[470,0,479,490,467,503,483,493,492,485],
[506,522,0,526,472,520,470,501,519,515],
[499,511,475,0,483,514,480,491,541,492],
[494,534,529,518,0,505,514,494,524,503],
[489,498,481,487,496,0,469,493,515,483],
[492,518,531,521,487,532,0,523,547,521],
[496,508,500,510,507,508,478,0,529,489],
[478,509,482,460,477,486,454,472,0,492],
[465,516,486,509,498,518,480,512,509,0]])



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
result = np.append(np.array([10, 1001, 87, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,485,498,475,473,502,471,511,497,493],
[516,0,501,503,473,513,522,494,507,483],
[503,500,0,490,442,506,475,472,500,468],
[526,498,511,0,505,519,491,502,516,507],
[528,528,559,496,0,556,513,524,510,498],
[499,488,495,482,445,0,486,478,510,471],
[530,479,526,510,488,515,0,475,507,484],
[490,507,529,499,477,523,526,0,497,451],
[504,494,501,485,491,491,494,504,0,467],
[508,518,533,494,503,530,517,550,534,0]])



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
result = np.append(np.array([10, 1001, 88, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,437,469,397,431,453,477,428,433,427],
[564,0,487,507,488,476,530,483,516,497],
[532,514,0,484,459,505,533,495,498,487],
[604,494,517,0,502,497,538,495,559,512],
[570,513,542,499,0,487,535,480,515,491],
[548,525,496,504,514,0,525,492,523,510],
[524,471,468,463,466,476,0,472,453,440],
[573,518,506,506,521,509,529,0,490,506],
[568,485,503,442,486,478,548,511,0,511],
[574,504,514,489,510,491,561,495,490,0]])



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
result = np.append(np.array([10, 1001, 89, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,504,529,470,513,500,492,445,479,492],
[497,0,467,464,482,451,489,449,489,500],
[472,534,0,460,508,490,483,469,486,483],
[531,537,541,0,502,490,529,477,528,478],
[488,519,493,499,0,477,520,453,473,488],
[501,550,511,511,524,0,511,511,483,506],
[509,512,518,472,481,490,0,500,489,495],
[556,552,532,524,548,490,501,0,547,554],
[522,512,515,473,528,518,512,454,0,510],
[509,501,518,523,513,495,506,447,491,0]])



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
result = np.append(np.array([10, 1001, 90, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,491,489,502,477,498,479,510,504,494],
[510,0,515,485,497,524,507,503,514,523],
[512,486,0,494,499,495,480,494,504,460],
[499,516,507,0,514,506,504,507,504,507],
[524,504,502,487,0,486,480,516,504,490],
[503,477,506,495,515,0,486,486,513,487],
[522,494,521,497,521,515,0,501,495,494],
[491,498,507,494,485,515,500,0,501,455],
[497,487,497,497,497,488,506,500,0,486],
[507,478,541,494,511,514,507,546,515,0]])



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
result = np.append(np.array([10, 1001, 91, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,517,501,490,502,507,494,491,484,488],
[484,0,470,482,461,492,481,462,468,464],
[500,531,0,495,524,520,510,487,475,498],
[511,519,506,0,494,516,504,483,482,490],
[499,540,477,507,0,513,497,506,518,488],
[494,509,481,485,488,0,488,482,466,474],
[507,520,491,497,504,513,0,505,491,493],
[510,539,514,518,495,519,496,0,489,516],
[517,533,526,519,483,535,510,512,0,514],
[513,537,503,511,513,527,508,485,487,0]])



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
result = np.append(np.array([10, 1001, 92, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,470,506,486,524,509,519,456,535,430],
[531,0,581,455,487,595,543,523,571,477],
[495,420,0,493,454,470,552,480,465,442],
[515,546,508,0,475,559,560,505,551,493],
[477,514,547,526,0,594,521,499,607,490],
[492,406,531,442,407,0,494,403,470,525],
[482,458,449,441,480,507,0,451,561,443],
[545,478,521,496,502,598,550,0,609,474],
[466,430,536,450,394,531,440,392,0,417],
[571,524,559,508,511,476,558,527,584,0]])



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
result = np.append(np.array([10, 1001, 93, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,506,536,527,532,508,533,499,486,579],
[495,0,505,515,531,497,533,525,482,571],
[465,496,0,493,504,492,530,428,462,529],
[474,486,508,0,483,493,533,486,481,523],
[469,470,497,518,0,493,561,502,500,534],
[493,504,509,508,508,0,532,522,505,536],
[468,468,471,468,440,469,0,457,457,506],
[502,476,573,515,499,479,544,0,516,531],
[515,519,539,520,501,496,544,485,0,582],
[422,430,472,478,467,465,495,470,419,0]])



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
result = np.append(np.array([10, 1001, 94, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,479,484,478,494,482,484,484,476,482],
[522,0,482,490,521,508,484,534,509,522],
[517,519,0,502,504,491,509,519,488,523],
[523,511,499,0,531,507,510,528,494,520],
[507,480,497,470,0,492,489,520,478,501],
[519,493,510,494,509,0,520,510,485,508],
[517,517,492,491,512,481,0,517,488,501],
[517,467,482,473,481,491,484,0,459,477],
[525,492,513,507,523,516,513,542,0,520],
[519,479,478,481,500,493,500,524,481,0]])



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
result = np.append(np.array([10, 1001, 95, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,491,542,523,488,498,464,487,486,462],
[510,0,503,490,517,498,465,505,471,473],
[459,498,0,523,472,493,474,466,478,472],
[478,511,478,0,474,483,488,492,506,507],
[513,484,529,527,0,517,501,523,508,485],
[503,503,508,518,484,0,479,514,491,507],
[537,536,527,513,500,522,0,539,498,492],
[514,496,535,509,478,487,462,0,491,491],
[515,530,523,495,493,510,503,510,0,480],
[539,528,529,494,516,494,509,510,521,0]])



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
result = np.append(np.array([10, 1001, 96, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,506,485,481,494,496,495,484,475,519],
[495,0,497,473,488,483,499,494,496,515],
[516,504,0,511,475,500,513,513,503,510],
[520,528,490,0,508,508,533,504,514,524],
[507,513,526,493,0,501,530,523,514,525],
[505,518,501,493,500,0,506,515,493,510],
[506,502,488,468,471,495,0,489,474,507],
[517,507,488,497,478,486,512,0,487,500],
[526,505,498,487,487,508,527,514,0,530],
[482,486,491,477,476,491,494,501,471,0]])



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
result = np.append(np.array([10, 1001, 97, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,500,497,504,494,523,507,515,496,461],
[501,0,477,515,485,487,507,497,492,481],
[504,524,0,517,538,516,536,542,526,494],
[497,486,484,0,486,511,515,532,489,474],
[507,516,463,515,0,510,515,537,504,514],
[478,514,485,490,491,0,517,495,517,497],
[494,494,465,486,486,484,0,488,480,474],
[486,504,459,469,464,506,513,0,489,477],
[505,509,475,512,497,484,521,512,0,503],
[540,520,507,527,487,504,527,524,498,0]])



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
result = np.append(np.array([10, 1001, 98, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,570,513,509,526,485,525,504,501,495],
[431,0,458,445,472,439,449,525,472,443],
[488,543,0,489,517,488,505,554,517,490],
[492,556,512,0,520,517,521,534,519,512],
[475,529,484,481,0,492,480,539,489,478],
[516,562,513,484,509,0,487,525,505,468],
[476,552,496,480,521,514,0,528,512,501],
[497,476,447,467,462,476,473,0,469,449],
[500,529,484,482,512,496,489,532,0,501],
[506,558,511,489,523,533,500,552,500,0]])



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
result = np.append(np.array([10, 1001, 99, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,546,519,545,535,499,529,526,543,526],
[455,0,473,512,516,485,470,471,486,488],
[482,528,0,514,492,496,526,477,499,500],
[456,489,487,0,491,506,497,474,493,495],
[466,485,509,510,0,495,497,476,512,489],
[502,516,505,495,506,0,486,491,497,512],
[472,531,475,504,504,515,0,482,490,464],
[475,530,524,527,525,510,519,0,541,501],
[458,515,502,508,489,504,511,460,0,473],
[475,513,501,506,512,489,537,500,528,0]])



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
result = np.append(np.array([10, 1001, 100, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,506,498,488,503,479,485,472,507,498],
[495,0,528,498,514,489,519,492,532,520],
[503,473,0,482,494,489,504,472,491,467],
[513,503,519,0,502,503,515,501,538,475],
[498,487,507,499,0,509,494,494,479,496],
[522,512,512,498,492,0,506,461,509,470],
[516,482,497,486,507,495,0,492,498,504],
[529,509,529,500,507,540,509,0,547,506],
[494,469,510,463,522,492,503,454,0,496],
[503,481,534,526,505,531,497,495,505,0]])



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
result = np.append(np.array([10, 1001, 101, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,482,524,491,510,521,523,512,531,536],
[519,0,506,487,505,499,506,524,505,531],
[477,495,0,503,496,501,505,510,509,520],
[510,514,498,0,507,496,502,500,515,513],
[491,496,505,494,0,496,508,511,505,537],
[480,502,500,505,505,0,529,505,524,510],
[478,495,496,499,493,472,0,492,505,529],
[489,477,491,501,490,496,509,0,489,515],
[470,496,492,486,496,477,496,512,0,498],
[465,470,481,488,464,491,472,486,503,0]])



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
result = np.append(np.array([10, 1001, 102, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,405,497,464,497,469,443,434,421,525],
[596,0,519,558,534,516,488,490,433,596],
[504,482,0,569,458,504,494,548,531,625],
[537,443,432,0,479,468,446,383,479,537],
[504,467,543,522,0,531,541,444,435,541],
[532,485,497,533,470,0,464,499,455,541],
[558,513,507,555,460,537,0,425,403,482],
[567,511,453,618,557,502,576,0,481,579],
[580,568,470,522,566,546,598,520,0,571],
[476,405,376,464,460,460,519,422,430,0]])



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
result = np.append(np.array([10, 1001, 103, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,510,514,519,493,513,522,494,512,515],
[491,0,520,515,501,535,523,485,523,512],
[487,481,0,463,480,475,487,480,488,483],
[482,486,538,0,496,508,483,476,505,525],
[508,500,521,505,0,528,494,511,523,527],
[488,466,526,493,473,0,462,451,513,490],
[479,478,514,518,507,539,0,493,508,516],
[507,516,521,525,490,550,508,0,501,554],
[489,478,513,496,478,488,493,500,0,512],
[486,489,518,476,474,511,485,447,489,0]])



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
result = np.append(np.array([10, 1001, 104, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,484,429,445,445,445,499,427,468,441],
[517,0,471,473,466,455,495,454,501,443],
[572,530,0,499,469,471,522,493,525,521],
[556,528,502,0,482,493,532,488,531,505],
[556,535,532,519,0,510,545,513,531,494],
[556,546,530,508,491,0,525,501,530,491],
[502,506,479,469,456,476,0,451,498,431],
[574,547,508,513,488,500,550,0,537,510],
[533,500,476,470,470,471,503,464,0,451],
[560,558,480,496,507,510,570,491,550,0]])



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
result = np.append(np.array([10, 1001, 105, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,503,505,505,488,504,473,494,474,475],
[498,0,514,483,495,494,481,502,493,483],
[496,487,0,489,504,478,477,489,477,474],
[496,518,512,0,505,520,492,500,496,502],
[513,506,497,496,0,513,477,519,489,490],
[497,507,523,481,488,0,486,507,482,464],
[528,520,524,509,524,515,0,507,504,494],
[507,499,512,501,482,494,494,0,499,488],
[527,508,524,505,512,519,497,502,0,504],
[526,518,527,499,511,537,507,513,497,0]])



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
result = np.append(np.array([10, 1001, 106, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,420,502,454,430,398,519,454,437,518],
[581,0,551,526,518,496,573,499,530,523],
[499,450,0,441,344,511,504,435,513,466],
[547,475,560,0,491,486,550,545,528,515],
[571,483,657,510,0,518,544,492,524,592],
[603,505,490,515,483,0,584,536,557,538],
[482,428,497,451,457,417,0,446,495,475],
[547,502,566,456,509,465,555,0,520,491],
[564,471,488,473,477,444,506,481,0,470],
[483,478,535,486,409,463,526,510,531,0]])



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
result = np.append(np.array([10, 1001, 107, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,473,495,480,506,502,499,457,477,518],
[528,0,535,526,525,504,525,524,481,539],
[506,466,0,508,481,462,515,483,469,499],
[521,475,493,0,488,461,489,465,449,523],
[495,476,520,513,0,470,491,441,466,504],
[499,497,539,540,531,0,494,460,506,547],
[502,476,486,512,510,507,0,503,465,523],
[544,477,518,536,560,541,498,0,510,551],
[524,520,532,552,535,495,536,491,0,535],
[483,462,502,478,497,454,478,450,466,0]])



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
result = np.append(np.array([10, 1001, 108, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,491,483,511,486,480,485,510,499,481],
[510,0,525,519,493,494,500,513,517,513],
[518,476,0,512,489,495,486,510,496,516],
[490,482,489,0,478,467,488,508,494,486],
[515,508,512,523,0,502,519,510,527,497],
[521,507,506,534,499,0,511,524,527,525],
[516,501,515,513,482,490,0,496,519,504],
[491,488,491,493,491,477,505,0,504,496],
[502,484,505,507,474,474,482,497,0,499],
[520,488,485,515,504,476,497,505,502,0]])



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
result = np.append(np.array([10, 1001, 109, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,504,498,491,506,564,499,525,499,455],
[497,0,481,519,503,478,485,497,526,506],
[503,520,0,525,542,535,523,540,492,475],
[510,482,476,0,495,498,492,498,522,468],
[495,498,459,506,0,497,493,504,482,402],
[437,523,466,503,504,0,480,510,467,434],
[502,516,478,509,508,521,0,513,523,495],
[476,504,461,503,497,491,488,0,497,445],
[502,475,509,479,519,534,478,504,0,445],
[546,495,526,533,599,567,506,556,556,0]])



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
result = np.append(np.array([10, 1001, 110, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,507,506,509,500,524,496,515,494,524],
[494,0,541,505,526,528,519,503,503,499],
[495,460,0,486,494,514,500,519,482,529],
[492,496,515,0,521,511,502,505,490,504],
[501,475,507,480,0,514,508,501,509,513],
[477,473,487,490,487,0,471,492,482,475],
[505,482,501,499,493,530,0,508,506,505],
[486,498,482,496,500,509,493,0,482,500],
[507,498,519,511,492,519,495,519,0,502],
[477,502,472,497,488,526,496,501,499,0]])



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
result = np.append(np.array([10, 1001, 111, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,506,488,510,520,477,519,518,496,509],
[495,0,480,498,498,505,524,516,501,477],
[513,521,0,508,518,489,558,526,515,483],
[491,503,493,0,524,480,524,507,487,496],
[481,503,483,477,0,481,540,498,515,492],
[524,496,512,521,520,0,533,533,518,492],
[482,477,443,477,461,468,0,483,486,465],
[483,485,475,494,503,468,518,0,482,492],
[505,500,486,514,486,483,515,519,0,497],
[492,524,518,505,509,509,536,509,504,0]])



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
result = np.append(np.array([10, 1001, 112, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,493,477,484,514,499,501,516,531,521],
[508,0,492,507,523,504,530,526,509,523],
[524,509,0,472,527,514,519,537,518,503],
[517,494,529,0,512,518,516,529,534,535],
[487,478,474,489,0,492,479,522,516,507],
[502,497,487,483,509,0,491,522,509,506],
[500,471,482,485,522,510,0,511,496,504],
[485,475,464,472,479,479,490,0,497,497],
[470,492,483,467,485,492,505,504,0,496],
[480,478,498,466,494,495,497,504,505,0]])



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
result = np.append(np.array([10, 1001, 113, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,489,494,471,445,547,567,451,505,503],
[512,0,474,535,453,645,551,500,521,527],
[507,527,0,510,534,582,500,466,492,505],
[530,466,491,0,474,614,545,517,534,499],
[556,548,467,527,0,610,582,545,561,564],
[454,356,419,387,391,0,442,421,435,426],
[434,450,501,456,419,559,0,475,504,433],
[550,501,535,484,456,580,526,0,463,510],
[496,480,509,467,440,566,497,538,0,503],
[498,474,496,502,437,575,568,491,498,0]])



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
result = np.append(np.array([10, 1001, 114, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,481,500,470,532,489,492,471,500,445],
[520,0,481,476,520,512,473,499,513,510],
[501,520,0,512,510,493,492,476,524,521],
[531,525,489,0,543,474,492,454,507,493],
[469,481,491,458,0,465,493,436,481,435],
[512,489,508,527,536,0,504,473,545,482],
[509,528,509,509,508,497,0,515,514,510],
[530,502,525,547,565,528,486,0,520,510],
[501,488,477,494,520,456,487,481,0,508],
[556,491,480,508,566,519,491,491,493,0]])



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
result = np.append(np.array([10, 1001, 115, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,520,547,481,497,464,528,446,485,474],
[481,0,532,524,550,445,558,506,494,523],
[454,469,0,494,493,451,546,487,508,489],
[520,477,507,0,530,505,492,462,499,476],
[504,451,508,471,0,474,534,489,461,471],
[537,556,550,496,527,0,562,501,550,518],
[473,443,455,509,467,439,0,464,472,489],
[555,495,514,539,512,500,537,0,505,521],
[516,507,493,502,540,451,529,496,0,511],
[527,478,512,525,530,483,512,480,490,0]])



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
result = np.append(np.array([10, 1001, 116, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,486,474,509,500,516,501,501,492,527],
[515,0,503,500,497,497,512,502,514,498],
[527,498,0,514,516,492,525,514,494,547],
[492,501,487,0,499,505,515,493,510,540],
[501,504,485,502,0,499,496,496,507,544],
[485,504,509,496,502,0,505,493,501,524],
[500,489,476,486,505,496,0,485,517,509],
[500,499,487,508,505,508,516,0,489,526],
[509,487,507,491,494,500,484,512,0,520],
[474,503,454,461,457,477,492,475,481,0]])



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
result = np.append(np.array([10, 1001, 117, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,477,499,509,522,516,520,524,502,530],
[524,0,503,523,540,521,499,538,528,509],
[502,498,0,524,525,510,490,529,511,506],
[492,478,477,0,505,500,487,502,469,491],
[479,461,476,496,0,484,483,493,483,468],
[485,480,491,501,517,0,477,511,493,491],
[481,502,511,514,518,524,0,537,507,502],
[477,463,472,499,508,490,464,0,489,483],
[499,473,490,532,518,508,494,512,0,496],
[471,492,495,510,533,510,499,518,505,0]])



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
result = np.append(np.array([10, 1001, 118, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,490,477,441,460,482,512,429,468,418],
[511,0,488,455,386,512,502,468,468,430],
[524,513,0,414,419,483,456,428,478,413],
[560,546,587,0,447,596,497,470,486,522],
[541,615,582,554,0,562,535,467,521,510],
[519,489,518,405,439,0,518,399,440,447],
[489,499,545,504,466,483,0,519,475,494],
[572,533,573,531,534,602,482,0,485,501],
[533,533,523,515,480,561,526,516,0,457],
[583,571,588,479,491,554,507,500,544,0]])



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
result = np.append(np.array([10, 1001, 119, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,486,502,463,502,512,553,505,483,470],
[515,0,511,525,486,521,537,543,512,510],
[499,490,0,442,500,472,482,475,448,451],
[538,476,559,0,537,545,531,508,499,498],
[499,515,501,464,0,490,500,508,441,476],
[489,480,529,456,511,0,520,512,478,486],
[448,464,519,470,501,481,0,526,452,453],
[496,458,526,493,493,489,475,0,454,492],
[518,489,553,502,560,523,549,547,0,492],
[531,491,550,503,525,515,548,509,509,0]])



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
result = np.append(np.array([10, 1001, 120, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,529,480,464,517,514,481,490,489,472],
[472,0,476,457,473,495,426,462,470,444],
[521,525,0,508,496,498,497,507,534,490],
[537,544,493,0,506,519,527,507,520,489],
[484,528,505,495,0,514,546,478,493,509],
[487,506,503,482,487,0,447,481,456,464],
[520,575,504,474,455,554,0,521,504,515],
[511,539,494,494,523,520,480,0,486,510],
[512,531,467,481,508,545,497,515,0,491],
[529,557,511,512,492,537,486,491,510,0]])



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
result = np.append(np.array([10, 1001, 121, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,506,478,466,497,509,441,498,457,491],
[495,0,478,492,501,495,518,484,477,498],
[523,523,0,477,507,526,507,503,513,517],
[535,509,524,0,508,520,507,493,517,506],
[504,500,494,493,0,502,520,497,489,513],
[492,506,475,481,499,0,509,504,483,499],
[560,483,494,494,481,492,0,503,524,510],
[503,517,498,508,504,497,498,0,446,547],
[544,524,488,484,512,518,477,555,0,531],
[510,503,484,495,488,502,491,454,470,0]])



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
result = np.append(np.array([10, 1001, 122, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,514,486,497,515,474,510,474,522,521],
[487,0,496,496,500,500,505,496,515,497],
[515,505,0,486,484,494,493,468,490,514],
[504,505,515,0,512,509,502,500,485,504],
[486,501,517,489,0,496,488,497,510,523],
[527,501,507,492,505,0,503,484,513,532],
[491,496,508,499,513,498,0,510,509,502],
[527,505,533,501,504,517,491,0,511,521],
[479,486,511,516,491,488,492,490,0,499],
[480,504,487,497,478,469,499,480,502,0]])



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
result = np.append(np.array([10, 1001, 123, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,481,497,524,483,518,499,469,487,505],
[520,0,513,534,514,519,523,496,496,509],
[504,488,0,526,495,532,494,504,491,519],
[477,467,475,0,479,495,473,467,469,501],
[518,487,506,522,0,526,498,500,491,505],
[483,482,469,506,475,0,490,476,470,495],
[502,478,507,528,503,511,0,504,501,508],
[532,505,497,534,501,525,497,0,484,515],
[514,505,510,532,510,531,500,517,0,512],
[496,492,482,500,496,506,493,486,489,0]])



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
result = np.append(np.array([10, 1001, 124, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,498,484,554,484,519,510,495,495,457],
[503,0,483,543,513,513,534,471,506,501],
[517,518,0,564,495,526,525,515,480,508],
[447,458,437,0,456,468,475,410,423,441],
[517,488,506,545,0,468,543,504,496,472],
[482,488,475,533,533,0,518,477,486,450],
[491,467,476,526,458,483,0,468,464,467],
[506,530,486,591,497,524,533,0,469,470],
[506,495,521,578,505,515,537,532,0,474],
[544,500,493,560,529,551,534,531,527,0]])



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
result = np.append(np.array([10, 1001, 125, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,496,467,487,481,484,490,521,480,493],
[505,0,466,481,507,487,470,512,481,506],
[534,535,0,504,510,523,505,522,517,500],
[514,520,497,0,501,513,504,495,510,520],
[520,494,491,500,0,525,508,508,519,505],
[517,514,478,488,476,0,515,546,501,502],
[511,531,496,497,493,486,0,529,509,489],
[480,489,479,506,493,455,472,0,467,472],
[521,520,484,491,482,500,492,534,0,506],
[508,495,501,481,496,499,512,529,495,0]])



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
result = np.append(np.array([10, 1001, 126, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,541,541,504,512,434,559,461,486,458],
[460,0,397,449,419,415,485,396,423,443],
[460,604,0,557,576,474,494,523,531,530],
[497,552,444,0,470,472,519,538,407,406],
[489,582,425,531,0,472,525,496,510,526],
[567,586,527,529,529,0,580,563,522,470],
[442,516,507,482,476,421,0,462,477,512],
[540,605,478,463,505,438,539,0,450,521],
[515,578,470,594,491,479,524,551,0,484],
[543,558,471,595,475,531,489,480,517,0]])



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
result = np.append(np.array([10, 1001, 127, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,528,527,498,515,519,501,554,532,487],
[473,0,481,456,526,491,478,526,485,474],
[474,520,0,482,509,464,506,493,499,501],
[503,545,519,0,539,495,505,534,535,515],
[486,475,492,462,0,487,501,510,511,486],
[482,510,537,506,514,0,489,518,508,475],
[500,523,495,496,500,512,0,547,502,509],
[447,475,508,467,491,483,454,0,496,463],
[469,516,502,466,490,493,499,505,0,477],
[514,527,500,486,515,526,492,538,524,0]])



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
result = np.append(np.array([10, 1001, 128, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,520,519,504,501,500,494,529,541,511],
[481,0,514,505,477,459,517,542,502,495],
[482,487,0,495,462,485,472,506,504,533],
[497,496,506,0,469,496,473,567,522,507],
[500,524,539,532,0,524,517,563,524,498],
[501,542,516,505,477,0,497,557,524,517],
[507,484,529,528,484,504,0,563,531,522],
[472,459,495,434,438,444,438,0,473,479],
[460,499,497,479,477,477,470,528,0,504],
[490,506,468,494,503,484,479,522,497,0]])



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
result = np.append(np.array([10, 1001, 129, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,488,511,517,495,504,507,494,521,507],
[513,0,519,513,497,504,486,513,520,514],
[490,482,0,477,501,509,480,527,531,461],
[484,488,524,0,483,495,448,452,524,486],
[506,504,500,518,0,531,492,519,526,496],
[497,497,492,506,470,0,477,493,523,524],
[494,515,521,553,509,524,0,517,551,506],
[507,488,474,549,482,508,484,0,523,489],
[480,481,470,477,475,478,450,478,0,456],
[494,487,540,515,505,477,495,512,545,0]])



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
result = np.append(np.array([10, 1001, 130, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,529,500,491,472,517,527,510,532,516],
[472,0,464,476,472,504,492,494,486,464],
[501,537,0,491,474,510,527,513,514,517],
[510,525,510,0,509,520,530,524,499,530],
[529,529,527,492,0,537,568,535,528,514],
[484,497,491,481,464,0,501,492,499,470],
[474,509,474,471,433,500,0,476,454,474],
[491,507,488,477,466,509,525,0,500,506],
[469,515,487,502,473,502,547,501,0,502],
[485,537,484,471,487,531,527,495,499,0]])



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
result = np.append(np.array([10, 1001, 131, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,499,512,498,492,495,483,502,501,498],
[502,0,516,516,527,521,510,484,523,512],
[489,485,0,510,480,512,465,526,530,498],
[503,485,491,0,497,507,473,478,517,522],
[509,474,521,504,0,514,471,460,518,503],
[506,480,489,494,487,0,484,460,511,508],
[518,491,536,528,530,517,0,514,529,528],
[499,517,475,523,541,541,487,0,536,523],
[500,478,471,484,483,490,472,465,0,487],
[503,489,503,479,498,493,473,478,514,0]])



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
result = np.append(np.array([10, 1001, 132, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,477,488,475,495,491,484,499,482,488],
[524,0,494,508,493,500,526,514,502,495],
[513,507,0,508,523,488,505,515,509,505],
[526,493,493,0,486,496,502,530,513,495],
[506,508,478,515,0,496,487,513,499,509],
[510,501,513,505,505,0,499,519,518,502],
[517,475,496,499,514,502,0,519,507,494],
[502,487,486,471,488,482,482,0,478,496],
[519,499,492,488,502,483,494,523,0,490],
[513,506,496,506,492,499,507,505,511,0]])



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
result = np.append(np.array([10, 1001, 133, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,484,479,459,498,470,484,522,491,476],
[517,0,468,503,499,490,492,511,474,498],
[522,533,0,487,513,509,519,519,494,490],
[542,498,514,0,513,513,532,533,515,515],
[503,502,488,488,0,504,504,506,486,507],
[531,511,492,488,497,0,490,506,474,518],
[517,509,482,469,497,511,0,514,506,510],
[479,490,482,468,495,495,487,0,467,489],
[510,527,507,486,515,527,495,534,0,533],
[525,503,511,486,494,483,491,512,468,0]])



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
result = np.append(np.array([10, 1001, 134, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,534,543,501,509,491,530,522,530,485],
[467,0,509,506,514,514,477,510,511,495],
[458,492,0,481,448,524,423,536,467,511],
[500,495,520,0,496,455,421,503,499,469],
[492,487,553,505,0,532,492,571,539,483],
[510,487,477,546,469,0,525,608,538,473],
[471,524,578,580,509,476,0,506,548,480],
[479,491,465,498,430,393,495,0,439,439],
[471,490,534,502,462,463,453,562,0,515],
[516,506,490,532,518,528,521,562,486,0]])



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
result = np.append(np.array([10, 1001, 135, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,469,509,437,492,474,481,493,467,448],
[532,0,523,485,494,497,485,490,501,504],
[492,478,0,463,469,447,439,444,478,419],
[564,516,538,0,472,414,537,543,539,495],
[509,507,532,529,0,490,511,550,544,455],
[527,504,554,587,511,0,538,571,519,492],
[520,516,562,464,490,463,0,509,552,463],
[508,511,557,458,451,430,492,0,539,459],
[534,500,523,462,457,482,449,462,0,471],
[553,497,582,506,546,509,538,542,530,0]])



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
result = np.append(np.array([10, 1001, 136, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,507,504,445,478,487,474,444,464,500],
[494,0,481,491,446,506,475,473,490,509],
[497,520,0,542,503,498,535,492,498,571],
[556,510,459,0,500,483,493,496,472,533],
[523,555,498,501,0,528,516,470,502,528],
[514,495,503,518,473,0,515,476,486,527],
[527,526,466,508,485,486,0,495,486,532],
[557,528,509,505,531,525,506,0,477,551],
[537,511,503,529,499,515,515,524,0,575],
[501,492,430,468,473,474,469,450,426,0]])



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
result = np.append(np.array([10, 1001, 137, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,495,509,536,500,513,501,507,510,535],
[506,0,505,471,497,511,512,475,469,533],
[492,496,0,493,461,511,462,509,468,495],
[465,530,508,0,490,516,505,493,493,545],
[501,504,540,511,0,532,473,496,520,533],
[488,490,490,485,469,0,487,480,477,538],
[500,489,539,496,528,514,0,501,509,572],
[494,526,492,508,505,521,500,0,493,524],
[491,532,533,508,481,524,492,508,0,560],
[466,468,506,456,468,463,429,477,441,0]])



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
result = np.append(np.array([10, 1001, 138, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,562,442,482,537,467,424,508,506,481],
[439,0,476,435,520,459,409,452,487,489],
[559,525,0,512,570,521,485,553,524,468],
[519,566,489,0,495,449,523,523,509,477],
[464,481,431,506,0,448,448,451,430,437],
[534,542,480,552,553,0,464,541,508,516],
[577,592,516,478,553,537,0,529,504,538],
[493,549,448,478,550,460,472,0,488,468],
[495,514,477,492,571,493,497,513,0,497],
[520,512,533,524,564,485,463,533,504,0]])



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
result = np.append(np.array([10, 1001, 139, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,474,508,511,492,495,507,483,449,500],
[527,0,514,501,531,499,524,502,496,530],
[493,487,0,492,471,478,496,464,466,505],
[490,500,509,0,482,489,503,491,468,509],
[509,470,530,519,0,478,518,480,524,518],
[506,502,523,512,523,0,527,500,487,544],
[494,477,505,498,483,474,0,483,467,516],
[518,499,537,510,521,501,518,0,525,542],
[552,505,535,533,477,514,534,476,0,546],
[501,471,496,492,483,457,485,459,455,0]])



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
result = np.append(np.array([10, 1001, 140, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,445,336,425,249,458,439,271,548,388],
[556,0,598,528,443,793,681,428,721,526],
[665,403,0,364,335,566,495,432,633,441],
[576,473,637,0,461,557,339,534,635,558],
[752,558,666,540,0,560,371,456,573,539],
[543,208,435,444,441,0,400,382,496,386],
[562,320,506,662,630,601,0,450,784,462],
[730,573,569,467,545,619,551,0,864,460],
[453,280,368,366,428,505,217,137,0,397],
[613,475,560,443,462,615,539,541,604,0]])



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
result = np.append(np.array([10, 1001, 141, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,577,480,515,495,427,493,508,513,473],
[424,0,471,459,447,407,413,444,446,461],
[521,530,0,510,458,501,476,492,533,495],
[486,542,491,0,496,468,466,513,518,488],
[506,554,543,505,0,445,453,494,504,501],
[574,594,500,533,556,0,497,522,562,515],
[508,588,525,535,548,504,0,483,523,509],
[493,557,509,488,507,479,518,0,532,480],
[488,555,468,483,497,439,478,469,0,468],
[528,540,506,513,500,486,492,521,533,0]])



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
result = np.append(np.array([10, 1001, 142, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,470,448,495,450,548,525,508,475,499],
[531,0,480,469,487,497,509,501,507,467],
[553,521,0,513,496,519,543,511,516,530],
[506,532,488,0,496,509,571,517,483,496],
[551,514,505,505,0,523,552,477,530,526],
[453,504,482,492,478,0,526,485,484,491],
[476,492,458,430,449,475,0,460,478,467],
[493,500,490,484,524,516,541,0,513,507],
[526,494,485,518,471,517,523,488,0,459],
[502,534,471,505,475,510,534,494,542,0]])



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
result = np.append(np.array([10, 1001, 143, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,464,488,523,528,449,505,523,501,451],
[537,0,515,511,483,498,498,513,491,501],
[513,486,0,553,524,502,547,545,466,504],
[478,490,448,0,472,448,487,537,449,450],
[473,518,477,529,0,476,501,503,448,462],
[552,503,499,553,525,0,505,537,488,526],
[496,503,454,514,500,496,0,494,500,468],
[478,488,456,464,498,464,507,0,458,439],
[500,510,535,552,553,513,501,543,0,540],
[550,500,497,551,539,475,533,562,461,0]])



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
result = np.append(np.array([10, 1001, 144, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,484,500,460,498,491,515,474,522,495],
[517,0,485,490,495,498,503,491,517,504],
[501,516,0,485,510,480,490,500,502,461],
[541,511,516,0,522,553,533,493,507,541],
[503,506,491,479,0,501,498,498,507,490],
[510,503,521,448,500,0,496,468,518,494],
[486,498,511,468,503,505,0,509,533,500],
[527,510,501,508,503,533,492,0,510,534],
[479,484,499,494,494,483,468,491,0,489],
[506,497,540,460,511,507,501,467,512,0]])



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
result = np.append(np.array([10, 1001, 145, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,593,524,473,541,566,529,604,602,522],
[408,0,534,487,433,545,496,566,443,545],
[477,467,0,575,505,487,403,496,473,555],
[528,514,426,0,433,568,502,613,484,536],
[460,568,496,568,0,523,621,564,544,668],
[435,456,514,433,478,0,553,642,464,524],
[472,505,598,499,380,448,0,583,565,386],
[397,435,505,388,437,359,418,0,485,483],
[399,558,528,517,457,537,436,516,0,513],
[479,456,446,465,333,477,615,518,488,0]])



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
result = np.append(np.array([10, 1001, 146, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,498,473,501,467,512,520,506,510,488],
[503,0,474,503,456,474,498,477,466,458],
[528,527,0,528,490,528,533,476,522,509],
[500,498,473,0,451,501,513,458,462,453],
[534,545,511,550,0,546,526,495,516,511],
[489,527,473,500,455,0,520,485,475,491],
[481,503,468,488,475,481,0,457,510,497],
[495,524,525,543,506,516,544,0,520,515],
[491,535,479,539,485,526,491,481,0,501],
[513,543,492,548,490,510,504,486,500,0]])



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
result = np.append(np.array([10, 1001, 147, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,471,477,504,480,460,494,476,503,453],
[530,0,506,482,521,510,512,519,538,509],
[524,495,0,507,493,503,491,496,507,488],
[497,519,494,0,506,493,506,484,493,481],
[521,480,508,495,0,482,513,510,510,506],
[541,491,498,508,519,0,523,505,514,509],
[507,489,510,495,488,478,0,498,503,484],
[525,482,505,517,491,496,503,0,520,494],
[498,463,494,508,491,487,498,481,0,489],
[548,492,513,520,495,492,517,507,512,0]])



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
result = np.append(np.array([10, 1001, 148, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,517,543,481,493,515,518,518,514,537],
[484,0,552,500,485,498,499,502,529,505],
[458,449,0,457,456,473,510,464,447,469],
[520,501,544,0,454,489,506,500,521,499],
[508,516,545,547,0,522,536,484,505,515],
[486,503,528,512,479,0,461,482,523,505],
[483,502,491,495,465,540,0,495,530,512],
[483,499,537,501,517,519,506,0,509,514],
[487,472,554,480,496,478,471,492,0,503],
[464,496,532,502,486,496,489,487,498,0]])



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
result = np.append(np.array([10, 1001, 149, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,499,526,502,481,509,494,492,501,480],
[502,0,521,501,507,488,487,479,499,466],
[475,480,0,466,506,476,457,490,484,468],
[499,500,535,0,493,488,497,506,494,494],
[520,494,495,508,0,509,495,486,485,490],
[492,513,525,513,492,0,461,474,493,473],
[507,514,544,504,506,540,0,504,514,500],
[509,522,511,495,515,527,497,0,512,505],
[500,502,517,507,516,508,487,489,0,482],
[521,535,533,507,511,528,501,496,519,0]])



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
result = np.append(np.array([10, 1001, 150, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,526,491,507,475,496,486,467,467,488],
[475,0,487,468,437,501,469,494,501,430],
[510,514,0,481,475,474,484,463,502,494],
[494,533,520,0,445,520,518,483,504,488],
[526,564,526,556,0,519,517,529,516,483],
[505,500,527,481,482,0,489,474,493,476],
[515,532,517,483,484,512,0,526,490,502],
[534,507,538,518,472,527,475,0,499,466],
[534,500,499,497,485,508,511,502,0,496],
[513,571,507,513,518,525,499,535,505,0]])



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
result = np.append(np.array([10, 1001, 151, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,496,479,441,514,502,458,511,488,502],
[505,0,455,452,506,443,486,510,521,515],
[522,546,0,507,523,520,507,504,502,468],
[560,549,494,0,536,553,549,555,544,497],
[487,495,478,465,0,493,490,549,514,437],
[499,558,481,448,508,0,501,530,489,470],
[543,515,494,452,511,500,0,513,477,447],
[490,491,497,446,452,471,488,0,474,471],
[513,480,499,457,487,512,524,527,0,489],
[499,486,533,504,564,531,554,530,512,0]])



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
result = np.append(np.array([10, 1001, 152, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,462,502,489,493,494,505,504,510,499],
[539,0,510,481,496,497,505,501,500,501],
[499,491,0,466,489,482,489,485,492,501],
[512,520,535,0,499,507,533,518,499,513],
[508,505,512,502,0,510,502,496,499,503],
[507,504,519,494,491,0,498,510,504,504],
[496,496,512,468,499,503,0,501,487,501],
[497,500,516,483,505,491,500,0,493,503],
[491,501,509,502,502,497,514,508,0,491],
[502,500,500,488,498,497,500,498,510,0]])



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
result = np.append(np.array([10, 1001, 153, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,531,274,385,551,436,375,288,396,438],
[470,0,370,577,629,600,480,418,606,553],
[727,631,0,662,676,679,436,595,808,486],
[616,424,339,0,551,485,464,498,697,661],
[450,372,325,450,0,388,316,344,594,340],
[565,401,322,516,613,0,387,408,745,559],
[626,521,565,537,685,614,0,403,598,629],
[713,583,406,503,657,593,598,0,588,505],
[605,395,193,304,407,256,403,413,0,310],
[563,448,515,340,661,442,372,496,691,0]])



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
result = np.append(np.array([10, 1001, 154, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,501,506,501,557,528,461,507,566,490],
[500,0,508,528,504,509,534,493,531,425],
[495,493,0,489,534,554,488,509,540,479],
[500,473,512,0,489,527,459,490,499,455],
[444,497,467,512,0,514,473,511,543,481],
[473,492,447,474,487,0,476,490,530,435],
[540,467,513,542,528,525,0,526,538,514],
[494,508,492,511,490,511,475,0,499,468],
[435,470,461,502,458,471,463,502,0,478],
[511,576,522,546,520,566,487,533,523,0]])



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
result = np.append(np.array([10, 1001, 155, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,490,530,463,475,531,473,476,501,462],
[511,0,483,517,508,520,520,508,517,480],
[471,518,0,507,478,504,480,512,503,496],
[538,484,494,0,473,542,503,527,506,501],
[526,493,523,528,0,509,518,518,526,503],
[470,481,497,459,492,0,495,519,483,489],
[528,481,521,498,483,506,0,520,529,505],
[525,493,489,474,483,482,481,0,537,462],
[500,484,498,495,475,518,472,464,0,499],
[539,521,505,500,498,512,496,539,502,0]])



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
result = np.append(np.array([10, 1001, 156, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,447,468,461,458,502,480,441,460,457],
[554,0,496,508,501,550,525,514,511,536],
[533,505,0,465,493,516,538,508,482,500],
[540,493,536,0,516,536,539,505,505,518],
[543,500,508,485,0,532,531,517,481,526],
[499,451,485,465,469,0,500,473,479,487],
[521,476,463,462,470,501,0,483,484,466],
[560,487,493,496,484,528,518,0,495,490],
[541,490,519,496,520,522,517,506,0,483],
[544,465,501,483,475,514,535,511,518,0]])



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
result = np.append(np.array([10, 1001, 157, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,476,478,464,481,428,476,494,423,479],
[525,0,488,466,454,446,466,480,460,488],
[523,513,0,471,471,491,477,494,459,537],
[537,535,530,0,518,467,498,496,501,508],
[520,547,530,483,0,476,496,478,459,514],
[573,555,510,534,525,0,519,506,477,516],
[525,535,524,503,505,482,0,479,476,527],
[507,521,507,505,523,495,522,0,474,526],
[578,541,542,500,542,524,525,527,0,538],
[522,513,464,493,487,485,474,475,463,0]])



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
result = np.append(np.array([10, 1001, 158, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,533,487,489,444,523,507,377,529,550],
[468,0,511,563,525,512,527,424,566,460],
[514,490,0,465,487,511,514,404,518,575],
[512,438,536,0,476,541,474,449,515,485],
[557,476,514,525,0,544,533,505,531,576],
[478,489,490,460,457,0,526,405,477,471],
[494,474,487,527,468,475,0,433,480,526],
[624,577,597,552,496,596,568,0,634,608],
[472,435,483,486,470,524,521,367,0,526],
[451,541,426,516,425,530,475,393,475,0]])



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
result = np.append(np.array([10, 1001, 159, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,512,530,499,523,507,501,514,485,512],
[489,0,522,469,534,499,515,504,493,539],
[471,479,0,474,526,490,483,497,489,517],
[502,532,527,0,507,502,512,521,493,533],
[478,467,475,494,0,484,489,494,495,493],
[494,502,511,499,517,0,512,527,491,535],
[500,486,518,489,512,489,0,510,507,520],
[487,497,504,480,507,474,491,0,502,498],
[516,508,512,508,506,510,494,499,0,513],
[489,462,484,468,508,466,481,503,488,0]])



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
result = np.append(np.array([10, 1001, 160, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,510,499,473,489,497,466,496,498,495],
[491,0,490,480,479,501,495,472,509,483],
[502,511,0,498,525,513,501,483,514,523],
[528,521,503,0,510,500,489,498,492,510],
[512,522,476,491,0,498,510,506,506,500],
[504,500,488,501,503,0,490,484,514,462],
[535,506,500,512,491,511,0,483,487,480],
[505,529,518,503,495,517,518,0,534,501],
[503,492,487,509,495,487,514,467,0,496],
[506,518,478,491,501,539,521,500,505,0]])



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
result = np.append(np.array([10, 1001, 161, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,526,512,517,493,532,476,495,497,492],
[475,0,490,497,501,489,502,473,481,491],
[489,511,0,477,503,515,482,492,487,507],
[484,504,524,0,522,556,497,481,518,512],
[508,500,498,479,0,517,484,476,479,485],
[469,512,486,445,484,0,475,469,478,500],
[525,499,519,504,517,526,0,505,499,487],
[506,528,509,520,525,532,496,0,501,513],
[504,520,514,483,522,523,502,500,0,499],
[509,510,494,489,516,501,514,488,502,0]])



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
result = np.append(np.array([10, 1001, 162, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,521,486,509,501,500,513,530,502,491],
[480,0,467,499,476,515,499,511,481,490],
[515,534,0,527,513,519,521,544,508,488],
[492,502,474,0,498,491,480,500,484,501],
[500,525,488,503,0,540,512,533,517,484],
[501,486,482,510,461,0,484,507,480,490],
[488,502,480,521,489,517,0,514,477,503],
[471,490,457,501,468,494,487,0,485,488],
[499,520,493,517,484,521,524,516,0,511],
[510,511,513,500,517,511,498,513,490,0]])



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
result = np.append(np.array([10, 1001, 163, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,510,514,555,517,498,540,520,543,516],
[491,0,495,467,497,498,515,490,524,480],
[487,506,0,524,499,500,513,503,514,501],
[446,534,477,0,490,500,471,478,522,498],
[484,504,502,511,0,508,486,475,512,501],
[503,503,501,501,493,0,512,532,530,491],
[461,486,488,530,515,489,0,510,526,553],
[481,511,498,523,526,469,491,0,537,497],
[458,477,487,479,489,471,475,464,0,463],
[485,521,500,503,500,510,448,504,538,0]])



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
result = np.append(np.array([10, 1001, 164, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,518,518,486,521,513,529,510,503,507],
[483,0,503,482,485,486,505,486,491,511],
[483,498,0,472,504,490,522,498,505,512],
[515,519,529,0,508,505,545,504,499,504],
[480,516,497,493,0,486,512,482,478,518],
[488,515,511,496,515,0,536,496,498,515],
[472,496,479,456,489,465,0,484,468,506],
[491,515,503,497,519,505,517,0,501,519],
[498,510,496,502,523,503,533,500,0,522],
[494,490,489,497,483,486,495,482,479,0]])



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
result = np.append(np.array([10, 1001, 165, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,513,500,487,509,499,504,533,513,506],
[488,0,477,487,531,500,524,529,534,510],
[501,524,0,507,538,496,514,521,510,519],
[514,514,494,0,526,520,523,540,555,541],
[492,470,463,475,0,510,495,505,524,503],
[502,501,505,481,491,0,475,517,537,532],
[497,477,487,478,506,526,0,484,509,518],
[468,472,480,461,496,484,517,0,503,530],
[488,467,491,446,477,464,492,498,0,488],
[495,491,482,460,498,469,483,471,513,0]])



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
result = np.append(np.array([10, 1001, 166, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,435,515,482,478,478,502,492,460,464],
[566,0,493,524,504,510,546,545,519,507],
[486,508,0,478,534,500,510,526,501,527],
[519,477,523,0,484,512,515,526,499,516],
[523,497,467,517,0,519,516,528,505,486],
[523,491,501,489,482,0,501,517,491,505],
[499,455,491,486,485,500,0,527,508,501],
[509,456,475,475,473,484,474,0,479,472],
[541,482,500,502,496,510,493,522,0,493],
[537,494,474,485,515,496,500,529,508,0]])



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
result = np.append(np.array([10, 1001, 167, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,478,488,483,504,497,485,493,468,493],
[523,0,525,507,499,500,494,478,508,503],
[513,476,0,477,520,530,511,489,480,484],
[518,494,524,0,528,523,491,512,491,483],
[497,502,481,473,0,503,501,492,479,488],
[504,501,471,478,498,0,495,489,476,464],
[516,507,490,510,500,506,0,491,498,498],
[508,523,512,489,509,512,510,0,504,496],
[533,493,521,510,522,525,503,497,0,518],
[508,498,517,518,513,537,503,505,483,0]])



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
result = np.append(np.array([10, 1001, 168, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,520,472,494,497,539,538,527,542,484],
[481,0,516,519,478,493,486,501,516,519],
[529,485,0,518,493,517,534,511,531,529],
[507,482,483,0,512,531,513,510,510,508],
[504,523,508,489,0,504,537,516,517,509],
[462,508,484,470,497,0,486,508,503,472],
[463,515,467,488,464,515,0,517,515,484],
[474,500,490,491,485,493,484,0,509,480],
[459,485,470,491,484,498,486,492,0,486],
[517,482,472,493,492,529,517,521,515,0]])



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
result = np.append(np.array([10, 1001, 169, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,518,459,517,465,513,443,448,471,552],
[483,0,467,491,535,446,393,472,483,497],
[542,534,0,482,546,522,504,464,542,561],
[484,510,519,0,495,513,446,499,561,564],
[536,466,455,506,0,453,385,482,512,538],
[488,555,479,488,548,0,466,511,523,537],
[558,608,497,555,616,535,0,585,554,573],
[553,529,537,502,519,490,416,0,522,561],
[530,518,459,440,489,478,447,479,0,510],
[449,504,440,437,463,464,428,440,491,0]])



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
result = np.append(np.array([10, 1001, 170, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,507,516,509,484,480,494,525,520,501],
[494,0,530,474,497,463,494,506,482,478],
[485,471,0,494,482,474,480,509,484,480],
[492,527,507,0,491,493,508,521,511,472],
[517,504,519,510,0,506,476,510,514,503],
[521,538,527,508,495,0,496,518,522,504],
[507,507,521,493,525,505,0,532,512,514],
[476,495,492,480,491,483,469,0,495,486],
[481,519,517,490,487,479,489,506,0,498],
[500,523,521,529,498,497,487,515,503,0]])



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
result = np.append(np.array([10, 1001, 171, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,503,506,510,487,507,506,524,533,512],
[498,0,500,501,510,510,523,488,530,515],
[495,501,0,506,489,487,490,512,503,526],
[491,500,495,0,480,474,500,495,530,511],
[514,491,512,521,0,491,532,516,524,540],
[494,491,514,527,510,0,487,506,509,505],
[495,478,511,501,469,514,0,510,516,500],
[477,513,489,506,485,495,491,0,488,520],
[468,471,498,471,477,492,485,513,0,505],
[489,486,475,490,461,496,501,481,496,0]])



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
result = np.append(np.array([10, 1001, 172, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,483,476,503,499,498,500,542,505,514],
[518,0,484,508,517,490,496,533,495,531],
[525,517,0,502,509,512,497,544,507,542],
[498,493,499,0,524,498,536,542,510,523],
[502,484,492,477,0,498,479,544,500,520],
[503,511,489,503,503,0,509,526,516,522],
[501,505,504,465,522,492,0,518,497,514],
[459,468,457,459,457,475,483,0,471,492],
[496,506,494,491,501,485,504,530,0,508],
[487,470,459,478,481,479,487,509,493,0]])



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
result = np.append(np.array([10, 1001, 173, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,498,480,505,496,502,507,526,486,497],
[503,0,492,491,502,510,508,513,501,494],
[521,509,0,491,505,500,498,506,480,500],
[496,510,510,0,506,513,515,523,500,522],
[505,499,496,495,0,485,496,500,494,501],
[499,491,501,488,516,0,514,517,483,490],
[494,493,503,486,505,487,0,512,484,479],
[475,488,495,478,501,484,489,0,471,498],
[515,500,521,501,507,518,517,530,0,517],
[504,507,501,479,500,511,522,503,484,0]])



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
result = np.append(np.array([10, 1001, 174, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,517,470,533,473,501,531,504,513,528],
[484,0,498,496,461,472,506,459,529,538],
[531,503,0,499,471,477,504,481,536,460],
[468,505,502,0,400,469,508,506,479,500],
[528,540,530,601,0,492,548,525,558,502],
[500,529,524,532,509,0,525,491,570,543],
[470,495,497,493,453,476,0,520,513,499],
[497,542,520,495,476,510,481,0,532,469],
[488,472,465,522,443,431,488,469,0,456],
[473,463,541,501,499,458,502,532,545,0]])



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
result = np.append(np.array([10, 1001, 175, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,474,533,533,515,477,483,530,503,523],
[527,0,555,577,511,480,492,499,511,546],
[468,446,0,520,481,438,462,479,484,503],
[468,424,481,0,478,423,431,455,475,472],
[486,490,520,523,0,456,499,498,474,546],
[524,521,563,578,545,0,522,541,497,548],
[518,509,539,570,502,479,0,518,484,531],
[471,502,522,546,503,460,483,0,488,506],
[498,490,517,526,527,504,517,513,0,537],
[478,455,498,529,455,453,470,495,464,0]])



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
result = np.append(np.array([10, 1001, 176, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,500,515,506,528,508,493,501,509,501],
[501,0,501,504,492,505,494,477,502,506],
[486,500,0,513,492,470,504,482,470,483],
[495,497,488,0,515,483,466,471,470,482],
[473,509,509,486,0,501,496,470,504,484],
[493,496,531,518,500,0,499,482,483,509],
[508,507,497,535,505,502,0,469,512,498],
[500,524,519,530,531,519,532,0,546,531],
[492,499,531,531,497,518,489,455,0,521],
[500,495,518,519,517,492,503,470,480,0]])



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
result = np.append(np.array([10, 1001, 177, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,509,506,539,529,491,519,508,547,519],
[492,0,465,503,480,476,506,503,517,500],
[495,536,0,543,541,503,554,523,548,522],
[462,498,458,0,503,463,497,470,500,468],
[472,521,460,498,0,480,518,500,507,486],
[510,525,498,538,521,0,521,510,552,510],
[482,495,447,504,483,480,0,478,507,478],
[493,498,478,531,501,491,523,0,499,496],
[454,484,453,501,494,449,494,502,0,467],
[482,501,479,533,515,491,523,505,534,0]])



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
result = np.append(np.array([10, 1001, 178, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,479,526,536,542,524,528,491,485,507],
[522,0,494,548,516,574,512,499,494,500],
[475,507,0,523,512,516,497,469,444,507],
[465,453,478,0,483,507,494,463,456,492],
[459,485,489,518,0,518,515,503,480,498],
[477,427,485,494,483,0,458,455,481,482],
[473,489,504,507,486,543,0,425,472,519],
[510,502,532,538,498,546,576,0,510,500],
[516,507,557,545,521,520,529,491,0,533],
[494,501,494,509,503,519,482,501,468,0]])



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
result = np.append(np.array([10, 1001, 179, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,491,483,504,471,496,472,494,479,500],
[510,0,507,507,459,502,490,501,494,488],
[518,494,0,524,459,503,527,508,506,501],
[497,494,477,0,482,489,496,511,487,516],
[530,542,542,519,0,521,520,496,501,528],
[505,499,498,512,480,0,507,512,501,530],
[529,511,474,505,481,494,0,517,500,507],
[507,500,493,490,505,489,484,0,498,524],
[522,507,495,514,500,500,501,503,0,495],
[501,513,500,485,473,471,494,477,506,0]])



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
result = np.append(np.array([10, 1001, 180, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,483,490,504,466,528,463,500,449,487],
[518,0,495,426,522,497,521,511,514,564],
[511,506,0,462,548,519,509,489,443,533],
[497,575,539,0,552,561,556,530,508,553],
[535,479,453,449,0,530,491,461,476,483],
[473,504,482,440,471,0,450,430,436,502],
[538,480,492,445,510,551,0,503,464,496],
[501,490,512,471,540,571,498,0,515,548],
[552,487,558,493,525,565,537,486,0,542],
[514,437,468,448,518,499,505,453,459,0]])



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
result = np.append(np.array([10, 1001, 181, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,496,550,523,505,484,487,526,462,455],
[505,0,469,514,483,482,456,496,426,491],
[451,532,0,499,525,542,513,529,464,471],
[478,487,502,0,506,511,476,489,501,488],
[496,518,476,495,0,478,516,561,518,508],
[517,519,459,490,523,0,468,471,464,459],
[514,545,488,525,485,533,0,493,479,497],
[475,505,472,512,440,530,508,0,497,490],
[539,575,537,500,483,537,522,504,0,517],
[546,510,530,513,493,542,504,511,484,0]])



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
result = np.append(np.array([10, 1001, 182, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,532,439,462,474,466,468,495,452,481],
[469,0,421,497,491,473,451,463,477,500],
[562,580,0,495,517,549,543,535,531,546],
[539,504,506,0,508,537,442,515,484,512],
[527,510,484,493,0,533,511,492,502,547],
[535,528,452,464,468,0,516,521,504,502],
[533,550,458,559,490,485,0,523,481,575],
[506,538,466,486,509,480,478,0,488,514],
[549,524,470,517,499,497,520,513,0,504],
[520,501,455,489,454,499,426,487,497,0]])



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
result = np.append(np.array([10, 1001, 183, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,532,507,523,514,497,534,462,476,496],
[469,0,499,521,521,463,489,491,452,476],
[494,502,0,509,500,491,509,486,493,505],
[478,480,492,0,491,481,489,518,452,489],
[487,480,501,510,0,463,500,487,479,477],
[504,538,510,520,538,0,528,527,495,507],
[467,512,492,512,501,473,0,475,496,514],
[539,510,515,483,514,474,526,0,523,481],
[525,549,508,549,522,506,505,478,0,517],
[505,525,496,512,524,494,487,520,484,0]])



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
result = np.append(np.array([10, 1001, 184, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,517,474,496,487,515,505,522,484,517],
[484,0,497,498,527,496,488,511,505,502],
[527,504,0,527,524,493,525,505,521,535],
[505,503,474,0,490,492,518,495,504,492],
[514,474,477,511,0,477,499,494,508,497],
[486,505,508,509,524,0,483,503,512,508],
[496,513,476,483,502,518,0,487,502,537],
[479,490,496,506,507,498,514,0,523,507],
[517,496,480,497,493,489,499,478,0,527],
[484,499,466,509,504,493,464,494,474,0]])



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
result = np.append(np.array([10, 1001, 185, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,531,474,556,545,545,544,506,546,547],
[470,0,473,534,509,490,527,464,480,499],
[527,528,0,510,500,460,504,528,558,555],
[445,467,491,0,546,500,511,447,571,488],
[456,492,501,455,0,454,488,494,530,483],
[456,511,541,501,547,0,509,515,511,511],
[457,474,497,490,513,492,0,517,510,485],
[495,537,473,554,507,486,484,0,482,506],
[455,521,443,430,471,490,491,519,0,488],
[454,502,446,513,518,490,516,495,513,0]])



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
result = np.append(np.array([10, 1001, 186, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,499,531,552,521,531,506,502,507,532],
[502,0,512,509,520,540,494,504,507,499],
[470,489,0,495,491,510,441,494,497,507],
[449,492,506,0,532,516,471,491,505,500],
[480,481,510,469,0,535,450,497,511,470],
[470,461,491,485,466,0,439,491,482,483],
[495,507,560,530,551,562,0,549,551,523],
[499,497,507,510,504,510,452,0,479,490],
[494,494,504,496,490,519,450,522,0,528],
[469,502,494,501,531,518,478,511,473,0]])



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
result = np.append(np.array([10, 1001, 187, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,465,455,508,461,519,499,498,495,551],
[536,0,534,497,518,549,553,513,533,563],
[546,467,0,463,501,488,522,483,467,529],
[493,504,538,0,498,496,529,520,505,551],
[540,483,500,503,0,502,541,538,506,514],
[482,452,513,505,499,0,525,506,482,552],
[502,448,479,472,460,476,0,499,467,493],
[503,488,518,481,463,495,502,0,447,532],
[506,468,534,496,495,519,534,554,0,515],
[450,438,472,450,487,449,508,469,486,0]])



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
result = np.append(np.array([10, 1001, 188, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,539,529,492,511,505,512,530,512,509],
[462,0,514,491,513,484,487,521,508,507],
[472,487,0,482,495,481,473,492,515,492],
[509,510,519,0,514,490,461,518,525,497],
[490,488,506,487,0,479,466,487,500,485],
[496,517,520,511,522,0,485,523,516,519],
[489,514,528,540,535,516,0,541,508,527],
[471,480,509,483,514,478,460,0,477,489],
[489,493,486,476,501,485,493,524,0,493],
[492,494,509,504,516,482,474,512,508,0]])



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
result = np.append(np.array([10, 1001, 189, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,484,507,498,497,482,513,495,502,489],
[517,0,510,509,470,481,511,484,516,509],
[494,491,0,490,505,499,520,507,524,511],
[503,492,511,0,500,507,511,501,511,497],
[504,531,496,501,0,510,510,505,515,522],
[519,520,502,494,491,0,520,537,523,496],
[488,490,481,490,491,481,0,477,479,480],
[506,517,494,500,496,464,524,0,520,514],
[499,485,477,490,486,478,522,481,0,500],
[512,492,490,504,479,505,521,487,501,0]])



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
result = np.append(np.array([10, 1001, 190, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,483,529,515,523,540,504,479,477,506],
[518,0,522,489,511,527,536,488,482,537],
[472,479,0,488,519,519,499,476,482,498],
[486,512,513,0,521,541,529,502,487,499],
[478,490,482,480,0,505,514,453,475,499],
[461,474,482,460,496,0,513,469,489,490],
[497,465,502,472,487,488,0,487,455,494],
[522,513,525,499,548,532,514,0,510,488],
[524,519,519,514,526,512,546,491,0,521],
[495,464,503,502,502,511,507,513,480,0]])



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
result = np.append(np.array([10, 1001, 191, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,616,513,552,608,431,510,485,481,650],
[385,0,333,438,418,411,400,444,477,520],
[488,668,0,541,548,519,568,534,503,566],
[449,563,460,0,466,419,417,389,468,474],
[393,583,453,535,0,536,546,446,486,540],
[570,590,482,582,465,0,477,465,422,690],
[491,601,433,584,455,524,0,505,516,625],
[516,557,467,612,555,536,496,0,522,631],
[520,524,498,533,515,579,485,479,0,533],
[351,481,435,527,461,311,376,370,468,0]])



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
result = np.append(np.array([10, 1001, 192, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,484,478,527,516,505,524,493,469,481],
[517,0,505,531,521,541,527,539,482,505],
[523,496,0,519,548,547,541,522,499,518],
[474,470,482,0,502,508,520,502,455,471],
[485,480,453,499,0,498,540,513,475,471],
[496,460,454,493,503,0,496,498,438,498],
[477,474,460,481,461,505,0,484,474,493],
[508,462,479,499,488,503,517,0,471,504],
[532,519,502,546,526,563,527,530,0,489],
[520,496,483,530,530,503,508,497,512,0]])



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
result = np.append(np.array([10, 1001, 193, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,516,505,511,483,515,507,485,496,482],
[485,0,463,482,477,504,481,474,480,489],
[496,538,0,522,507,496,511,493,498,511],
[490,519,479,0,489,514,501,488,486,485],
[518,524,494,512,0,516,509,508,506,481],
[486,497,505,487,485,0,503,505,491,491],
[494,520,490,500,492,498,0,488,508,512],
[516,527,508,513,493,496,513,0,480,484],
[505,521,503,515,495,510,493,521,0,517],
[519,512,490,516,520,510,489,517,484,0]])



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
result = np.append(np.array([10, 1001, 194, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,509,495,490,497,486,479,503,482,497],
[492,0,484,484,477,478,468,498,488,483],
[506,517,0,482,493,509,481,502,485,507],
[511,517,519,0,498,515,492,491,505,503],
[504,524,508,503,0,520,499,518,501,494],
[515,523,492,486,481,0,478,492,500,505],
[522,533,520,509,502,523,0,528,489,495],
[498,503,499,510,483,509,473,0,491,495],
[519,513,516,496,500,501,512,510,0,507],
[504,518,494,498,507,496,506,506,494,0]])



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
result = np.append(np.array([10, 1001, 195, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,475,501,481,485,483,486,479,503,518],
[526,0,513,477,504,498,500,516,515,529],
[500,488,0,515,506,502,491,498,483,524],
[520,524,486,0,511,519,516,494,489,525],
[516,497,495,490,0,514,490,463,475,521],
[518,503,499,482,487,0,489,494,501,515],
[515,501,510,485,511,512,0,501,493,519],
[522,485,503,507,538,507,500,0,525,528],
[498,486,518,512,526,500,508,476,0,501],
[483,472,477,476,480,486,482,473,500,0]])



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
result = np.append(np.array([10, 1001, 196, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,506,529,476,475,505,473,492,492,516],
[495,0,476,476,498,535,494,503,483,477],
[472,525,0,480,508,539,474,506,488,468],
[525,525,521,0,500,532,476,529,517,513],
[526,503,493,501,0,528,528,511,498,496],
[496,466,462,469,473,0,479,512,476,494],
[528,507,527,525,473,522,0,511,493,496],
[509,498,495,472,490,489,490,0,485,484],
[509,518,513,484,503,525,508,516,0,473],
[485,524,533,488,505,507,505,517,528,0]])



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
result = np.append(np.array([10, 1001, 197, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,514,462,513,479,492,481,469,499,491],
[487,0,477,483,486,513,479,514,496,475],
[539,524,0,536,542,521,552,499,526,526],
[488,518,465,0,489,492,486,492,512,497],
[522,515,459,512,0,519,507,501,532,493],
[509,488,480,509,482,0,485,524,502,499],
[520,522,449,515,494,516,0,511,524,496],
[532,487,502,509,500,477,490,0,531,492],
[502,505,475,489,469,499,477,470,0,505],
[510,526,475,504,508,502,505,509,496,0]])



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
result = np.append(np.array([10, 1001, 198, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,505,497,524,494,510,530,530,514,498],
[496,0,504,516,494,502,496,513,510,502],
[504,497,0,500,500,489,496,513,515,478],
[477,485,501,0,467,493,468,480,498,460],
[507,507,501,534,0,508,498,527,510,495],
[491,499,512,508,493,0,489,521,510,497],
[471,505,505,533,503,512,0,510,533,508],
[471,488,488,521,474,480,491,0,492,470],
[487,491,486,503,491,491,468,509,0,481],
[503,499,523,541,506,504,493,531,520,0]])



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
result = np.append(np.array([10, 1001, 199, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,503,467,475,517,478,477,497,490,491],
[498,0,443,486,481,472,471,474,451,532],
[534,558,0,495,514,493,526,556,528,556],
[526,515,506,0,545,476,478,493,480,527],
[484,520,487,456,0,529,488,509,487,518],
[523,529,508,525,472,0,500,491,508,519],
[524,530,475,523,513,501,0,481,483,509],
[504,527,445,508,492,510,520,0,433,505],
[511,550,473,521,514,493,518,568,0,523],
[510,469,445,474,483,482,492,496,478,0]])



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
result = np.append(np.array([10, 1001, 200, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/me/me_10_1001.csv", index=False, header=False)