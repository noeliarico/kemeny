
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg

rep = 3
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,514,529,519,499,478,505,503,533,497],
[486,0,513,466,462,485,478,520,519,496],
[471,487,0,458,502,461,430,463,508,483],
[481,534,542,0,480,502,500,514,543,481],
[501,538,498,520,0,498,526,516,547,502],
[522,515,539,498,502,0,489,516,512,488],
[495,522,570,500,474,511,0,492,490,518],
[497,480,537,486,484,484,508,0,513,515],
[467,481,492,457,453,488,510,487,0,457],
[503,504,517,519,498,512,482,485,543,0]])



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
result = np.append(np.array([10, 1000, 1, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,506,482,520,498,478,515,465,486,507],
[494,0,482,502,460,454,470,477,483,499],
[518,518,0,557,536,465,485,500,513,530],
[480,498,443,0,505,497,512,491,452,516],
[502,540,464,495,0,507,516,494,505,543],
[522,546,535,503,493,0,512,496,525,541],
[485,530,515,488,484,488,0,477,508,538],
[535,523,500,509,506,504,523,0,499,538],
[514,517,487,548,495,475,492,501,0,512],
[493,501,470,484,457,459,462,462,488,0]])



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
result = np.append(np.array([10, 1000, 2, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,558,479,471,519,494,481,488,499,505],
[442,0,469,461,468,430,432,442,449,457],
[521,531,0,491,497,492,462,482,494,486],
[529,539,509,0,528,476,489,521,515,539],
[481,532,503,472,0,467,474,485,462,499],
[506,570,508,524,533,0,501,469,532,540],
[519,568,538,511,526,499,0,492,537,561],
[512,558,518,479,515,531,508,0,532,533],
[501,551,506,485,538,468,463,468,0,507],
[495,543,514,461,501,460,439,467,493,0]])



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
result = np.append(np.array([10, 1000, 3, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,485,504,448,489,621,518,579,435,527],
[515,0,495,532,558,493,515,539,517,488],
[496,505,0,561,530,513,473,567,462,517],
[552,468,439,0,441,508,510,547,541,506],
[511,442,470,559,0,531,461,558,470,556],
[379,507,487,492,469,0,468,468,464,505],
[482,485,527,490,539,532,0,579,446,538],
[421,461,433,453,442,532,421,0,421,480],
[565,483,538,459,530,536,554,579,0,504],
[473,512,483,494,444,495,462,520,496,0]])



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
result = np.append(np.array([10, 1000, 4, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,539,506,551,515,531,487,580,557,512],
[461,0,478,471,471,491,459,531,493,444],
[494,522,0,498,471,504,454,550,519,495],
[449,529,502,0,478,483,479,575,512,483],
[485,529,529,522,0,542,504,572,580,499],
[469,509,496,517,458,0,477,538,511,505],
[513,541,546,521,496,523,0,598,542,499],
[420,469,450,425,428,462,402,0,481,443],
[443,507,481,488,420,489,458,519,0,489],
[488,556,505,517,501,495,501,557,511,0]])



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
result = np.append(np.array([10, 1000, 5, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,513,535,495,498,507,512,474,506,506],
[487,0,479,481,496,519,510,524,524,503],
[465,521,0,457,483,488,474,469,474,461],
[505,519,543,0,479,524,524,510,507,523],
[502,504,517,521,0,486,521,489,485,521],
[493,481,512,476,514,0,516,470,510,507],
[488,490,526,476,479,484,0,487,468,502],
[526,476,531,490,511,530,513,0,484,478],
[494,476,526,493,515,490,532,516,0,533],
[494,497,539,477,479,493,498,522,467,0]])



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
result = np.append(np.array([10, 1000, 6, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,509,464,516,499,512,516,517,512,518],
[491,0,472,509,537,530,554,542,505,524],
[536,528,0,523,475,516,533,480,506,509],
[484,491,477,0,496,522,522,511,502,497],
[501,463,525,504,0,515,509,540,474,494],
[488,470,484,478,485,0,465,505,475,480],
[484,446,467,478,491,535,0,524,477,466],
[483,458,520,489,460,495,476,0,493,489],
[488,495,494,498,526,525,523,507,0,521],
[482,476,491,503,506,520,534,511,479,0]])



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
result = np.append(np.array([10, 1000, 7, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,507,499,529,500,505,502,472,484,523],
[493,0,507,504,495,482,491,491,491,504],
[501,493,0,525,511,505,516,503,487,510],
[471,496,475,0,488,493,487,486,487,514],
[500,505,489,512,0,486,497,497,469,488],
[495,518,495,507,514,0,520,484,521,511],
[498,509,484,513,503,480,0,503,491,510],
[528,509,497,514,503,516,497,0,497,502],
[516,509,513,513,531,479,509,503,0,508],
[477,496,490,486,512,489,490,498,492,0]])



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
result = np.append(np.array([10, 1000, 8, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,482,470,487,473,493,472,480,485,484],
[518,0,521,506,500,518,494,517,511,503],
[530,479,0,483,503,527,479,511,509,516],
[513,494,517,0,516,506,495,518,510,522],
[527,500,497,484,0,525,511,542,498,523],
[507,482,473,494,475,0,483,501,504,493],
[528,506,521,505,489,517,0,527,515,506],
[520,483,489,482,458,499,473,0,499,498],
[515,489,491,490,502,496,485,501,0,508],
[516,497,484,478,477,507,494,502,492,0]])



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
result = np.append(np.array([10, 1000, 9, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,462,477,490,482,506,509,490,456,496],
[538,0,490,511,516,509,541,527,490,517],
[523,510,0,506,500,485,515,512,495,533],
[510,489,494,0,503,500,521,509,473,498],
[518,484,500,497,0,495,517,511,509,511],
[494,491,515,500,505,0,510,504,489,524],
[491,459,485,479,483,490,0,487,469,488],
[510,473,488,491,489,496,513,0,488,507],
[544,510,505,527,491,511,531,512,0,530],
[504,483,467,502,489,476,512,493,470,0]])



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
result = np.append(np.array([10, 1000, 10, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,436,529,457,507,420,390,505,437,520],
[564,0,456,529,447,483,469,462,548,503],
[471,544,0,532,447,494,530,502,548,508],
[543,471,468,0,563,488,503,544,542,534],
[493,553,553,437,0,525,503,518,518,538],
[580,517,506,512,475,0,478,581,552,525],
[610,531,470,497,497,522,0,544,502,526],
[495,538,498,456,482,419,456,0,489,502],
[563,452,452,458,482,448,498,511,0,513],
[480,497,492,466,462,475,474,498,487,0]])



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
result = np.append(np.array([10, 1000, 11, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,534,534,504,535,470,487,508,532,550],
[466,0,466,495,507,440,456,486,478,493],
[466,534,0,519,528,479,514,496,558,541],
[496,505,481,0,508,471,480,490,537,500],
[465,493,472,492,0,450,446,445,485,497],
[530,560,521,529,550,0,499,530,542,544],
[513,544,486,520,554,501,0,528,491,517],
[492,514,504,510,555,470,472,0,493,529],
[468,522,442,463,515,458,509,507,0,525],
[450,507,459,500,503,456,483,471,475,0]])



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
result = np.append(np.array([10, 1000, 12, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,463,513,507,491,520,498,512,492,516],
[537,0,497,554,512,532,533,497,512,515],
[487,503,0,513,513,524,519,495,512,528],
[493,446,487,0,471,503,487,462,465,511],
[509,488,487,529,0,529,518,493,491,501],
[480,468,476,497,471,0,471,469,461,483],
[502,467,481,513,482,529,0,466,476,506],
[488,503,505,538,507,531,534,0,487,519],
[508,488,488,535,509,539,524,513,0,501],
[484,485,472,489,499,517,494,481,499,0]])



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
result = np.append(np.array([10, 1000, 13, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,508,533,504,522,524,489,530,517,526],
[492,0,530,515,542,479,470,496,514,502],
[467,470,0,520,501,485,455,488,501,496],
[496,485,480,0,511,460,460,486,526,506],
[478,458,499,489,0,436,464,505,495,508],
[476,521,515,540,564,0,486,518,523,508],
[511,530,545,540,536,514,0,494,507,534],
[470,504,512,514,495,482,506,0,538,474],
[483,486,499,474,505,477,493,462,0,504],
[474,498,504,494,492,492,466,526,496,0]])



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
result = np.append(np.array([10, 1000, 14, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,470,518,464,481,510,521,502,475,482],
[530,0,530,503,494,512,537,523,510,485],
[482,470,0,471,454,466,492,501,488,458],
[536,497,529,0,495,508,533,506,525,507],
[519,506,546,505,0,497,542,504,529,516],
[490,488,534,492,503,0,521,513,468,484],
[479,463,508,467,458,479,0,531,458,468],
[498,477,499,494,496,487,469,0,487,466],
[525,490,512,475,471,532,542,513,0,497],
[518,515,542,493,484,516,532,534,503,0]])



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
result = np.append(np.array([10, 1000, 15, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,508,498,503,505,486,520,488,519,482],
[492,0,502,538,523,506,530,516,528,521],
[502,498,0,504,520,495,504,520,516,518],
[497,462,496,0,506,495,485,492,481,485],
[495,477,480,494,0,465,474,460,490,513],
[514,494,505,505,535,0,516,486,527,497],
[480,470,496,515,526,484,0,486,489,498],
[512,484,480,508,540,514,514,0,523,498],
[481,472,484,519,510,473,511,477,0,492],
[518,479,482,515,487,503,502,502,508,0]])



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
result = np.append(np.array([10, 1000, 16, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,497,504,506,471,499,463,503,489,470],
[503,0,511,513,475,500,492,516,502,461],
[496,489,0,518,473,497,482,487,483,481],
[494,487,482,0,469,466,460,482,468,441],
[529,525,527,531,0,516,500,537,533,498],
[501,500,503,534,484,0,482,515,504,472],
[537,508,518,540,500,518,0,536,534,515],
[497,484,513,518,463,485,464,0,515,464],
[511,498,517,532,467,496,466,485,0,490],
[530,539,519,559,502,528,485,536,510,0]])



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
result = np.append(np.array([10, 1000, 17, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,490,462,467,555,570,508,430,438,506],
[510,0,463,476,540,555,467,455,410,520],
[538,537,0,504,563,508,511,512,464,512],
[533,524,496,0,563,578,491,484,497,521],
[445,460,437,437,0,499,509,419,444,475],
[430,445,492,422,501,0,466,410,399,459],
[492,533,489,509,491,534,0,454,456,482],
[570,545,488,516,581,590,546,0,511,581],
[562,590,536,503,556,601,544,489,0,521],
[494,480,488,479,525,541,518,419,479,0]])



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
result = np.append(np.array([10, 1000, 18, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,519,518,514,552,469,532,500,522,482],
[481,0,463,483,496,457,504,469,500,470],
[482,537,0,531,524,489,520,502,489,517],
[486,517,469,0,506,468,525,477,501,500],
[448,504,476,494,0,459,497,471,486,480],
[531,543,511,532,541,0,533,520,496,527],
[468,496,480,475,503,467,0,478,484,459],
[500,531,498,523,529,480,522,0,502,516],
[478,500,511,499,514,504,516,498,0,499],
[518,530,483,500,520,473,541,484,501,0]])



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
result = np.append(np.array([10, 1000, 19, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,665,688,529,462,447,636,615,685,577],
[335,0,517,480,429,445,620,490,438,358],
[312,483,0,375,430,331,603,425,393,365],
[471,520,625,0,562,519,562,507,514,380],
[538,571,570,438,0,481,665,447,412,353],
[553,555,669,481,519,0,630,478,518,406],
[364,380,397,438,335,370,0,369,369,294],
[385,510,575,493,553,522,631,0,450,265],
[315,562,607,486,588,482,631,550,0,367],
[423,642,635,620,647,594,706,735,633,0]])



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
result = np.append(np.array([10, 1000, 20, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,523,453,531,472,515,469,460,474,477],
[477,0,461,517,479,514,480,464,487,483],
[547,539,0,532,486,531,506,515,536,503],
[469,483,468,0,464,501,473,426,466,455],
[528,521,514,536,0,535,514,495,533,518],
[485,486,469,499,465,0,508,443,479,458],
[531,520,494,527,486,492,0,488,506,509],
[540,536,485,574,505,557,512,0,518,523],
[526,513,464,534,467,521,494,482,0,488],
[523,517,497,545,482,542,491,477,512,0]])



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
result = np.append(np.array([10, 1000, 21, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,513,501,521,497,504,526,490,497,502],
[487,0,500,509,476,499,515,514,493,471],
[499,500,0,521,493,521,521,490,506,503],
[479,491,479,0,456,512,517,506,480,475],
[503,524,507,544,0,539,523,504,523,491],
[496,501,479,488,461,0,541,481,494,488],
[474,485,479,483,477,459,0,510,508,450],
[510,486,510,494,496,519,490,0,486,483],
[503,507,494,520,477,506,492,514,0,484],
[498,529,497,525,509,512,550,517,516,0]])



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
result = np.append(np.array([10, 1000, 22, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,479,486,493,508,523,476,521,496,525],
[521,0,519,478,503,508,505,483,493,497],
[514,481,0,518,506,509,524,517,508,524],
[507,522,482,0,521,481,517,515,470,534],
[492,497,494,479,0,486,528,508,513,526],
[477,492,491,519,514,0,540,521,492,534],
[524,495,476,483,472,460,0,532,492,527],
[479,517,483,485,492,479,468,0,493,532],
[504,507,492,530,487,508,508,507,0,542],
[475,503,476,466,474,466,473,468,458,0]])



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
result = np.append(np.array([10, 1000, 23, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,486,496,498,506,522,477,546,511,468],
[514,0,497,493,507,505,469,547,487,493],
[504,503,0,513,528,535,473,519,509,490],
[502,507,487,0,519,505,492,532,507,535],
[494,493,472,481,0,481,503,534,501,472],
[478,495,465,495,519,0,447,510,495,462],
[523,531,527,508,497,553,0,546,531,532],
[454,453,481,468,466,490,454,0,481,473],
[489,513,491,493,499,505,469,519,0,519],
[532,507,510,465,528,538,468,527,481,0]])



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
result = np.append(np.array([10, 1000, 24, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,481,518,474,480,484,474,491,507,469],
[519,0,513,494,528,523,512,510,490,492],
[482,487,0,488,495,491,492,489,465,472],
[526,506,512,0,508,506,514,536,498,502],
[520,472,505,492,0,498,495,483,488,457],
[516,477,509,494,502,0,492,488,497,468],
[526,488,508,486,505,508,0,519,495,486],
[509,490,511,464,517,512,481,0,494,480],
[493,510,535,502,512,503,505,506,0,488],
[531,508,528,498,543,532,514,520,512,0]])



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
result = np.append(np.array([10, 1000, 25, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,536,524,503,524,459,525,527,576,543],
[464,0,458,501,491,513,502,552,530,564],
[476,542,0,500,508,531,491,577,555,552],
[497,499,500,0,492,491,492,580,513,564],
[476,509,492,508,0,494,497,536,496,497],
[541,487,469,509,506,0,484,606,531,561],
[475,498,509,508,503,516,0,541,499,546],
[473,448,423,420,464,394,459,0,484,494],
[424,470,445,487,504,469,501,516,0,506],
[457,436,448,436,503,439,454,506,494,0]])



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
result = np.append(np.array([10, 1000, 26, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,524,519,511,523,505,493,486,508,503],
[476,0,491,487,498,490,511,496,490,473],
[481,509,0,509,500,500,493,505,478,471],
[489,513,491,0,506,470,494,490,497,481],
[477,502,500,494,0,488,499,499,512,514],
[495,510,500,530,512,0,527,517,517,516],
[507,489,507,506,501,473,0,500,497,494],
[514,504,495,510,501,483,500,0,492,482],
[492,510,522,503,488,483,503,508,0,489],
[497,527,529,519,486,484,506,518,511,0]])



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
result = np.append(np.array([10, 1000, 27, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,530,474,456,537,498,500,511,591,459],
[470,0,480,454,556,435,501,407,545,433],
[526,520,0,471,573,454,480,389,505,434],
[544,546,529,0,576,468,512,497,535,465],
[463,444,427,424,0,378,415,388,497,418],
[502,565,546,532,622,0,545,465,561,514],
[500,499,520,488,585,455,0,465,563,423],
[489,593,611,503,612,535,535,0,569,459],
[409,455,495,465,503,439,437,431,0,400],
[541,567,566,535,582,486,577,541,600,0]])



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
result = np.append(np.array([10, 1000, 28, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,481,531,479,460,454,496,491,499,490],
[519,0,512,521,451,547,521,497,545,525],
[469,488,0,455,445,451,498,458,503,440],
[521,479,545,0,517,509,547,497,540,524],
[540,549,555,483,0,526,511,520,572,557],
[546,453,549,491,474,0,550,513,540,516],
[504,479,502,453,489,450,0,514,510,553],
[509,503,542,503,480,487,486,0,523,493],
[501,455,497,460,428,460,490,477,0,464],
[510,475,560,476,443,484,447,507,536,0]])



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
result = np.append(np.array([10, 1000, 29, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,500,520,501,497,515,500,504,509,519],
[500,0,535,470,495,489,507,517,519,510],
[480,465,0,467,471,478,479,507,496,494],
[499,530,533,0,497,506,502,526,523,520],
[503,505,529,503,0,493,516,524,524,526],
[485,511,522,494,507,0,519,496,510,505],
[500,493,521,498,484,481,0,495,499,505],
[496,483,493,474,476,504,505,0,513,498],
[491,481,504,477,476,490,501,487,0,485],
[481,490,506,480,474,495,495,502,515,0]])



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
result = np.append(np.array([10, 1000, 30, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,497,530,501,476,489,522,511,493,515],
[503,0,508,472,488,468,475,511,457,517],
[470,492,0,476,457,447,474,501,468,492],
[499,528,524,0,520,501,505,526,496,523],
[524,512,543,480,0,511,516,510,486,503],
[511,532,553,499,489,0,504,537,496,527],
[478,525,526,495,484,496,0,542,521,509],
[489,489,499,474,490,463,458,0,486,495],
[507,543,532,504,514,504,479,514,0,520],
[485,483,508,477,497,473,491,505,480,0]])



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
result = np.append(np.array([10, 1000, 31, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,504,491,491,513,501,491,478,506,497],
[496,0,498,493,489,494,487,505,488,509],
[509,502,0,488,505,469,483,496,505,520],
[509,507,512,0,510,494,508,509,500,515],
[487,511,495,490,0,493,477,506,482,495],
[499,506,531,506,507,0,496,534,505,517],
[509,513,517,492,523,504,0,508,504,516],
[522,495,504,491,494,466,492,0,504,509],
[494,512,495,500,518,495,496,496,0,518],
[503,491,480,485,505,483,484,491,482,0]])



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
result = np.append(np.array([10, 1000, 32, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,500,502,490,513,483,463,508,547,541],
[500,0,469,479,510,477,484,530,523,475],
[498,531,0,525,490,481,495,527,517,514],
[510,521,475,0,487,495,516,460,549,518],
[487,490,510,513,0,491,472,525,529,515],
[517,523,519,505,509,0,488,561,549,531],
[537,516,505,484,528,512,0,553,566,506],
[492,470,473,540,475,439,447,0,537,509],
[453,477,483,451,471,451,434,463,0,469],
[459,525,486,482,485,469,494,491,531,0]])



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
result = np.append(np.array([10, 1000, 33, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,719,659,470,453,516,582,589,558,491],
[281,0,430,328,430,381,390,488,386,381],
[341,570,0,467,469,466,551,484,479,475],
[530,672,533,0,522,575,573,598,564,439],
[547,570,531,478,0,512,479,606,450,545],
[484,619,534,425,488,0,549,618,532,504],
[418,610,449,427,521,451,0,595,443,373],
[411,512,516,402,394,382,405,0,408,398],
[442,614,521,436,550,468,557,592,0,481],
[509,619,525,561,455,496,627,602,519,0]])



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
result = np.append(np.array([10, 1000, 34, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,513,511,510,494,516,520,503,538,514],
[487,0,488,492,495,510,489,486,523,507],
[489,512,0,503,516,530,514,484,532,512],
[490,508,497,0,484,501,509,500,524,513],
[506,505,484,516,0,513,501,506,527,518],
[484,490,470,499,487,0,491,475,514,506],
[480,511,486,491,499,509,0,464,514,513],
[497,514,516,500,494,525,536,0,543,526],
[462,477,468,476,473,486,486,457,0,464],
[486,493,488,487,482,494,487,474,536,0]])



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
result = np.append(np.array([10, 1000, 35, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,479,462,516,514,547,471,498,554,496],
[521,0,489,482,486,524,528,494,523,499],
[538,511,0,506,481,524,517,484,550,550],
[484,518,494,0,498,530,507,464,518,519],
[486,514,519,502,0,549,486,523,517,473],
[453,476,476,470,451,0,517,453,498,490],
[529,472,483,493,514,483,0,493,538,497],
[502,506,516,536,477,547,507,0,527,548],
[446,477,450,482,483,502,462,473,0,465],
[504,501,450,481,527,510,503,452,535,0]])



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
result = np.append(np.array([10, 1000, 36, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,507,475,526,477,518,497,535,446,501],
[493,0,467,508,441,490,485,528,477,467],
[525,533,0,550,523,514,535,544,498,505],
[474,492,450,0,465,501,484,539,462,483],
[523,559,477,535,0,538,520,549,477,524],
[482,510,486,499,462,0,492,532,505,518],
[503,515,465,516,480,508,0,539,444,497],
[465,472,456,461,451,468,461,0,414,451],
[554,523,502,538,523,495,556,586,0,550],
[499,533,495,517,476,482,503,549,450,0]])



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
result = np.append(np.array([10, 1000, 37, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,522,498,511,511,516,515,525,495,493],
[478,0,476,484,489,483,504,491,468,465],
[502,524,0,489,522,521,497,532,516,525],
[489,516,511,0,523,503,490,511,501,490],
[489,511,478,477,0,503,500,509,503,469],
[484,517,479,497,497,0,506,521,505,494],
[485,496,503,510,500,494,0,510,510,488],
[475,509,468,489,491,479,490,0,489,471],
[505,532,484,499,497,495,490,511,0,483],
[507,535,475,510,531,506,512,529,517,0]])



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
result = np.append(np.array([10, 1000, 38, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,509,513,512,503,495,492,514,501,522],
[491,0,485,491,500,489,509,509,487,504],
[487,515,0,508,477,508,511,503,495,533],
[488,509,492,0,512,484,518,503,496,528],
[497,500,523,488,0,481,488,519,507,519],
[505,511,492,516,519,0,530,514,512,536],
[508,491,489,482,512,470,0,495,496,506],
[486,491,497,497,481,486,505,0,475,514],
[499,513,505,504,493,488,504,525,0,505],
[478,496,467,472,481,464,494,486,495,0]])



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
result = np.append(np.array([10, 1000, 39, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,477,529,485,482,495,508,431,514,492],
[523,0,542,502,516,534,493,500,525,485],
[471,458,0,501,484,509,511,472,501,485],
[515,498,499,0,465,523,463,479,504,488],
[518,484,516,535,0,504,490,497,516,476],
[505,466,491,477,496,0,498,468,521,494],
[492,507,489,537,510,502,0,485,524,504],
[569,500,528,521,503,532,515,0,540,536],
[486,475,499,496,484,479,476,460,0,515],
[508,515,515,512,524,506,496,464,485,0]])



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
result = np.append(np.array([10, 1000, 40, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,468,487,443,480,465,461,504,516,506],
[532,0,494,481,517,465,494,506,540,524],
[513,506,0,459,540,462,540,519,553,499],
[557,519,541,0,523,500,530,534,546,531],
[520,483,460,477,0,472,493,500,518,496],
[535,535,538,500,528,0,503,558,532,503],
[539,506,460,470,507,497,0,533,523,467],
[496,494,481,466,500,442,467,0,504,476],
[484,460,447,454,482,468,477,496,0,485],
[494,476,501,469,504,497,533,524,515,0]])



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
result = np.append(np.array([10, 1000, 41, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,519,520,509,522,488,519,497,492,497],
[481,0,514,514,485,496,476,511,497,506],
[480,486,0,471,496,472,469,493,489,486],
[491,486,529,0,506,480,476,502,513,501],
[478,515,504,494,0,483,485,495,499,498],
[512,504,528,520,517,0,495,522,517,488],
[481,524,531,524,515,505,0,513,513,501],
[503,489,507,498,505,478,487,0,502,473],
[508,503,511,487,501,483,487,498,0,481],
[503,494,514,499,502,512,499,527,519,0]])



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
result = np.append(np.array([10, 1000, 42, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,501,517,482,501,477,498,518,499,499],
[499,0,510,486,492,478,493,477,513,482],
[483,490,0,490,508,501,517,500,516,496],
[518,514,510,0,521,518,516,516,517,497],
[499,508,492,479,0,471,481,494,491,486],
[523,522,499,482,529,0,506,519,522,503],
[502,507,483,484,519,494,0,509,511,504],
[482,523,500,484,506,481,491,0,505,515],
[501,487,484,483,509,478,489,495,0,495],
[501,518,504,503,514,497,496,485,505,0]])



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
result = np.append(np.array([10, 1000, 43, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,546,538,526,525,498,526,500,511,516],
[454,0,498,473,485,480,484,451,459,465],
[462,502,0,500,495,489,474,473,502,480],
[474,527,500,0,479,493,466,483,494,484],
[475,515,505,521,0,494,491,483,477,461],
[502,520,511,507,506,0,501,473,501,488],
[474,516,526,534,509,499,0,509,500,498],
[500,549,527,517,517,527,491,0,484,499],
[489,541,498,506,523,499,500,516,0,489],
[484,535,520,516,539,512,502,501,511,0]])



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
result = np.append(np.array([10, 1000, 44, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,527,536,485,493,484,475,459,540,529],
[473,0,513,437,480,534,444,500,507,441],
[464,487,0,470,530,509,494,497,539,504],
[515,563,530,0,498,518,532,551,608,488],
[507,520,470,502,0,466,485,502,509,500],
[516,466,491,482,534,0,492,485,545,458],
[525,556,506,468,515,508,0,535,539,495],
[541,500,503,449,498,515,465,0,561,497],
[460,493,461,392,491,455,461,439,0,417],
[471,559,496,512,500,542,505,503,583,0]])



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
result = np.append(np.array([10, 1000, 45, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,606,545,500,451,540,573,563,570,593],
[394,0,562,484,450,445,538,505,494,521],
[455,438,0,451,414,487,498,412,478,480],
[500,516,549,0,488,544,538,501,531,513],
[549,550,586,512,0,531,601,455,541,539],
[460,555,513,456,469,0,483,512,407,543],
[427,462,502,462,399,517,0,481,406,475],
[437,495,588,499,545,488,519,0,474,570],
[430,506,522,469,459,593,594,526,0,517],
[407,479,520,487,461,457,525,430,483,0]])



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
result = np.append(np.array([10, 1000, 46, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,468,489,499,499,514,508,473,479,547],
[532,0,506,558,536,523,528,519,494,548],
[511,494,0,530,487,498,529,506,499,561],
[501,442,470,0,485,462,465,467,460,511],
[501,464,513,515,0,473,526,540,499,546],
[486,477,502,538,527,0,534,529,501,514],
[492,472,471,535,474,466,0,496,480,512],
[527,481,494,533,460,471,504,0,456,542],
[521,506,501,540,501,499,520,544,0,497],
[453,452,439,489,454,486,488,458,503,0]])



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
result = np.append(np.array([10, 1000, 47, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,525,529,504,515,517,485,507,502,518],
[475,0,491,481,497,486,490,488,486,482],
[471,509,0,501,496,503,484,487,493,509],
[496,519,499,0,505,496,493,502,494,515],
[485,503,504,495,0,510,477,486,494,499],
[483,514,497,504,490,0,507,495,495,519],
[515,510,516,507,523,493,0,516,500,520],
[493,512,513,498,514,505,484,0,506,498],
[498,514,507,506,506,505,500,494,0,515],
[482,518,491,485,501,481,480,502,485,0]])



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
result = np.append(np.array([10, 1000, 48, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,497,493,523,493,526,508,512,506,493],
[503,0,505,507,491,507,519,517,486,500],
[507,495,0,515,482,536,520,478,493,494],
[477,493,485,0,462,496,503,481,489,482],
[507,509,518,538,0,518,520,498,508,511],
[474,493,464,504,482,0,502,482,520,489],
[492,481,480,497,480,498,0,479,487,475],
[488,483,522,519,502,518,521,0,525,495],
[494,514,507,511,492,480,513,475,0,475],
[507,500,506,518,489,511,525,505,525,0]])



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
result = np.append(np.array([10, 1000, 49, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,487,516,504,515,458,494,495,476,484],
[513,0,546,516,473,474,506,519,508,510],
[484,454,0,499,498,461,503,484,499,468],
[496,484,501,0,481,468,502,489,503,495],
[485,527,502,519,0,492,513,490,477,507],
[542,526,539,532,508,0,518,509,485,524],
[506,494,497,498,487,482,0,509,497,504],
[505,481,516,511,510,491,491,0,490,491],
[524,492,501,497,523,515,503,510,0,487],
[516,490,532,505,493,476,496,509,513,0]])



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
result = np.append(np.array([10, 1000, 50, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,475,478,513,485,482,536,510,533,528],
[525,0,518,540,491,503,537,513,484,533],
[522,482,0,548,509,502,561,527,543,539],
[487,460,452,0,513,477,526,508,510,521],
[515,509,491,487,0,496,515,520,531,545],
[518,497,498,523,504,0,538,515,525,543],
[464,463,439,474,485,462,0,511,504,507],
[490,487,473,492,480,485,489,0,532,514],
[467,516,457,490,469,475,496,468,0,521],
[472,467,461,479,455,457,493,486,479,0]])



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
result = np.append(np.array([10, 1000, 51, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,609,583,490,620,560,537,636,422,605],
[391,0,432,404,520,414,556,541,414,380],
[417,568,0,416,523,456,586,477,550,454],
[510,596,584,0,438,479,486,584,503,431],
[380,480,477,562,0,503,473,687,511,562],
[440,586,544,521,497,0,497,569,518,428],
[463,444,414,514,527,503,0,528,436,477],
[364,459,523,416,313,431,472,0,490,448],
[578,586,450,497,489,482,564,510,0,439],
[395,620,546,569,438,572,523,552,561,0]])



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
result = np.append(np.array([10, 1000, 52, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,530,508,509,538,455,468,513,489,477],
[470,0,501,501,505,441,535,508,474,470],
[492,499,0,479,497,481,506,479,487,490],
[491,499,521,0,526,444,517,494,512,501],
[462,495,503,474,0,446,498,468,490,409],
[545,559,519,556,554,0,550,523,497,518],
[532,465,494,483,502,450,0,472,457,464],
[487,492,521,506,532,477,528,0,476,486],
[511,526,513,488,510,503,543,524,0,488],
[523,530,510,499,591,482,536,514,512,0]])



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
result = np.append(np.array([10, 1000, 53, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,524,510,521,486,513,501,522,548,542],
[476,0,490,528,455,481,503,500,510,521],
[490,510,0,526,509,481,476,530,520,512],
[479,472,474,0,453,471,467,499,507,510],
[514,545,491,547,0,550,513,542,557,550],
[487,519,519,529,450,0,477,518,518,517],
[499,497,524,533,487,523,0,529,531,524],
[478,500,470,501,458,482,471,0,520,493],
[452,490,480,493,443,482,469,480,0,491],
[458,479,488,490,450,483,476,507,509,0]])



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
result = np.append(np.array([10, 1000, 54, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,486,489,506,515,476,510,507,489,515],
[514,0,492,514,519,505,539,512,501,538],
[511,508,0,498,551,505,520,513,532,507],
[494,486,502,0,505,490,493,511,481,503],
[485,481,449,495,0,478,485,476,497,506],
[524,495,495,510,522,0,519,495,528,524],
[490,461,480,507,515,481,0,498,507,501],
[493,488,487,489,524,505,502,0,499,475],
[511,499,468,519,503,472,493,501,0,483],
[485,462,493,497,494,476,499,525,517,0]])



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
result = np.append(np.array([10, 1000, 55, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,462,494,510,515,492,499,478,480,540],
[538,0,457,552,493,515,512,497,517,535],
[506,543,0,552,540,546,531,516,493,540],
[490,448,448,0,452,503,480,465,443,491],
[485,507,460,548,0,479,538,485,503,525],
[508,485,454,497,521,0,520,449,517,482],
[501,488,469,520,462,480,0,467,516,525],
[522,503,484,535,515,551,533,0,504,531],
[520,483,507,557,497,483,484,496,0,533],
[460,465,460,509,475,518,475,469,467,0]])



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
result = np.append(np.array([10, 1000, 56, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,492,487,497,513,500,486,489,490,512],
[508,0,527,509,514,534,475,508,488,508],
[513,473,0,502,506,505,480,476,474,514],
[503,491,498,0,500,507,499,511,501,512],
[487,486,494,500,0,492,481,503,477,497],
[500,466,495,493,508,0,481,496,509,506],
[514,525,520,501,519,519,0,492,518,534],
[511,492,524,489,497,504,508,0,513,525],
[510,512,526,499,523,491,482,487,0,491],
[488,492,486,488,503,494,466,475,509,0]])



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
result = np.append(np.array([10, 1000, 57, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,511,476,537,477,512,486,485,489,501],
[489,0,466,483,491,488,486,491,485,475],
[524,534,0,514,521,497,495,504,513,525],
[463,517,486,0,500,508,506,501,492,485],
[523,509,479,500,0,511,480,494,497,496],
[488,512,503,492,489,0,473,484,486,480],
[514,514,505,494,520,527,0,521,515,503],
[515,509,496,499,506,516,479,0,515,493],
[511,515,487,508,503,514,485,485,0,491],
[499,525,475,515,504,520,497,507,509,0]])



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
result = np.append(np.array([10, 1000, 58, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,513,465,489,502,483,484,482,523,471],
[487,0,460,484,489,507,498,477,513,508],
[535,540,0,517,516,510,508,493,547,511],
[511,516,483,0,513,527,507,475,519,519],
[498,511,484,487,0,502,485,482,515,520],
[517,493,490,473,498,0,484,488,506,491],
[516,502,492,493,515,516,0,503,515,497],
[518,523,507,525,518,512,497,0,523,513],
[477,487,453,481,485,494,485,477,0,490],
[529,492,489,481,480,509,503,487,510,0]])



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
result = np.append(np.array([10, 1000, 59, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,482,483,526,533,479,510,514,472,483],
[518,0,510,515,502,527,502,521,470,500],
[517,490,0,526,538,507,524,501,489,501],
[474,485,474,0,511,510,460,523,480,458],
[467,498,462,489,0,484,508,482,456,469],
[521,473,493,490,516,0,481,463,439,485],
[490,498,476,540,492,519,0,510,519,507],
[486,479,499,477,518,537,490,0,475,496],
[528,530,511,520,544,561,481,525,0,523],
[517,500,499,542,531,515,493,504,477,0]])



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
result = np.append(np.array([10, 1000, 60, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,495,523,504,548,492,531,517,511,490],
[505,0,529,497,527,514,526,512,519,534],
[477,471,0,495,484,508,505,500,504,501],
[496,503,505,0,505,534,515,518,506,485],
[452,473,516,495,0,477,464,497,490,486],
[508,486,492,466,523,0,495,486,485,475],
[469,474,495,485,536,505,0,515,499,504],
[483,488,500,482,503,514,485,0,490,504],
[489,481,496,494,510,515,501,510,0,496],
[510,466,499,515,514,525,496,496,504,0]])



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
result = np.append(np.array([10, 1000, 61, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,515,502,514,504,523,513,499,515,506],
[485,0,482,474,503,480,512,513,501,473],
[498,518,0,479,505,491,491,500,511,486],
[486,526,521,0,504,519,522,502,493,506],
[496,497,495,496,0,485,489,493,482,501],
[477,520,509,481,515,0,493,482,483,493],
[487,488,509,478,511,507,0,504,493,497],
[501,487,500,498,507,518,496,0,494,517],
[485,499,489,507,518,517,507,506,0,498],
[494,527,514,494,499,507,503,483,502,0]])



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
result = np.append(np.array([10, 1000, 62, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,475,479,530,494,479,481,443,530,477],
[525,0,498,502,503,487,497,473,531,499],
[521,502,0,514,537,506,491,486,537,497],
[470,498,486,0,485,481,487,455,547,488],
[506,497,463,515,0,511,506,486,558,524],
[521,513,494,519,489,0,504,479,540,498],
[519,503,509,513,494,496,0,479,539,514],
[557,527,514,545,514,521,521,0,554,495],
[470,469,463,453,442,460,461,446,0,456],
[523,501,503,512,476,502,486,505,544,0]])



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
result = np.append(np.array([10, 1000, 63, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,464,474,457,478,482,447,485,454,472],
[536,0,508,523,530,529,489,515,494,520],
[526,492,0,519,504,537,512,512,485,525],
[543,477,481,0,500,526,505,525,493,495],
[522,470,496,500,0,503,491,497,477,482],
[518,471,463,474,497,0,465,481,482,489],
[553,511,488,495,509,535,0,517,510,508],
[515,485,488,475,503,519,483,0,511,509],
[546,506,515,507,523,518,490,489,0,515],
[528,480,475,505,518,511,492,491,485,0]])



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
result = np.append(np.array([10, 1000, 64, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,504,471,485,491,492,479,485,474,492],
[496,0,552,511,529,509,519,515,520,513],
[529,448,0,501,518,476,513,511,494,500],
[515,489,499,0,498,515,499,504,505,489],
[509,471,482,502,0,511,501,499,506,470],
[508,491,524,485,489,0,504,523,508,492],
[521,481,487,501,499,496,0,500,507,468],
[515,485,489,496,501,477,500,0,473,483],
[526,480,506,495,494,492,493,527,0,458],
[508,487,500,511,530,508,532,517,542,0]])



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
result = np.append(np.array([10, 1000, 65, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,728,597,386,597,597,597,597,728,939],
[272,0,211,386,211,272,658,211,386,211],
[403,789,0,728,939,1000,789,728,789,1000],
[614,614,272,0,553,614,1000,272,403,614],
[403,789,61,447,0,658,789,447,789,403],
[403,728,0,386,342,0,789,386,728,342],
[403,342,211,0,211,211,0,211,342,553],
[403,789,272,728,553,614,789,0,789,614],
[272,614,211,597,211,272,658,211,0,211],
[61,789,0,386,597,658,447,386,789,0]])



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
result = np.append(np.array([10, 1000, 66, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,444,466,430,514,456,480,432,454,460],
[556,0,534,452,488,525,544,500,527,436],
[534,466,0,471,524,482,521,465,476,428],
[570,548,529,0,497,509,518,510,481,510],
[486,512,476,503,0,429,536,469,481,455],
[544,475,518,491,571,0,546,491,489,469],
[520,456,479,482,464,454,0,480,477,411],
[568,500,535,490,531,509,520,0,535,439],
[546,473,524,519,519,511,523,465,0,466],
[540,564,572,490,545,531,589,561,534,0]])



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
result = np.append(np.array([10, 1000, 67, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,490,517,480,525,526,537,516,480,502],
[510,0,513,477,527,484,548,533,470,468],
[483,487,0,477,494,475,508,503,462,468],
[520,523,523,0,536,531,541,528,500,488],
[475,473,506,464,0,488,510,466,466,486],
[474,516,525,469,512,0,527,518,465,482],
[463,452,492,459,490,473,0,499,457,475],
[484,467,497,472,534,482,501,0,477,467],
[520,530,538,500,534,535,543,523,0,527],
[498,532,532,512,514,518,525,533,473,0]])



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
result = np.append(np.array([10, 1000, 68, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,491,453,501,470,453,436,482,425,519],
[509,0,475,537,455,455,459,499,454,454],
[547,525,0,559,519,572,545,555,461,537],
[499,463,441,0,447,486,507,476,434,420],
[530,545,481,553,0,487,494,537,495,527],
[547,545,428,514,513,0,484,492,476,498],
[564,541,455,493,506,516,0,502,465,533],
[518,501,445,524,463,508,498,0,499,495],
[575,546,539,566,505,524,535,501,0,499],
[481,546,463,580,473,502,467,505,501,0]])



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
result = np.append(np.array([10, 1000, 69, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,496,475,473,457,419,444,458,497,437],
[504,0,504,511,439,467,445,453,473,453],
[525,496,0,535,480,485,493,516,502,484],
[527,489,465,0,461,433,459,418,464,464],
[543,561,520,539,0,460,497,478,482,472],
[581,533,515,567,540,0,570,492,506,480],
[556,555,507,541,503,430,0,439,506,478],
[542,547,484,582,522,508,561,0,552,535],
[503,527,498,536,518,494,494,448,0,483],
[563,547,516,536,528,520,522,465,517,0]])



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
result = np.append(np.array([10, 1000, 70, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,525,481,540,553,517,497,499,492,502],
[475,0,473,526,501,469,480,504,491,452],
[519,527,0,526,529,502,477,483,487,501],
[460,474,474,0,516,478,463,447,441,460],
[447,499,471,484,0,456,467,460,469,425],
[483,531,498,522,544,0,512,490,487,465],
[503,520,523,537,533,488,0,482,544,492],
[501,496,517,553,540,510,518,0,523,498],
[508,509,513,559,531,513,456,477,0,478],
[498,548,499,540,575,535,508,502,522,0]])



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
result = np.append(np.array([10, 1000, 71, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,531,489,495,491,508,493,482,500,519],
[469,0,508,473,494,533,453,504,488,505],
[511,492,0,492,518,495,474,500,487,494],
[505,527,508,0,495,491,482,484,543,525],
[509,506,482,505,0,482,499,481,482,501],
[492,467,505,509,518,0,499,493,519,512],
[507,547,526,518,501,501,0,493,493,538],
[518,496,500,516,519,507,507,0,520,507],
[500,512,513,457,518,481,507,480,0,511],
[481,495,506,475,499,488,462,493,489,0]])



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
result = np.append(np.array([10, 1000, 72, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,580,517,511,491,497,507,533,501,508],
[420,0,478,443,459,461,464,458,456,454],
[483,522,0,470,492,473,504,520,491,490],
[489,557,530,0,524,498,514,518,511,507],
[509,541,508,476,0,492,492,530,487,495],
[503,539,527,502,508,0,498,538,504,490],
[493,536,496,486,508,502,0,501,484,461],
[467,542,480,482,470,462,499,0,482,482],
[499,544,509,489,513,496,516,518,0,499],
[492,546,510,493,505,510,539,518,501,0]])



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
result = np.append(np.array([10, 1000, 73, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,462,451,466,468,526,483,579,574,555],
[538,0,479,537,571,528,496,513,594,569],
[549,521,0,634,586,555,498,637,636,538],
[534,463,366,0,443,465,475,498,559,492],
[532,429,414,557,0,486,459,612,603,487],
[474,472,445,535,514,0,523,585,525,499],
[517,504,502,525,541,477,0,639,602,479],
[421,487,363,502,388,415,361,0,574,495],
[426,406,364,441,397,475,398,426,0,521],
[445,431,462,508,513,501,521,505,479,0]])



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
result = np.append(np.array([10, 1000, 74, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,498,480,485,494,471,471,479,494,500],
[502,0,478,472,482,458,476,473,479,478],
[520,522,0,507,479,487,481,493,501,517],
[515,528,493,0,491,484,483,487,494,473],
[506,518,521,509,0,477,500,508,514,511],
[529,542,513,516,523,0,499,494,504,518],
[529,524,519,517,500,501,0,511,498,517],
[521,527,507,513,492,506,489,0,484,501],
[506,521,499,506,486,496,502,516,0,496],
[500,522,483,527,489,482,483,499,504,0]])



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
result = np.append(np.array([10, 1000, 75, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,511,471,531,500,498,479,512,497,479],
[489,0,444,524,496,450,529,478,514,516],
[529,556,0,542,502,498,535,552,510,505],
[469,476,458,0,465,469,525,489,450,498],
[500,504,498,535,0,514,521,550,534,514],
[502,550,502,531,486,0,537,507,471,508],
[521,471,465,475,479,463,0,466,486,528],
[488,522,448,511,450,493,534,0,501,492],
[503,486,490,550,466,529,514,499,0,500],
[521,484,495,502,486,492,472,508,500,0]])



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
result = np.append(np.array([10, 1000, 76, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,502,481,525,488,522,504,500,505,494],
[498,0,486,537,514,507,522,510,515,520],
[519,514,0,509,530,515,536,514,495,525],
[475,463,491,0,492,490,487,516,486,486],
[512,486,470,508,0,532,497,526,534,494],
[478,493,485,510,468,0,489,478,495,491],
[496,478,464,513,503,511,0,496,502,496],
[500,490,486,484,474,522,504,0,513,498],
[495,485,505,514,466,505,498,487,0,488],
[506,480,475,514,506,509,504,502,512,0]])



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
result = np.append(np.array([10, 1000, 77, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,488,533,524,510,491,509,511,507,547],
[512,0,498,506,520,484,482,496,481,493],
[467,502,0,531,524,469,507,476,503,509],
[476,494,469,0,506,451,481,464,479,504],
[490,480,476,494,0,485,509,488,473,489],
[509,516,531,549,515,0,513,520,491,525],
[491,518,493,519,491,487,0,511,491,505],
[489,504,524,536,512,480,489,0,508,522],
[493,519,497,521,527,509,509,492,0,529],
[453,507,491,496,511,475,495,478,471,0]])



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
result = np.append(np.array([10, 1000, 78, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,499,501,498,521,500,509,501,505,488],
[501,0,490,495,496,467,499,506,480,486],
[499,510,0,509,532,494,524,511,493,516],
[502,505,491,0,501,493,518,503,504,500],
[479,504,468,499,0,473,509,499,507,504],
[500,533,506,507,527,0,528,520,517,512],
[491,501,476,482,491,472,0,499,500,511],
[499,494,489,497,501,480,501,0,483,512],
[495,520,507,496,493,483,500,517,0,504],
[512,514,484,500,496,488,489,488,496,0]])



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
result = np.append(np.array([10, 1000, 79, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,481,488,493,478,480,488,510,482,485],
[519,0,492,503,491,461,518,513,510,467],
[512,508,0,501,505,469,518,497,504,474],
[507,497,499,0,497,489,492,503,510,485],
[522,509,495,503,0,512,529,542,513,485],
[520,539,531,511,488,0,513,510,525,505],
[512,482,482,508,471,487,0,506,492,492],
[490,487,503,497,458,490,494,0,501,494],
[518,490,496,490,487,475,508,499,0,488],
[515,533,526,515,515,495,508,506,512,0]])



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
result = np.append(np.array([10, 1000, 80, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,497,382,465,354,547,451,468,380,571],
[503,0,350,370,387,455,458,356,301,502],
[618,650,0,634,392,582,584,412,533,599],
[535,630,366,0,474,466,543,464,421,588],
[646,613,608,526,0,524,498,617,531,608],
[453,545,418,534,476,0,446,441,463,436],
[549,542,416,457,502,554,0,432,419,616],
[532,644,588,536,383,559,568,0,546,609],
[620,699,467,579,469,537,581,454,0,627],
[429,498,401,412,392,564,384,391,373,0]])



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
result = np.append(np.array([10, 1000, 81, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,481,469,498,488,485,485,495,476,495],
[519,0,493,513,489,499,510,488,506,495],
[531,507,0,505,481,501,523,519,491,526],
[502,487,495,0,474,496,497,496,481,503],
[512,511,519,526,0,505,512,505,472,514],
[515,501,499,504,495,0,498,513,499,491],
[515,490,477,503,488,502,0,491,496,532],
[505,512,481,504,495,487,509,0,503,517],
[524,494,509,519,528,501,504,497,0,526],
[505,505,474,497,486,509,468,483,474,0]])



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
result = np.append(np.array([10, 1000, 82, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,465,520,560,537,604,520,506,515,593],
[535,0,525,497,582,489,593,508,538,523],
[480,475,0,449,477,572,569,408,485,579],
[440,503,551,0,555,456,582,518,533,561],
[463,418,523,445,0,486,490,420,543,557],
[396,511,428,544,514,0,496,455,470,486],
[480,407,431,418,510,504,0,421,459,491],
[494,492,592,482,580,545,579,0,511,602],
[485,462,515,467,457,530,541,489,0,503],
[407,477,421,439,443,514,509,398,497,0]])



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
result = np.append(np.array([10, 1000, 83, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,520,502,491,542,440,490,453,478,491],
[480,0,479,486,494,520,467,499,522,495],
[498,521,0,428,546,514,504,508,482,472],
[509,514,572,0,562,489,504,482,483,489],
[458,506,454,438,0,451,452,445,430,444],
[560,480,486,511,549,0,473,449,490,503],
[510,533,496,496,548,527,0,470,470,508],
[547,501,492,518,555,551,530,0,505,535],
[522,478,518,517,570,510,530,495,0,524],
[509,505,528,511,556,497,492,465,476,0]])



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
result = np.append(np.array([10, 1000, 84, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,548,532,532,531,497,508,518,522,515],
[452,0,492,478,479,454,458,478,477,491],
[468,508,0,483,479,453,463,468,456,480],
[468,522,517,0,487,504,466,487,513,488],
[469,521,521,513,0,492,485,513,512,520],
[503,546,547,496,508,0,510,501,488,515],
[492,542,537,534,515,490,0,511,504,528],
[482,522,532,513,487,499,489,0,473,489],
[478,523,544,487,488,512,496,527,0,492],
[485,509,520,512,480,485,472,511,508,0]])



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
result = np.append(np.array([10, 1000, 85, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,454,460,527,593,483,521,508,441,467],
[546,0,482,516,523,424,488,491,448,483],
[540,518,0,499,635,453,562,501,557,517],
[473,484,501,0,634,469,566,529,524,519],
[407,477,365,366,0,358,565,467,383,454],
[517,576,547,531,642,0,596,531,494,501],
[479,512,438,434,435,404,0,432,389,477],
[492,509,499,471,533,469,568,0,475,529],
[559,552,443,476,617,506,611,525,0,543],
[533,517,483,481,546,499,523,471,457,0]])



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
result = np.append(np.array([10, 1000, 86, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,499,525,502,541,550,507,516,503,497],
[501,0,515,489,505,519,496,503,462,462],
[475,485,0,483,511,512,511,486,479,484],
[498,511,517,0,520,511,544,497,502,501],
[459,495,489,480,0,509,478,483,464,466],
[450,481,488,489,491,0,481,451,462,479],
[493,504,489,456,522,519,0,494,492,494],
[484,497,514,503,517,549,506,0,501,505],
[497,538,521,498,536,538,508,499,0,485],
[503,538,516,499,534,521,506,495,515,0]])



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
result = np.append(np.array([10, 1000, 87, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,536,541,533,569,492,574,491,545,541],
[464,0,529,491,487,451,532,455,469,501],
[459,471,0,509,536,471,527,485,496,497],
[467,509,491,0,520,505,531,519,512,525],
[431,513,464,480,0,458,530,441,497,478],
[508,549,529,495,542,0,584,498,565,567],
[426,468,473,469,470,416,0,431,465,491],
[509,545,515,481,559,502,569,0,522,530],
[455,531,504,488,503,435,535,478,0,506],
[459,499,503,475,522,433,509,470,494,0]])



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
result = np.append(np.array([10, 1000, 88, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,529,510,472,512,503,515,484,541,450],
[471,0,510,465,465,496,493,520,509,485],
[490,490,0,461,455,494,464,480,490,464],
[528,535,539,0,451,574,542,511,566,509],
[488,535,545,549,0,567,530,520,534,542],
[497,504,506,426,433,0,461,501,510,459],
[485,507,536,458,470,539,0,491,541,470],
[516,480,520,489,480,499,509,0,542,486],
[459,491,510,434,466,490,459,458,0,460],
[550,515,536,491,458,541,530,514,540,0]])



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
result = np.append(np.array([10, 1000, 89, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,406,509,389,529,499,472,435,433,455],
[594,0,560,510,567,590,540,541,466,569],
[491,440,0,496,558,474,478,486,503,548],
[611,490,504,0,592,546,542,515,480,531],
[471,433,442,408,0,513,510,424,490,456],
[501,410,526,454,487,0,457,465,436,499],
[528,460,522,458,490,543,0,491,514,485],
[565,459,514,485,576,535,509,0,486,532],
[567,534,497,520,510,564,486,514,0,515],
[545,431,452,469,544,501,515,468,485,0]])



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
result = np.append(np.array([10, 1000, 90, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,575,456,517,503,488,431,543,474,457],
[425,0,402,450,486,436,432,525,401,447],
[544,598,0,501,540,507,509,591,528,488],
[483,550,499,0,445,518,478,542,491,423],
[497,514,460,555,0,500,449,503,483,405],
[512,564,493,482,500,0,502,581,497,492],
[569,568,491,522,551,498,0,610,520,501],
[457,475,409,458,497,419,390,0,459,396],
[526,599,472,509,517,503,480,541,0,545],
[543,553,512,577,595,508,499,604,455,0]])



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
result = np.append(np.array([10, 1000, 91, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,501,475,487,520,508,529,505,546,514],
[499,0,498,506,535,505,528,505,536,514],
[525,502,0,542,532,522,514,520,525,500],
[513,494,458,0,474,474,521,482,500,499],
[480,465,468,526,0,529,492,490,506,498],
[492,495,478,526,471,0,498,488,520,519],
[471,472,486,479,508,502,0,509,515,495],
[495,495,480,518,510,512,491,0,510,522],
[454,464,475,500,494,480,485,490,0,483],
[486,486,500,501,502,481,505,478,517,0]])



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
result = np.append(np.array([10, 1000, 92, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,472,509,491,487,491,481,447,484,479],
[528,0,538,529,496,521,531,501,505,493],
[491,462,0,495,461,459,482,458,454,438],
[509,471,505,0,482,512,532,464,481,498],
[513,504,539,518,0,515,532,498,509,492],
[509,479,541,488,485,0,492,454,497,481],
[519,469,518,468,468,508,0,456,468,502],
[553,499,542,536,502,546,544,0,493,516],
[516,495,546,519,491,503,532,507,0,490],
[521,507,562,502,508,519,498,484,510,0]])



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
result = np.append(np.array([10, 1000, 93, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,495,513,526,517,529,509,505,523,489],
[505,0,492,483,486,475,480,484,486,458],
[487,508,0,500,503,488,502,505,507,487],
[474,517,500,0,480,468,472,501,509,456],
[483,514,497,520,0,485,489,496,503,473],
[471,525,512,532,515,0,495,508,516,512],
[491,520,498,528,511,505,0,508,538,494],
[495,516,495,499,504,492,492,0,523,459],
[477,514,493,491,497,484,462,477,0,491],
[511,542,513,544,527,488,506,541,509,0]])



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
result = np.append(np.array([10, 1000, 94, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,500,502,489,487,492,519,470,514,505],
[500,0,499,460,466,486,505,472,468,499],
[498,501,0,484,476,506,517,488,498,496],
[511,540,516,0,518,501,505,506,507,488],
[513,534,524,482,0,529,511,512,514,512],
[508,514,494,499,471,0,527,509,513,499],
[481,495,483,495,489,473,0,508,512,483],
[530,528,512,494,488,491,492,0,499,489],
[486,532,502,493,486,487,488,501,0,470],
[495,501,504,512,488,501,517,511,530,0]])



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
result = np.append(np.array([10, 1000, 95, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,510,490,497,464,491,545,504,503,517],
[490,0,492,490,500,512,524,495,529,526],
[510,508,0,474,502,506,538,500,538,540],
[503,510,526,0,518,475,520,474,537,520],
[536,500,498,482,0,484,531,475,536,528],
[509,488,494,525,516,0,538,490,520,510],
[455,476,462,480,469,462,0,439,478,483],
[496,505,500,526,525,510,561,0,544,530],
[497,471,462,463,464,480,522,456,0,485],
[483,474,460,480,472,490,517,470,515,0]])



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
result = np.append(np.array([10, 1000, 96, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,485,485,554,440,482,531,496,560,583],
[515,0,504,592,402,517,555,607,574,516],
[515,496,0,606,504,506,506,489,623,632],
[446,408,394,0,415,473,463,507,446,444],
[560,598,496,585,0,600,590,587,618,621],
[518,483,494,527,400,0,546,537,542,518],
[469,445,494,537,410,454,0,501,573,513],
[504,393,511,493,413,463,499,0,545,552],
[440,426,377,554,382,458,427,455,0,501],
[417,484,368,556,379,482,487,448,499,0]])



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
result = np.append(np.array([10, 1000, 97, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,440,447,450,506,455,467,472,475,487],
[560,0,516,620,537,557,538,543,568,499],
[553,484,0,520,551,620,519,545,588,563],
[550,380,480,0,510,564,442,491,461,432],
[494,463,449,490,0,529,535,536,446,431],
[545,443,380,436,471,0,455,542,404,410],
[533,462,481,558,465,545,0,553,522,480],
[528,457,455,509,464,458,447,0,471,405],
[525,432,412,539,554,596,478,529,0,521],
[513,501,437,568,569,590,520,595,479,0]])



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
result = np.append(np.array([10, 1000, 98, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,503,475,514,476,488,497,543,484,521],
[497,0,520,484,497,540,483,520,521,524],
[525,480,0,531,529,534,499,534,526,565],
[486,516,469,0,460,505,498,514,489,535],
[524,503,471,540,0,502,485,559,493,514],
[512,460,466,495,498,0,467,521,457,498],
[503,517,501,502,515,533,0,539,499,528],
[457,480,466,486,441,479,461,0,478,508],
[516,479,474,511,507,543,501,522,0,503],
[479,476,435,465,486,502,472,492,497,0]])



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
result = np.append(np.array([10, 1000, 99, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,497,466,484,514,499,503,480,498,537],
[503,0,493,488,510,511,517,514,482,549],
[534,507,0,513,527,499,507,520,526,548],
[516,512,487,0,513,517,504,508,499,537],
[486,490,473,487,0,505,476,486,488,552],
[501,489,501,483,495,0,527,520,503,556],
[497,483,493,496,524,473,0,489,499,525],
[520,486,480,492,514,480,511,0,506,523],
[502,518,474,501,512,497,501,494,0,522],
[463,451,452,463,448,444,475,477,478,0]])



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
result = np.append(np.array([10, 1000, 100, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,447,460,463,475,447,445,466,460,471],
[553,0,490,522,509,504,499,526,533,517],
[540,510,0,502,494,467,487,512,491,526],
[537,478,498,0,501,478,495,476,506,490],
[525,491,506,499,0,494,514,504,513,502],
[553,496,533,522,506,0,519,499,500,496],
[555,501,513,505,486,481,0,505,517,488],
[534,474,488,524,496,501,495,0,505,501],
[540,467,509,494,487,500,483,495,0,485],
[529,483,474,510,498,504,512,499,515,0]])



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
result = np.append(np.array([10, 1000, 101, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,546,457,513,511,531,526,468,507,525],
[454,0,434,482,436,469,462,449,436,439],
[543,566,0,541,492,526,497,516,574,540],
[487,518,459,0,457,514,474,438,529,460],
[489,564,508,543,0,540,508,467,528,538],
[469,531,474,486,460,0,467,457,513,457],
[474,538,503,526,492,533,0,483,516,519],
[532,551,484,562,533,543,517,0,581,517],
[493,564,426,471,472,487,484,419,0,494],
[475,561,460,540,462,543,481,483,506,0]])



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
result = np.append(np.array([10, 1000, 102, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,540,511,491,529,546,508,560,499,547],
[460,0,513,482,498,531,486,524,471,462],
[489,487,0,477,481,513,486,515,495,487],
[509,518,523,0,509,567,519,545,535,492],
[471,502,519,491,0,537,482,508,513,482],
[454,469,487,433,463,0,454,478,456,450],
[492,514,514,481,518,546,0,538,509,502],
[440,476,485,455,492,522,462,0,491,468],
[501,529,505,465,487,544,491,509,0,484],
[453,538,513,508,518,550,498,532,516,0]])



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
result = np.append(np.array([10, 1000, 103, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,474,491,485,463,497,476,507,482,506],
[526,0,501,514,465,518,515,497,501,458],
[509,499,0,507,455,534,488,510,492,468],
[515,486,493,0,460,532,497,491,491,486],
[537,535,545,540,0,557,516,535,522,495],
[503,482,466,468,443,0,478,480,484,464],
[524,485,512,503,484,522,0,495,525,474],
[493,503,490,509,465,520,505,0,513,467],
[518,499,508,509,478,516,475,487,0,482],
[494,542,532,514,505,536,526,533,518,0]])



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
result = np.append(np.array([10, 1000, 104, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,490,503,465,482,509,507,480,512,504],
[510,0,508,490,498,496,502,498,520,513],
[497,492,0,495,485,518,511,509,507,504],
[535,510,505,0,498,518,518,506,528,511],
[518,502,515,502,0,495,511,494,513,510],
[491,504,482,482,505,0,504,510,503,506],
[493,498,489,482,489,496,0,506,487,487],
[520,502,491,494,506,490,494,0,482,513],
[488,480,493,472,487,497,513,518,0,493],
[496,487,496,489,490,494,513,487,507,0]])



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
result = np.append(np.array([10, 1000, 105, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,446,543,535,476,533,464,527,543,560],
[554,0,523,564,388,495,445,592,563,603],
[457,477,0,552,436,527,397,490,553,473],
[465,436,448,0,381,485,411,437,510,498],
[524,612,564,619,0,482,496,556,542,542],
[467,505,473,515,518,0,533,470,663,653],
[536,555,603,589,504,467,0,554,607,587],
[473,408,510,563,444,530,446,0,536,618],
[457,437,447,490,458,337,393,464,0,498],
[440,397,527,502,458,347,413,382,502,0]])



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
result = np.append(np.array([10, 1000, 106, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,486,485,513,497,488,478,500,509,494],
[514,0,537,500,530,537,519,491,527,526],
[515,463,0,490,495,493,480,496,516,464],
[487,500,510,0,521,499,495,488,532,491],
[503,470,505,479,0,479,484,505,504,464],
[512,463,507,501,521,0,488,489,507,494],
[522,481,520,505,516,512,0,503,503,494],
[500,509,504,512,495,511,497,0,502,473],
[491,473,484,468,496,493,497,498,0,462],
[506,474,536,509,536,506,506,527,538,0]])



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
result = np.append(np.array([10, 1000, 107, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,547,433,412,461,423,479,482,390,439],
[453,0,438,443,425,431,435,490,490,372],
[567,562,0,497,553,501,595,541,565,493],
[588,557,503,0,599,573,590,557,531,483],
[539,575,447,401,0,471,499,519,524,438],
[577,569,499,427,529,0,521,581,554,451],
[521,565,405,410,501,479,0,481,533,449],
[518,510,459,443,481,419,519,0,495,473],
[610,510,435,469,476,446,467,505,0,518],
[561,628,507,517,562,549,551,527,482,0]])



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
result = np.append(np.array([10, 1000, 108, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,521,535,499,503,519,504,508,503,494],
[479,0,486,490,484,502,489,491,510,496],
[465,514,0,488,504,493,493,475,475,500],
[501,510,512,0,499,518,481,495,490,508],
[497,516,496,501,0,489,488,503,521,499],
[481,498,507,482,511,0,485,473,485,475],
[496,511,507,519,512,515,0,512,513,503],
[492,509,525,505,497,527,488,0,511,521],
[497,490,525,510,479,515,487,489,0,499],
[506,504,500,492,501,525,497,479,501,0]])



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
result = np.append(np.array([10, 1000, 109, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,526,505,504,564,533,539,503,584,456],
[474,0,536,451,478,502,543,495,585,448],
[495,464,0,495,482,510,521,537,538,450],
[496,549,505,0,468,558,532,517,551,530],
[436,522,518,532,0,574,504,494,602,461],
[467,498,490,442,426,0,453,449,510,495],
[461,457,479,468,496,547,0,436,538,452],
[497,505,463,483,506,551,564,0,560,498],
[416,415,462,449,398,490,462,440,0,383],
[544,552,550,470,539,505,548,502,617,0]])



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
result = np.append(np.array([10, 1000, 110, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,531,517,514,543,491,557,498,524,574],
[469,0,486,513,559,494,559,525,512,550],
[483,514,0,513,530,500,552,466,477,531],
[486,487,487,0,538,502,567,507,522,547],
[457,441,470,462,0,449,503,472,470,510],
[509,506,500,498,551,0,559,528,533,570],
[443,441,448,433,497,441,0,455,461,489],
[502,475,534,493,528,472,545,0,537,550],
[476,488,523,478,530,467,539,463,0,544],
[426,450,469,453,490,430,511,450,456,0]])



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
result = np.append(np.array([10, 1000, 111, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,501,478,511,514,515,491,516,519,509],
[499,0,493,524,516,520,507,502,520,503],
[522,507,0,517,508,527,514,492,520,506],
[489,476,483,0,504,528,486,486,514,486],
[486,484,492,496,0,515,470,475,517,486],
[485,480,473,472,485,0,477,486,496,486],
[509,493,486,514,530,523,0,492,533,504],
[484,498,508,514,525,514,508,0,520,504],
[481,480,480,486,483,504,467,480,0,490],
[491,497,494,514,514,514,496,496,510,0]])



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
result = np.append(np.array([10, 1000, 112, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,505,510,523,526,519,495,498,512,514],
[495,0,499,510,508,517,514,507,504,516],
[490,501,0,513,509,521,497,521,504,521],
[477,490,487,0,530,506,489,510,490,496],
[474,492,491,470,0,504,487,503,491,527],
[481,483,479,494,496,0,483,498,489,500],
[505,486,503,511,513,517,0,501,510,516],
[502,493,479,490,497,502,499,0,484,484],
[488,496,496,510,509,511,490,516,0,515],
[486,484,479,504,473,500,484,516,485,0]])



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
result = np.append(np.array([10, 1000, 113, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,546,516,514,540,492,529,498,495,491],
[454,0,473,479,511,472,469,471,463,472],
[484,527,0,520,536,512,517,476,490,478],
[486,521,480,0,517,504,515,487,488,501],
[460,489,464,483,0,453,481,445,484,448],
[508,528,488,496,547,0,495,489,508,495],
[471,531,483,485,519,505,0,480,457,463],
[502,529,524,513,555,511,520,0,523,488],
[505,537,510,512,516,492,543,477,0,487],
[509,528,522,499,552,505,537,512,513,0]])



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
result = np.append(np.array([10, 1000, 114, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,497,475,488,492,484,493,465,506,509],
[503,0,514,508,495,489,526,501,516,522],
[525,486,0,510,499,494,537,504,503,494],
[512,492,490,0,480,482,515,490,529,500],
[508,505,501,520,0,521,518,499,486,519],
[516,511,506,518,479,0,524,464,496,494],
[507,474,463,485,482,476,0,473,467,505],
[535,499,496,510,501,536,527,0,544,525],
[494,484,497,471,514,504,533,456,0,514],
[491,478,506,500,481,506,495,475,486,0]])



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
result = np.append(np.array([10, 1000, 115, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,501,481,498,518,495,526,499,510,470],
[499,0,462,478,490,512,498,497,518,476],
[519,538,0,523,515,504,512,521,514,489],
[502,522,477,0,516,499,515,499,522,501],
[482,510,485,484,0,501,527,513,521,482],
[505,488,496,501,499,0,496,498,509,465],
[474,502,488,485,473,504,0,494,502,494],
[501,503,479,501,487,502,506,0,508,481],
[490,482,486,478,479,491,498,492,0,474],
[530,524,511,499,518,535,506,519,526,0]])



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
result = np.append(np.array([10, 1000, 116, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,473,472,482,500,498,476,490,515,507],
[527,0,489,502,513,503,472,516,491,507],
[528,511,0,492,512,518,498,519,524,514],
[518,498,508,0,528,518,503,515,517,522],
[500,487,488,472,0,491,489,504,505,496],
[502,497,482,482,509,0,500,501,534,502],
[524,528,502,497,511,500,0,508,522,520],
[510,484,481,485,496,499,492,0,508,506],
[485,509,476,483,495,466,478,492,0,493],
[493,493,486,478,504,498,480,494,507,0]])



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
result = np.append(np.array([10, 1000, 117, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,578,539,476,551,537,514,578,544,497],
[422,0,559,550,536,619,573,610,469,461],
[461,441,0,481,502,497,514,532,489,451],
[524,450,519,0,518,530,519,508,546,506],
[449,464,498,482,0,510,505,565,474,539],
[463,381,503,470,490,0,467,516,418,419],
[486,427,486,481,495,533,0,512,477,449],
[422,390,468,492,435,484,488,0,383,442],
[456,531,511,454,526,582,523,617,0,498],
[503,539,549,494,461,581,551,558,502,0]])



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
result = np.append(np.array([10, 1000, 118, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,482,503,691,534,635,559,457,634,680],
[518,0,465,643,538,521,626,473,519,619],
[497,535,0,577,550,529,504,445,638,623],
[309,357,423,0,448,464,386,369,488,525],
[466,462,450,552,0,537,368,434,535,684],
[365,479,471,536,463,0,506,389,512,612],
[441,374,496,614,632,494,0,431,586,685],
[543,527,555,631,566,611,569,0,491,743],
[366,481,362,512,465,488,414,509,0,514],
[320,381,377,475,316,388,315,257,486,0]])



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
result = np.append(np.array([10, 1000, 119, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,496,463,480,487,448,507,482,504,496],
[504,0,473,487,491,485,513,492,502,527],
[537,527,0,507,490,499,531,507,547,531],
[520,513,493,0,487,486,512,496,541,503],
[513,509,510,513,0,493,535,541,533,526],
[552,515,501,514,507,0,545,495,539,534],
[493,487,469,488,465,455,0,483,518,507],
[518,508,493,504,459,505,517,0,520,504],
[496,498,453,459,467,461,482,480,0,504],
[504,473,469,497,474,466,493,496,496,0]])



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
result = np.append(np.array([10, 1000, 120, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,508,513,526,549,502,508,528,514,451],
[492,0,476,507,507,499,598,518,573,519],
[487,524,0,540,520,459,531,448,560,466],
[474,493,460,0,453,482,477,475,513,395],
[451,493,480,547,0,464,493,489,495,511],
[498,501,541,518,536,0,503,517,532,501],
[492,402,469,523,507,497,0,498,532,466],
[472,482,552,525,511,483,502,0,528,511],
[486,427,440,487,505,468,468,472,0,430],
[549,481,534,605,489,499,534,489,570,0]])



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
result = np.append(np.array([10, 1000, 121, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,521,525,527,518,532,492,509,543,532],
[479,0,463,473,490,489,457,504,520,477],
[475,537,0,522,546,477,509,498,474,489],
[473,527,478,0,515,514,462,500,475,501],
[482,510,454,485,0,483,455,485,495,486],
[468,511,523,486,517,0,487,534,522,527],
[508,543,491,538,545,513,0,531,504,529],
[491,496,502,500,515,466,469,0,501,511],
[457,480,526,525,505,478,496,499,0,491],
[468,523,511,499,514,473,471,489,509,0]])



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
result = np.append(np.array([10, 1000, 122, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,501,528,542,504,507,474,512,526,517],
[499,0,487,532,493,506,493,511,546,504],
[472,513,0,525,532,507,503,557,546,532],
[458,468,475,0,485,491,486,489,541,509],
[496,507,468,515,0,505,500,512,538,508],
[493,494,493,509,495,0,450,481,505,507],
[526,507,497,514,500,550,0,503,541,534],
[488,489,443,511,488,519,497,0,535,536],
[474,454,454,459,462,495,459,465,0,477],
[483,496,468,491,492,493,466,464,523,0]])



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
result = np.append(np.array([10, 1000, 123, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,513,496,525,488,469,489,475,582,471],
[487,0,490,527,492,499,510,456,543,498],
[504,510,0,521,433,453,471,442,522,505],
[475,473,479,0,440,419,468,443,496,487],
[512,508,567,560,0,537,483,504,571,523],
[531,501,547,581,463,0,497,453,587,509],
[511,490,529,532,517,503,0,478,532,511],
[525,544,558,557,496,547,522,0,559,559],
[418,457,478,504,429,413,468,441,0,423],
[529,502,495,513,477,491,489,441,577,0]])



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
result = np.append(np.array([10, 1000, 124, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,482,479,471,489,505,483,484,520,507],
[518,0,540,539,518,500,554,547,515,545],
[521,460,0,486,465,429,497,521,477,497],
[529,461,514,0,490,477,517,528,478,529],
[511,482,535,510,0,503,512,508,528,543],
[495,500,571,523,497,0,541,536,544,566],
[517,446,503,483,488,459,0,528,470,508],
[516,453,479,472,492,464,472,0,523,526],
[480,485,523,522,472,456,530,477,0,518],
[493,455,503,471,457,434,492,474,482,0]])



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
result = np.append(np.array([10, 1000, 125, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,530,506,509,501,508,502,520,498,500],
[470,0,489,479,478,479,478,485,461,471],
[494,511,0,488,490,481,495,491,479,481],
[491,521,512,0,489,488,515,500,476,501],
[499,522,510,511,0,490,485,490,501,514],
[492,521,519,512,510,0,515,510,502,501],
[498,522,505,485,515,485,0,499,471,510],
[480,515,509,500,510,490,501,0,478,485],
[502,539,521,524,499,498,529,522,0,496],
[500,529,519,499,486,499,490,515,504,0]])



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
result = np.append(np.array([10, 1000, 126, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,491,496,484,492,485,503,505,473,481],
[509,0,503,514,524,501,534,518,508,491],
[504,497,0,519,509,503,520,520,495,485],
[516,486,481,0,503,499,524,521,503,491],
[508,476,491,497,0,466,501,513,476,486],
[515,499,497,501,534,0,534,537,500,502],
[497,466,480,476,499,466,0,486,457,461],
[495,482,480,479,487,463,514,0,457,455],
[527,492,505,497,524,500,543,543,0,477],
[519,509,515,509,514,498,539,545,523,0]])



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
result = np.append(np.array([10, 1000, 127, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,714,554,546,434,673,526,779,673,602],
[286,0,405,422,258,507,524,505,392,432],
[446,595,0,441,422,568,536,517,484,746],
[454,578,559,0,375,563,536,595,498,564],
[566,742,578,625,0,767,492,661,624,601],
[327,493,432,437,233,0,458,532,495,550],
[474,476,464,464,508,542,0,577,471,690],
[221,495,483,405,339,468,423,0,655,573],
[327,608,516,502,376,505,529,345,0,558],
[398,568,254,436,399,450,310,427,442,0]])



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
result = np.append(np.array([10, 1000, 128, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,479,467,504,482,513,500,495,512,501],
[521,0,487,493,502,505,522,504,507,477],
[533,513,0,519,513,521,542,545,538,499],
[496,507,481,0,494,510,501,499,505,493],
[518,498,487,506,0,506,516,524,516,517],
[487,495,479,490,494,0,514,509,501,492],
[500,478,458,499,484,486,0,481,509,474],
[505,496,455,501,476,491,519,0,511,478],
[488,493,462,495,484,499,491,489,0,469],
[499,523,501,507,483,508,526,522,531,0]])



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
result = np.append(np.array([10, 1000, 129, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,526,477,491,542,485,507,554,512,592],
[474,0,501,510,512,547,538,561,528,558],
[523,499,0,471,535,506,538,543,503,520],
[509,490,529,0,511,514,495,550,521,571],
[458,488,465,489,0,479,474,528,500,531],
[515,453,494,486,521,0,473,530,512,549],
[493,462,462,505,526,527,0,534,511,550],
[446,439,457,450,472,470,466,0,471,510],
[488,472,497,479,500,488,489,529,0,528],
[408,442,480,429,469,451,450,490,472,0]])



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
result = np.append(np.array([10, 1000, 130, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,473,500,506,508,484,492,494,489,525],
[527,0,539,519,535,509,532,519,499,545],
[500,461,0,484,498,487,499,514,498,529],
[494,481,516,0,505,511,494,521,492,549],
[492,465,502,495,0,477,482,500,483,507],
[516,491,513,489,523,0,527,528,517,559],
[508,468,501,506,518,473,0,537,480,541],
[506,481,486,479,500,472,463,0,493,493],
[511,501,502,508,517,483,520,507,0,534],
[475,455,471,451,493,441,459,507,466,0]])



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
result = np.append(np.array([10, 1000, 131, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,489,498,494,495,514,539,483,492,493],
[511,0,488,499,466,485,492,449,504,461],
[502,512,0,472,496,473,524,497,498,464],
[506,501,528,0,517,474,498,506,537,499],
[505,534,504,483,0,506,497,483,529,465],
[486,515,527,526,494,0,540,487,489,516],
[461,508,476,502,503,460,0,481,503,475],
[517,551,503,494,517,513,519,0,530,488],
[508,496,502,463,471,511,497,470,0,472],
[507,539,536,501,535,484,525,512,528,0]])



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
result = np.append(np.array([10, 1000, 132, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,473,495,431,426,521,502,437,522,492],
[527,0,478,494,504,579,525,476,543,507],
[505,522,0,460,523,538,488,481,546,506],
[569,506,540,0,526,570,525,519,587,497],
[574,496,477,474,0,532,505,506,547,549],
[479,421,462,430,468,0,466,434,507,474],
[498,475,512,475,495,534,0,496,545,495],
[563,524,519,481,494,566,504,0,543,530],
[478,457,454,413,453,493,455,457,0,455],
[508,493,494,503,451,526,505,470,545,0]])



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
result = np.append(np.array([10, 1000, 133, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,490,485,496,486,481,496,495,502,508],
[510,0,492,506,499,501,495,512,531,517],
[515,508,0,537,504,483,510,514,515,535],
[504,494,463,0,500,511,495,479,501,518],
[514,501,496,500,0,485,513,497,511,526],
[519,499,517,489,515,0,515,511,535,532],
[504,505,490,505,487,485,0,503,530,510],
[505,488,486,521,503,489,497,0,517,515],
[498,469,485,499,489,465,470,483,0,507],
[492,483,465,482,474,468,490,485,493,0]])



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
result = np.append(np.array([10, 1000, 134, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,497,504,535,514,540,533,492,537,512],
[503,0,519,556,522,509,522,520,540,488],
[496,481,0,496,488,483,509,509,498,487],
[465,444,504,0,495,487,466,463,503,456],
[486,478,512,505,0,520,499,498,504,498],
[460,491,517,513,480,0,508,497,494,484],
[467,478,491,534,501,492,0,483,518,489],
[508,480,491,537,502,503,517,0,490,511],
[463,460,502,497,496,506,482,510,0,475],
[488,512,513,544,502,516,511,489,525,0]])



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
result = np.append(np.array([10, 1000, 135, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,463,507,506,502,516,500,504,486,513],
[537,0,513,518,502,521,498,529,512,522],
[493,487,0,510,494,501,493,518,494,496],
[494,482,490,0,498,523,505,507,492,508],
[498,498,506,502,0,517,505,495,492,493],
[484,479,499,477,483,0,479,499,473,494],
[500,502,507,495,495,521,0,516,501,501],
[496,471,482,493,505,501,484,0,484,496],
[514,488,506,508,508,527,499,516,0,522],
[487,478,504,492,507,506,499,504,478,0]])



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
result = np.append(np.array([10, 1000, 136, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,481,509,478,519,491,457,503,480,490],
[519,0,531,480,478,506,459,515,483,491],
[491,469,0,476,475,464,474,506,484,497],
[522,520,524,0,494,488,454,521,498,503],
[481,522,525,506,0,479,508,501,464,512],
[509,494,536,512,521,0,426,513,485,505],
[543,541,526,546,492,574,0,545,528,544],
[497,485,494,479,499,487,455,0,474,505],
[520,517,516,502,536,515,472,526,0,505],
[510,509,503,497,488,495,456,495,495,0]])



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
result = np.append(np.array([10, 1000, 137, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,451,453,501,452,486,456,464,460,473],
[549,0,479,528,494,556,506,497,501,520],
[547,521,0,527,505,541,520,521,475,498],
[499,472,473,0,454,505,486,494,483,464],
[548,506,495,546,0,531,520,512,526,502],
[514,444,459,495,469,0,482,469,471,460],
[544,494,480,514,480,518,0,496,460,478],
[536,503,479,506,488,531,504,0,477,517],
[540,499,525,517,474,529,540,523,0,519],
[527,480,502,536,498,540,522,483,481,0]])



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
result = np.append(np.array([10, 1000, 138, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,495,470,489,525,497,482,491,519,504],
[505,0,502,502,522,516,506,488,510,488],
[530,498,0,492,517,520,486,466,509,517],
[511,498,508,0,536,524,503,501,510,503],
[475,478,483,464,0,500,479,476,512,506],
[503,484,480,476,500,0,478,472,497,512],
[518,494,514,497,521,522,0,523,541,502],
[509,512,534,499,524,528,477,0,508,532],
[481,490,491,490,488,503,459,492,0,491],
[496,512,483,497,494,488,498,468,509,0]])



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
result = np.append(np.array([10, 1000, 139, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,494,427,448,443,420,449,411,492,475],
[506,0,470,498,439,469,457,472,511,473],
[573,530,0,507,441,457,445,470,507,496],
[552,502,493,0,434,488,433,464,459,478],
[557,561,559,566,0,525,494,578,570,517],
[580,531,543,512,475,0,499,465,562,493],
[551,543,555,567,506,501,0,530,565,468],
[589,528,530,536,422,535,470,0,566,489],
[508,489,493,541,430,438,435,434,0,448],
[525,527,504,522,483,507,532,511,552,0]])



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
result = np.append(np.array([10, 1000, 140, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,538,541,487,538,511,494,520,497,525],
[462,0,510,485,504,489,476,472,488,496],
[459,490,0,483,482,468,468,477,461,488],
[513,515,517,0,504,513,492,505,507,514],
[462,496,518,496,0,492,488,476,487,497],
[489,511,532,487,508,0,512,507,497,518],
[506,524,532,508,512,488,0,492,515,516],
[480,528,523,495,524,493,508,0,490,510],
[503,512,539,493,513,503,485,510,0,503],
[475,504,512,486,503,482,484,490,497,0]])



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
result = np.append(np.array([10, 1000, 141, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,490,576,507,522,518,504,519,531,506],
[510,0,570,517,477,520,521,500,564,513],
[424,430,0,447,441,444,481,416,496,445],
[493,483,553,0,488,528,495,425,452,505],
[478,523,559,512,0,516,499,461,561,505],
[482,480,556,472,484,0,481,477,497,474],
[496,479,519,505,501,519,0,495,498,519],
[481,500,584,575,539,523,505,0,507,528],
[469,436,504,548,439,503,502,493,0,487],
[494,487,555,495,495,526,481,472,513,0]])



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
result = np.append(np.array([10, 1000, 142, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,590,551,563,499,520,507,529,527,518],
[410,0,493,476,459,401,491,473,395,468],
[449,507,0,502,481,463,487,495,441,467],
[437,524,498,0,514,474,471,530,421,481],
[501,541,519,486,0,472,517,487,464,492],
[480,599,537,526,528,0,566,554,473,536],
[493,509,513,529,483,434,0,523,484,465],
[471,527,505,470,513,446,477,0,449,453],
[473,605,559,579,536,527,516,551,0,576],
[482,532,533,519,508,464,535,547,424,0]])



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
result = np.append(np.array([10, 1000, 143, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,497,510,488,483,492,478,524,491,472],
[503,0,521,495,520,497,492,519,503,504],
[490,479,0,482,512,475,498,484,472,473],
[512,505,518,0,506,488,475,520,493,501],
[517,480,488,494,0,514,499,514,486,484],
[508,503,525,512,486,0,474,519,485,495],
[522,508,502,525,501,526,0,526,494,518],
[476,481,516,480,486,481,474,0,495,482],
[509,497,528,507,514,515,506,505,0,486],
[528,496,527,499,516,505,482,518,514,0]])



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
result = np.append(np.array([10, 1000, 144, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,500,492,514,510,498,511,491,507,484],
[500,0,494,538,506,510,512,490,511,498],
[508,506,0,534,519,516,513,502,514,491],
[486,462,466,0,492,494,489,472,517,497],
[490,494,481,508,0,486,488,476,488,472],
[502,490,484,506,514,0,472,469,496,505],
[489,488,487,511,512,528,0,480,516,511],
[509,510,498,528,524,531,520,0,541,514],
[493,489,486,483,512,504,484,459,0,503],
[516,502,509,503,528,495,489,486,497,0]])



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
result = np.append(np.array([10, 1000, 145, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,511,505,475,478,481,483,491,477,464],
[489,0,508,501,485,476,489,477,475,485],
[495,492,0,487,479,471,482,493,471,476],
[525,499,513,0,495,521,504,521,492,503],
[522,515,521,505,0,494,499,510,482,500],
[519,524,529,479,506,0,518,505,502,506],
[517,511,518,496,501,482,0,495,480,500],
[509,523,507,479,490,495,505,0,477,505],
[523,525,529,508,518,498,520,523,0,513],
[536,515,524,497,500,494,500,495,487,0]])



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
result = np.append(np.array([10, 1000, 146, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,496,478,512,483,494,470,513,507,516],
[504,0,514,504,519,523,481,482,495,495],
[522,486,0,477,504,502,507,478,503,480],
[488,496,523,0,500,504,493,484,509,515],
[517,481,496,500,0,484,486,460,490,476],
[506,477,498,496,516,0,485,477,486,476],
[530,519,493,507,514,515,0,482,510,490],
[487,518,522,516,540,523,518,0,507,511],
[493,505,497,491,510,514,490,493,0,492],
[484,505,520,485,524,524,510,489,508,0]])



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
result = np.append(np.array([10, 1000, 147, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,469,512,528,456,508,542,506,526,486],
[531,0,542,526,503,518,535,498,564,477],
[488,458,0,501,457,510,496,499,548,486],
[472,474,499,0,439,519,457,452,474,481],
[544,497,543,561,0,535,511,491,554,547],
[492,482,490,481,465,0,495,475,534,525],
[458,465,504,543,489,505,0,488,517,483],
[494,502,501,548,509,525,512,0,532,537],
[474,436,452,526,446,466,483,468,0,491],
[514,523,514,519,453,475,517,463,509,0]])



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
result = np.append(np.array([10, 1000, 148, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,507,518,500,510,513,466,503,473,470],
[493,0,505,552,554,568,508,504,534,530],
[482,495,0,531,503,545,484,524,530,521],
[500,448,469,0,480,503,448,451,495,507],
[490,446,497,520,0,554,398,459,519,454],
[487,432,455,497,446,0,455,394,458,478],
[534,492,516,552,602,545,0,517,538,540],
[497,496,476,549,541,606,483,0,523,532],
[527,466,470,505,481,542,462,477,0,513],
[530,470,479,493,546,522,460,468,487,0]])



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
result = np.append(np.array([10, 1000, 149, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,510,472,621,421,573,521,575,750,538],
[490,0,481,636,532,397,659,543,711,615],
[528,519,0,615,404,378,423,596,736,584],
[379,364,385,0,362,401,443,410,655,535],
[579,468,596,638,0,531,581,564,748,557],
[427,603,622,599,469,0,538,659,640,487],
[479,341,577,557,419,462,0,533,576,447],
[425,457,404,590,436,341,467,0,571,588],
[250,289,264,345,252,360,424,429,0,339],
[462,385,416,465,443,513,553,412,661,0]])



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
result = np.append(np.array([10, 1000, 150, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,476,484,490,489,471,467,502,485,485],
[524,0,492,510,495,515,480,492,501,491],
[516,508,0,501,470,546,511,499,484,491],
[510,490,499,0,509,542,513,487,502,524],
[511,505,530,491,0,521,489,503,499,467],
[529,485,454,458,479,0,461,471,511,484],
[533,520,489,487,511,539,0,499,508,504],
[498,508,501,513,497,529,501,0,493,497],
[515,499,516,498,501,489,492,507,0,511],
[515,509,509,476,533,516,496,503,489,0]])



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
result = np.append(np.array([10, 1000, 151, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,497,509,532,546,521,525,498,521,559],
[503,0,526,518,517,520,561,531,514,500],
[491,474,0,494,540,494,518,515,528,529],
[468,482,506,0,512,490,514,487,514,523],
[454,483,460,488,0,467,516,489,479,508],
[479,480,506,510,533,0,534,515,529,527],
[475,439,482,486,484,466,0,503,481,509],
[502,469,485,513,511,485,497,0,501,520],
[479,486,472,486,521,471,519,499,0,502],
[441,500,471,477,492,473,491,480,498,0]])



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
result = np.append(np.array([10, 1000, 152, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,478,481,452,497,499,477,504,452,479],
[522,0,514,489,505,498,484,541,489,463],
[519,486,0,478,534,483,498,508,496,445],
[548,511,522,0,497,509,523,584,526,515],
[503,495,466,503,0,506,465,527,512,486],
[501,502,517,491,494,0,486,535,520,489],
[523,516,502,477,535,514,0,540,497,456],
[496,459,492,416,473,465,460,0,449,464],
[548,511,504,474,488,480,503,551,0,467],
[521,537,555,485,514,511,544,536,533,0]])



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
result = np.append(np.array([10, 1000, 153, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,508,512,502,508,518,479,529,528,549],
[492,0,546,555,503,517,538,503,533,513],
[488,454,0,467,469,490,469,500,484,487],
[498,445,533,0,496,478,477,510,465,509],
[492,497,531,504,0,525,503,524,497,513],
[482,483,510,522,475,0,482,487,487,527],
[521,462,531,523,497,518,0,514,490,515],
[471,497,500,490,476,513,486,0,486,518],
[472,467,516,535,503,513,510,514,0,502],
[451,487,513,491,487,473,485,482,498,0]])



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
result = np.append(np.array([10, 1000, 154, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,524,505,472,493,533,527,491,488,499],
[476,0,514,494,482,514,498,475,500,479],
[495,486,0,462,498,479,505,469,475,481],
[528,506,538,0,503,572,555,481,511,527],
[507,518,502,497,0,536,510,501,498,490],
[467,486,521,428,464,0,454,444,472,456],
[473,502,495,445,490,546,0,453,484,463],
[509,525,531,519,499,556,547,0,500,512],
[512,500,525,489,502,528,516,500,0,510],
[501,521,519,473,510,544,537,488,490,0]])



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
result = np.append(np.array([10, 1000, 155, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,511,529,516,518,527,632,530,445,442],
[489,0,422,435,455,436,544,432,391,424],
[471,578,0,556,495,493,575,499,447,417],
[484,565,444,0,443,454,610,484,378,431],
[482,545,505,557,0,548,633,460,478,556],
[473,564,507,546,452,0,600,517,391,468],
[368,456,425,390,367,400,0,352,407,335],
[470,568,501,516,540,483,648,0,403,440],
[555,609,553,622,522,609,593,597,0,468],
[558,576,583,569,444,532,665,560,532,0]])



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
result = np.append(np.array([10, 1000, 156, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,484,498,509,534,491,504,530,492,501],
[516,0,486,545,539,503,519,539,499,505],
[502,514,0,523,507,499,510,522,488,474],
[491,455,477,0,489,456,484,498,478,478],
[466,461,493,511,0,475,491,521,503,494],
[509,497,501,544,525,0,490,520,498,501],
[496,481,490,516,509,510,0,532,492,477],
[470,461,478,502,479,480,468,0,447,471],
[508,501,512,522,497,502,508,553,0,497],
[499,495,526,522,506,499,523,529,503,0]])



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
result = np.append(np.array([10, 1000, 157, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,509,479,514,501,501,454,519,511,524],
[491,0,528,474,498,526,477,502,498,503],
[521,472,0,484,481,516,453,525,504,468],
[486,526,516,0,486,520,500,533,522,525],
[499,502,519,514,0,539,485,510,516,518],
[499,474,484,480,461,0,457,489,486,530],
[546,523,547,500,515,543,0,514,531,551],
[481,498,475,467,490,511,486,0,488,480],
[489,502,496,478,484,514,469,512,0,516],
[476,497,532,475,482,470,449,520,484,0]])



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
result = np.append(np.array([10, 1000, 158, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,447,557,440,520,501,400,498,337,517],
[553,0,543,525,587,463,450,520,435,515],
[443,457,0,449,452,490,385,433,343,466],
[560,475,551,0,506,553,463,484,414,595],
[480,413,548,494,0,534,449,405,508,477],
[499,537,510,447,466,0,369,525,417,590],
[600,550,615,537,551,631,0,484,478,593],
[502,480,567,516,595,475,516,0,475,551],
[663,565,657,586,492,583,522,525,0,595],
[483,485,534,405,523,410,407,449,405,0]])



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
result = np.append(np.array([10, 1000, 159, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,481,518,515,491,498,516,486,490,496],
[519,0,523,491,517,500,518,488,504,525],
[482,477,0,489,452,479,496,460,475,491],
[485,509,511,0,481,477,505,478,491,488],
[509,483,548,519,0,482,526,482,537,520],
[502,500,521,523,518,0,544,500,500,533],
[484,482,504,495,474,456,0,480,486,499],
[514,512,540,522,518,500,520,0,533,527],
[510,496,525,509,463,500,514,467,0,526],
[504,475,509,512,480,467,501,473,474,0]])



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
result = np.append(np.array([10, 1000, 160, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,498,471,478,464,447,465,460,475,455],
[502,0,500,482,492,479,488,479,509,501],
[529,500,0,505,480,506,496,469,516,488],
[522,518,495,0,500,479,515,490,511,491],
[536,508,520,500,0,475,483,502,497,481],
[553,521,494,521,525,0,495,504,504,493],
[535,512,504,485,517,505,0,486,507,481],
[540,521,531,510,498,496,514,0,521,500],
[525,491,484,489,503,496,493,479,0,481],
[545,499,512,509,519,507,519,500,519,0]])



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
result = np.append(np.array([10, 1000, 161, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,532,505,493,506,507,469,461,509,532],
[468,0,506,456,463,475,498,461,496,481],
[495,494,0,417,471,465,454,475,472,476],
[507,544,583,0,497,542,487,510,526,506],
[494,537,529,503,0,484,497,507,472,480],
[493,525,535,458,516,0,501,481,497,500],
[531,502,546,513,503,499,0,507,508,508],
[539,539,525,490,493,519,493,0,515,517],
[491,504,528,474,528,503,492,485,0,507],
[468,519,524,494,520,500,492,483,493,0]])



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
result = np.append(np.array([10, 1000, 162, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,497,472,513,491,494,503,523,513,499],
[503,0,489,525,499,483,505,489,476,498],
[528,511,0,501,496,518,532,550,539,486],
[487,475,499,0,504,474,499,534,510,509],
[509,501,504,496,0,524,508,494,526,496],
[506,517,482,526,476,0,534,520,482,473],
[497,495,468,501,492,466,0,500,499,469],
[477,511,450,466,506,480,500,0,503,484],
[487,524,461,490,474,518,501,497,0,504],
[501,502,514,491,504,527,531,516,496,0]])



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
result = np.append(np.array([10, 1000, 163, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,467,475,503,463,495,491,477,497,514],
[533,0,499,526,501,512,507,533,511,527],
[525,501,0,533,477,462,529,477,503,496],
[497,474,467,0,471,488,507,481,466,510],
[537,499,523,529,0,530,526,496,511,529],
[505,488,538,512,470,0,478,501,494,506],
[509,493,471,493,474,522,0,491,491,514],
[523,467,523,519,504,499,509,0,496,536],
[503,489,497,534,489,506,509,504,0,495],
[486,473,504,490,471,494,486,464,505,0]])



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
result = np.append(np.array([10, 1000, 164, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,480,545,442,521,476,549,475,520,492],
[520,0,550,478,482,514,515,510,487,527],
[455,450,0,446,476,470,513,467,490,418],
[558,522,554,0,518,576,584,519,468,539],
[479,518,524,482,0,494,554,496,494,481],
[524,486,530,424,506,0,482,509,512,491],
[451,485,487,416,446,518,0,471,499,452],
[525,490,533,481,504,491,529,0,485,497],
[480,513,510,532,506,488,501,515,0,500],
[508,473,582,461,519,509,548,503,500,0]])



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
result = np.append(np.array([10, 1000, 165, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,434,473,523,450,440,418,413,413,475],
[566,0,559,527,478,505,482,464,456,523],
[527,441,0,562,442,472,489,461,427,504],
[477,473,438,0,430,422,434,423,409,472],
[550,522,558,570,0,530,481,520,466,504],
[560,495,528,578,470,0,471,463,463,542],
[582,518,511,566,519,529,0,528,500,568],
[587,536,539,577,480,537,472,0,467,544],
[587,544,573,591,534,537,500,533,0,559],
[525,477,496,528,496,458,432,456,441,0]])



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
result = np.append(np.array([10, 1000, 166, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,478,498,497,476,450,489,463,513,461],
[522,0,514,486,505,506,508,505,545,519],
[502,486,0,479,465,474,467,468,499,473],
[503,514,521,0,508,487,496,471,492,489],
[524,495,535,492,0,490,496,491,520,501],
[550,494,526,513,510,0,502,481,522,509],
[511,492,533,504,504,498,0,492,524,478],
[537,495,532,529,509,519,508,0,535,490],
[487,455,501,508,480,478,476,465,0,474],
[539,481,527,511,499,491,522,510,526,0]])



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
result = np.append(np.array([10, 1000, 167, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,524,545,495,507,480,524,525,500,519],
[476,0,524,477,479,481,495,519,494,499],
[455,476,0,478,453,471,487,464,448,457],
[505,523,522,0,498,493,494,526,490,473],
[493,521,547,502,0,500,512,524,495,494],
[520,519,529,507,500,0,505,524,520,504],
[476,505,513,506,488,495,0,504,512,488],
[475,481,536,474,476,476,496,0,490,469],
[500,506,552,510,505,480,488,510,0,494],
[481,501,543,527,506,496,512,531,506,0]])



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
result = np.append(np.array([10, 1000, 168, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,480,503,485,508,512,477,495,477,469],
[520,0,496,515,494,504,466,471,464,502],
[497,504,0,546,477,475,505,495,469,451],
[515,485,454,0,503,480,483,479,477,483],
[492,506,523,497,0,511,488,483,505,509],
[488,496,525,520,489,0,526,506,470,453],
[523,534,495,517,512,474,0,501,474,479],
[505,529,505,521,517,494,499,0,458,510],
[523,536,531,523,495,530,526,542,0,482],
[531,498,549,517,491,547,521,490,518,0]])



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
result = np.append(np.array([10, 1000, 169, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,510,534,504,480,505,499,515,507,485],
[490,0,517,490,489,472,472,506,501,465],
[466,483,0,470,491,470,457,504,499,467],
[496,510,530,0,500,493,498,512,497,500],
[520,511,509,500,0,512,499,524,499,500],
[495,528,530,507,488,0,472,506,485,478],
[501,528,543,502,501,528,0,524,499,502],
[485,494,496,488,476,494,476,0,506,483],
[493,499,501,503,501,515,501,494,0,488],
[515,535,533,500,500,522,498,517,512,0]])



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
result = np.append(np.array([10, 1000, 170, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,457,571,476,460,446,503,591,521,499],
[543,0,537,469,414,421,366,615,551,456],
[429,463,0,452,441,444,325,553,511,455],
[524,531,548,0,517,618,365,655,603,464],
[540,586,559,483,0,472,460,613,511,515],
[554,579,556,382,528,0,469,561,546,440],
[497,634,675,635,540,531,0,613,592,498],
[409,385,447,345,387,439,387,0,498,322],
[479,449,489,397,489,454,408,502,0,379],
[501,544,545,536,485,560,502,678,621,0]])



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
result = np.append(np.array([10, 1000, 171, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,495,496,489,529,540,488,495,530,504],
[505,0,498,535,486,553,544,489,525,471],
[504,502,0,525,513,565,508,515,525,482],
[511,465,475,0,461,518,482,476,508,462],
[471,514,487,539,0,518,502,512,543,494],
[460,447,435,482,482,0,462,466,496,460],
[512,456,492,518,498,538,0,493,513,509],
[505,511,485,524,488,534,507,0,492,468],
[470,475,475,492,457,504,487,508,0,459],
[496,529,518,538,506,540,491,532,541,0]])



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
result = np.append(np.array([10, 1000, 172, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,492,509,486,499,526,515,515,493,522],
[508,0,466,497,494,507,511,509,480,520],
[491,534,0,505,509,507,520,512,500,530],
[514,503,495,0,492,518,516,503,484,510],
[501,506,491,508,0,493,522,490,484,498],
[474,493,493,482,507,0,517,525,478,537],
[485,489,480,484,478,483,0,511,454,508],
[485,491,488,497,510,475,489,0,478,499],
[507,520,500,516,516,522,546,522,0,542],
[478,480,470,490,502,463,492,501,458,0]])



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
result = np.append(np.array([10, 1000, 173, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,512,536,502,510,518,504,530,497,511],
[488,0,518,484,507,493,506,512,487,513],
[464,482,0,464,496,491,482,484,473,487],
[498,516,536,0,499,501,503,521,498,525],
[490,493,504,501,0,498,493,517,516,504],
[482,507,509,499,502,0,505,514,486,509],
[496,494,518,497,507,495,0,515,495,506],
[470,488,516,479,483,486,485,0,490,491],
[503,513,527,502,484,514,505,510,0,499],
[489,487,513,475,496,491,494,509,501,0]])



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
result = np.append(np.array([10, 1000, 174, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,445,545,482,547,570,547,524,503,478],
[555,0,563,480,579,551,548,537,508,580],
[455,437,0,459,517,513,506,490,479,465],
[518,520,541,0,555,528,544,525,495,489],
[453,421,483,445,0,464,520,475,440,487],
[430,449,487,472,536,0,540,500,465,473],
[453,452,494,456,480,460,0,494,432,455],
[476,463,510,475,525,500,506,0,499,487],
[497,492,521,505,560,535,568,501,0,506],
[522,420,535,511,513,527,545,513,494,0]])



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
result = np.append(np.array([10, 1000, 175, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,515,509,509,486,479,474,498,527,498],
[485,0,485,490,463,509,487,527,509,486],
[491,515,0,496,478,522,507,513,502,479],
[491,510,504,0,482,492,513,545,505,501],
[514,537,522,518,0,487,492,519,520,530],
[521,491,478,508,513,0,500,523,542,512],
[526,513,493,487,508,500,0,544,526,520],
[502,473,487,455,481,477,456,0,516,505],
[473,491,498,495,480,458,474,484,0,483],
[502,514,521,499,470,488,480,495,517,0]])



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
result = np.append(np.array([10, 1000, 176, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,524,500,509,467,485,515,503,509,530],
[476,0,486,440,494,500,507,481,500,495],
[500,514,0,503,530,513,510,507,514,514],
[491,560,497,0,493,514,533,489,518,529],
[533,506,470,507,0,478,532,486,508,542],
[515,500,487,486,522,0,530,496,499,535],
[485,493,490,467,468,470,0,504,496,527],
[497,519,493,511,514,504,496,0,509,522],
[491,500,486,482,492,501,504,491,0,513],
[470,505,486,471,458,465,473,478,487,0]])



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
result = np.append(np.array([10, 1000, 177, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,404,453,418,405,473,479,417,429,360],
[596,0,543,480,523,593,611,511,535,482],
[547,457,0,496,438,532,534,483,530,476],
[582,520,504,0,486,580,591,553,511,507],
[595,477,562,514,0,586,630,538,502,460],
[527,407,468,420,414,0,474,508,483,406],
[521,389,466,409,370,526,0,500,410,345],
[583,489,517,447,462,492,500,0,430,417],
[571,465,470,489,498,517,590,570,0,445],
[640,518,524,493,540,594,655,583,555,0]])



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
result = np.append(np.array([10, 1000, 178, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,532,513,512,490,532,482,499,493,501],
[468,0,486,482,499,509,508,474,474,498],
[487,514,0,484,505,515,497,495,484,512],
[488,518,516,0,507,551,499,491,519,509],
[510,501,495,493,0,529,483,488,481,502],
[468,491,485,449,471,0,465,475,475,501],
[518,492,503,501,517,535,0,512,504,486],
[501,526,505,509,512,525,488,0,500,503],
[507,526,516,481,519,525,496,500,0,505],
[499,502,488,491,498,499,514,497,495,0]])



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
result = np.append(np.array([10, 1000, 179, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,524,486,504,503,502,504,531,505,491],
[476,0,471,494,476,510,499,522,482,490],
[514,529,0,525,518,507,516,557,510,484],
[496,506,475,0,496,499,480,508,489,498],
[497,524,482,504,0,537,517,538,519,486],
[498,490,493,501,463,0,486,514,480,491],
[496,501,484,520,483,514,0,511,479,502],
[469,478,443,492,462,486,489,0,486,480],
[495,518,490,511,481,520,521,514,0,506],
[509,510,516,502,514,509,498,520,494,0]])



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
result = np.append(np.array([10, 1000, 180, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,508,500,499,504,497,503,497,508,488],
[492,0,504,486,488,488,482,471,489,471],
[500,496,0,499,495,509,507,500,488,483],
[501,514,501,0,519,492,516,540,497,507],
[496,512,505,481,0,494,509,526,494,522],
[503,512,491,508,506,0,507,510,516,520],
[497,518,493,484,491,493,0,496,505,509],
[503,529,500,460,474,490,504,0,473,492],
[492,511,512,503,506,484,495,527,0,512],
[512,529,517,493,478,480,491,508,488,0]])



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
result = np.append(np.array([10, 1000, 181, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,491,516,534,525,519,516,539,545,504],
[509,0,499,544,526,534,552,569,549,527],
[484,501,0,489,505,501,500,519,501,463],
[466,456,511,0,496,501,480,485,493,501],
[475,474,495,504,0,502,503,512,504,502],
[481,466,499,499,498,0,536,557,506,512],
[484,448,500,520,497,464,0,552,511,484],
[461,431,481,515,488,443,448,0,493,466],
[455,451,499,507,496,494,489,507,0,475],
[496,473,537,499,498,488,516,534,525,0]])



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
result = np.append(np.array([10, 1000, 182, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,488,448,458,490,473,496,512,470,512],
[512,0,460,459,493,480,521,501,505,513],
[552,540,0,527,555,497,561,539,517,554],
[542,541,473,0,529,520,563,552,539,524],
[510,507,445,471,0,500,514,514,518,504],
[527,520,503,480,500,0,516,517,532,527],
[504,479,439,437,486,484,0,453,484,485],
[488,499,461,448,486,483,547,0,484,523],
[530,495,483,461,482,468,516,516,0,512],
[488,487,446,476,496,473,515,477,488,0]])



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
result = np.append(np.array([10, 1000, 183, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,511,518,498,528,521,504,517,511,485],
[489,0,494,498,478,508,504,490,480,490],
[482,506,0,501,512,506,484,511,501,515],
[502,502,499,0,523,515,500,507,494,506],
[472,522,488,477,0,485,502,506,503,499],
[479,492,494,485,515,0,507,500,503,500],
[496,496,516,500,498,493,0,516,496,512],
[483,510,489,493,494,500,484,0,500,495],
[489,520,499,506,497,497,504,500,0,495],
[515,510,485,494,501,500,488,505,505,0]])



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
result = np.append(np.array([10, 1000, 184, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,464,490,488,505,509,497,470,470,496],
[536,0,491,499,518,527,504,504,508,509],
[510,509,0,500,505,524,503,509,527,523],
[512,501,500,0,516,518,509,525,491,496],
[495,482,495,484,0,487,485,498,488,526],
[491,473,476,482,513,0,492,489,493,483],
[503,496,497,491,515,508,0,518,506,528],
[530,496,491,475,502,511,482,0,501,502],
[530,492,473,509,512,507,494,499,0,513],
[504,491,477,504,474,517,472,498,487,0]])



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
result = np.append(np.array([10, 1000, 185, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,497,501,494,494,500,469,479,464,507],
[503,0,498,476,501,481,472,452,485,486],
[499,502,0,471,548,527,496,494,497,511],
[506,524,529,0,548,515,495,511,496,481],
[506,499,452,452,0,476,484,455,456,482],
[500,519,473,485,524,0,510,486,478,470],
[531,528,504,505,516,490,0,474,495,518],
[521,548,506,489,545,514,526,0,515,521],
[536,515,503,504,544,522,505,485,0,510],
[493,514,489,519,518,530,482,479,490,0]])



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
result = np.append(np.array([10, 1000, 186, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,487,491,471,513,486,491,498,454,444],
[513,0,502,510,506,510,507,486,519,485],
[509,498,0,494,520,543,515,505,485,470],
[529,490,506,0,524,517,512,512,491,448],
[487,494,480,476,0,506,492,499,456,452],
[514,490,457,483,494,0,473,484,482,430],
[509,493,485,488,508,527,0,497,493,462],
[502,514,495,488,501,516,503,0,492,459],
[546,481,515,509,544,518,507,508,0,508],
[556,515,530,552,548,570,538,541,492,0]])



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
result = np.append(np.array([10, 1000, 187, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,540,536,517,558,470,518,518,486,456],
[460,0,470,453,464,416,428,475,478,442],
[464,530,0,490,517,455,479,495,474,482],
[483,547,510,0,547,498,476,522,526,445],
[442,536,483,453,0,453,407,423,447,441],
[530,584,545,502,547,0,456,516,529,504],
[482,572,521,524,593,544,0,480,513,480],
[482,525,505,478,577,484,520,0,464,458],
[514,522,526,474,553,471,487,536,0,484],
[544,558,518,555,559,496,520,542,516,0]])



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
result = np.append(np.array([10, 1000, 188, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,538,555,534,495,524,496,501,563,511],
[462,0,521,513,497,466,403,419,542,447],
[445,479,0,474,469,479,434,417,520,457],
[466,487,526,0,517,510,440,436,508,487],
[505,503,531,483,0,464,500,468,564,464],
[476,534,521,490,536,0,424,436,540,503],
[504,597,566,560,500,576,0,479,574,531],
[499,581,583,564,532,564,521,0,548,548],
[437,458,480,492,436,460,426,452,0,444],
[489,553,543,513,536,497,469,452,556,0]])



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
result = np.append(np.array([10, 1000, 189, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,488,515,470,463,489,479,467,482,473],
[512,0,518,467,493,476,483,479,478,476],
[485,482,0,486,476,478,484,479,480,482],
[530,533,514,0,496,518,501,517,521,487],
[537,507,524,504,0,514,482,488,504,493],
[511,524,522,482,486,0,484,480,509,487],
[521,517,516,499,518,516,0,511,500,499],
[533,521,521,483,512,520,489,0,518,513],
[518,522,520,479,496,491,500,482,0,502],
[527,524,518,513,507,513,501,487,498,0]])



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
result = np.append(np.array([10, 1000, 190, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,494,441,502,531,526,456,537,484,528],
[506,0,438,469,567,600,458,579,484,441],
[559,562,0,497,561,568,498,496,542,470],
[498,531,503,0,555,508,470,511,448,464],
[469,433,439,445,0,541,432,499,439,448],
[474,400,432,492,459,0,424,474,416,468],
[544,542,502,530,568,576,0,571,536,500],
[463,421,504,489,501,526,429,0,462,435],
[516,516,458,552,561,584,464,538,0,474],
[472,559,530,536,552,532,500,565,526,0]])



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
result = np.append(np.array([10, 1000, 191, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,546,508,542,521,485,537,535,546,529],
[454,0,512,485,469,471,522,517,535,525],
[492,488,0,481,520,456,496,529,512,498],
[458,515,519,0,511,457,517,536,537,511],
[479,531,480,489,0,461,523,530,515,502],
[515,529,544,543,539,0,540,551,523,496],
[463,478,504,483,477,460,0,513,498,486],
[465,483,471,464,470,449,487,0,471,485],
[454,465,488,463,485,477,502,529,0,485],
[471,475,502,489,498,504,514,515,515,0]])



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
result = np.append(np.array([10, 1000, 192, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,494,517,524,484,519,502,499,471,475],
[506,0,527,525,532,524,518,489,499,462],
[483,473,0,474,428,456,488,468,452,477],
[476,475,526,0,458,427,523,474,440,458],
[516,468,572,542,0,491,535,541,537,532],
[481,476,544,573,509,0,525,513,467,483],
[498,482,512,477,465,475,0,478,467,449],
[501,511,532,526,459,487,522,0,436,478],
[529,501,548,560,463,533,533,564,0,492],
[525,538,523,542,468,517,551,522,508,0]])



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
result = np.append(np.array([10, 1000, 193, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,434,458,487,501,483,479,524,507,489],
[566,0,491,527,543,509,517,562,523,544],
[542,509,0,498,528,510,486,545,524,543],
[513,473,502,0,539,498,531,545,551,516],
[499,457,472,461,0,485,469,527,501,491],
[517,491,490,502,515,0,490,537,544,510],
[521,483,514,469,531,510,0,518,521,532],
[476,438,455,455,473,463,482,0,487,496],
[493,477,476,449,499,456,479,513,0,483],
[511,456,457,484,509,490,468,504,517,0]])



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
result = np.append(np.array([10, 1000, 194, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,495,503,491,510,490,518,543,496,505],
[505,0,512,498,513,484,500,519,489,498],
[497,488,0,488,499,521,504,529,495,507],
[509,502,512,0,509,483,507,541,483,502],
[490,487,501,491,0,496,517,547,471,498],
[510,516,479,517,504,0,526,516,516,523],
[482,500,496,493,483,474,0,520,470,476],
[457,481,471,459,453,484,480,0,451,471],
[504,511,505,517,529,484,530,549,0,494],
[495,502,493,498,502,477,524,529,506,0]])



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
result = np.append(np.array([10, 1000, 195, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,454,474,526,647,585,586,564,464,724],
[546,0,356,422,609,526,558,460,460,612],
[526,644,0,536,549,533,602,506,414,790],
[474,578,464,0,633,564,601,481,518,708],
[353,391,451,367,0,397,446,387,438,503],
[415,474,467,436,603,0,582,450,504,726],
[414,442,398,399,554,418,0,385,393,587],
[436,540,494,519,613,550,615,0,485,717],
[536,540,586,482,562,496,607,515,0,603],
[276,388,210,292,497,274,413,283,397,0]])



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
result = np.append(np.array([10, 1000, 196, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,482,537,527,504,493,481,501,493,512],
[518,0,498,537,484,462,464,474,496,539],
[463,502,0,526,509,453,482,468,495,532],
[473,463,474,0,491,449,444,444,474,478],
[496,516,491,509,0,477,485,480,502,527],
[507,538,547,551,523,0,497,510,513,520],
[519,536,518,556,515,503,0,500,505,538],
[499,526,532,556,520,490,500,0,525,516],
[507,504,505,526,498,487,495,475,0,522],
[488,461,468,522,473,480,462,484,478,0]])



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
result = np.append(np.array([10, 1000, 197, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,480,508,501,520,497,491,500,525,490],
[520,0,493,527,508,516,511,499,521,499],
[492,507,0,510,512,491,512,506,505,491],
[499,473,490,0,510,487,472,480,492,470],
[480,492,488,490,0,497,505,493,508,477],
[503,484,509,513,503,0,497,488,501,492],
[509,489,488,528,495,503,0,480,507,469],
[500,501,494,520,507,512,520,0,529,511],
[475,479,495,508,492,499,493,471,0,480],
[510,501,509,530,523,508,531,489,520,0]])



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
result = np.append(np.array([10, 1000, 198, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,497,533,517,578,486,512,494,527,543],
[503,0,570,546,521,526,523,489,536,539],
[467,430,0,509,456,462,478,423,467,480],
[483,454,491,0,457,443,445,478,481,502],
[422,479,544,543,0,475,506,483,470,487],
[514,474,538,557,525,0,554,514,532,568],
[488,477,522,555,494,446,0,468,512,525],
[506,511,577,522,517,486,532,0,511,539],
[473,464,533,519,530,468,488,489,0,534],
[457,461,520,498,513,432,475,461,466,0]])



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
result = np.append(np.array([10, 1000, 199, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,498,513,559,509,483,506,540,562,588],
[502,0,524,556,477,492,489,540,611,528],
[487,476,0,610,504,574,479,492,569,572],
[441,444,390,0,397,482,427,395,508,450],
[491,523,496,603,0,448,514,496,547,505],
[517,508,426,518,552,0,470,536,539,556],
[494,511,521,573,486,530,0,569,530,536],
[460,460,508,605,504,464,431,0,604,493],
[438,389,431,492,453,461,470,396,0,401],
[412,472,428,550,495,444,464,507,599,0]])



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
result = np.append(np.array([10, 1000, 200, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/mebb/mebb_10_1000.csv", index=False, header=False)