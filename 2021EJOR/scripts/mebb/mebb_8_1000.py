
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg

rep = 3
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,499,487,449,504,461,505,486],
[501,0,501,503,514,478,472,494],
[513,499,0,474,491,496,513,486],
[551,497,526,0,498,492,496,511],
[496,486,509,502,0,478,496,479],
[539,522,504,508,522,0,504,486],
[495,528,487,504,504,496,0,497],
[514,506,514,489,521,514,503,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 1, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,479,500,474,511,494,497,472],
[521,0,486,500,540,527,513,499],
[500,514,0,491,536,528,515,498],
[526,500,509,0,532,516,499,503],
[489,460,464,468,0,515,488,446],
[506,473,472,484,485,0,477,475],
[503,487,485,501,512,523,0,492],
[528,501,502,497,554,525,508,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 2, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,484,507,477,504,450,454,498],
[516,0,504,516,507,474,494,494],
[493,496,0,489,479,458,487,499],
[523,484,511,0,502,479,472,493],
[496,493,521,498,0,449,450,471],
[550,526,542,521,551,0,518,486],
[546,506,513,528,550,482,0,508],
[502,506,501,507,529,514,492,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 3, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,525,459,494,509,465,463,467],
[475,0,486,464,474,453,483,497],
[541,514,0,505,535,469,531,494],
[506,536,495,0,527,468,486,519],
[491,526,465,473,0,468,490,509],
[535,547,531,532,532,0,558,486],
[537,517,469,514,510,442,0,477],
[533,503,506,481,491,514,523,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 4, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,468,505,491,470,486,485,471],
[532,0,500,528,514,505,516,474],
[495,500,0,516,519,489,517,487],
[509,472,484,0,462,461,466,473],
[530,486,481,538,0,505,486,490],
[514,495,511,539,495,0,485,507],
[515,484,483,534,514,515,0,500],
[529,526,513,527,510,493,500,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 5, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,551,509,538,492,488,467,526],
[449,0,416,464,439,487,420,434],
[491,584,0,571,534,590,535,552],
[462,536,429,0,511,496,467,495],
[508,561,466,489,0,544,496,462],
[512,513,410,504,456,0,485,460],
[533,580,465,533,504,515,0,434],
[474,566,448,505,538,540,566,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 6, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,489,501,501,515,531,506,477],
[511,0,483,426,538,522,457,503],
[499,517,0,488,499,549,483,496],
[499,574,512,0,489,513,470,505],
[485,462,501,511,0,459,484,482],
[469,478,451,487,541,0,486,480],
[494,543,517,530,516,514,0,523],
[523,497,504,495,518,520,477,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 7, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,463,472,475,485,464,491,468],
[537,0,516,483,517,500,500,498],
[528,484,0,500,508,497,524,493],
[525,517,500,0,543,518,535,501],
[515,483,492,457,0,459,493,463],
[536,500,503,482,541,0,524,500],
[509,500,476,465,507,476,0,463],
[532,502,507,499,537,500,537,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 8, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,558,565,450,612,583,520,612],
[442,0,408,428,466,445,494,589],
[435,592,0,502,579,445,450,421],
[550,572,498,0,543,564,623,617],
[388,534,421,457,0,485,435,476],
[417,555,555,436,515,0,498,571],
[480,506,550,377,565,502,0,544],
[388,411,579,383,524,429,456,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 9, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,485,500,514,565,490,514,569],
[515,0,477,477,513,488,475,546],
[500,523,0,518,526,451,481,522],
[486,523,482,0,588,501,475,558],
[435,487,474,412,0,481,502,542],
[510,512,549,499,519,0,497,567],
[486,525,519,525,498,503,0,524],
[431,454,478,442,458,433,476,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 10, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,600,692,463,470,653,506,494],
[400,0,615,381,479,639,359,465],
[308,385,0,264,412,572,400,415],
[537,619,736,0,546,748,359,518],
[530,521,588,454,0,661,401,454],
[347,361,428,252,339,0,280,373],
[494,641,600,641,599,720,0,626],
[506,535,585,482,546,627,374,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 11, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,509,501,528,519,515,500,503],
[491,0,473,529,519,483,504,526],
[499,527,0,536,531,491,464,519],
[472,471,464,0,507,470,469,500],
[481,481,469,493,0,485,457,471],
[485,517,509,530,515,0,495,509],
[500,496,536,531,543,505,0,537],
[497,474,481,500,529,491,463,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 12, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,502,536,500,508,504,504,510],
[498,0,518,497,504,524,487,510],
[464,482,0,450,468,465,518,444],
[500,503,550,0,546,529,506,535],
[492,496,532,454,0,487,502,496],
[496,476,535,471,513,0,451,485],
[496,513,482,494,498,549,0,464],
[490,490,556,465,504,515,536,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 13, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,530,507,506,494,480,496,486],
[470,0,460,444,464,465,489,476],
[493,540,0,487,502,486,504,514],
[494,556,513,0,537,511,529,523],
[506,536,498,463,0,489,501,518],
[520,535,514,489,511,0,522,511],
[504,511,496,471,499,478,0,496],
[514,524,486,477,482,489,504,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 14, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,466,504,494,498,499,477,514],
[534,0,495,495,517,530,500,502],
[496,505,0,489,504,503,495,500],
[506,505,511,0,519,509,489,518],
[502,483,496,481,0,507,489,510],
[501,470,497,491,493,0,497,497],
[523,500,505,511,511,503,0,523],
[486,498,500,482,490,503,477,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 15, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,542,549,537,546,564,487,508],
[458,0,482,421,525,512,453,482],
[451,518,0,481,534,454,472,474],
[463,579,519,0,569,478,516,570],
[454,475,466,431,0,431,392,430],
[436,488,546,522,569,0,510,555],
[513,547,528,484,608,490,0,553],
[492,518,526,430,570,445,447,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 16, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,501,502,470,522,468,521,495],
[499,0,503,485,508,468,506,512],
[498,497,0,480,501,481,520,490],
[530,515,520,0,559,486,535,514],
[478,492,499,441,0,462,499,516],
[532,532,519,514,538,0,518,498],
[479,494,480,465,501,482,0,495],
[505,488,510,486,484,502,505,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 17, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,508,602,500,551,518,549,478],
[492,0,496,478,500,494,540,505],
[398,504,0,438,491,433,531,471],
[500,522,562,0,549,515,595,506],
[449,500,509,451,0,506,539,484],
[482,506,567,485,494,0,579,514],
[451,460,469,405,461,421,0,512],
[522,495,529,494,516,486,488,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 18, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,536,413,409,553,493,501,479],
[464,0,450,439,496,481,477,379],
[587,550,0,515,553,498,560,554],
[591,561,485,0,573,568,550,497],
[447,504,447,427,0,410,427,501],
[507,519,502,432,590,0,561,448],
[499,523,440,450,573,439,0,427],
[521,621,446,503,499,552,573,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 19, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,508,514,523,522,513,504,497],
[492,0,486,531,484,477,479,502],
[486,514,0,512,497,501,458,480],
[477,469,488,0,489,462,487,485],
[478,516,503,511,0,494,479,468],
[487,523,499,538,506,0,476,485],
[496,521,542,513,521,524,0,495],
[503,498,520,515,532,515,505,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 20, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,498,516,509,492,501,481,486],
[502,0,507,472,499,485,485,481],
[484,493,0,476,489,508,486,472],
[491,528,524,0,513,528,491,486],
[508,501,511,487,0,476,491,488],
[499,515,492,472,524,0,506,516],
[519,515,514,509,509,494,0,495],
[514,519,528,514,512,484,505,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 21, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,493,491,471,487,481,505,480],
[507,0,507,497,517,501,514,511],
[509,493,0,469,535,496,492,496],
[529,503,531,0,533,532,496,517],
[513,483,465,467,0,495,479,497],
[519,499,504,468,505,0,506,485],
[495,486,508,504,521,494,0,503],
[520,489,504,483,503,515,497,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 22, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,562,525,503,500,504,517,518],
[438,0,437,558,477,467,468,395],
[475,563,0,574,489,482,500,472],
[497,442,426,0,450,454,453,448],
[500,523,511,550,0,510,493,476],
[496,533,518,546,490,0,486,458],
[483,532,500,547,507,514,0,515],
[482,605,528,552,524,542,485,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 23, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,479,480,456,444,472,448,467],
[521,0,508,492,485,536,533,506],
[520,492,0,493,526,503,524,510],
[544,508,507,0,486,559,530,521],
[556,515,474,514,0,510,530,544],
[528,464,497,441,490,0,475,492],
[552,467,476,470,470,525,0,471],
[533,494,490,479,456,508,529,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 24, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,486,488,489,499,506,510,497],
[514,0,474,504,517,499,511,490],
[512,526,0,502,514,506,520,500],
[511,496,498,0,503,482,501,516],
[501,483,486,497,0,492,495,488],
[494,501,494,518,508,0,519,525],
[490,489,480,499,505,481,0,491],
[503,510,500,484,512,475,509,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 25, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,562,554,553,562,574,522,489],
[438,0,495,452,523,520,499,477],
[446,505,0,543,481,499,524,530],
[447,548,457,0,490,552,523,486],
[438,477,519,510,0,535,459,443],
[426,480,501,448,465,0,456,449],
[478,501,476,477,541,544,0,565],
[511,523,470,514,557,551,435,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 26, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,502,497,510,500,500,481,493],
[498,0,513,528,491,477,503,510],
[503,487,0,503,478,492,495,498],
[490,472,497,0,482,464,479,506],
[500,509,522,518,0,513,529,517],
[500,523,508,536,487,0,508,526],
[519,497,505,521,471,492,0,490],
[507,490,502,494,483,474,510,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 27, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,486,481,516,440,495,547,477],
[514,0,445,512,436,467,521,446],
[519,555,0,508,435,536,488,440],
[484,488,492,0,440,481,529,420],
[560,564,565,560,0,489,513,508],
[505,533,464,519,511,0,523,445],
[453,479,512,471,487,477,0,463],
[523,554,560,580,492,555,537,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 28, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,506,497,494,503,508,529,493],
[494,0,502,494,521,512,506,482],
[503,498,0,482,480,493,491,486],
[506,506,518,0,500,504,509,500],
[497,479,520,500,0,501,510,465],
[492,488,507,496,499,0,500,502],
[471,494,509,491,490,500,0,480],
[507,518,514,500,535,498,520,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 29, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,469,497,481,452,462,503,528],
[531,0,514,508,467,511,522,540],
[503,486,0,472,467,477,491,485],
[519,492,528,0,498,522,523,552],
[548,533,533,502,0,484,521,522],
[538,489,523,478,516,0,518,533],
[497,478,509,477,479,482,0,525],
[472,460,515,448,478,467,475,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 30, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,518,519,491,464,501,516,503],
[482,0,479,497,470,501,483,512],
[481,521,0,485,469,519,472,483],
[509,503,515,0,500,498,489,502],
[536,530,531,500,0,532,509,483],
[499,499,481,502,468,0,474,488],
[484,517,528,511,491,526,0,489],
[497,488,517,498,517,512,511,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 31, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,497,522,547,572,469,527,477],
[503,0,516,485,537,461,530,472],
[478,484,0,497,552,489,467,475],
[453,515,503,0,459,400,415,459],
[428,463,448,541,0,457,471,504],
[531,539,511,600,543,0,552,471],
[473,470,533,585,529,448,0,441],
[523,528,525,541,496,529,559,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 32, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,491,485,512,459,519,446,527],
[509,0,519,448,485,546,443,508],
[515,481,0,531,516,563,527,582],
[488,552,469,0,482,530,475,511],
[541,515,484,518,0,567,511,561],
[481,454,437,470,433,0,476,468],
[554,557,473,525,489,524,0,545],
[473,492,418,489,439,532,455,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 33, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,713,330,802,802,694,419,492],
[287,0,356,1000,630,611,287,409],
[670,644,0,802,802,783,261,581],
[198,0,198,0,320,320,198,320],
[198,370,198,680,0,364,370,320],
[306,389,217,680,636,0,459,492],
[581,713,739,802,630,541,0,320],
[508,591,419,680,680,508,680,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 34, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,527,503,513,525,540,493,523],
[473,0,485,495,491,495,483,510],
[497,515,0,513,530,516,502,512],
[487,505,487,0,497,494,477,502],
[475,509,470,503,0,497,456,511],
[460,505,484,506,503,0,451,512],
[507,517,498,523,544,549,0,568],
[477,490,488,498,489,488,432,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 35, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,493,484,492,495,517,500,482],
[507,0,497,497,490,530,491,506],
[516,503,0,500,475,502,486,510],
[508,503,500,0,485,517,509,511],
[505,510,525,515,0,523,485,506],
[483,470,498,483,477,0,466,488],
[500,509,514,491,515,534,0,510],
[518,494,490,489,494,512,490,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 36, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,498,510,500,550,541,463,486],
[502,0,504,505,546,524,493,497],
[490,496,0,463,498,507,471,449],
[500,495,537,0,523,536,510,524],
[450,454,502,477,0,483,468,476],
[459,476,493,464,517,0,479,479],
[537,507,529,490,532,521,0,510],
[514,503,551,476,524,521,490,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 37, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,551,545,553,486,552,493,511],
[449,0,487,472,485,471,466,461],
[455,513,0,513,477,499,465,478],
[447,528,487,0,472,474,487,476],
[514,515,523,528,0,480,502,490],
[448,529,501,526,520,0,513,519],
[507,534,535,513,498,487,0,495],
[489,539,522,524,510,481,505,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 38, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,474,455,425,446,382,330,404],
[526,0,499,535,583,470,423,495],
[545,501,0,452,472,422,435,570],
[575,465,548,0,441,491,438,489],
[554,417,528,559,0,516,468,432],
[618,530,578,509,484,0,502,410],
[670,577,565,562,532,498,0,586],
[596,505,430,511,568,590,414,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 39, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,513,528,475,503,522,507,519],
[487,0,527,463,472,489,516,483],
[472,473,0,446,478,498,510,446],
[525,537,554,0,485,524,523,478],
[497,528,522,515,0,503,535,489],
[478,511,502,476,497,0,503,472],
[493,484,490,477,465,497,0,471],
[481,517,554,522,511,528,529,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 40, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,595,552,1000,498,828,767,648],
[405,0,233,723,551,523,581,662],
[448,767,0,881,537,509,767,648],
[0,277,119,0,318,61,119,318],
[502,449,463,682,0,391,621,820],
[172,477,491,939,609,0,939,662],
[233,419,233,881,379,61,0,551],
[352,338,352,682,180,338,449,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 41, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,532,464,469,488,524,465,507],
[468,0,483,473,495,483,482,525],
[536,517,0,509,458,506,512,522],
[531,527,491,0,479,506,493,552],
[512,505,542,521,0,511,481,539],
[476,517,494,494,489,0,502,491],
[535,518,488,507,519,498,0,543],
[493,475,478,448,461,509,457,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 42, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,522,516,434,510,505,514,478],
[478,0,520,467,457,443,483,450],
[484,480,0,435,475,456,493,443],
[566,533,565,0,527,499,576,517],
[490,543,525,473,0,464,486,498],
[495,557,544,501,536,0,584,505],
[486,517,507,424,514,416,0,490],
[522,550,557,483,502,495,510,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 43, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,452,496,396,441,536,512,421],
[548,0,595,555,502,511,494,511],
[504,405,0,420,464,515,461,408],
[604,445,580,0,503,533,514,496],
[559,498,536,497,0,553,573,512],
[464,489,485,467,447,0,495,430],
[488,506,539,486,427,505,0,445],
[579,489,592,504,488,570,555,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 44, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,502,496,492,485,476,483,472],
[498,0,483,507,517,530,503,493],
[504,517,0,501,506,490,504,478],
[508,493,499,0,483,490,468,497],
[515,483,494,517,0,507,462,474],
[524,470,510,510,493,0,501,502],
[517,497,496,532,538,499,0,499],
[528,507,522,503,526,498,501,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 45, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,483,540,497,456,493,522,492],
[517,0,565,510,486,507,570,521],
[460,435,0,462,462,466,502,457],
[503,490,538,0,456,527,538,502],
[544,514,538,544,0,556,565,485],
[507,493,534,473,444,0,518,480],
[478,430,498,462,435,482,0,452],
[508,479,543,498,515,520,548,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 46, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,507,496,468,473,501,526,517],
[493,0,485,461,479,495,506,532],
[504,515,0,512,465,480,502,470],
[532,539,488,0,483,514,548,540],
[527,521,535,517,0,489,543,547],
[499,505,520,486,511,0,497,522],
[474,494,498,452,457,503,0,515],
[483,468,530,460,453,478,485,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 47, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,485,543,471,498,516,503,483],
[515,0,521,460,477,486,498,463],
[457,479,0,455,498,463,476,469],
[529,540,545,0,529,520,521,484],
[502,523,502,471,0,497,496,521],
[484,514,537,480,503,0,517,492],
[497,502,524,479,504,483,0,479],
[517,537,531,516,479,508,521,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 48, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,479,485,497,511,477,487,491],
[521,0,505,532,554,527,515,493],
[515,495,0,519,512,494,512,485],
[503,468,481,0,487,499,482,496],
[489,446,488,513,0,471,473,483],
[523,473,506,501,529,0,491,518],
[513,485,488,518,527,509,0,501],
[509,507,515,504,517,482,499,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 49, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,527,503,514,521,498,496,506],
[473,0,464,455,483,489,459,496],
[497,536,0,518,529,514,511,516],
[486,545,482,0,507,495,501,502],
[479,517,471,493,0,493,479,492],
[502,511,486,505,507,0,454,487],
[504,541,489,499,521,546,0,516],
[494,504,484,498,508,513,484,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 50, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,485,513,487,531,486,469,480],
[515,0,526,529,549,491,521,484],
[487,474,0,459,538,515,500,461],
[513,471,541,0,562,519,511,531],
[469,451,462,438,0,458,479,453],
[514,509,485,481,542,0,498,447],
[531,479,500,489,521,502,0,491],
[520,516,539,469,547,553,509,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 51, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,525,512,548,473,510,522,489],
[475,0,536,518,472,426,486,503],
[488,464,0,473,461,465,474,475],
[452,482,527,0,433,446,470,479],
[527,528,539,567,0,534,530,499],
[490,574,535,554,466,0,512,556],
[478,514,526,530,470,488,0,493],
[511,497,525,521,501,444,507,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 52, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,545,480,492,471,484,515,479],
[455,0,502,487,425,474,468,504],
[520,498,0,515,526,459,461,527],
[508,513,485,0,504,481,507,558],
[529,575,474,496,0,527,497,534],
[516,526,541,519,473,0,473,504],
[485,532,539,493,503,527,0,517],
[521,496,473,442,466,496,483,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 53, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,484,483,502,499,513,517,474],
[516,0,505,503,519,525,493,468],
[517,495,0,536,517,530,541,501],
[498,497,464,0,505,513,511,473],
[501,481,483,495,0,493,490,470],
[487,475,470,487,507,0,507,484],
[483,507,459,489,510,493,0,461],
[526,532,499,527,530,516,539,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 54, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,469,473,536,377,380,365,424],
[531,0,480,545,427,433,426,503],
[527,520,0,639,472,505,484,635],
[464,455,361,0,421,371,387,410],
[623,573,528,579,0,534,476,528],
[620,567,495,629,466,0,518,551],
[635,574,516,613,524,482,0,550],
[576,497,365,590,472,449,450,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 55, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,497,558,544,486,535,514,519],
[503,0,541,492,492,536,499,492],
[442,459,0,502,451,451,479,478],
[456,508,498,0,473,505,485,498],
[514,508,549,527,0,532,564,490],
[465,464,549,495,468,0,480,483],
[486,501,521,515,436,520,0,481],
[481,508,522,502,510,517,519,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 56, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,446,512,531,539,495,506,501],
[554,0,531,550,554,498,546,525],
[488,469,0,556,532,500,531,519],
[469,450,444,0,480,426,508,465],
[461,446,468,520,0,449,545,487],
[505,502,500,574,551,0,576,560],
[494,454,469,492,455,424,0,510],
[499,475,481,535,513,440,490,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 57, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,483,485,434,479,462,462,474],
[517,0,481,469,487,525,508,525],
[515,519,0,473,438,492,488,512],
[566,531,527,0,478,498,500,512],
[521,513,562,522,0,520,496,509],
[538,475,508,502,480,0,516,503],
[538,492,512,500,504,484,0,500],
[526,475,488,488,491,497,500,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 58, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,522,510,512,499,547,520,525],
[478,0,466,479,527,482,516,525],
[490,534,0,523,524,510,512,534],
[488,521,477,0,517,494,482,505],
[501,473,476,483,0,475,496,521],
[453,518,490,506,525,0,525,509],
[480,484,488,518,504,475,0,545],
[475,475,466,495,479,491,455,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 59, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,504,491,495,508,503,502,512],
[496,0,495,500,485,503,498,495],
[509,505,0,503,513,515,505,490],
[505,500,497,0,507,497,523,499],
[492,515,487,493,0,476,488,504],
[497,497,485,503,524,0,499,503],
[498,502,495,477,512,501,0,507],
[488,505,510,501,496,497,493,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 60, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,513,500,506,520,515,502,487],
[487,0,526,533,497,524,511,505],
[500,474,0,516,495,511,518,485],
[494,467,484,0,481,503,478,506],
[480,503,505,519,0,529,484,479],
[485,476,489,497,471,0,464,445],
[498,489,482,522,516,536,0,490],
[513,495,515,494,521,555,510,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 61, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,508,517,479,477,504,513,503],
[492,0,538,527,490,506,501,482],
[483,462,0,498,469,473,486,488],
[521,473,502,0,491,504,481,499],
[523,510,531,509,0,526,498,498],
[496,494,527,496,474,0,502,512],
[487,499,514,519,502,498,0,490],
[497,518,512,501,502,488,510,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 62, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,492,514,502,495,486,507,495],
[508,0,516,489,510,516,537,514],
[486,484,0,487,504,516,502,491],
[498,511,513,0,483,510,522,503],
[505,490,496,517,0,508,526,510],
[514,484,484,490,492,0,537,495],
[493,463,498,478,474,463,0,458],
[505,486,509,497,490,505,542,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 63, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,510,416,447,489,515,446,519],
[490,0,473,442,505,524,467,491],
[584,527,0,463,541,575,513,527],
[553,558,537,0,522,550,472,541],
[511,495,459,478,0,510,504,525],
[485,476,425,450,490,0,447,540],
[554,533,487,528,496,553,0,530],
[481,509,473,459,475,460,470,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 64, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,514,515,498,512,521,488,506],
[486,0,500,504,482,488,455,516],
[485,500,0,499,487,489,506,506],
[502,496,501,0,500,479,476,494],
[488,518,513,500,0,484,509,483],
[479,512,511,521,516,0,498,524],
[512,545,494,524,491,502,0,487],
[494,484,494,506,517,476,513,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 65, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,486,505,497,501,511,528,520],
[514,0,515,525,500,487,535,510],
[495,485,0,509,474,488,514,527],
[503,475,491,0,484,482,534,509],
[499,500,526,516,0,518,524,519],
[489,513,512,518,482,0,528,533],
[472,465,486,466,476,472,0,474],
[480,490,473,491,481,467,526,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 66, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,494,460,407,465,527,457,507],
[506,0,469,501,454,535,489,511],
[540,531,0,538,543,536,494,522],
[593,499,462,0,488,575,462,509],
[535,546,457,512,0,591,507,567],
[473,465,464,425,409,0,507,467],
[543,511,506,538,493,493,0,485],
[493,489,478,491,433,533,515,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 67, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,528,519,519,507,482,531,500],
[472,0,493,504,466,451,500,479],
[481,507,0,508,490,477,511,501],
[481,496,492,0,481,477,495,488],
[493,534,510,519,0,515,529,488],
[518,549,523,523,485,0,513,489],
[469,500,489,505,471,487,0,484],
[500,521,499,512,512,511,516,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 68, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,599,591,504,537,494,530,576],
[401,0,491,425,456,419,463,419],
[409,509,0,449,455,441,477,458],
[496,575,551,0,534,500,481,501],
[463,544,545,466,0,539,622,560],
[506,581,559,500,461,0,542,512],
[470,537,523,519,378,458,0,480],
[424,581,542,499,440,488,520,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 69, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,481,494,476,514,509,520,510],
[519,0,550,496,509,555,542,485],
[506,450,0,477,473,505,530,491],
[524,504,523,0,496,523,514,494],
[486,491,527,504,0,517,472,497],
[491,445,495,477,483,0,486,455],
[480,458,470,486,528,514,0,478],
[490,515,509,506,503,545,522,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 70, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,482,514,499,499,523,493,520],
[518,0,492,496,504,516,466,506],
[486,508,0,534,484,508,492,543],
[501,504,466,0,510,501,504,522],
[501,496,516,490,0,525,483,516],
[477,484,492,499,475,0,461,513],
[507,534,508,496,517,539,0,507],
[480,494,457,478,484,487,493,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 71, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,532,532,484,506,489,502,501],
[468,0,487,454,493,472,492,486],
[468,513,0,462,481,461,495,495],
[516,546,538,0,518,480,521,508],
[494,507,519,482,0,459,499,499],
[511,528,539,520,541,0,522,500],
[498,508,505,479,501,478,0,492],
[499,514,505,492,501,500,508,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 72, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,449,478,450,485,482,487,503],
[551,0,549,454,530,517,498,499],
[522,451,0,456,453,445,460,475],
[550,546,544,0,537,451,497,531],
[515,470,547,463,0,478,490,525],
[518,483,555,549,522,0,533,517],
[513,502,540,503,510,467,0,504],
[497,501,525,469,475,483,496,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 73, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,491,497,496,485,495,458,497],
[509,0,480,502,490,499,516,488],
[503,520,0,507,504,526,507,500],
[504,498,493,0,538,491,492,478],
[515,510,496,462,0,468,508,465],
[505,501,474,509,532,0,496,482],
[542,484,493,508,492,504,0,487],
[503,512,500,522,535,518,513,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 74, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,359,540,365,484,494,492,468],
[641,0,526,526,504,488,507,575],
[460,474,0,416,427,406,452,559],
[635,474,584,0,580,503,522,598],
[516,496,573,420,0,415,478,559],
[506,512,594,497,585,0,587,739],
[508,493,548,478,522,413,0,557],
[532,425,441,402,441,261,443,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 75, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,483,525,503,490,579,477,520],
[517,0,454,436,451,500,381,444],
[475,546,0,440,404,528,491,468],
[497,564,560,0,620,622,559,442],
[510,549,596,380,0,576,413,436],
[421,500,472,378,424,0,431,461],
[523,619,509,441,587,569,0,478],
[480,556,532,558,564,539,522,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 76, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,485,495,514,473,497,514,507],
[515,0,531,515,502,483,537,521],
[505,469,0,504,495,486,503,496],
[486,485,496,0,460,499,502,480],
[527,498,505,540,0,518,516,529],
[503,517,514,501,482,0,523,513],
[486,463,497,498,484,477,0,490],
[493,479,504,520,471,487,510,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 77, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,472,491,481,494,487,481,490],
[528,0,518,495,502,505,493,486],
[509,482,0,463,487,487,469,470],
[519,505,537,0,504,491,513,501],
[506,498,513,496,0,491,488,488],
[513,495,513,509,509,0,500,506],
[519,507,531,487,512,500,0,505],
[510,514,530,499,512,494,495,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 78, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,483,482,494,462,500,489,499],
[517,0,505,491,507,509,529,506],
[518,495,0,506,513,512,524,496],
[506,509,494,0,520,492,527,511],
[538,493,487,480,0,508,530,497],
[500,491,488,508,492,0,509,505],
[511,471,476,473,470,491,0,505],
[501,494,504,489,503,495,495,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 79, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,434,420,531,662,484,447,413],
[566,0,473,575,642,497,451,460],
[580,527,0,516,667,499,562,548],
[469,425,484,0,658,528,560,418],
[338,358,333,342,0,320,403,355],
[516,503,501,472,680,0,484,420],
[553,549,438,440,597,516,0,456],
[587,540,452,582,645,580,544,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 80, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,492,492,536,511,501,542,508],
[508,0,498,493,503,496,511,508],
[508,502,0,523,508,486,510,477],
[464,507,477,0,494,491,535,492],
[489,497,492,506,0,495,495,496],
[499,504,514,509,505,0,504,514],
[458,489,490,465,505,496,0,469],
[492,492,523,508,504,486,531,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 81, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,489,524,477,503,576,520,511],
[511,0,520,501,513,522,484,499],
[476,480,0,465,490,553,458,491],
[523,499,535,0,523,566,497,490],
[497,487,510,477,0,562,503,476],
[424,478,447,434,438,0,426,424],
[480,516,542,503,497,574,0,504],
[489,501,509,510,524,576,496,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 82, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,503,504,505,480,492,482,497],
[497,0,498,491,476,496,487,511],
[496,502,0,484,488,489,492,501],
[495,509,516,0,498,493,515,494],
[520,524,512,502,0,492,519,524],
[508,504,511,507,508,0,500,502],
[518,513,508,485,481,500,0,509],
[503,489,499,506,476,498,491,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 83, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,500,484,489,483,494,493,535],
[500,0,502,509,495,501,505,521],
[516,498,0,518,483,491,522,528],
[511,491,482,0,518,527,534,497],
[517,505,517,482,0,506,517,519],
[506,499,509,473,494,0,505,514],
[507,495,478,466,483,495,0,511],
[465,479,472,503,481,486,489,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 84, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,477,523,513,530,514,480,489],
[523,0,521,535,524,482,474,494],
[477,479,0,481,499,503,481,488],
[487,465,519,0,489,494,488,499],
[470,476,501,511,0,499,471,501],
[486,518,497,506,501,0,460,507],
[520,526,519,512,529,540,0,500],
[511,506,512,501,499,493,500,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 85, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,491,496,523,486,521,503,507],
[509,0,489,513,519,525,507,519],
[504,511,0,515,507,514,489,521],
[477,487,485,0,480,497,500,476],
[514,481,493,520,0,521,497,504],
[479,475,486,503,479,0,488,502],
[497,493,511,500,503,512,0,504],
[493,481,479,524,496,498,496,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 86, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,514,528,519,521,514,500,522],
[486,0,498,497,500,525,491,520],
[472,502,0,489,496,482,476,479],
[481,503,511,0,483,487,500,497],
[479,500,504,517,0,491,500,497],
[486,475,518,513,509,0,487,508],
[500,509,524,500,500,513,0,506],
[478,480,521,503,503,492,494,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 87, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,506,522,513,488,510,473,501],
[494,0,516,479,514,490,464,478],
[478,484,0,497,463,476,434,471],
[487,521,503,0,490,475,466,505],
[512,486,537,510,0,515,481,484],
[490,510,524,525,485,0,485,497],
[527,536,566,534,519,515,0,498],
[499,522,529,495,516,503,502,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 88, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,465,484,486,472,511,455,461],
[535,0,476,506,519,504,550,507],
[516,524,0,521,494,536,507,498],
[514,494,479,0,509,500,505,520],
[528,481,506,491,0,531,486,521],
[489,496,464,500,469,0,494,517],
[545,450,493,495,514,506,0,511],
[539,493,502,480,479,483,489,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 89, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,496,489,523,502,527,490,525],
[504,0,508,490,526,501,491,526],
[511,492,0,546,502,504,531,514],
[477,510,454,0,502,488,526,502],
[498,474,498,498,0,465,475,510],
[473,499,496,512,535,0,479,525],
[510,509,469,474,525,521,0,528],
[475,474,486,498,490,475,472,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 90, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,468,470,499,539,483,544,491],
[532,0,556,492,520,590,534,536],
[530,444,0,495,502,472,513,537],
[501,508,505,0,611,455,535,575],
[461,480,498,389,0,494,450,486],
[517,410,528,545,506,0,501,471],
[456,466,487,465,550,499,0,546],
[509,464,463,425,514,529,454,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 91, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,494,509,475,442,471,481,484],
[506,0,514,481,509,479,476,497],
[491,486,0,448,451,482,493,475],
[525,519,552,0,471,483,492,525],
[558,491,549,529,0,525,535,529],
[529,521,518,517,475,0,502,541],
[519,524,507,508,465,498,0,506],
[516,503,525,475,471,459,494,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 92, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,454,490,522,499,557,496,490],
[546,0,526,508,494,528,509,496],
[510,474,0,503,509,539,495,491],
[478,492,497,0,507,516,517,467],
[501,506,491,493,0,519,512,503],
[443,472,461,484,481,0,454,461],
[504,491,505,483,488,546,0,484],
[510,504,509,533,497,539,516,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 93, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,464,525,482,547,504,471,495],
[536,0,551,550,530,532,477,514],
[475,449,0,531,490,546,493,491],
[518,450,469,0,520,494,504,446],
[453,470,510,480,0,454,449,481],
[496,468,454,506,546,0,510,496],
[529,523,507,496,551,490,0,473],
[505,486,509,554,519,504,527,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 94, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,488,488,516,499,507,522,498],
[512,0,453,529,475,547,528,491],
[512,547,0,497,513,526,504,464],
[484,471,503,0,510,480,541,501],
[501,525,487,490,0,490,503,506],
[493,453,474,520,510,0,562,517],
[478,472,496,459,497,438,0,477],
[502,509,536,499,494,483,523,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 95, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,477,485,494,497,474,501,497],
[523,0,495,484,478,484,509,505],
[515,505,0,486,495,486,507,493],
[506,516,514,0,513,493,532,489],
[503,522,505,487,0,501,503,502],
[526,516,514,507,499,0,525,498],
[499,491,493,468,497,475,0,486],
[503,495,507,511,498,502,514,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 96, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,528,497,517,560,550,517,500],
[472,0,516,552,599,582,511,560],
[503,484,0,554,520,567,548,471],
[483,448,446,0,535,549,485,464],
[440,401,480,465,0,546,484,433],
[450,418,433,451,454,0,472,407],
[483,489,452,515,516,528,0,476],
[500,440,529,536,567,593,524,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 97, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,517,510,500,496,496,491,520],
[483,0,515,490,484,499,478,475],
[490,485,0,495,488,496,478,505],
[500,510,505,0,483,518,513,531],
[504,516,512,517,0,505,491,500],
[504,501,504,482,495,0,485,503],
[509,522,522,487,509,515,0,504],
[480,525,495,469,500,497,496,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 98, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,468,489,522,494,513,494,484],
[532,0,498,496,487,473,462,509],
[511,502,0,490,497,489,501,478],
[478,504,510,0,508,509,505,547],
[506,513,503,492,0,488,510,494],
[487,527,511,491,512,0,504,501],
[506,538,499,495,490,496,0,521],
[516,491,522,453,506,499,479,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 99, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,533,492,455,491,507,509,513],
[467,0,413,490,473,481,498,448],
[508,587,0,494,500,514,488,489],
[545,510,506,0,505,495,482,498],
[509,527,500,495,0,513,494,483],
[493,519,486,505,487,0,475,511],
[491,502,512,518,506,525,0,506],
[487,552,511,502,517,489,494,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 100, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,500,505,512,516,505,513,505],
[500,0,506,504,492,502,484,500],
[495,494,0,507,496,491,514,507],
[488,496,493,0,495,482,494,511],
[484,508,504,505,0,517,508,506],
[495,498,509,518,483,0,496,514],
[487,516,486,506,492,504,0,513],
[495,500,493,489,494,486,487,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 101, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,488,500,481,468,488,503,454],
[512,0,489,507,490,486,515,505],
[500,511,0,506,484,481,521,510],
[519,493,494,0,503,483,495,486],
[532,510,516,497,0,488,516,499],
[512,514,519,517,512,0,522,494],
[497,485,479,505,484,478,0,475],
[546,495,490,514,501,506,525,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 102, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,471,480,566,508,443,573,509],
[529,0,437,484,469,494,518,495],
[520,563,0,579,528,494,617,505],
[434,516,421,0,496,506,567,508],
[492,531,472,504,0,395,531,517],
[557,506,506,494,605,0,521,488],
[427,482,383,433,469,479,0,500],
[491,505,495,492,483,512,500,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 103, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,510,493,522,480,526,499,540],
[490,0,491,499,528,485,555,532],
[507,509,0,495,512,497,539,518],
[478,501,505,0,507,496,518,540],
[520,472,488,493,0,490,484,504],
[474,515,503,504,510,0,504,517],
[501,445,461,482,516,496,0,507],
[460,468,482,460,496,483,493,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 104, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,506,559,505,446,477,483,498],
[494,0,484,447,488,512,507,474],
[441,516,0,478,466,460,465,411],
[495,553,522,0,507,523,487,477],
[554,512,534,493,0,479,465,518],
[523,488,540,477,521,0,513,461],
[517,493,535,513,535,487,0,460],
[502,526,589,523,482,539,540,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 105, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,534,493,500,508,524,535,529],
[466,0,456,468,490,500,478,518],
[507,544,0,545,511,527,495,529],
[500,532,455,0,475,488,477,511],
[492,510,489,525,0,500,485,526],
[476,500,473,512,500,0,476,553],
[465,522,505,523,515,524,0,540],
[471,482,471,489,474,447,460,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 106, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,485,488,482,492,503,507,495],
[515,0,473,504,482,504,498,493],
[512,527,0,502,493,514,509,509],
[518,496,498,0,484,512,502,499],
[508,518,507,516,0,520,479,494],
[497,496,486,488,480,0,491,486],
[493,502,491,498,521,509,0,499],
[505,507,491,501,506,514,501,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 107, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,493,556,531,510,564,536,671],
[507,0,500,555,555,572,500,601],
[444,500,0,451,460,562,473,527],
[469,445,549,0,558,565,465,575],
[490,445,540,442,0,560,509,608],
[436,428,438,435,440,0,429,532],
[464,500,527,535,491,571,0,571],
[329,399,473,425,392,468,429,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 108, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,502,507,484,516,503,491,487],
[498,0,515,500,518,514,482,491],
[493,485,0,491,454,465,483,481],
[516,500,509,0,503,518,517,475],
[484,482,546,497,0,507,527,514],
[497,486,535,482,493,0,497,494],
[509,518,517,483,473,503,0,487],
[513,509,519,525,486,506,513,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 109, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,479,485,532,494,532,497,542],
[521,0,491,524,500,519,494,529],
[515,509,0,523,509,481,525,522],
[468,476,477,0,482,464,468,494],
[506,500,491,518,0,506,497,539],
[468,481,519,536,494,0,497,523],
[503,506,475,532,503,503,0,503],
[458,471,478,506,461,477,497,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 110, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,546,494,418,453,477,541,508],
[454,0,481,422,444,511,523,523],
[506,519,0,510,494,464,513,471],
[582,578,490,0,476,506,535,558],
[547,556,506,524,0,493,571,531],
[523,489,536,494,507,0,519,485],
[459,477,487,465,429,481,0,464],
[492,477,529,442,469,515,536,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 111, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,492,487,489,461,533,495,534],
[508,0,501,505,509,546,497,520],
[513,499,0,509,495,523,463,501],
[511,495,491,0,483,476,489,510],
[539,491,505,517,0,552,521,517],
[467,454,477,524,448,0,494,507],
[505,503,537,511,479,506,0,549],
[466,480,499,490,483,493,451,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 112, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,503,504,530,511,516,497,508],
[497,0,493,543,508,494,504,534],
[496,507,0,519,513,494,491,520],
[470,457,481,0,457,497,488,504],
[489,492,487,543,0,482,496,513],
[484,506,506,503,518,0,500,527],
[503,496,509,512,504,500,0,509],
[492,466,480,496,487,473,491,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 113, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,517,492,484,497,507,491,468],
[483,0,494,487,510,500,505,510],
[508,506,0,511,512,499,482,481],
[516,513,489,0,495,511,447,476],
[503,490,488,505,0,512,507,485],
[493,500,501,489,488,0,484,488],
[509,495,518,553,493,516,0,506],
[532,490,519,524,515,512,494,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 114, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,463,460,509,522,513,468,515],
[537,0,511,549,527,493,503,536],
[540,489,0,541,545,509,516,504],
[491,451,459,0,463,434,486,481],
[478,473,455,537,0,425,489,491],
[487,507,491,566,575,0,509,527],
[532,497,484,514,511,491,0,521],
[485,464,496,519,509,473,479,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 115, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,574,583,553,539,545,493,526],
[426,0,493,466,461,479,410,441],
[417,507,0,423,435,526,432,410],
[447,534,577,0,463,491,506,449],
[461,539,565,537,0,591,521,500],
[455,521,474,509,409,0,442,424],
[507,590,568,494,479,558,0,488],
[474,559,590,551,500,576,512,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 116, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,445,427,442,454,436,417,427],
[555,0,434,463,450,434,396,432],
[573,566,0,498,494,492,509,437],
[558,537,502,0,494,514,434,519],
[546,550,506,506,0,461,466,460],
[564,566,508,486,539,0,480,516],
[583,604,491,566,534,520,0,475],
[573,568,563,481,540,484,525,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 117, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,510,508,514,496,559,534,511],
[490,0,451,482,501,502,501,491],
[492,549,0,527,499,557,527,531],
[486,518,473,0,483,536,518,472],
[504,499,501,517,0,532,519,504],
[441,498,443,464,468,0,471,474],
[466,499,473,482,481,529,0,503],
[489,509,469,528,496,526,497,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 118, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,502,521,495,525,516,532,544],
[498,0,517,520,516,535,498,545],
[479,483,0,492,480,479,498,516],
[505,480,508,0,500,538,508,520],
[475,484,520,500,0,496,482,528],
[484,465,521,462,504,0,510,509],
[468,502,502,492,518,490,0,527],
[456,455,484,480,472,491,473,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 119, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,471,470,487,521,455,469,447],
[529,0,519,511,500,505,503,492],
[530,481,0,535,508,499,504,504],
[513,489,465,0,496,476,480,505],
[479,500,492,504,0,493,491,483],
[545,495,501,524,507,0,500,530],
[531,497,496,520,509,500,0,507],
[553,508,496,495,517,470,493,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 120, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,494,486,490,529,487,484,506],
[506,0,516,479,526,493,489,550],
[514,484,0,500,527,505,508,561],
[510,521,500,0,482,504,470,519],
[471,474,473,518,0,517,509,526],
[513,507,495,496,483,0,493,515],
[516,511,492,530,491,507,0,524],
[494,450,439,481,474,485,476,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 121, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,482,510,550,499,516,511,504],
[518,0,525,535,532,482,452,491],
[490,475,0,527,512,543,465,509],
[450,465,473,0,495,480,438,502],
[501,468,488,505,0,509,438,473],
[484,518,457,520,491,0,443,539],
[489,548,535,562,562,557,0,512],
[496,509,491,498,527,461,488,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 122, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,502,478,486,528,458,484,461],
[498,0,481,485,531,474,506,497],
[522,519,0,515,523,488,545,517],
[514,515,485,0,489,547,530,501],
[472,469,477,511,0,500,499,473],
[542,526,512,453,500,0,521,471],
[516,494,455,470,501,479,0,468],
[539,503,483,499,527,529,532,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 123, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,482,506,496,480,518,508,480],
[518,0,542,517,503,537,512,480],
[494,458,0,506,487,506,506,459],
[504,483,494,0,484,514,494,484],
[520,497,513,516,0,530,489,493],
[482,463,494,486,470,0,470,483],
[492,488,494,506,511,530,0,501],
[520,520,541,516,507,517,499,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 124, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,542,502,470,541,517,476,479],
[458,0,466,429,480,465,468,456],
[498,534,0,475,520,516,501,478],
[530,571,525,0,558,561,493,524],
[459,520,480,442,0,525,450,470],
[483,535,484,439,475,0,446,464],
[524,532,499,507,550,554,0,503],
[521,544,522,476,530,536,497,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 125, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,475,574,478,537,622,671,463],
[525,0,548,633,569,697,634,481],
[426,452,0,488,434,495,596,386],
[522,367,512,0,391,550,602,473],
[463,431,566,609,0,704,590,561],
[378,303,505,450,296,0,596,380],
[329,366,404,398,410,404,0,462],
[537,519,614,527,439,620,538,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 126, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,497,447,467,573,481,522,485],
[503,0,410,497,537,478,496,433],
[553,590,0,523,564,546,535,494],
[533,503,477,0,517,461,546,498],
[427,463,436,483,0,451,479,446],
[519,522,454,539,549,0,519,530],
[478,504,465,454,521,481,0,452],
[515,567,506,502,554,470,548,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 127, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,480,488,494,497,489,459,475],
[520,0,525,521,546,519,496,506],
[512,475,0,507,530,517,499,486],
[506,479,493,0,515,510,464,476],
[503,454,470,485,0,491,473,493],
[511,481,483,490,509,0,480,496],
[541,504,501,536,527,520,0,496],
[525,494,514,524,507,504,504,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 128, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,507,525,535,490,504,493,527],
[493,0,522,555,503,484,502,509],
[475,478,0,564,501,493,469,512],
[465,445,436,0,459,464,447,474],
[510,497,499,541,0,511,470,532],
[496,516,507,536,489,0,481,522],
[507,498,531,553,530,519,0,534],
[473,491,488,526,468,478,466,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 129, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,484,531,517,527,491,530,539],
[516,0,519,466,530,499,508,530],
[469,481,0,479,486,462,502,508],
[483,534,521,0,512,513,523,553],
[473,470,514,488,0,507,500,515],
[509,501,538,487,493,0,530,507],
[470,492,498,477,500,470,0,501],
[461,470,492,447,485,493,499,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 130, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,479,494,507,476,486,501,477],
[521,0,499,511,506,504,523,520],
[506,501,0,494,497,499,504,494],
[493,489,506,0,495,496,504,484],
[524,494,503,505,0,492,523,500],
[514,496,501,504,508,0,509,501],
[499,477,496,496,477,491,0,486],
[523,480,506,516,500,499,514,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 131, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,545,504,504,495,531,507,504],
[455,0,474,459,466,487,472,461],
[496,526,0,507,500,516,531,485],
[496,541,493,0,507,524,543,486],
[505,534,500,493,0,506,505,508],
[469,513,484,476,494,0,525,485],
[493,528,469,457,495,475,0,478],
[496,539,515,514,492,515,522,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 132, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,476,465,469,474,452,496,457],
[524,0,531,514,483,511,533,485],
[535,469,0,522,453,496,515,460],
[531,486,478,0,475,521,525,462],
[526,517,547,525,0,497,524,449],
[548,489,504,479,503,0,517,505],
[504,467,485,475,476,483,0,449],
[543,515,540,538,551,495,551,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 133, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,491,474,496,518,514,484,501],
[509,0,502,517,492,503,472,501],
[526,498,0,540,521,490,516,534],
[504,483,460,0,504,498,484,471],
[482,508,479,496,0,520,494,466],
[486,497,510,502,480,0,520,471],
[516,528,484,516,506,480,0,480],
[499,499,466,529,534,529,520,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 134, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,474,469,503,499,506,488,506],
[526,0,497,509,518,523,510,505],
[531,503,0,525,534,513,496,516],
[497,491,475,0,517,518,485,514],
[501,482,466,483,0,510,474,503],
[494,477,487,482,490,0,480,483],
[512,490,504,515,526,520,0,527],
[494,495,484,486,497,517,473,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 135, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,494,525,458,488,462,494,478],
[506,0,496,485,498,506,488,470],
[475,504,0,472,492,459,494,462],
[542,515,528,0,516,509,521,495],
[512,502,508,484,0,497,486,493],
[538,494,541,491,503,0,517,523],
[506,512,506,479,514,483,0,488],
[522,530,538,505,507,477,512,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 136, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,521,523,523,497,528,520,517],
[479,0,484,507,524,491,515,505],
[477,516,0,514,521,492,491,502],
[477,493,486,0,508,504,512,491],
[503,476,479,492,0,497,505,500],
[472,509,508,496,503,0,501,508],
[480,485,509,488,495,499,0,487],
[483,495,498,509,500,492,513,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 137, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,479,506,493,522,522,491,485],
[521,0,522,518,536,561,519,488],
[494,478,0,497,524,568,482,499],
[507,482,503,0,516,509,487,500],
[478,464,476,484,0,541,479,466],
[478,439,432,491,459,0,466,449],
[509,481,518,513,521,534,0,496],
[515,512,501,500,534,551,504,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 138, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,503,493,505,524,496,524,495],
[497,0,509,511,527,493,516,489],
[507,491,0,511,519,500,498,479],
[495,489,489,0,505,499,504,505],
[476,473,481,495,0,491,494,495],
[504,507,500,501,509,0,511,513],
[476,484,502,496,506,489,0,514],
[505,511,521,495,505,487,486,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 139, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,489,496,477,520,530,461,479],
[511,0,497,489,525,483,474,501],
[504,503,0,498,527,513,502,530],
[523,511,502,0,516,537,471,495],
[480,475,473,484,0,487,459,468],
[470,517,487,463,513,0,472,512],
[539,526,498,529,541,528,0,500],
[521,499,470,505,532,488,500,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 140, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,480,510,478,488,482,459,471],
[520,0,500,522,514,520,464,499],
[490,500,0,498,501,512,479,483],
[522,478,502,0,497,524,469,494],
[512,486,499,503,0,505,494,512],
[518,480,488,476,495,0,480,480],
[541,536,521,531,506,520,0,500],
[529,501,517,506,488,520,500,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 141, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,491,524,510,474,527,507,490],
[509,0,473,460,464,503,480,509],
[476,527,0,485,479,497,492,474],
[490,540,515,0,519,485,552,477],
[526,536,521,481,0,564,496,509],
[473,497,503,515,436,0,514,454],
[493,520,508,448,504,486,0,427],
[510,491,526,523,491,546,573,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 142, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,473,465,424,464,464,473,489],
[527,0,516,490,467,514,510,530],
[535,484,0,451,503,505,524,520],
[576,510,549,0,493,512,545,524],
[536,533,497,507,0,492,507,526],
[536,486,495,488,508,0,478,481],
[527,490,476,455,493,522,0,495],
[511,470,480,476,474,519,505,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 143, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,521,514,499,501,530,495,475],
[479,0,510,511,478,483,493,484],
[486,490,0,466,459,510,497,475],
[501,489,534,0,506,517,486,480],
[499,522,541,494,0,508,504,516],
[470,517,490,483,492,0,474,496],
[505,507,503,514,496,526,0,514],
[525,516,525,520,484,504,486,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 144, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,482,511,485,486,494,488,488],
[518,0,509,498,517,493,506,496],
[489,491,0,483,488,473,492,493],
[515,502,517,0,512,496,522,493],
[514,483,512,488,0,500,504,494],
[506,507,527,504,500,0,532,515],
[512,494,508,478,496,468,0,490],
[512,504,507,507,506,485,510,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 145, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,465,532,519,691,555,469,618],
[535,0,740,612,506,548,485,463],
[468,260,0,361,382,440,483,370],
[481,388,639,0,410,534,343,324],
[309,494,618,590,0,431,594,379],
[445,452,560,466,569,0,547,468],
[531,515,517,657,406,453,0,365],
[382,537,630,676,621,532,635,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 146, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,487,481,478,504,491,511,488],
[513,0,479,506,488,469,512,504],
[519,521,0,487,499,522,513,523],
[522,494,513,0,521,502,520,498],
[496,512,501,479,0,472,524,493],
[509,531,478,498,528,0,522,506],
[489,488,487,480,476,478,0,502],
[512,496,477,502,507,494,498,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 147, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,447,512,473,512,432,502,503],
[553,0,506,459,524,545,518,537],
[488,494,0,450,511,474,515,526],
[527,541,550,0,552,560,476,538],
[488,476,489,448,0,463,497,482],
[568,455,526,440,537,0,514,564],
[498,482,485,524,503,486,0,526],
[497,463,474,462,518,436,474,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 148, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,565,543,521,538,455,623,532],
[435,0,438,463,496,467,527,497],
[457,562,0,457,566,459,630,542],
[479,537,543,0,535,500,594,508],
[462,504,434,465,0,505,594,482],
[545,533,541,500,495,0,556,555],
[377,473,370,406,406,444,0,450],
[468,503,458,492,518,445,550,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 149, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,489,486,489,483,471,478,484],
[511,0,491,517,485,470,486,509],
[514,509,0,512,505,500,526,517],
[511,483,488,0,495,476,510,524],
[517,515,495,505,0,461,489,513],
[529,530,500,524,539,0,489,529],
[522,514,474,490,511,511,0,517],
[516,491,483,476,487,471,483,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 150, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,478,498,479,507,490,513,497],
[522,0,476,490,518,520,511,504],
[502,524,0,500,516,486,511,524],
[521,510,500,0,514,513,503,503],
[493,482,484,486,0,510,518,514],
[510,480,514,487,490,0,490,507],
[487,489,489,497,482,510,0,490],
[503,496,476,497,486,493,510,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 151, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,496,503,494,477,540,523,505],
[504,0,485,498,491,515,499,491],
[497,515,0,514,506,506,517,505],
[506,502,486,0,472,513,507,488],
[523,509,494,528,0,535,533,526],
[460,485,494,487,465,0,486,503],
[477,501,483,493,467,514,0,497],
[495,509,495,512,474,497,503,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 152, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,486,505,513,501,504,511,516],
[514,0,504,492,501,503,515,495],
[495,496,0,513,494,513,519,482],
[487,508,487,0,525,488,501,506],
[499,499,506,475,0,498,506,486],
[496,497,487,512,502,0,503,517],
[489,485,481,499,494,497,0,485],
[484,505,518,494,514,483,515,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 153, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,500,456,466,465,477,507,480],
[500,0,497,494,542,516,529,512],
[544,503,0,486,511,498,541,516],
[534,506,514,0,505,498,523,512],
[535,458,489,495,0,497,508,500],
[523,484,502,502,503,0,529,499],
[493,471,459,477,492,471,0,478],
[520,488,484,488,500,501,522,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 154, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,526,458,498,480,509,523,474],
[474,0,434,484,446,509,499,410],
[542,566,0,533,493,549,529,508],
[502,516,467,0,489,523,523,504],
[520,554,507,511,0,550,552,487],
[491,491,451,477,450,0,498,462],
[477,501,471,477,448,502,0,456],
[526,590,492,496,513,538,544,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 155, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,498,478,495,490,522,463,496],
[502,0,509,488,494,512,489,486],
[522,491,0,494,502,510,490,492],
[505,512,506,0,502,513,498,496],
[510,506,498,498,0,522,519,506],
[478,488,490,487,478,0,475,490],
[537,511,510,502,481,525,0,505],
[504,514,508,504,494,510,495,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 156, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,513,530,503,489,518,529,513],
[487,0,509,500,513,486,516,477],
[470,491,0,475,495,497,509,476],
[497,500,525,0,454,468,500,458],
[511,487,505,546,0,516,528,479],
[482,514,503,532,484,0,531,452],
[471,484,491,500,472,469,0,452],
[487,523,524,542,521,548,548,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 157, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,521,551,515,511,483,523,509],
[479,0,523,492,513,505,483,463],
[449,477,0,473,463,464,451,461],
[485,508,527,0,503,507,508,522],
[489,487,537,497,0,482,509,501],
[517,495,536,493,518,0,494,519],
[477,517,549,492,491,506,0,516],
[491,537,539,478,499,481,484,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 158, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,517,505,526,523,490,516,539],
[483,0,490,501,499,408,444,540],
[495,510,0,503,498,425,493,506],
[474,499,497,0,512,463,474,534],
[477,501,502,488,0,488,530,562],
[510,592,575,537,512,0,493,596],
[484,556,507,526,470,507,0,554],
[461,460,494,466,438,404,446,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 159, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,480,471,483,473,495,514,495],
[520,0,501,526,506,514,490,525],
[529,499,0,520,521,537,485,545],
[517,474,480,0,455,486,492,501],
[527,494,479,545,0,497,524,545],
[505,486,463,514,503,0,476,542],
[486,510,515,508,476,524,0,537],
[505,475,455,499,455,458,463,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 160, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,455,495,465,479,490,465,445],
[545,0,477,512,450,446,474,456],
[505,523,0,507,473,504,478,441],
[535,488,493,0,489,435,521,429],
[521,550,527,511,0,533,535,471],
[510,554,496,565,467,0,536,504],
[535,526,522,479,465,464,0,483],
[555,544,559,571,529,496,517,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 161, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,492,522,542,542,516,497,501],
[508,0,501,512,522,460,509,502],
[478,499,0,536,474,494,489,501],
[458,488,464,0,449,507,517,478],
[458,478,526,551,0,459,488,473],
[484,540,506,493,541,0,475,514],
[503,491,511,483,512,525,0,472],
[499,498,499,522,527,486,528,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 162, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,508,518,522,517,493,497,498],
[492,0,482,513,511,466,498,503],
[482,518,0,503,509,500,496,506],
[478,487,497,0,514,475,490,480],
[483,489,491,486,0,488,482,481],
[507,534,500,525,512,0,518,500],
[503,502,504,510,518,482,0,507],
[502,497,494,520,519,500,493,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 163, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,429,347,501,447,416,605,564],
[571,0,615,554,705,516,420,642],
[653,385,0,594,457,395,601,540],
[499,446,406,0,528,595,585,745],
[553,295,543,472,0,598,487,444],
[584,484,605,405,402,0,495,715],
[395,580,399,415,513,505,0,620],
[436,358,460,255,556,285,380,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 164, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,532,506,491,537,508,510,481],
[468,0,491,452,489,488,437,457],
[494,509,0,475,502,478,460,483],
[509,548,525,0,552,521,457,480],
[463,511,498,448,0,460,493,461],
[492,512,522,479,540,0,477,496],
[490,563,540,543,507,523,0,508],
[519,543,517,520,539,504,492,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 165, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,476,530,491,501,480,451,486],
[524,0,522,470,515,523,500,506],
[470,478,0,459,475,509,455,448],
[509,530,541,0,520,542,514,491],
[499,485,525,480,0,499,449,456],
[520,477,491,458,501,0,481,468],
[549,500,545,486,551,519,0,509],
[514,494,552,509,544,532,491,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 166, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,490,490,483,500,515,512,489],
[510,0,511,501,515,518,518,498],
[510,489,0,491,506,515,528,504],
[517,499,509,0,500,521,515,502],
[500,485,494,500,0,507,511,500],
[485,482,485,479,493,0,493,486],
[488,482,472,485,489,507,0,493],
[511,502,496,498,500,514,507,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 167, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,492,507,520,500,513,516,491],
[508,0,503,516,506,488,502,490],
[493,497,0,515,479,500,493,495],
[480,484,485,0,466,480,495,485],
[500,494,521,534,0,509,529,515],
[487,512,500,520,491,0,502,512],
[484,498,507,505,471,498,0,492],
[509,510,505,515,485,488,508,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 168, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,488,510,494,503,489,517,525],
[512,0,511,516,489,525,534,519],
[490,489,0,485,481,485,498,501],
[506,484,515,0,492,479,482,500],
[497,511,519,508,0,507,514,492],
[511,475,515,521,493,0,503,492],
[483,466,502,518,486,497,0,498],
[475,481,499,500,508,508,502,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 169, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,481,495,546,526,465,480,509],
[519,0,519,522,496,475,556,506],
[505,481,0,530,580,478,491,539],
[454,478,470,0,500,455,449,500],
[474,504,420,500,0,468,489,453],
[535,525,522,545,532,0,522,484],
[520,444,509,551,511,478,0,549],
[491,494,461,500,547,516,451,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 170, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,523,513,537,521,492,486,523],
[477,0,475,507,480,480,477,496],
[487,525,0,517,497,494,514,508],
[463,493,483,0,475,480,448,475],
[479,520,503,525,0,480,499,487],
[508,520,506,520,520,0,520,494],
[514,523,486,552,501,480,0,501],
[477,504,492,525,513,506,499,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 171, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,556,489,492,459,491,455,501],
[444,0,473,498,438,467,505,455],
[511,527,0,518,435,489,448,427],
[508,502,482,0,452,457,476,501],
[541,562,565,548,0,524,493,517],
[509,533,511,543,476,0,533,486],
[545,495,552,524,507,467,0,505],
[499,545,573,499,483,514,495,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 172, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,500,486,477,489,523,489,485],
[500,0,497,520,521,547,487,492],
[514,503,0,485,517,485,480,465],
[523,480,515,0,494,524,535,519],
[511,479,483,506,0,509,489,529],
[477,453,515,476,491,0,446,472],
[511,513,520,465,511,554,0,479],
[515,508,535,481,471,528,521,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 173, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,512,499,456,516,530,508,489],
[488,0,461,450,496,485,467,443],
[501,539,0,500,552,536,546,526],
[544,550,500,0,505,535,566,528],
[484,504,448,495,0,540,501,448],
[470,515,464,465,460,0,485,440],
[492,533,454,434,499,515,0,431],
[511,557,474,472,552,560,569,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 174, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,536,516,554,624,541,530,482],
[464,0,513,591,572,571,509,451],
[484,487,0,529,547,513,485,496],
[446,409,471,0,520,482,478,464],
[376,428,453,480,0,467,502,474],
[459,429,487,518,533,0,418,444],
[470,491,515,522,498,582,0,515],
[518,549,504,536,526,556,485,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 175, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,472,493,517,488,485,484,498],
[528,0,489,521,498,506,501,515],
[507,511,0,510,501,491,521,509],
[483,479,490,0,484,483,476,482],
[512,502,499,516,0,501,498,503],
[515,494,509,517,499,0,507,489],
[516,499,479,524,502,493,0,527],
[502,485,491,518,497,511,473,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 176, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,516,527,525,556,498,495,533],
[484,0,514,492,466,484,490,538],
[473,486,0,496,488,479,514,525],
[475,508,504,0,514,540,513,506],
[444,534,512,486,0,489,509,491],
[502,516,521,460,511,0,516,547],
[505,510,486,487,491,484,0,514],
[467,462,475,494,509,453,486,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 177, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,522,516,494,491,495,510,507],
[478,0,503,490,492,508,516,498],
[484,497,0,505,479,481,506,529],
[506,510,495,0,488,506,503,501],
[509,508,521,512,0,495,525,537],
[505,492,519,494,505,0,500,516],
[490,484,494,497,475,500,0,511],
[493,502,471,499,463,484,489,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 178, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,501,504,467,526,504,519,511],
[499,0,519,508,557,503,524,550],
[496,481,0,467,521,490,489,503],
[533,492,533,0,562,519,552,550],
[474,443,479,438,0,465,488,472],
[496,497,510,481,535,0,524,517],
[481,476,511,448,512,476,0,478],
[489,450,497,450,528,483,522,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 179, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,518,504,517,533,520,500,512],
[482,0,492,501,505,504,478,494],
[496,508,0,505,512,501,493,504],
[483,499,495,0,526,517,478,509],
[467,495,488,474,0,507,478,510],
[480,496,499,483,493,0,493,486],
[500,522,507,522,522,507,0,505],
[488,506,496,491,490,514,495,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 180, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,505,476,456,457,471,488,467],
[495,0,482,473,483,491,478,486],
[524,518,0,488,517,492,513,489],
[544,527,512,0,492,493,500,491],
[543,517,483,508,0,514,514,515],
[529,509,508,507,486,0,517,477],
[512,522,487,500,486,483,0,510],
[533,514,511,509,485,523,490,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 181, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,473,494,534,457,458,545,459],
[527,0,512,563,577,489,601,555],
[506,488,0,505,470,434,513,475],
[466,437,495,0,537,442,511,493],
[543,423,530,463,0,470,589,533],
[542,511,566,558,530,0,583,494],
[455,399,487,489,411,417,0,458],
[541,445,525,507,467,506,542,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 182, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,440,516,544,555,568,471,537],
[560,0,530,488,511,534,473,539],
[484,470,0,469,531,497,512,563],
[456,512,531,0,543,516,491,546],
[445,489,469,457,0,472,501,533],
[432,466,503,484,528,0,460,517],
[529,527,488,509,499,540,0,592],
[463,461,437,454,467,483,408,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 183, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,529,497,513,506,462,498,474],
[471,0,510,484,501,455,484,457],
[503,490,0,503,484,488,493,473],
[487,516,497,0,499,486,472,501],
[494,499,516,501,0,480,495,511],
[538,545,512,514,520,0,514,496],
[502,516,507,528,505,486,0,510],
[526,543,527,499,489,504,490,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 184, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,537,529,488,472,474,502,497],
[463,0,473,497,451,476,472,468],
[471,527,0,493,473,485,502,480],
[512,503,507,0,470,468,481,491],
[528,549,527,530,0,506,497,517],
[526,524,515,532,494,0,513,533],
[498,528,498,519,503,487,0,483],
[503,532,520,509,483,467,517,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 185, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,541,494,497,511,497,502,505],
[459,0,446,485,461,485,479,486],
[506,554,0,481,473,490,494,518],
[503,515,519,0,461,538,467,524],
[489,539,527,539,0,528,513,513],
[503,515,510,462,472,0,483,465],
[498,521,506,533,487,517,0,487],
[495,514,482,476,487,535,513,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 186, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,503,486,453,485,501,533,465],
[497,0,496,456,498,503,516,486],
[514,504,0,493,489,505,551,506],
[547,544,507,0,509,500,535,529],
[515,502,511,491,0,527,539,490],
[499,497,495,500,473,0,516,515],
[467,484,449,465,461,484,0,454],
[535,514,494,471,510,485,546,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 187, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,502,491,486,483,512,488,480],
[498,0,519,503,497,510,495,486],
[509,481,0,475,477,496,491,482],
[514,497,525,0,510,533,520,520],
[517,503,523,490,0,519,500,500],
[488,490,504,467,481,0,493,485],
[512,505,509,480,500,507,0,517],
[520,514,518,480,500,515,483,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 188, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,503,561,565,535,523,494,503],
[497,0,559,566,517,532,505,484],
[439,441,0,467,453,501,496,426],
[435,434,533,0,500,456,446,443],
[465,483,547,500,0,459,499,468],
[477,468,499,544,541,0,474,482],
[506,495,504,554,501,526,0,467],
[497,516,574,557,532,518,533,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 189, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,497,515,489,513,483,488,496],
[503,0,491,479,491,483,478,500],
[485,509,0,503,497,482,486,529],
[511,521,497,0,503,504,502,513],
[487,509,503,497,0,496,470,510],
[517,517,518,496,504,0,490,507],
[512,522,514,498,530,510,0,521],
[504,500,471,487,490,493,479,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 190, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,493,473,455,455,479,461,482],
[507,0,501,481,483,460,464,465],
[527,499,0,467,473,504,491,489],
[545,519,533,0,500,527,520,487],
[545,517,527,500,0,511,523,520],
[521,540,496,473,489,0,509,462],
[539,536,509,480,477,491,0,482],
[518,535,511,513,480,538,518,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 191, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,504,481,487,482,499,486,479],
[496,0,513,506,515,523,508,506],
[519,487,0,501,507,490,483,481],
[513,494,499,0,476,517,487,517],
[518,485,493,524,0,494,503,517],
[501,477,510,483,506,0,506,511],
[514,492,517,513,497,494,0,514],
[521,494,519,483,483,489,486,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 192, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,438,500,506,485,520,535,510],
[562,0,523,468,510,512,528,516],
[500,477,0,485,493,530,560,480],
[494,532,515,0,491,546,607,520],
[515,490,507,509,0,500,525,492],
[480,488,470,454,500,0,568,489],
[465,472,440,393,475,432,0,469],
[490,484,520,480,508,511,531,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 193, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,515,485,517,506,498,519,514],
[485,0,485,475,538,520,497,498],
[515,515,0,525,501,517,500,522],
[483,525,475,0,517,545,508,511],
[494,462,499,483,0,482,524,488],
[502,480,483,455,518,0,500,494],
[481,503,500,492,476,500,0,499],
[486,502,478,489,512,506,501,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 194, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,473,486,501,522,484,494,456],
[527,0,509,506,499,528,489,497],
[514,491,0,503,528,485,443,444],
[499,494,497,0,516,504,478,463],
[478,501,472,484,0,505,507,464],
[516,472,515,496,495,0,478,467],
[506,511,557,522,493,522,0,507],
[544,503,556,537,536,533,493,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 195, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,531,457,447,452,492,432,467],
[469,0,481,459,512,510,427,484],
[543,519,0,510,501,573,517,479],
[553,541,490,0,488,546,500,483],
[548,488,499,512,0,503,436,502],
[508,490,427,454,497,0,450,412],
[568,573,483,500,564,550,0,528],
[533,516,521,517,498,588,472,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 196, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,536,515,486,483,477,480,506],
[464,0,528,456,453,442,483,466],
[485,472,0,435,494,452,444,484],
[514,544,565,0,528,530,455,493],
[517,547,506,472,0,508,502,508],
[523,558,548,470,492,0,517,485],
[520,517,556,545,498,483,0,501],
[494,534,516,507,492,515,499,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 197, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,472,536,503,519,495,498,479],
[528,0,533,515,550,532,481,526],
[464,467,0,512,528,477,462,456],
[497,485,488,0,544,529,468,490],
[481,450,472,456,0,491,461,496],
[505,468,523,471,509,0,501,493],
[502,519,538,532,539,499,0,549],
[521,474,544,510,504,507,451,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 198, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,537,537,500,523,524,568,525],
[463,0,483,471,468,468,541,517],
[463,517,0,468,493,471,494,479],
[500,529,532,0,552,542,547,533],
[477,532,507,448,0,474,485,510],
[476,532,529,458,526,0,512,537],
[432,459,506,453,515,488,0,486],
[475,483,521,467,490,463,514,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 199, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,511,504,497,506,489,485,502],
[489,0,463,499,507,478,483,491],
[496,537,0,493,498,509,510,502],
[503,501,507,0,490,495,483,486],
[494,493,502,510,0,480,499,501],
[511,522,491,505,520,0,491,515],
[515,517,490,517,501,509,0,482],
[498,509,498,514,499,485,518,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 1000, 200, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/mebb/mebb_8_1000.csv", index=False, header=False)