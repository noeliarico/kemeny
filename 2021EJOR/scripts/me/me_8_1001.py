
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg

rep = 3
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,499,488,449,504,461,505,486],
[502,0,502,503,514,479,473,494],
[513,499,0,474,491,496,513,486],
[552,498,527,0,499,493,497,512],
[497,487,510,502,0,479,497,479],
[540,522,505,508,522,0,504,486],
[496,528,488,504,504,497,0,497],
[515,507,515,489,522,515,504,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 1, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,555,564,554,535,465,556,535],
[446,0,528,528,497,435,533,470],
[437,473,0,454,497,432,466,457],
[447,473,547,0,487,450,531,492],
[466,504,504,514,0,434,539,454],
[536,566,569,551,567,0,567,474],
[445,468,535,470,462,434,0,454],
[466,531,544,509,547,527,547,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 2, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,476,492,502,485,547,462,569],
[525,0,556,510,498,546,494,534],
[509,445,0,479,530,543,499,490],
[499,491,522,0,528,523,510,562],
[516,503,471,473,0,519,508,540],
[454,455,458,478,482,0,470,555],
[539,507,502,491,493,531,0,515],
[432,467,511,439,461,446,486,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 3, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,503,532,519,547,539,556,491],
[498,0,512,507,527,521,503,516],
[469,489,0,471,530,522,481,512],
[482,494,530,0,523,503,504,494],
[454,474,471,478,0,463,457,467],
[462,480,479,498,538,0,481,502],
[445,498,520,497,544,520,0,498],
[510,485,489,507,534,499,503,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 4, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,504,489,499,500,486,511,502],
[497,0,504,476,520,510,514,486],
[512,497,0,486,508,501,519,484],
[502,525,515,0,531,519,518,497],
[501,481,493,470,0,474,517,480],
[515,491,500,482,527,0,529,508],
[490,487,482,483,484,472,0,478],
[499,515,517,504,521,493,523,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 5, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,543,562,533,503,493,547,550],
[458,0,526,516,516,486,515,486],
[439,475,0,502,452,461,496,465],
[468,485,499,0,493,466,489,524],
[498,485,549,508,0,506,540,529],
[508,515,540,535,495,0,515,528],
[454,486,505,512,461,486,0,497],
[451,515,536,477,472,473,504,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 6, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,601,693,463,470,653,506,495],
[400,0,615,381,479,639,359,465],
[308,386,0,264,412,572,400,416],
[538,620,737,0,546,749,359,519],
[531,522,589,455,0,662,402,455],
[348,362,429,252,339,0,280,374],
[495,642,601,642,599,721,0,627],
[506,536,585,482,546,627,374,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 7, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,552,618,595,476,450,475,423],
[449,0,639,571,493,464,421,542],
[383,362,0,434,405,392,457,502],
[406,430,567,0,445,487,445,554],
[525,508,596,556,0,467,515,548],
[551,537,609,514,534,0,587,489],
[526,580,544,556,486,414,0,451],
[578,459,499,447,453,512,550,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 8, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,511,518,528,530,532,520,496],
[490,0,507,535,544,521,514,534],
[483,494,0,498,516,486,484,486],
[473,466,503,0,519,506,495,493],
[471,457,485,482,0,481,473,470],
[469,480,515,495,520,0,495,492],
[481,487,517,506,528,506,0,517],
[505,467,515,508,531,509,484,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 9, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,485,512,487,493,519,517,490],
[516,0,486,490,500,532,530,509],
[489,515,0,483,500,485,526,513],
[514,511,518,0,529,535,540,500],
[508,501,501,472,0,514,525,507],
[482,469,516,466,487,0,516,495],
[484,471,475,461,476,485,0,489],
[511,492,488,501,494,506,512,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 10, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,545,508,496,515,492,507,499],
[456,0,479,491,497,505,499,487],
[493,522,0,527,506,517,511,497],
[505,510,474,0,498,477,507,493],
[486,504,495,503,0,508,495,484],
[509,496,484,524,493,0,511,518],
[494,502,490,494,506,490,0,488],
[502,514,504,508,517,483,513,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 11, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,517,517,523,526,521,513,473],
[484,0,476,493,499,502,502,463],
[484,525,0,511,503,505,517,505],
[478,508,490,0,492,493,490,444],
[475,502,498,509,0,511,483,496],
[480,499,496,508,490,0,500,475],
[488,499,484,511,518,501,0,482],
[528,538,496,557,505,526,519,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 12, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,520,487,529,495,433,451,495],
[481,0,509,485,493,483,414,505],
[514,492,0,498,445,419,446,497],
[472,516,503,0,465,426,441,490],
[506,508,556,536,0,521,480,565],
[568,518,582,575,480,0,509,542],
[550,587,555,560,521,492,0,524],
[506,496,504,511,436,459,477,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 13, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,513,454,475,517,488,484,474],
[488,0,464,467,497,456,529,457],
[547,537,0,531,516,505,496,504],
[526,534,470,0,553,568,529,532],
[484,504,485,448,0,495,448,510],
[513,545,496,433,506,0,509,485],
[517,472,505,472,553,492,0,523],
[527,544,497,469,491,516,478,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 14, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,463,494,496,489,486,469,469],
[538,0,533,511,549,523,526,500],
[507,468,0,495,490,484,482,465],
[505,490,506,0,499,500,490,464],
[512,452,511,502,0,497,499,480],
[515,478,517,501,504,0,489,512],
[532,475,519,511,502,512,0,504],
[532,501,536,537,521,489,497,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 15, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,667,431,359,431,511,471,287],
[334,0,472,547,580,327,657,371],
[570,529,0,291,510,373,557,312],
[642,454,710,0,707,274,840,453],
[570,421,491,294,0,185,471,346],
[490,674,628,727,816,0,739,642],
[530,344,444,161,530,262,0,433],
[714,630,689,548,655,359,568,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 16, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,507,512,493,487,497,513,482],
[494,0,511,500,504,516,533,503],
[489,490,0,485,512,503,501,487],
[508,501,516,0,521,500,507,501],
[514,497,489,480,0,502,495,499],
[504,485,498,501,499,0,504,468],
[488,468,500,494,506,497,0,467],
[519,498,514,500,502,533,534,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 17, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,496,526,518,519,505,513,532],
[505,0,518,523,505,508,498,520],
[475,483,0,498,485,511,493,490],
[483,478,503,0,494,497,486,495],
[482,496,516,507,0,486,487,510],
[496,493,490,504,515,0,488,510],
[488,503,508,515,514,513,0,512],
[469,481,511,506,491,491,489,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 18, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,517,512,494,508,571,524,513],
[484,0,522,461,460,498,519,495],
[489,479,0,496,509,520,453,452],
[507,540,505,0,493,536,529,497],
[493,541,492,508,0,509,522,517],
[430,503,481,465,492,0,491,506],
[477,482,548,472,479,510,0,451],
[488,506,549,504,484,495,550,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 19, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,504,474,516,565,482,424,502],
[497,0,492,530,536,485,481,513],
[527,509,0,544,508,489,480,522],
[485,471,457,0,507,550,462,521],
[436,465,493,494,0,504,505,496],
[519,516,512,451,497,0,480,510],
[577,520,521,539,496,521,0,489],
[499,488,479,480,505,491,512,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 20, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,508,494,502,531,523,527,495],
[493,0,499,489,494,525,537,521],
[507,502,0,526,489,519,519,531],
[499,512,475,0,473,525,526,498],
[470,507,512,528,0,508,532,517],
[478,476,482,476,493,0,525,496],
[474,464,482,475,469,476,0,514],
[506,480,470,503,484,505,487,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 21, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,458,482,431,422,547,408,382],
[543,0,545,522,458,582,388,444],
[519,456,0,478,496,509,557,447],
[570,479,523,0,590,586,475,534],
[579,543,505,411,0,546,481,490],
[454,419,492,415,455,0,394,338],
[593,613,444,526,520,607,0,528],
[619,557,554,467,511,663,473,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 22, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,525,508,472,481,498,550,522],
[476,0,482,534,506,489,515,522],
[493,519,0,460,470,504,498,515],
[529,467,541,0,543,497,543,516],
[520,495,531,458,0,533,529,453],
[503,512,497,504,468,0,543,537],
[451,486,503,458,472,458,0,512],
[479,479,486,485,548,464,489,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 23, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,513,496,561,514,436,547,507],
[488,0,519,581,483,487,473,540],
[505,482,0,440,487,440,536,492],
[440,420,561,0,438,432,413,506],
[487,518,514,563,0,444,531,558],
[565,514,561,569,557,0,508,488],
[454,528,465,588,470,493,0,489],
[494,461,509,495,443,513,512,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 24, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,534,510,564,500,561,480,525],
[467,0,465,485,493,490,480,461],
[491,536,0,531,517,512,497,542],
[437,516,470,0,462,457,493,472],
[501,508,484,539,0,543,519,518],
[440,511,489,544,458,0,513,504],
[521,521,504,508,482,488,0,486],
[476,540,459,529,483,497,515,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 25, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,515,520,528,498,539,532,521],
[486,0,496,482,517,488,527,484],
[481,505,0,485,496,508,495,508],
[473,519,516,0,522,493,533,497],
[503,484,505,479,0,502,502,501],
[462,513,493,508,499,0,505,502],
[469,474,506,468,499,496,0,487],
[480,517,493,504,500,499,514,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 26, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,481,486,498,461,483,511,498],
[520,0,516,523,501,499,531,522],
[515,485,0,484,493,506,511,506],
[503,478,517,0,497,489,496,512],
[540,500,508,504,0,513,528,526],
[518,502,495,512,488,0,513,518],
[490,470,490,505,473,488,0,511],
[503,479,495,489,475,483,490,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 27, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,479,491,506,477,524,500,486],
[522,0,510,508,492,531,501,516],
[510,491,0,490,473,511,475,497],
[495,493,511,0,466,511,489,500],
[524,509,528,535,0,538,496,517],
[477,470,490,490,463,0,471,490],
[501,500,526,512,505,530,0,517],
[515,485,504,501,484,511,484,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 28, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,506,395,429,342,313,443,481],
[495,0,519,536,434,423,553,520],
[606,482,0,532,515,426,528,515],
[572,465,469,0,462,446,517,543],
[659,567,486,539,0,536,558,511],
[688,578,575,555,465,0,574,569],
[558,448,473,484,443,427,0,538],
[520,481,486,458,490,432,463,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 29, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,486,498,532,507,494,487,486],
[515,0,518,566,481,506,530,527],
[503,483,0,522,496,480,481,512],
[469,435,479,0,441,450,453,520],
[494,520,505,560,0,475,532,514],
[507,495,521,551,526,0,483,523],
[514,471,520,548,469,518,0,524],
[515,474,489,481,487,478,477,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 30, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,507,513,527,515,510,505,481],
[494,0,478,511,528,523,500,514],
[488,523,0,498,528,513,539,486],
[474,490,503,0,498,523,524,479],
[486,473,473,503,0,474,498,482],
[491,478,488,478,527,0,498,482],
[496,501,462,477,503,503,0,460],
[520,487,515,522,519,519,541,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 31, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,502,500,504,504,511,509,522],
[499,0,527,471,513,528,502,511],
[501,474,0,480,469,483,479,484],
[497,530,521,0,487,503,515,506],
[497,488,532,514,0,503,514,499],
[490,473,518,498,498,0,514,515],
[492,499,522,486,487,487,0,494],
[479,490,517,495,502,486,507,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 32, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,501,488,462,487,484,483,466],
[500,0,505,502,495,501,488,494],
[513,496,0,468,466,483,495,491],
[539,499,533,0,495,501,515,500],
[514,506,535,506,0,532,498,519],
[517,500,518,500,469,0,496,507],
[518,513,506,486,503,505,0,499],
[535,507,510,501,482,494,502,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 33, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,480,502,490,461,488,497,468],
[521,0,515,503,484,518,542,507],
[499,486,0,450,465,472,509,489],
[511,498,551,0,499,516,513,515],
[540,517,536,502,0,514,514,481],
[513,483,529,485,487,0,527,489],
[504,459,492,488,487,474,0,480],
[533,494,512,486,520,512,521,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 34, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,479,459,498,484,474,486,467],
[522,0,499,507,510,501,508,497],
[542,502,0,507,532,488,526,514],
[503,494,494,0,513,505,496,485],
[517,491,469,488,0,481,478,496],
[527,500,513,496,520,0,532,504],
[515,493,475,505,523,469,0,487],
[534,504,487,516,505,497,514,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 35, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,518,481,504,493,513,506,499],
[483,0,489,456,493,490,493,499],
[520,512,0,504,488,471,499,488],
[497,545,497,0,501,503,517,514],
[508,508,513,500,0,474,523,514],
[488,511,530,498,527,0,508,522],
[495,508,502,484,478,493,0,496],
[502,502,513,487,487,479,505,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 36, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,485,542,456,489,528,516,526],
[516,0,535,492,492,517,499,548],
[459,466,0,446,470,483,478,476],
[545,509,555,0,504,542,490,543],
[512,509,531,497,0,509,488,553],
[473,484,518,459,492,0,511,530],
[485,502,523,511,513,490,0,522],
[475,453,525,458,448,471,479,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 37, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,471,515,498,527,485,478,488],
[530,0,499,501,538,516,516,497],
[486,502,0,476,525,497,472,488],
[503,500,525,0,530,508,502,504],
[474,463,476,471,0,479,469,471],
[516,485,504,493,522,0,483,500],
[523,485,529,499,532,518,0,500],
[513,504,513,497,530,501,501,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 38, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,484,509,502,500,530,515,506],
[517,0,494,460,488,522,502,515],
[492,507,0,507,501,500,525,539],
[499,541,494,0,487,498,520,512],
[501,513,500,514,0,516,530,510],
[471,479,501,503,485,0,501,513],
[486,499,476,481,471,500,0,503],
[495,486,462,489,491,488,498,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 39, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,509,565,524,487,442,440,515],
[492,0,590,519,567,483,448,581],
[436,411,0,467,496,431,397,485],
[477,482,534,0,467,466,398,468],
[514,434,505,534,0,463,449,519],
[559,518,570,535,538,0,514,479],
[561,553,604,603,552,487,0,562],
[486,420,516,533,482,522,439,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 40, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,497,563,487,464,523,510,520],
[504,0,504,446,521,509,455,467],
[438,497,0,513,538,498,478,487],
[514,555,488,0,516,520,463,522],
[537,480,463,485,0,477,492,513],
[478,492,503,481,524,0,486,497],
[491,546,523,538,509,515,0,499],
[481,534,514,479,488,504,502,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 41, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,504,524,521,495,510,511,524],
[497,0,526,499,517,481,518,498],
[477,475,0,493,509,507,482,496],
[480,502,508,0,492,510,498,509],
[506,484,492,509,0,516,513,496],
[491,520,494,491,485,0,481,486],
[490,483,519,503,488,520,0,521],
[477,503,505,492,505,515,480,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 42, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,597,490,571,568,526,577,524],
[404,0,454,459,465,475,497,457],
[511,547,0,580,496,534,572,534],
[430,542,421,0,473,553,558,506],
[433,536,505,528,0,482,587,547],
[475,526,467,448,519,0,564,529],
[424,504,429,443,414,437,0,470],
[477,544,467,495,454,472,531,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 43, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,482,490,554,470,441,445,487],
[519,0,514,567,557,498,549,552],
[511,487,0,563,572,524,499,534],
[447,434,438,0,449,492,447,442],
[531,444,429,552,0,478,496,488],
[560,503,477,509,523,0,538,530],
[556,452,502,554,505,463,0,479],
[514,449,467,559,513,471,522,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 44, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,509,493,525,538,475,519,513],
[492,0,494,517,535,508,470,499],
[508,507,0,497,547,486,511,538],
[476,484,504,0,491,466,494,502],
[463,466,454,510,0,476,455,470],
[526,493,515,535,525,0,509,541],
[482,531,490,507,546,492,0,493],
[488,502,463,499,531,460,508,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 45, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,543,587,475,605,535,432,544],
[458,0,468,408,441,411,427,459],
[414,533,0,444,480,433,493,457],
[526,593,557,0,513,561,424,567],
[396,560,521,488,0,428,427,435],
[466,590,568,440,573,0,505,505],
[569,574,508,577,574,496,0,537],
[457,542,544,434,566,496,464,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 46, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,491,502,482,500,487,488,478],
[510,0,541,512,545,497,509,502],
[499,460,0,465,492,491,477,491],
[519,489,536,0,520,507,494,516],
[501,456,509,481,0,473,493,467],
[514,504,510,494,528,0,515,490],
[513,492,524,507,508,486,0,494],
[523,499,510,485,534,511,507,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 47, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,493,479,475,493,474,492,492],
[508,0,503,518,521,491,520,532],
[522,498,0,502,474,474,492,515],
[526,483,499,0,504,478,499,507],
[508,480,527,497,0,502,513,502],
[527,510,527,523,499,0,511,505],
[509,481,509,502,488,490,0,488],
[509,469,486,494,499,496,513,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 48, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,484,509,529,513,528,507,492],
[517,0,495,515,511,531,510,517],
[492,506,0,521,495,515,523,503],
[472,486,480,0,506,512,493,487],
[488,490,506,495,0,516,507,483],
[473,470,486,489,485,0,475,482],
[494,491,478,508,494,526,0,477],
[509,484,498,514,518,519,524,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 49, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,492,552,418,534,525,542,469],
[509,0,576,520,494,507,474,497],
[449,425,0,468,424,421,468,487],
[583,481,533,0,472,527,425,540],
[467,507,577,529,0,499,510,503],
[476,494,580,474,502,0,503,455],
[459,527,533,576,491,498,0,466],
[532,504,514,461,498,546,535,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 50, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,490,512,480,461,489,479,499],
[511,0,504,497,508,506,506,548],
[489,497,0,496,464,520,503,541],
[521,504,505,0,506,495,503,518],
[540,493,537,495,0,532,502,541],
[512,495,481,506,469,0,484,495],
[522,495,498,498,499,517,0,512],
[502,453,460,483,460,506,489,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 51, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,489,520,506,486,520,533,532],
[512,0,515,492,512,547,544,536],
[481,486,0,490,474,520,514,501],
[495,509,511,0,474,519,544,528],
[515,489,527,527,0,551,545,549],
[481,454,481,482,450,0,510,475],
[468,457,487,457,456,491,0,481],
[469,465,500,473,452,526,520,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 52, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,514,539,536,498,510,523,511],
[487,0,519,523,478,511,507,480],
[462,482,0,533,487,482,515,501],
[465,478,468,0,470,478,486,480],
[503,523,514,531,0,494,527,527],
[491,490,519,523,507,0,514,480],
[478,494,486,515,474,487,0,475],
[490,521,500,521,474,521,526,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 53, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,476,441,476,477,456,462,475],
[525,0,489,504,527,501,508,496],
[560,512,0,468,510,486,478,516],
[525,497,533,0,518,528,534,502],
[524,474,491,483,0,474,474,502],
[545,500,515,473,527,0,456,480],
[539,493,523,467,527,545,0,509],
[526,505,485,499,499,521,492,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 54, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,497,494,521,509,561,541,525],
[504,0,530,477,497,520,491,521],
[507,471,0,436,455,469,490,483],
[480,524,565,0,518,530,530,528],
[492,504,546,483,0,516,541,504],
[440,481,532,471,485,0,461,520],
[460,510,511,471,460,540,0,523],
[476,480,518,473,497,481,478,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 55, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,500,539,510,499,504,495,483],
[501,0,539,513,485,499,505,511],
[462,462,0,510,458,483,479,479],
[491,488,491,0,485,481,488,481],
[502,516,543,516,0,511,476,493],
[497,502,518,520,490,0,503,506],
[506,496,522,513,525,498,0,488],
[518,490,522,520,508,495,513,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 56, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,485,493,483,508,502,484,486],
[516,0,513,504,489,522,471,497],
[508,488,0,490,499,515,506,506],
[518,497,511,0,501,515,495,492],
[493,512,502,500,0,501,487,487],
[499,479,486,486,500,0,493,509],
[517,530,495,506,514,508,0,502],
[515,504,495,509,514,492,499,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 57, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,516,523,523,510,475,529,485],
[485,0,492,537,507,450,509,492],
[478,509,0,529,487,492,476,500],
[478,464,472,0,509,490,466,473],
[491,494,514,492,0,474,483,474],
[526,551,509,511,527,0,510,499],
[472,492,525,535,518,491,0,506],
[516,509,501,528,527,502,495,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 58, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,379,531,376,531,725,546,531],
[622,0,686,413,367,1001,382,261],
[470,315,0,251,406,655,315,385],
[625,588,750,0,264,977,670,431],
[470,634,595,737,0,846,716,455],
[276,0,346,24,155,0,82,191],
[455,619,686,331,285,919,0,416],
[470,740,616,570,546,810,585,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 59, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,506,493,502,531,529,508,516],
[495,0,507,484,502,513,527,515],
[508,494,0,464,511,508,502,495],
[499,517,537,0,505,507,509,525],
[470,499,490,496,0,503,488,485],
[472,488,493,494,498,0,513,486],
[493,474,499,492,513,488,0,526],
[485,486,506,476,516,515,475,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 60, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,477,524,523,506,516,513,514],
[524,0,529,556,569,485,518,541],
[477,472,0,540,520,493,502,510],
[478,445,461,0,486,500,492,494],
[495,432,481,515,0,478,509,500],
[485,516,508,501,523,0,484,561],
[488,483,499,509,492,517,0,497],
[487,460,491,507,501,440,504,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 61, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,564,525,552,479,535,514,544],
[437,0,531,474,488,513,506,584],
[476,470,0,470,521,503,489,499],
[449,527,531,0,505,555,578,488],
[522,513,480,496,0,566,506,552],
[466,488,498,446,435,0,462,507],
[487,495,512,423,495,539,0,516],
[457,417,502,513,449,494,485,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 62, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,500,517,517,498,501,532,511],
[501,0,520,500,493,459,523,489],
[484,481,0,506,500,498,500,473],
[484,501,495,0,472,506,500,486],
[503,508,501,529,0,508,509,482],
[500,542,503,495,493,0,529,497],
[469,478,501,501,492,472,0,471],
[490,512,528,515,519,504,530,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 63, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,489,497,517,489,516,510,510],
[512,0,504,484,508,513,540,517],
[504,497,0,497,508,522,531,507],
[484,517,504,0,513,496,534,505],
[512,493,493,488,0,500,537,486],
[485,488,479,505,501,0,517,516],
[491,461,470,467,464,484,0,491],
[491,484,494,496,515,485,510,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 64, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,555,531,552,531,443,546,498],
[446,0,466,509,522,522,467,459],
[470,535,0,463,575,503,518,452],
[449,492,538,0,603,463,500,501],
[470,479,426,398,0,465,419,466],
[558,479,498,538,536,0,537,502],
[455,534,483,501,582,464,0,419],
[503,542,549,500,535,499,582,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 65, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,486,475,512,487,492,497,498],
[515,0,532,499,503,500,526,470],
[526,469,0,527,526,519,520,493],
[489,502,474,0,468,504,510,509],
[514,498,475,533,0,526,493,501],
[509,501,482,497,475,0,523,508],
[504,475,481,491,508,478,0,521],
[503,531,508,492,500,493,480,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 66, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,526,517,427,567,468,382,500],
[475,0,576,503,542,503,468,569],
[484,425,0,420,450,388,433,481],
[574,498,581,0,515,475,487,579],
[434,459,551,486,0,408,396,462],
[533,498,613,526,593,0,530,630],
[619,533,568,514,605,471,0,567],
[501,432,520,422,539,371,434,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 67, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,520,522,501,505,493,514,517],
[481,0,502,459,507,496,493,523],
[479,499,0,463,499,489,498,515],
[500,542,538,0,516,520,520,510],
[496,494,502,485,0,460,493,519],
[508,505,512,481,541,0,521,521],
[487,508,503,481,508,480,0,540],
[484,478,486,491,482,480,461,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 68, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,525,503,519,497,490,482,481],
[476,0,498,515,517,519,508,500],
[498,503,0,505,503,494,508,494],
[482,486,496,0,510,483,504,481],
[504,484,498,491,0,476,524,509],
[511,482,507,518,525,0,518,480],
[519,493,493,497,477,483,0,459],
[520,501,507,520,492,521,542,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 69, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,490,516,520,508,528,526,535],
[511,0,466,506,495,528,476,501],
[485,535,0,512,500,527,502,525],
[481,495,489,0,498,542,515,492],
[493,506,501,503,0,531,500,474],
[473,473,474,459,470,0,493,460],
[475,525,499,486,501,508,0,505],
[466,500,476,509,527,541,496,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 70, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,514,533,491,486,529,517,537],
[487,0,515,520,494,516,529,506],
[468,486,0,514,508,532,510,505],
[510,481,487,0,501,525,514,522],
[515,507,493,500,0,528,509,520],
[472,485,469,476,473,0,503,478],
[484,472,491,487,492,498,0,475],
[464,495,496,479,481,523,526,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 71, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,480,503,512,472,511,495,503],
[521,0,524,500,534,520,537,535],
[498,477,0,512,489,504,490,509],
[489,501,489,0,467,492,506,469],
[529,467,512,534,0,528,503,508],
[490,481,497,509,473,0,491,516],
[506,464,511,495,498,510,0,505],
[498,466,492,532,493,485,496,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 72, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,536,563,510,495,513,457,580],
[465,0,513,554,540,563,484,506],
[438,488,0,488,514,474,390,477],
[491,447,513,0,464,461,488,488],
[506,461,487,537,0,479,488,487],
[488,438,527,540,522,0,486,466],
[544,517,611,513,513,515,0,470],
[421,495,524,513,514,535,531,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 73, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,510,545,497,512,488,501,571],
[491,0,521,468,509,489,476,560],
[456,480,0,489,483,488,492,510],
[504,533,512,0,548,491,511,573],
[489,492,518,453,0,516,518,521],
[513,512,513,510,485,0,495,559],
[500,525,509,490,483,506,0,551],
[430,441,491,428,480,442,450,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 74, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,497,519,499,505,501,498,527],
[504,0,485,460,484,479,495,510],
[482,516,0,479,524,502,489,512],
[502,541,522,0,513,491,502,516],
[496,517,477,488,0,491,501,513],
[500,522,499,510,510,0,505,533],
[503,506,512,499,500,496,0,533],
[474,491,489,485,488,468,468,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 75, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,501,489,497,494,492,495,487],
[500,0,493,515,500,498,501,504],
[512,508,0,523,502,511,498,503],
[504,486,478,0,491,484,488,484],
[507,501,499,510,0,505,512,512],
[509,503,490,517,496,0,516,477],
[506,500,503,513,489,485,0,508],
[514,497,498,517,489,524,493,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 76, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,489,505,493,523,487,504,498],
[512,0,494,503,539,506,528,511],
[496,507,0,514,503,490,497,469],
[508,498,487,0,536,505,512,524],
[478,462,498,465,0,495,500,492],
[514,495,511,496,506,0,516,514],
[497,473,504,489,501,485,0,487],
[503,490,532,477,509,487,514,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 77, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,516,514,486,524,495,530,511],
[485,0,493,476,509,480,504,508],
[487,508,0,509,505,498,511,492],
[515,525,492,0,533,514,537,523],
[477,492,496,468,0,460,485,492],
[506,521,503,487,541,0,530,523],
[471,497,490,464,516,471,0,513],
[490,493,509,478,509,478,488,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 78, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,504,511,507,501,474,519,487],
[497,0,500,460,502,484,494,508],
[490,501,0,463,535,512,495,493],
[494,541,538,0,539,513,544,542],
[500,499,466,462,0,501,512,488],
[527,517,489,488,500,0,549,488],
[482,507,506,457,489,452,0,494],
[514,493,508,459,513,513,507,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 79, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,469,512,514,507,552,520,483],
[532,0,518,491,481,520,529,507],
[489,483,0,498,484,527,508,480],
[487,510,503,0,480,533,531,486],
[494,520,517,521,0,520,546,512],
[449,481,474,468,481,0,486,481],
[481,472,493,470,455,515,0,477],
[518,494,521,515,489,520,524,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 80, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,503,499,514,525,539,493,547],
[498,0,487,510,508,533,482,526],
[502,514,0,503,486,526,501,525],
[487,491,498,0,499,510,526,508],
[476,493,515,502,0,514,494,521],
[462,468,475,491,487,0,483,500],
[508,519,500,475,507,518,0,519],
[454,475,476,493,480,501,482,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 81, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,500,509,497,476,523,493,501],
[501,0,504,515,500,504,495,493],
[492,497,0,507,507,524,532,493],
[504,486,494,0,500,513,479,486],
[525,501,494,501,0,504,486,436],
[478,497,477,488,497,0,486,482],
[508,506,469,522,515,515,0,482],
[500,508,508,515,565,519,519,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 82, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,467,535,535,468,542,515,529],
[534,0,543,559,506,562,510,496],
[466,458,0,511,469,536,500,461],
[466,442,490,0,452,462,483,459],
[533,495,532,549,0,518,514,504],
[459,439,465,539,483,0,494,466],
[486,491,501,518,487,507,0,505],
[472,505,540,542,497,535,496,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 83, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,530,514,489,478,497,512,535],
[471,0,491,473,479,511,484,531],
[487,510,0,487,472,511,494,507],
[512,528,514,0,509,493,481,548],
[523,522,529,492,0,517,495,530],
[504,490,490,508,484,0,483,546],
[489,517,507,520,506,518,0,558],
[466,470,494,453,471,455,443,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 84, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,541,537,489,522,543,541,549],
[460,0,484,502,510,491,503,506],
[464,517,0,468,513,485,501,518],
[512,499,533,0,501,507,520,545],
[479,491,488,500,0,511,506,519],
[458,510,516,494,490,0,503,503],
[460,498,500,481,495,498,0,514],
[452,495,483,456,482,498,487,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 85, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,491,531,456,463,460,461,497],
[510,0,529,493,470,494,490,458],
[470,472,0,461,471,495,464,518],
[545,508,540,0,464,513,553,555],
[538,531,530,537,0,486,576,496],
[541,507,506,488,515,0,476,583],
[540,511,537,448,425,525,0,563],
[504,543,483,446,505,418,438,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 86, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,506,478,508,523,525,504,529],
[495,0,544,515,522,525,499,519],
[523,457,0,518,522,509,450,538],
[493,486,483,0,531,523,490,541],
[478,479,479,470,0,483,466,524],
[476,476,492,478,518,0,491,523],
[497,502,551,511,535,510,0,506],
[472,482,463,460,477,478,495,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 87, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,507,493,523,482,498,511,530],
[494,0,479,481,506,496,503,508],
[508,522,0,510,503,479,505,507],
[478,520,491,0,481,504,509,514],
[519,495,498,520,0,482,529,507],
[503,505,522,497,519,0,528,508],
[490,498,496,492,472,473,0,481],
[471,493,494,487,494,493,520,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 88, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,542,175,752,616,521,542,385],
[459,0,547,980,757,519,694,613],
[826,454,0,826,757,509,540,836],
[249,21,175,0,548,443,327,406],
[385,244,244,453,0,223,474,309],
[480,482,492,558,778,0,471,492],
[459,307,461,674,527,530,0,461],
[616,388,165,595,692,509,540,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 89, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,512,445,508,625,514,502,456],
[489,0,380,440,523,384,540,483],
[556,621,0,484,573,539,778,555],
[493,561,517,0,479,323,524,477],
[376,478,428,522,0,378,496,441],
[487,617,462,678,623,0,478,493],
[499,461,223,477,505,523,0,310],
[545,518,446,524,560,508,691,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 90, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,520,478,459,484,495,502,509],
[481,0,436,481,465,495,496,474],
[523,565,0,492,485,502,493,503],
[542,520,509,0,501,513,503,492],
[517,536,516,500,0,499,526,512],
[506,506,499,488,502,0,510,494],
[499,505,508,498,475,491,0,494],
[492,527,498,509,489,507,507,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 91, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,509,505,487,493,513,519,513],
[492,0,498,495,486,494,494,500],
[496,503,0,516,512,495,516,503],
[514,506,485,0,503,499,508,514],
[508,515,489,498,0,487,512,494],
[488,507,506,502,514,0,468,523],
[482,507,485,493,489,533,0,499],
[488,501,498,487,507,478,502,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 92, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,478,457,481,472,488,491,440],
[523,0,473,493,487,500,497,501],
[544,528,0,509,493,501,482,476],
[520,508,492,0,510,489,456,476],
[529,514,508,491,0,499,497,481],
[513,501,500,512,502,0,522,475],
[510,504,519,545,504,479,0,475],
[561,500,525,525,520,526,526,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 93, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,478,498,490,498,530,487,499],
[523,0,498,535,505,518,490,490],
[503,503,0,503,513,534,493,506],
[511,466,498,0,534,525,505,507],
[503,496,488,467,0,523,488,498],
[471,483,467,476,478,0,473,476],
[514,511,508,496,513,528,0,514],
[502,511,495,494,503,525,487,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 94, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,489,485,495,480,501,488,513],
[512,0,503,505,504,482,513,522],
[516,498,0,500,498,521,517,525],
[506,496,501,0,504,481,500,523],
[521,497,503,497,0,491,498,512],
[500,519,480,520,510,0,516,514],
[513,488,484,501,503,485,0,518],
[488,479,476,478,489,487,483,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 95, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,510,494,474,474,530,507,506],
[491,0,458,465,474,513,488,496],
[507,543,0,512,492,538,505,496],
[527,536,489,0,509,558,517,516],
[527,527,509,492,0,538,507,530],
[471,488,463,443,463,0,488,496],
[494,513,496,484,494,513,0,506],
[495,505,505,485,471,505,495,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 96, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,484,524,478,499,526,511,515],
[517,0,523,496,516,509,503,520],
[477,478,0,466,488,476,506,482],
[523,505,535,0,479,507,494,516],
[502,485,513,522,0,538,528,484],
[475,492,525,494,463,0,510,502],
[490,498,495,507,473,491,0,494],
[486,481,519,485,517,499,507,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 97, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,510,499,528,480,473,492,475],
[491,0,499,519,516,491,521,497],
[502,502,0,490,506,522,484,493],
[473,482,511,0,476,477,497,458],
[521,485,495,525,0,482,529,497],
[528,510,479,524,519,0,500,535],
[509,480,517,504,472,501,0,493],
[526,504,508,543,504,466,508,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 98, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,600,546,556,577,540,498,582],
[401,0,432,335,443,477,514,671],
[455,569,0,402,385,504,383,590],
[445,666,599,0,563,529,463,553],
[424,558,616,438,0,321,364,475],
[461,524,497,472,680,0,453,513],
[503,487,618,538,637,548,0,625],
[419,330,411,448,526,488,376,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 99, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,477,503,478,493,490,483,440],
[524,0,507,491,552,508,514,488],
[498,494,0,466,450,487,481,445],
[523,510,535,0,543,522,488,501],
[508,449,551,458,0,518,479,449],
[511,493,514,479,483,0,479,492],
[518,487,520,513,522,522,0,468],
[561,513,556,500,552,509,533,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 100, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,502,509,522,505,526,473,503],
[499,0,514,514,541,487,484,497],
[492,487,0,513,514,531,511,537],
[479,487,488,0,479,527,474,515],
[496,460,487,522,0,509,459,523],
[475,514,470,474,492,0,482,520],
[528,517,490,527,542,519,0,526],
[498,504,464,486,478,481,475,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 101, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,503,549,495,494,522,493,503],
[498,0,472,474,493,462,484,475],
[452,529,0,446,458,463,473,469],
[506,527,555,0,512,489,478,506],
[507,508,543,489,0,488,477,492],
[479,539,538,512,513,0,499,501],
[508,517,528,523,524,502,0,482],
[498,526,532,495,509,500,519,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 102, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,529,487,540,475,492,473,582],
[472,0,538,585,456,499,480,498],
[514,463,0,473,426,449,430,416],
[461,416,528,0,429,432,433,440],
[526,545,575,572,0,537,510,471],
[509,502,552,569,464,0,532,542],
[528,521,571,568,491,469,0,565],
[419,503,585,561,530,459,436,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 103, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,458,463,471,480,531,536,539],
[543,0,461,488,516,493,484,528],
[538,540,0,490,525,540,554,512],
[530,513,511,0,520,497,492,504],
[521,485,476,481,0,475,481,514],
[470,508,461,504,526,0,515,512],
[465,517,447,509,520,486,0,513],
[462,473,489,497,487,489,488,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 104, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,494,496,475,486,495,506,515],
[507,0,505,507,490,505,500,496],
[505,496,0,512,506,501,516,516],
[526,494,489,0,492,510,522,523],
[515,511,495,509,0,486,508,500],
[506,496,500,491,515,0,480,486],
[495,501,485,479,493,521,0,495],
[486,505,485,478,501,515,506,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 105, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,544,531,520,516,502,477,506],
[457,0,482,448,479,478,457,474],
[470,519,0,505,532,493,462,514],
[481,553,496,0,521,507,502,497],
[485,522,469,480,0,448,488,478],
[499,523,508,494,553,0,481,493],
[524,544,539,499,513,520,0,543],
[495,527,487,504,523,508,458,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 106, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,484,497,484,509,501,479,506],
[517,0,518,507,496,515,482,529],
[504,483,0,502,497,508,487,505],
[517,494,499,0,512,489,503,510],
[492,505,504,489,0,477,487,521],
[500,486,493,512,524,0,478,503],
[522,519,514,498,514,523,0,518],
[495,472,496,491,480,498,483,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 107, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,490,509,499,502,479,491,504],
[511,0,509,515,485,516,507,495],
[492,492,0,508,491,491,501,478],
[502,486,493,0,483,495,496,485],
[499,516,510,518,0,509,499,495],
[522,485,510,506,492,0,502,482],
[510,494,500,505,502,499,0,508],
[497,506,523,516,506,519,493,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 108, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,547,466,549,543,558,452,509],
[454,0,479,545,523,575,536,534],
[535,522,0,529,525,606,508,500],
[452,456,472,0,488,547,475,459],
[458,478,476,513,0,531,476,428],
[443,426,395,454,470,0,468,476],
[549,465,493,526,525,533,0,485],
[492,467,501,542,573,525,516,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 109, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,459,515,507,439,470,506,469],
[542,0,535,526,477,523,512,510],
[486,466,0,518,451,482,552,480],
[494,475,483,0,463,480,513,494],
[562,524,550,538,0,550,513,480],
[531,478,519,521,451,0,526,478],
[495,489,449,488,488,475,0,482],
[532,491,521,507,521,523,519,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 110, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,522,512,485,509,512,502,502],
[479,0,468,463,474,487,452,464],
[489,533,0,484,502,524,491,485],
[516,538,517,0,496,534,491,529],
[492,527,499,505,0,521,488,494],
[489,514,477,467,480,0,472,493],
[499,549,510,510,513,529,0,503],
[499,537,516,472,507,508,498,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 111, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,529,498,513,501,531,530,502],
[472,0,488,476,478,509,498,483],
[503,513,0,512,501,510,514,499],
[488,525,489,0,507,521,524,493],
[500,523,500,494,0,536,522,522],
[470,492,491,480,465,0,487,479],
[471,503,487,477,479,514,0,476],
[499,518,502,508,479,522,525,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 112, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,486,483,472,495,504,484,488],
[515,0,504,523,503,525,497,504],
[518,497,0,494,511,498,499,491],
[529,478,507,0,512,503,504,500],
[506,498,490,489,0,503,488,495],
[497,476,503,498,498,0,483,480],
[517,504,502,497,513,518,0,492],
[513,497,510,501,506,521,509,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 113, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,496,500,490,519,513,506,495],
[505,0,474,501,501,480,488,486],
[501,527,0,496,500,506,496,504],
[511,500,505,0,511,493,511,517],
[482,500,501,490,0,493,510,485],
[488,521,495,508,508,0,523,504],
[495,513,505,490,491,478,0,484],
[506,515,497,484,516,497,517,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 114, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,497,529,534,509,497,488,478],
[504,0,510,488,495,489,479,493],
[472,491,0,487,485,494,498,482],
[467,513,514,0,482,490,479,463],
[492,506,516,519,0,518,513,489],
[504,512,507,511,483,0,501,478],
[513,522,503,522,488,500,0,510],
[523,508,519,538,512,523,491,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 115, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,508,483,499,503,478,473,495],
[493,0,502,485,486,492,486,477],
[518,499,0,511,481,492,496,502],
[502,516,490,0,485,474,484,503],
[498,515,520,516,0,508,494,495],
[523,509,509,527,493,0,501,515],
[528,515,505,517,507,500,0,497],
[506,524,499,498,506,486,504,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 116, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,508,475,526,533,601,504,545],
[493,0,450,456,493,578,446,416],
[526,551,0,599,530,509,492,451],
[475,545,402,0,482,473,493,388],
[468,508,471,519,0,528,439,473],
[400,423,492,528,473,0,356,356],
[497,555,509,508,562,645,0,556],
[456,585,550,613,528,645,445,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 117, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,522,516,496,539,537,513,571],
[479,0,476,501,493,520,510,520],
[485,525,0,515,523,534,503,566],
[505,500,486,0,547,500,520,562],
[462,508,478,454,0,475,522,506],
[464,481,467,501,526,0,511,530],
[488,491,498,481,479,490,0,527],
[430,481,435,439,495,471,474,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 118, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,498,535,547,512,507,558,495],
[503,0,533,537,525,510,512,491],
[466,468,0,506,494,477,473,462],
[454,464,495,0,501,475,507,456],
[489,476,507,500,0,495,501,451],
[494,491,524,526,506,0,530,504],
[443,489,528,494,500,471,0,458],
[506,510,539,545,550,497,543,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 119, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,464,503,510,493,511,483,489],
[537,0,536,554,499,494,495,501],
[498,465,0,546,482,515,492,491],
[491,447,455,0,451,457,483,463],
[508,502,519,550,0,506,520,468],
[490,507,486,544,495,0,488,461],
[518,506,509,518,481,513,0,483],
[512,500,510,538,533,540,518,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 120, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,366,536,450,553,489,403,436],
[635,0,540,523,529,469,422,467],
[465,461,0,484,381,399,419,528],
[551,478,517,0,568,498,532,507],
[448,472,620,433,0,522,403,479],
[512,532,602,503,479,0,369,444],
[598,579,582,469,598,632,0,517],
[565,534,473,494,522,557,484,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 121, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,450,371,597,318,429,376,477],
[551,0,487,539,407,264,487,568],
[630,514,0,751,595,502,457,509],
[404,462,250,0,338,358,256,459],
[683,594,406,663,0,492,479,584],
[572,737,499,643,509,0,623,625],
[625,514,544,745,522,378,0,634],
[524,433,492,542,417,376,367,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 122, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,545,524,499,516,492,485,466],
[456,0,509,472,531,485,480,465],
[477,492,0,471,455,458,502,484],
[502,529,530,0,504,518,512,484],
[485,470,546,497,0,491,500,458],
[509,516,543,483,510,0,523,493],
[516,521,499,489,501,478,0,504],
[535,536,517,517,543,508,497,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 123, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,512,494,500,517,506,508,495],
[489,0,486,503,521,501,495,506],
[507,515,0,487,519,512,505,513],
[501,498,514,0,523,508,502,532],
[484,480,482,478,0,502,472,491],
[495,500,489,493,499,0,498,508],
[493,506,496,499,529,503,0,491],
[506,495,488,469,510,493,510,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 124, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,500,495,475,521,510,484,484],
[501,0,487,476,504,486,481,472],
[506,514,0,496,528,494,505,508],
[526,525,505,0,545,523,481,511],
[480,497,473,456,0,502,481,468],
[491,515,507,478,499,0,494,490],
[517,520,496,520,520,507,0,503],
[517,529,493,490,533,511,498,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 125, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,515,483,494,512,496,493,480],
[486,0,501,503,531,495,512,496],
[518,500,0,525,551,520,540,505],
[507,498,476,0,518,491,501,472],
[489,470,450,483,0,473,497,454],
[505,506,481,510,528,0,514,485],
[508,489,461,500,504,487,0,463],
[521,505,496,529,547,516,538,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 126, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,475,514,480,497,478,489,496],
[526,0,512,527,524,495,514,518],
[487,489,0,506,507,490,498,492],
[521,474,495,0,509,517,495,503],
[504,477,494,492,0,495,498,489],
[523,506,511,484,506,0,492,501],
[512,487,503,506,503,509,0,516],
[505,483,509,498,512,500,485,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 127, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,461,539,495,495,484,472,466],
[540,0,547,489,562,537,533,502],
[462,454,0,457,511,444,436,482],
[506,512,544,0,501,475,521,467],
[506,439,490,500,0,509,479,444],
[517,464,557,526,492,0,435,480],
[529,468,565,480,522,566,0,483],
[535,499,519,534,557,521,518,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 128, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,467,463,478,459,456,479,504],
[534,0,499,474,539,541,476,497],
[538,502,0,445,498,536,485,476],
[523,527,556,0,485,548,502,551],
[542,462,503,516,0,521,493,493],
[545,460,465,453,480,0,485,453],
[522,525,516,499,508,516,0,499],
[497,504,525,450,508,548,502,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 129, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,509,509,486,523,501,506,518],
[492,0,471,505,532,489,548,486],
[492,530,0,524,558,515,566,529],
[515,496,477,0,583,514,571,535],
[478,469,443,418,0,477,515,475],
[500,512,486,487,524,0,559,524],
[495,453,435,430,486,442,0,454],
[483,515,472,466,526,477,547,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 130, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,524,507,530,479,541,512,561],
[477,0,549,503,492,542,522,537],
[494,452,0,468,453,496,482,533],
[471,498,533,0,488,538,530,525],
[522,509,548,513,0,533,481,504],
[460,459,505,463,468,0,462,501],
[489,479,519,471,520,539,0,534],
[440,464,468,476,497,500,467,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 131, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,525,523,516,507,499,513,523],
[476,0,514,501,471,505,505,497],
[478,487,0,512,476,491,475,487],
[485,500,489,0,491,486,487,508],
[494,530,525,510,0,531,512,496],
[502,496,510,515,470,0,524,477],
[488,496,526,514,489,477,0,522],
[478,504,514,493,505,524,479,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 132, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,483,489,458,509,499,502,488],
[518,0,438,558,561,549,446,471],
[512,563,0,459,564,544,435,533],
[543,443,542,0,527,513,458,520],
[492,440,437,474,0,508,426,516],
[502,452,457,488,493,0,421,502],
[499,555,566,543,575,580,0,557],
[513,530,468,481,485,499,444,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 133, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,495,490,502,477,472,490,474],
[506,0,533,521,522,535,507,499],
[511,468,0,521,495,489,474,486],
[499,480,480,0,492,512,477,511],
[524,479,506,509,0,529,517,496],
[529,466,512,489,472,0,489,475],
[511,494,527,524,484,512,0,517],
[527,502,515,490,505,526,484,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 134, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,460,474,475,488,506,451,477],
[541,0,498,497,515,493,482,486],
[527,503,0,514,523,524,501,498],
[526,504,487,0,514,507,466,468],
[513,486,478,487,0,490,481,487],
[495,508,477,494,511,0,506,505],
[550,519,500,535,520,495,0,484],
[524,515,503,533,514,496,517,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 135, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,567,475,382,544,575,474,461],
[434,0,358,458,497,494,496,413],
[526,643,0,473,541,563,504,493],
[619,543,528,0,576,532,558,498],
[457,504,460,425,0,455,481,414],
[426,507,438,469,546,0,473,463],
[527,505,497,443,520,528,0,518],
[540,588,508,503,587,538,483,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 136, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,474,498,495,483,518,467,508],
[527,0,507,506,511,533,490,524],
[503,494,0,508,457,494,476,537],
[506,495,493,0,468,505,480,536],
[518,490,544,533,0,550,526,540],
[483,468,507,496,451,0,467,520],
[534,511,525,521,475,534,0,547],
[493,477,464,465,461,481,454,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 137, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,499,482,497,473,458,494,494],
[502,0,483,496,462,497,504,495],
[519,518,0,507,486,487,479,511],
[504,505,494,0,476,484,469,517],
[528,539,515,525,0,476,490,537],
[543,504,514,517,525,0,475,528],
[507,497,522,532,511,526,0,542],
[507,506,490,484,464,473,459,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 138, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,519,501,492,476,518,504,503],
[482,0,502,472,496,516,472,481],
[500,499,0,464,478,504,472,490],
[509,529,537,0,509,520,488,524],
[525,505,523,492,0,514,498,502],
[483,485,497,481,487,0,462,492],
[497,529,529,513,503,539,0,534],
[498,520,511,477,499,509,467,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 139, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,486,528,464,467,449,453,527],
[515,0,509,484,481,455,488,521],
[473,492,0,400,477,431,447,456],
[537,517,601,0,497,509,540,521],
[534,520,524,504,0,471,513,500],
[552,546,570,492,530,0,525,521],
[548,513,554,461,488,476,0,517],
[474,480,545,480,501,480,484,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 140, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,531,504,537,500,516,501,517],
[470,0,501,484,482,480,510,476],
[497,500,0,503,464,493,489,488],
[464,517,498,0,461,508,485,507],
[501,519,537,540,0,498,487,527],
[485,521,508,493,503,0,480,498],
[500,491,512,516,514,521,0,505],
[484,525,513,494,474,503,496,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 141, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,539,497,525,472,523,499,495],
[462,0,503,506,483,539,521,480],
[504,498,0,499,491,511,462,496],
[476,495,502,0,442,497,507,457],
[529,518,510,559,0,561,523,497],
[478,462,490,504,440,0,476,493],
[502,480,539,494,478,525,0,510],
[506,521,505,544,504,508,491,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 142, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,484,433,491,497,463,504,466],
[517,0,521,565,492,478,507,459],
[568,480,0,501,503,455,460,475],
[510,436,500,0,514,494,464,462],
[504,509,498,487,0,475,427,471],
[538,523,546,507,526,0,485,506],
[497,494,541,537,574,516,0,524],
[535,542,526,539,530,495,477,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 143, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,498,519,543,526,512,501,537],
[503,0,502,513,552,519,494,522],
[482,499,0,525,521,517,498,533],
[458,488,476,0,496,513,491,531],
[475,449,480,505,0,448,447,491],
[489,482,484,488,553,0,487,501],
[500,507,503,510,554,514,0,502],
[464,479,468,470,510,500,499,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 144, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,497,497,502,513,483,461,496],
[504,0,541,513,504,497,476,508],
[504,460,0,506,487,474,474,512],
[499,488,495,0,477,502,476,490],
[488,497,514,524,0,488,473,516],
[518,504,527,499,513,0,508,517],
[540,525,527,525,528,493,0,539],
[505,493,489,511,485,484,462,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 145, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,482,501,484,519,494,491,481],
[519,0,509,514,503,536,525,470],
[500,492,0,525,529,546,512,509],
[517,487,476,0,517,501,525,493],
[482,498,472,484,0,505,493,468],
[507,465,455,500,496,0,489,460],
[510,476,489,476,508,512,0,492],
[520,531,492,508,533,541,509,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 146, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,475,463,437,510,501,494,509],
[526,0,487,534,531,524,538,457],
[538,514,0,508,529,543,498,492],
[564,467,493,0,522,544,525,539],
[491,470,472,479,0,536,467,483],
[500,477,458,457,465,0,527,461],
[507,463,503,476,534,474,0,486],
[492,544,509,462,518,540,515,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 147, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,512,512,485,479,482,467,492],
[489,0,494,487,494,476,485,501],
[489,507,0,496,487,502,479,474],
[516,514,505,0,501,523,493,515],
[522,507,514,500,0,503,486,502],
[519,525,499,478,498,0,483,512],
[534,516,522,508,515,518,0,492],
[509,500,527,486,499,489,509,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 148, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,499,493,482,470,518,495,489],
[502,0,521,485,488,519,499,487],
[508,480,0,502,480,525,492,487],
[519,516,499,0,501,526,496,507],
[531,513,521,500,0,534,509,511],
[483,482,476,475,467,0,498,488],
[506,502,509,505,492,503,0,498],
[512,514,514,494,490,513,503,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 149, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,483,539,478,564,569,503,507],
[518,0,495,462,509,523,478,521],
[462,506,0,500,569,574,486,516],
[523,539,501,0,486,547,488,494],
[437,492,432,515,0,512,496,457],
[432,478,427,454,489,0,483,456],
[498,523,515,513,505,518,0,480],
[494,480,485,507,544,545,521,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 150, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,490,479,513,504,500,517,483],
[511,0,477,506,516,512,514,502],
[522,524,0,507,500,519,518,533],
[488,495,494,0,504,508,498,518],
[497,485,501,497,0,503,490,518],
[501,489,482,493,498,0,490,504],
[484,487,483,503,511,511,0,519],
[518,499,468,483,483,497,482,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 151, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,475,548,504,487,543,538,507],
[526,0,500,471,509,558,610,540],
[453,501,0,480,426,522,497,509],
[497,530,521,0,439,551,512,496],
[514,492,575,562,0,522,538,571],
[458,443,479,450,479,0,572,508],
[463,391,504,489,463,429,0,473],
[494,461,492,505,430,493,528,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 152, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,479,510,483,503,515,500,476],
[522,0,495,503,505,531,523,501],
[491,506,0,497,522,513,529,480],
[518,498,504,0,522,521,540,494],
[498,496,479,479,0,497,506,477],
[486,470,488,480,504,0,514,472],
[501,478,472,461,495,487,0,448],
[525,500,521,507,524,529,553,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 153, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,501,507,524,519,493,589,618],
[500,0,560,511,538,526,470,545],
[494,441,0,430,484,538,494,453],
[477,490,571,0,574,504,450,533],
[482,463,517,427,0,429,476,516],
[508,475,463,497,572,0,479,510],
[412,531,507,551,525,522,0,496],
[383,456,548,468,485,491,505,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 154, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,512,516,473,525,496,512,481],
[489,0,476,488,474,464,498,497],
[485,525,0,498,486,506,493,495],
[528,513,503,0,500,504,523,511],
[476,527,515,501,0,520,533,506],
[505,537,495,497,481,0,505,488],
[489,503,508,478,468,496,0,478],
[520,504,506,490,495,513,523,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 155, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,501,501,493,503,527,492,498],
[500,0,499,494,483,504,513,494],
[500,502,0,488,526,496,508,514],
[508,507,513,0,511,493,540,545],
[498,518,475,490,0,475,487,511],
[474,497,505,508,526,0,489,519],
[509,488,493,461,514,512,0,505],
[503,507,487,456,490,482,496,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 156, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,509,487,518,502,497,486,492],
[492,0,486,499,498,488,485,502],
[514,515,0,508,493,513,493,507],
[483,502,493,0,493,508,503,498],
[499,503,508,508,0,488,487,502],
[504,513,488,493,513,0,479,497],
[515,516,508,498,514,522,0,508],
[509,499,494,503,499,504,493,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 157, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,482,498,517,533,532,510,525],
[519,0,467,517,516,506,508,503],
[503,534,0,556,591,484,502,506],
[484,484,445,0,517,499,466,509],
[468,485,410,484,0,510,488,498],
[469,495,517,502,491,0,524,530],
[491,493,499,535,513,477,0,528],
[476,498,495,492,503,471,473,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 158, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,481,510,472,478,465,493,498],
[520,0,490,509,492,501,513,475],
[491,511,0,489,492,499,493,494],
[529,492,512,0,521,528,521,522],
[523,509,509,480,0,526,519,504],
[536,500,502,473,475,0,520,511],
[508,488,508,480,482,481,0,490],
[503,526,507,479,497,490,511,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 159, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,491,475,505,492,512,490,512],
[510,0,497,505,505,501,493,516],
[526,504,0,510,495,527,511,528],
[496,496,491,0,474,502,486,508],
[509,496,506,527,0,509,507,532],
[489,500,474,499,492,0,492,500],
[511,508,490,515,494,509,0,505],
[489,485,473,493,469,501,496,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 160, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,434,460,541,475,451,456,486],
[567,0,523,594,519,487,603,477],
[541,478,0,608,471,491,487,507],
[460,407,393,0,349,316,451,479],
[526,482,530,652,0,489,578,511],
[550,514,510,685,512,0,619,485],
[545,398,514,550,423,382,0,423],
[515,524,494,522,490,516,578,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 161, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,469,562,548,528,507,556,519],
[532,0,649,519,580,535,498,534],
[439,352,0,525,445,433,434,429],
[453,482,476,0,480,382,435,466],
[473,421,556,521,0,457,503,476],
[494,466,568,619,544,0,578,551],
[445,503,567,566,498,423,0,498],
[482,467,572,535,525,450,503,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 162, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,491,479,501,489,499,514,473],
[510,0,492,533,484,525,537,485],
[522,509,0,509,509,527,503,472],
[500,468,492,0,472,494,494,452],
[512,517,492,529,0,531,519,504],
[502,476,474,507,470,0,500,476],
[487,464,498,507,482,501,0,473],
[528,516,529,549,497,525,528,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 163, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,498,497,503,520,494,510,498],
[503,0,490,494,492,487,521,483],
[504,511,0,517,497,498,556,520],
[498,507,484,0,492,488,531,513],
[481,509,504,509,0,502,527,507],
[507,514,503,513,499,0,506,520],
[491,480,445,470,474,495,0,494],
[503,518,481,488,494,481,507,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 164, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,504,468,478,488,517,508,488],
[497,0,471,482,501,501,491,473],
[533,530,0,491,497,511,520,489],
[523,519,510,0,528,551,524,495],
[513,500,504,473,0,495,502,506],
[484,500,490,450,506,0,491,461],
[493,510,481,477,499,510,0,490],
[513,528,512,506,495,540,511,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 165, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,468,467,469,459,485,477,476],
[533,0,501,496,485,489,490,498],
[534,500,0,529,480,511,514,513],
[532,505,472,0,476,514,480,487],
[542,516,521,525,0,511,498,503],
[516,512,490,487,490,0,484,486],
[524,511,487,521,503,517,0,526],
[525,503,488,514,498,515,475,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 166, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,501,509,508,478,486,472,476],
[500,0,475,489,475,477,496,487],
[492,526,0,512,510,509,499,520],
[493,512,489,0,494,505,477,509],
[523,526,491,507,0,505,499,512],
[515,524,492,496,496,0,505,478],
[529,505,502,524,502,496,0,507],
[525,514,481,492,489,523,494,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 167, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,480,479,483,474,518,492,500],
[521,0,504,505,487,530,515,490],
[522,497,0,484,495,518,505,491],
[518,496,517,0,484,525,504,523],
[527,514,506,517,0,530,493,510],
[483,471,483,476,471,0,481,486],
[509,486,496,497,508,520,0,507],
[501,511,510,478,491,515,494,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 168, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,531,517,489,534,534,519,502],
[470,0,505,479,506,483,451,434],
[484,496,0,515,487,488,482,405],
[512,522,486,0,549,562,489,478],
[467,495,514,452,0,508,451,451],
[467,518,513,439,493,0,493,440],
[482,550,519,512,550,508,0,470],
[499,567,596,523,550,561,531,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 169, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,457,498,472,470,489,447,463],
[544,0,517,499,532,548,512,500],
[503,484,0,485,490,530,440,470],
[529,502,516,0,523,504,493,470],
[531,469,511,478,0,521,465,491],
[512,453,471,497,480,0,455,460],
[554,489,561,508,536,546,0,503],
[538,501,531,531,510,541,498,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 170, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,496,483,524,510,485,511,509],
[505,0,500,514,501,539,502,526],
[518,501,0,526,520,501,470,541],
[477,487,475,0,474,482,497,549],
[491,500,481,527,0,546,509,514],
[516,462,500,519,455,0,486,502],
[490,499,531,504,492,515,0,513],
[492,475,460,452,487,499,488,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 171, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,560,452,490,540,475,421,479],
[441,0,414,429,496,451,452,442],
[549,587,0,533,532,553,524,422],
[511,572,468,0,537,505,466,478],
[461,505,469,464,0,423,435,381],
[526,550,448,496,578,0,469,480],
[580,549,477,535,566,532,0,557],
[522,559,579,523,620,521,444,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 172, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,504,507,501,545,507,497,524],
[497,0,509,518,519,494,484,504],
[494,492,0,522,538,509,510,511],
[500,483,479,0,513,523,501,507],
[456,482,463,488,0,463,442,468],
[494,507,492,478,538,0,467,527],
[504,517,491,500,559,534,0,535],
[477,497,490,494,533,474,466,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 173, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,509,485,530,489,492,412,500],
[492,0,494,495,447,485,477,522],
[516,507,0,489,478,511,462,492],
[471,506,512,0,487,478,483,540],
[512,554,523,514,0,508,451,560],
[509,516,490,523,493,0,502,520],
[589,524,539,518,550,499,0,571],
[501,479,509,461,441,481,430,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 174, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,455,525,505,551,440,514,516],
[546,0,550,474,503,486,498,488],
[476,451,0,494,496,460,496,488],
[496,527,507,0,525,493,504,502],
[450,498,505,476,0,523,487,511],
[561,515,541,508,478,0,531,497],
[487,503,505,497,514,470,0,485],
[485,513,513,499,490,504,516,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 175, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,496,526,536,500,489,471,492],
[505,0,479,517,484,497,485,494],
[475,522,0,504,504,498,504,502],
[465,484,497,0,475,484,453,472],
[501,517,497,526,0,482,479,455],
[512,504,503,517,519,0,512,479],
[530,516,497,548,522,489,0,494],
[509,507,499,529,546,522,507,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 176, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,507,480,509,482,470,519,445],
[494,0,486,453,435,422,468,429],
[521,515,0,499,490,449,517,485],
[492,548,502,0,461,470,520,483],
[519,566,511,540,0,491,512,528],
[531,579,552,531,510,0,543,496],
[482,533,484,481,489,458,0,412],
[556,572,516,518,473,505,589,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 177, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,503,498,475,492,505,442,496],
[498,0,549,508,513,522,464,510],
[503,452,0,478,498,486,466,488],
[526,493,523,0,510,519,507,494],
[509,488,503,491,0,493,439,479],
[496,479,515,482,508,0,473,488],
[559,537,535,494,562,528,0,535],
[505,491,513,507,522,513,466,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 178, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,522,500,528,499,481,516,493],
[479,0,492,509,462,470,506,495],
[501,509,0,501,479,483,505,491],
[473,492,500,0,476,503,503,485],
[502,539,522,525,0,516,542,500],
[520,531,518,498,485,0,487,520],
[485,495,496,498,459,514,0,521],
[508,506,510,516,501,481,480,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 179, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,496,519,519,402,468,464,450],
[505,0,471,479,469,474,458,493],
[482,530,0,493,502,485,482,513],
[482,522,508,0,437,485,489,496],
[599,532,499,564,0,531,532,528],
[533,527,516,516,470,0,489,526],
[537,543,519,512,469,512,0,488],
[551,508,488,505,473,475,513,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 180, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,491,497,513,503,522,504,486],
[510,0,499,511,496,523,498,496],
[504,502,0,521,493,521,492,498],
[488,490,480,0,490,490,494,467],
[498,505,508,511,0,504,493,485],
[479,478,480,511,497,0,499,476],
[497,503,509,507,508,502,0,517],
[515,505,503,534,516,525,484,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 181, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,515,503,493,490,472,454,549],
[486,0,493,435,458,470,452,490],
[498,508,0,501,521,480,487,510],
[508,566,500,0,537,501,501,498],
[511,543,480,464,0,472,461,507],
[529,531,521,500,529,0,507,485],
[547,549,514,500,540,494,0,534],
[452,511,491,503,494,516,467,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 182, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,502,505,506,513,502,499,533],
[499,0,524,514,490,506,514,520],
[496,477,0,496,497,511,484,510],
[495,487,505,0,483,490,507,509],
[488,511,504,518,0,521,493,501],
[499,495,490,511,480,0,497,509],
[502,487,517,494,508,504,0,516],
[468,481,491,492,500,492,485,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 183, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,632,464,384,220,438,472,333],
[369,0,281,354,344,251,213,395],
[537,720,0,565,418,362,398,557],
[617,647,436,0,401,498,514,624],
[781,657,583,600,0,528,460,533],
[563,750,639,503,473,0,441,641],
[529,788,603,487,541,560,0,551],
[668,606,444,377,468,360,450,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 184, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,529,486,518,553,527,549,541],
[472,0,433,505,514,454,515,501],
[515,568,0,525,580,499,577,552],
[483,496,476,0,573,530,511,532],
[448,487,421,428,0,442,497,495],
[474,547,502,471,559,0,547,500],
[452,486,424,490,504,454,0,524],
[460,500,449,469,506,501,477,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 185, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,494,502,534,482,528,542,490],
[507,0,478,498,488,553,469,478],
[499,523,0,515,472,565,526,486],
[467,503,486,0,493,526,509,474],
[519,513,529,508,0,576,500,542],
[473,448,436,475,425,0,445,430],
[459,532,475,492,501,556,0,525],
[511,523,515,527,459,571,476,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 186, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,492,483,487,505,492,487,474],
[509,0,494,505,506,524,501,505],
[518,507,0,477,509,492,498,506],
[514,496,524,0,543,506,513,513],
[496,495,492,458,0,496,508,502],
[509,477,509,495,505,0,500,499],
[514,500,503,488,493,501,0,493],
[527,496,495,488,499,502,508,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 187, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,513,481,481,521,510,505,483],
[488,0,479,487,488,489,478,492],
[520,522,0,513,531,498,517,513],
[520,514,488,0,534,530,512,514],
[480,513,470,467,0,496,485,492],
[491,512,503,471,505,0,502,487],
[496,523,484,489,516,499,0,489],
[518,509,488,487,509,514,512,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 188, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,498,515,503,513,492,489,487],
[503,0,499,496,516,477,487,477],
[486,502,0,500,519,478,524,492],
[498,505,501,0,510,501,508,489],
[488,485,482,491,0,478,514,480],
[509,524,523,500,523,0,524,515],
[512,514,477,493,487,477,0,488],
[514,524,509,512,521,486,513,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 189, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,516,482,389,446,446,422,481],
[485,0,434,422,408,497,390,446],
[519,567,0,473,535,503,497,456],
[612,579,528,0,557,478,542,526],
[555,593,466,444,0,496,531,499],
[555,504,498,523,505,0,498,474],
[579,611,504,459,470,503,0,557],
[520,555,545,475,502,527,444,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 190, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,448,517,509,442,458,446,463],
[553,0,542,543,525,474,517,498],
[484,459,0,508,508,461,502,485],
[492,458,493,0,432,453,463,458],
[559,476,493,569,0,499,485,467],
[543,527,540,548,502,0,481,501],
[555,484,499,538,516,520,0,452],
[538,503,516,543,534,500,549,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 191, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,575,519,585,522,500,611,456],
[426,0,547,543,493,491,634,527],
[482,454,0,557,528,477,585,553],
[416,458,444,0,456,457,558,428],
[479,508,473,545,0,518,584,526],
[501,510,524,544,483,0,563,455],
[390,367,416,443,417,438,0,446],
[545,474,448,573,475,546,555,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 192, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,490,495,501,503,495,510,497],
[511,0,495,493,523,508,516,505],
[506,506,0,509,509,518,496,512],
[500,508,492,0,495,520,526,490],
[498,478,492,506,0,483,519,476],
[506,493,483,481,518,0,507,500],
[491,485,505,475,482,494,0,505],
[504,496,489,511,525,501,496,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 193, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,513,479,472,514,483,509,498],
[488,0,478,473,491,495,497,490],
[522,523,0,511,527,496,533,503],
[529,528,490,0,513,502,512,519],
[487,510,474,488,0,484,512,513],
[518,506,505,499,517,0,527,510],
[492,504,468,489,489,474,0,503],
[503,511,498,482,488,491,498,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 194, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,486,493,487,524,502,479,501],
[515,0,508,532,499,485,502,505],
[508,493,0,498,492,505,477,487],
[514,469,503,0,498,500,499,487],
[477,502,509,503,0,490,487,493],
[499,516,496,501,511,0,494,489],
[522,499,524,502,514,507,0,502],
[500,496,514,514,508,512,499,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 195, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,527,520,534,532,487,541,525],
[474,0,511,499,497,499,499,466],
[481,490,0,488,514,461,490,472],
[467,502,513,0,479,484,504,484],
[469,504,487,522,0,479,473,468],
[514,502,540,517,522,0,498,488],
[460,502,511,497,528,503,0,508],
[476,535,529,517,533,513,493,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 196, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,542,519,522,481,500,481,520],
[459,0,485,492,478,467,460,522],
[482,516,0,472,465,454,473,473],
[479,509,529,0,483,463,447,507],
[520,523,536,518,0,494,510,537],
[501,534,547,538,507,0,500,536],
[520,541,528,554,491,501,0,513],
[481,479,528,494,464,465,488,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 197, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,539,501,507,509,500,483,534],
[462,0,501,451,473,473,471,500],
[500,500,0,495,462,508,499,537],
[494,550,506,0,500,503,516,520],
[492,528,539,501,0,502,503,512],
[501,528,493,498,499,0,473,534],
[518,530,502,485,498,528,0,523],
[467,501,464,481,489,467,478,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 198, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,514,478,482,512,525,503,544],
[487,0,470,491,494,503,466,494],
[523,531,0,514,512,506,494,543],
[519,510,487,0,521,525,507,519],
[489,507,489,480,0,511,481,500],
[476,498,495,476,490,0,517,470],
[498,535,507,494,520,484,0,512],
[457,507,458,482,501,531,489,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 199, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,479,490,486,508,506,492,484],
[522,0,527,523,504,526,489,523],
[511,474,0,505,492,499,478,484],
[515,478,496,0,496,502,499,490],
[493,497,509,505,0,482,503,494],
[495,475,502,499,519,0,502,499],
[509,512,523,502,498,499,0,503],
[517,478,517,511,507,502,498,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1001, 200, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/me/me_8_1001.csv", index=False, header=False)