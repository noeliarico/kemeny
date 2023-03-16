
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg

rep = 3
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,1005,965,883,1004,920,1011,963],
[995,0,1001,982,1028,960,931,979],
[1035,999,0,924,978,986,1012,965],
[1117,1018,1076,0,1004,994,994,1024],
[996,972,1022,996,0,960,993,943],
[1080,1040,1014,1006,1040,0,1003,969],
[989,1069,988,1006,1007,997,0,992],
[1037,1021,1035,976,1057,1031,1008,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 1, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,982,991,963,970,1024,989,1050],
[1018,0,996,971,997,1001,996,1011],
[1009,1004,0,995,1000,1003,987,1020],
[1037,1029,1005,0,1015,995,994,1020],
[1030,1003,1000,985,0,994,1007,998],
[976,999,997,1005,1006,0,985,992],
[1011,1004,1013,1006,993,1015,0,1017],
[950,989,980,980,1002,1008,983,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 2, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1035,1021,964,1032,984,1000,981],
[965,0,1043,1039,985,984,975,950],
[979,957,0,958,963,941,940,989],
[1036,961,1042,0,1016,965,957,990],
[968,1015,1037,984,0,969,928,950],
[1016,1016,1059,1035,1031,0,1039,979],
[1000,1025,1060,1043,1072,961,0,1000],
[1019,1050,1011,1010,1050,1021,1000,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 3, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1006,1034,1000,1014,998,1000,991],
[994,0,984,989,1006,1008,981,977],
[966,1016,0,972,996,968,1010,981],
[1000,1011,1028,0,1018,1042,992,1000],
[986,994,1004,982,0,1031,996,982],
[1002,992,1032,958,969,0,1010,996],
[1000,1019,990,1008,1004,990,0,988],
[1009,1023,1019,1000,1018,1004,1012,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 4, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1038,1061,967,996,1013,993,961],
[962,0,1005,939,932,938,967,969],
[939,995,0,998,989,941,924,908],
[1033,1061,1002,0,963,909,926,943],
[1004,1068,1011,1037,0,981,988,969],
[987,1062,1059,1091,1019,0,1012,1002],
[1007,1033,1076,1074,1012,988,0,1003],
[1039,1031,1092,1057,1031,998,997,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 5, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,958,1027,1045,997,953,966,1001],
[1042,0,1061,1013,1032,997,997,1030],
[973,939,0,939,937,981,906,1006],
[955,987,1061,0,940,964,949,981],
[1003,968,1063,1060,0,1054,1074,1024],
[1047,1003,1019,1036,946,0,1010,1034],
[1034,1003,1094,1051,926,990,0,962],
[999,970,994,1019,976,966,1038,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 6, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1006,1026,1012,1027,997,997,1003],
[994,0,997,1031,974,970,986,983],
[974,1003,0,999,1018,985,963,983],
[988,969,1001,0,983,982,1002,986],
[973,1026,982,1017,0,972,994,971],
[1003,1030,1015,1018,1028,0,1006,998],
[1003,1014,1037,998,1006,994,0,965],
[997,1017,1017,1014,1029,1002,1035,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 7, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1012,1009,1017,1028,993,1031,1000],
[988,0,985,1012,1024,1001,1018,990],
[991,1015,0,1017,1069,1024,996,991],
[983,988,983,0,1013,1005,982,979],
[972,976,931,987,0,989,976,993],
[1007,999,976,995,1011,0,984,967],
[969,982,1004,1018,1024,1016,0,994],
[1000,1010,1009,1021,1007,1033,1006,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 8, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,998,987,985,1001,1033,1042,1021],
[1002,0,967,995,1040,1002,1027,1008],
[1013,1033,0,1002,1023,1009,1026,999],
[1015,1005,998,0,987,983,1014,1037],
[999,960,977,1013,0,989,993,973],
[967,998,991,1017,1011,0,1046,1066],
[958,973,974,986,1007,954,0,982],
[979,992,1001,963,1027,934,1018,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 9, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1019,1009,1029,1037,1002,1006,998],
[981,0,1016,1003,1000,981,1027,982],
[991,984,0,987,998,944,980,976],
[971,997,1013,0,1004,967,982,967],
[963,1000,1002,996,0,970,1008,980],
[998,1019,1056,1033,1030,0,1021,1017],
[994,973,1020,1018,992,979,0,986],
[1002,1018,1024,1033,1020,983,1014,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 10, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,969,1012,999,1046,1002,952,981],
[1031,0,1028,1025,1032,984,1013,1008],
[988,972,0,993,970,993,999,983],
[1001,975,1007,0,1003,992,994,1009],
[954,968,1030,997,0,1008,990,956],
[998,1016,1007,1008,992,0,986,1009],
[1048,987,1001,1006,1010,1014,0,989],
[1019,992,1017,991,1044,991,1011,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 11, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1019,1149,962,1069,1009,1032,995],
[981,0,1070,979,941,1043,1021,949],
[851,930,0,992,970,1014,980,961],
[1038,1021,1008,0,1035,1058,1026,989],
[931,1059,1030,965,0,996,960,1006],
[991,957,986,942,1004,0,894,955],
[968,979,1020,974,1040,1106,0,1040],
[1005,1051,1039,1011,994,1045,960,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 12, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,977,1041,991,1034,966,1024,1034],
[1023,0,1029,973,1062,1004,1060,1015],
[959,971,0,986,927,925,952,939],
[1009,1027,1014,0,979,951,989,1019],
[966,938,1073,1021,0,915,972,1010],
[1034,996,1075,1049,1085,0,1013,1056],
[976,940,1048,1011,1028,987,0,1022],
[966,985,1061,981,990,944,978,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 13, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1055,981,1059,1036,1017,987,996],
[945,0,997,1019,1006,968,970,1058],
[1019,1003,0,1034,1031,1009,987,1019],
[941,981,966,0,1050,952,1034,1008],
[964,994,969,950,0,975,1006,956],
[983,1032,991,1048,1025,0,983,998],
[1013,1030,1013,966,994,1017,0,1030],
[1004,942,981,992,1044,1002,970,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 14, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,998,974,1019,988,994,993,1042],
[1002,0,1001,997,975,1002,982,1002],
[1026,999,0,961,1008,1043,1022,1032],
[981,1003,1039,0,951,993,999,990],
[1012,1025,992,1049,0,1005,1015,1042],
[1006,998,957,1007,995,0,1001,1023],
[1007,1018,978,1001,985,999,0,993],
[958,998,968,1010,958,977,1007,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 15, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1000,1138,1114,1095,1016,1036,969],
[1000,0,1029,945,1187,1067,1059,1022],
[862,971,0,1019,996,900,955,937],
[886,1055,981,0,1003,962,1068,952],
[905,813,1004,997,0,937,989,844],
[984,933,1100,1038,1063,0,943,1124],
[964,941,1045,932,1011,1057,0,985],
[1031,978,1063,1048,1156,876,1015,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 16, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1053,1037,1009,985,1030,1003,1030],
[947,0,992,1000,947,975,1008,1005],
[963,1008,0,972,997,987,1034,1008],
[991,1000,1028,0,951,982,1009,994],
[1015,1053,1003,1049,0,1017,1040,1000],
[970,1025,1013,1018,983,0,1028,1013],
[997,992,966,991,960,972,0,997],
[970,995,992,1006,1000,987,1003,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 17, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1063,1048,1015,1078,960,1065,1065],
[937,0,1086,988,1009,1052,957,1030],
[952,914,0,964,918,966,867,933],
[985,1012,1036,0,1027,1076,1012,1051],
[922,991,1082,973,0,1059,904,906],
[1040,948,1034,924,941,0,1108,946],
[935,1043,1133,988,1096,892,0,1006],
[935,970,1067,949,1094,1054,994,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 18, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1332,1010,1129,1115,1085,897,961],
[668,0,932,1005,1071,1055,1010,945],
[990,1068,0,1137,1216,1009,1289,1046],
[871,995,863,0,1139,1111,1027,982],
[885,929,784,861,0,803,897,858],
[915,945,991,889,1197,0,1090,930],
[1103,990,711,973,1103,910,0,845],
[1039,1055,954,1018,1142,1070,1155,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 19, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,992,991,998,1044,976,1065,1004],
[1008,0,1000,1040,1045,992,1037,1009],
[1009,1000,0,1023,1040,1020,1021,1043],
[1002,960,977,0,1041,953,1019,989],
[956,955,960,959,0,935,1023,948],
[1024,1008,980,1047,1065,0,1032,1050],
[935,963,979,981,977,968,0,985],
[996,991,957,1011,1052,950,1015,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 20, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1002,1002,954,1001,995,971,977],
[998,0,981,995,1021,987,983,986],
[998,1019,0,993,988,1017,1008,941],
[1046,1005,1007,0,990,1000,1023,986],
[999,979,1012,1010,0,981,1017,950],
[1005,1013,983,1000,1019,0,988,994],
[1029,1017,992,977,983,1012,0,1002],
[1023,1014,1059,1014,1050,1006,998,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 21, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,956,1011,955,1003,947,979,991],
[1044,0,983,990,1016,982,987,990],
[989,1017,0,952,991,967,929,989],
[1045,1010,1048,0,1016,1009,965,1017],
[997,984,1009,984,0,965,988,1022],
[1053,1018,1033,991,1035,0,1029,1031],
[1021,1013,1071,1035,1012,971,0,1041],
[1009,1010,1011,983,978,969,959,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 22, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,980,1014,982,1003,984,1015,973],
[1020,0,993,957,1015,978,1025,963],
[986,1007,0,996,1042,995,1073,1031],
[1018,1043,1004,0,999,1010,1014,1037],
[997,985,958,1001,0,955,994,934],
[1016,1022,1005,990,1045,0,1037,1004],
[985,975,927,986,1006,963,0,956],
[1027,1037,969,963,1066,996,1044,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 23, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,989,1005,995,991,1013,1018,972],
[1011,0,979,983,987,992,1016,1003],
[995,1021,0,1007,990,1000,1017,1012],
[1005,1017,993,0,957,1006,993,973],
[1009,1013,1010,1043,0,1010,1024,987],
[987,1008,1000,994,990,0,997,972],
[982,984,983,1007,976,1003,0,984],
[1028,997,988,1027,1013,1028,1016,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 24, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,988,1019,1012,954,1008,1004,1026],
[1012,0,1014,1047,991,1019,1039,993],
[981,986,0,1027,999,1000,1034,1019],
[988,953,973,0,964,988,984,972],
[1046,1009,1001,1036,0,989,1017,1039],
[992,981,1000,1012,1011,0,989,978],
[996,961,966,1016,983,1011,0,993],
[974,1007,981,1028,961,1022,1007,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 25, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,976,1032,996,1024,1015,980,997],
[1024,0,1034,952,975,973,980,1028],
[968,966,0,970,973,983,972,1034],
[1004,1048,1030,0,1032,1032,995,1054],
[976,1025,1027,968,0,1000,956,989],
[985,1027,1017,968,1000,0,1003,1062],
[1020,1020,1028,1005,1044,997,0,1014],
[1003,972,966,946,1011,938,986,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 26, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1047,1003,1013,1064,1070,1014,999],
[953,0,1003,996,1011,1005,953,979],
[997,997,0,983,1022,1022,982,980],
[987,1004,1017,0,1057,1039,982,1003],
[936,989,978,943,0,1003,1008,965],
[930,995,978,961,997,0,982,990],
[986,1047,1018,1018,992,1018,0,999],
[1001,1021,1020,997,1035,1010,1001,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 27, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,981,979,974,973,976,1042,993],
[1019,0,1025,1034,1002,993,1031,1016],
[1021,975,0,996,983,1000,1021,1010],
[1026,966,1004,0,980,988,1008,984],
[1027,998,1017,1020,0,1035,1023,1029],
[1024,1007,1000,1012,965,0,1028,1015],
[958,969,979,992,977,972,0,967],
[1007,984,990,1016,971,985,1033,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 28, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,927,958,985,1031,980,1025,966],
[1073,0,1005,975,1082,1024,1016,997],
[1042,995,0,1007,1058,1002,1044,1018],
[1015,1025,993,0,1050,1037,1019,1015],
[969,918,942,950,0,957,1005,955],
[1020,976,998,963,1043,0,1023,1025],
[975,984,956,981,995,977,0,942],
[1034,1003,982,985,1045,975,1058,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 29, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1024,966,1012,1058,1041,1044,1048],
[976,0,973,1007,1042,967,955,971],
[1034,1027,0,1050,1010,986,1012,1016],
[988,993,950,0,1059,963,963,1012],
[942,958,990,941,0,955,935,992],
[959,1033,1014,1037,1045,0,963,1012],
[956,1045,988,1037,1065,1037,0,1030],
[952,1029,984,988,1008,988,970,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 30, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1046,1095,858,911,1050,785,1079],
[954,0,963,891,915,1067,1024,913],
[905,1037,0,846,779,1035,822,1017],
[1142,1109,1154,0,879,1019,994,1024],
[1089,1085,1221,1121,0,1042,851,1062],
[950,933,965,981,958,0,745,946],
[1215,976,1178,1006,1149,1255,0,1141],
[921,1087,983,976,938,1054,859,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 31, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,993,1016,1015,1016,1010,1006,1002],
[1007,0,1033,1001,1041,1029,979,990],
[984,967,0,982,1006,977,963,978],
[985,999,1018,0,1008,982,1000,996],
[984,959,994,992,0,976,982,976],
[990,971,1023,1018,1024,0,995,993],
[994,1021,1037,1000,1018,1005,0,1008],
[998,1010,1022,1004,1024,1007,992,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 32, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,952,1008,1050,987,1005,1015,1007],
[1048,0,1073,985,987,1004,988,1020],
[992,927,0,969,932,949,978,933],
[950,1015,1031,0,1013,973,1060,966],
[1013,1013,1068,987,0,969,1020,963],
[995,996,1051,1027,1031,0,1013,987],
[985,1012,1022,940,980,987,0,1005],
[993,980,1067,1034,1037,1013,995,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 33, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1042,1013,1013,1029,979,1003,1039],
[958,0,976,979,1001,986,978,985],
[987,1024,0,1002,1032,1002,1000,1026],
[987,1021,998,0,1033,1028,978,1034],
[971,999,968,967,0,971,960,1016],
[1021,1014,998,972,1029,0,1027,1023],
[997,1022,1000,1022,1040,973,0,1046],
[961,1015,974,966,984,977,954,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 34, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1049,996,989,1012,998,1064,1004],
[951,0,988,986,1001,912,980,885],
[1004,1012,0,1035,933,924,1066,987],
[1011,1014,965,0,967,962,935,907],
[988,999,1067,1033,0,1027,989,962],
[1002,1088,1076,1038,973,0,1009,1060],
[936,1020,934,1065,1011,991,0,936],
[996,1115,1013,1093,1038,940,1064,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 35, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1035,1023,1025,993,1026,978,969],
[965,0,1020,980,1019,1049,1009,1039],
[977,980,0,1024,1012,1041,1014,990],
[975,1020,976,0,1015,1024,1031,976],
[1007,981,988,985,0,1004,1045,989],
[974,951,959,976,996,0,1008,945],
[1022,991,986,969,955,992,0,928],
[1031,961,1010,1024,1011,1055,1072,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 36, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,991,968,1044,1013,1005,981,1020],
[1009,0,996,1034,1018,1039,1004,1032],
[1032,1004,0,1037,996,1030,967,1049],
[956,966,963,0,948,969,991,977],
[987,982,1004,1052,0,1031,1004,1001],
[995,961,970,1031,969,0,979,1024],
[1019,996,1033,1009,996,1021,0,1006],
[980,968,951,1023,999,976,994,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 37, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,962,975,1053,1052,986,965,1013],
[1038,0,990,1065,1071,996,1034,1013],
[1025,1010,0,1055,992,1002,973,963],
[947,935,945,0,1014,936,901,965],
[948,929,1008,986,0,993,994,977],
[1014,1004,998,1064,1007,0,993,1004],
[1035,966,1027,1099,1006,1007,0,1013],
[987,987,1037,1035,1023,996,987,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 38, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,994,1096,1006,960,1053,1002,1061],
[1006,0,1070,941,1046,989,965,1053],
[904,930,0,840,945,944,903,950],
[994,1059,1160,0,1103,1084,1016,1069],
[1040,954,1055,897,0,1051,988,1024],
[947,1011,1056,916,949,0,994,1005],
[998,1035,1097,984,1012,1006,0,1047],
[939,947,1050,931,976,995,953,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 39, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,986,1001,991,997,1009,992,997],
[1014,0,994,954,995,989,1035,1024],
[999,1006,0,1010,1002,1007,1013,981],
[1009,1046,990,0,1037,1025,1036,1026],
[1003,1005,998,963,0,967,985,998],
[991,1011,993,975,1033,0,1014,1018],
[1008,965,987,964,1015,986,0,992],
[1003,976,1019,974,1002,982,1008,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 40, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,983,1000,999,1015,1051,1007,986],
[1017,0,1001,998,999,1023,1011,1007],
[1000,999,0,1013,978,1037,997,961],
[1001,1002,987,0,971,1006,997,974],
[985,1001,1022,1029,0,1030,1007,1003],
[949,977,963,994,970,0,1002,961],
[993,989,1003,1003,993,998,0,969],
[1014,993,1039,1026,997,1039,1031,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 41, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,999,999,1005,987,961,1005,965],
[1001,0,943,1045,969,978,970,966],
[1001,1057,0,1097,1044,1045,1046,995],
[995,955,903,0,958,959,987,958],
[1013,1031,956,1042,0,973,1018,996],
[1039,1022,955,1041,1027,0,1050,1000],
[995,1030,954,1013,982,950,0,985],
[1035,1034,1005,1042,1004,1000,1015,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 42, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,941,1004,854,939,978,989,1059],
[1059,0,1110,1094,1070,973,1137,1090],
[996,890,0,927,776,940,1097,937],
[1146,906,1073,0,1176,1056,1085,1106],
[1061,930,1224,824,0,956,1088,1010],
[1022,1027,1060,944,1044,0,1070,996],
[1011,863,903,915,912,930,0,1038],
[941,910,1063,894,990,1004,962,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 43, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1011,985,1000,993,1002,1000,987],
[989,0,1005,991,983,1015,998,986],
[1015,995,0,1003,986,1002,980,998],
[1000,1009,997,0,975,1000,1013,1011],
[1007,1017,1014,1025,0,1004,1032,972],
[998,985,998,1000,996,0,993,990],
[1000,1002,1020,987,968,1007,0,954],
[1013,1014,1002,989,1028,1010,1046,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 44, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1048,992,1006,1046,1036,1032,1046],
[952,0,993,928,1000,994,959,928],
[1008,1007,0,946,1026,1012,1000,1016],
[994,1072,1054,0,1034,1015,1014,1043],
[954,1000,974,966,0,1001,946,962],
[964,1006,988,985,999,0,961,1018],
[968,1041,1000,986,1054,1039,0,1001],
[954,1072,984,957,1038,982,999,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 45, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,986,1003,1006,1016,988,985,976],
[1014,0,1022,1045,1016,1005,1006,981],
[997,978,0,1020,1035,1008,1027,967],
[994,955,980,0,922,963,1001,998],
[984,984,965,1078,0,1021,1034,988],
[1012,995,992,1037,979,0,1058,953],
[1015,994,973,999,966,942,0,1030],
[1024,1019,1033,1002,1012,1047,970,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 46, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1010,1003,1024,1029,998,1020,996],
[990,0,1006,985,996,975,971,962],
[997,994,0,1019,1023,966,1030,1003],
[976,1015,981,0,988,953,982,982],
[971,1004,977,1012,0,1004,1001,995],
[1002,1025,1034,1047,996,0,977,994],
[980,1029,970,1018,999,1023,0,1025],
[1004,1038,997,1018,1005,1006,975,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 47, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,999,1011,988,1001,968,1010,994],
[1001,0,1038,1003,1011,990,1000,1024],
[989,962,0,1008,1008,1000,986,971],
[1012,997,992,0,1031,995,1015,1029],
[999,989,992,969,0,973,981,988],
[1032,1010,1000,1005,1027,0,1000,1013],
[990,1000,1014,985,1019,1000,0,996],
[1006,976,1029,971,1012,987,1004,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 48, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1002,1017,984,1004,966,960,970],
[998,0,998,978,977,961,960,994],
[983,1002,0,1000,1003,979,1004,982],
[1016,1022,1000,0,986,939,983,987],
[996,1023,997,1014,0,976,987,1011],
[1034,1039,1021,1061,1024,0,994,1024],
[1040,1040,996,1017,1013,1006,0,1024],
[1030,1006,1018,1013,989,976,976,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 49, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1002,971,988,968,987,1003,996],
[998,0,959,986,983,992,981,981],
[1029,1041,0,1016,994,1015,1018,1033],
[1012,1014,984,0,982,1004,999,1004],
[1032,1017,1006,1018,0,1000,981,980],
[1013,1008,985,996,1000,0,1002,999],
[997,1019,982,1001,1019,998,0,999],
[1004,1019,967,996,1020,1001,1001,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 50, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1076,1073,1058,995,1009,983,1000],
[924,0,1019,997,962,978,1013,973],
[927,981,0,962,937,945,1009,947],
[942,1003,1038,0,936,958,1005,940],
[1005,1038,1063,1064,0,983,1017,1051],
[991,1022,1055,1042,1017,0,977,997],
[1017,987,991,995,983,1023,0,935],
[1000,1027,1053,1060,949,1003,1065,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 51, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1042,1001,1032,978,993,988,1007],
[958,0,1003,1003,943,995,1001,980],
[999,997,0,988,1006,1008,1004,992],
[968,997,1012,0,915,1016,1003,1011],
[1022,1057,994,1085,0,1018,1016,1003],
[1007,1005,992,984,982,0,1004,964],
[1012,999,996,997,984,996,0,980],
[993,1020,1008,989,997,1036,1020,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 52, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,990,989,998,973,975,995,981],
[1010,0,1005,978,984,970,1029,1002],
[1011,995,0,1019,1001,989,1009,1025],
[1002,1022,981,0,982,1000,1014,999],
[1027,1016,999,1018,0,995,1028,1003],
[1025,1030,1011,1000,1005,0,1027,986],
[1005,971,991,986,972,973,0,956],
[1019,998,975,1001,997,1014,1044,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 53, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1032,999,975,985,991,1006,1006],
[968,0,983,962,968,974,990,1027],
[1001,1017,0,974,1006,974,1045,992],
[1025,1038,1026,0,1000,997,1017,1020],
[1015,1032,994,1000,0,1014,1019,1011],
[1009,1026,1026,1003,986,0,1043,1031],
[994,1010,955,983,981,957,0,1019],
[994,973,1008,980,989,969,981,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 54, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1011,1056,991,933,993,942,897],
[989,0,1018,993,959,927,912,1005],
[944,982,0,916,888,900,815,943],
[1009,1007,1084,0,963,978,887,976],
[1067,1041,1112,1037,0,981,1003,1055],
[1007,1073,1100,1022,1019,0,978,988],
[1058,1088,1185,1113,997,1022,0,1035],
[1103,995,1057,1024,945,1012,965,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 55, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1040,940,989,905,919,916,1011],
[960,0,943,875,917,949,938,971],
[1060,1057,0,973,902,1009,960,1048],
[1011,1125,1027,0,1014,974,1016,1098],
[1095,1083,1098,986,0,1013,1075,1022],
[1081,1051,991,1026,987,0,1024,997],
[1084,1062,1040,984,925,976,0,1055],
[989,1029,952,902,978,1003,945,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 56, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,962,956,997,999,996,983,987],
[1038,0,984,1011,1030,1029,967,980],
[1044,1016,0,1030,1016,1044,1026,996],
[1003,989,970,0,1044,1048,950,1019],
[1001,970,984,956,0,1037,966,961],
[1004,971,956,952,963,0,932,997],
[1017,1033,974,1050,1034,1068,0,1037],
[1013,1020,1004,981,1039,1003,963,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 57, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,870,940,764,980,1007,940,1028],
[1130,0,1060,969,1061,1000,973,1118],
[1060,940,0,913,923,1151,1072,1095],
[1236,1031,1087,0,996,1144,960,1101],
[1020,939,1077,1004,0,1087,979,1146],
[993,1000,849,856,913,0,909,1044],
[1060,1027,928,1040,1021,1091,0,1053],
[972,882,905,899,854,956,947,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 58, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1017,1055,1010,922,1051,976,1006],
[983,0,1005,993,976,1050,989,977],
[945,995,0,959,941,992,946,924],
[990,1007,1041,0,988,1040,1019,1049],
[1078,1024,1059,1012,0,1030,1052,995],
[949,950,1008,960,970,0,1087,965],
[1024,1011,1054,981,948,913,0,954],
[994,1023,1076,951,1005,1035,1046,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 59, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1005,981,1004,988,995,1002,1044],
[995,0,1019,1030,1017,967,980,1022],
[1019,981,0,1039,1000,973,974,1004],
[996,970,961,0,976,956,951,975],
[1012,983,1000,1024,0,944,965,1047],
[1005,1033,1027,1044,1056,0,984,1094],
[998,1020,1026,1049,1035,1016,0,1043],
[956,978,996,1025,953,906,957,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 60, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,947,988,977,1021,964,1005,968],
[1053,0,1019,1030,965,1000,1017,982],
[1012,981,0,1031,1030,996,1033,993],
[1023,970,969,0,944,1025,1046,1008],
[979,1035,970,1056,0,1067,1068,1014],
[1036,1000,1004,975,933,0,991,985],
[995,983,967,954,932,1009,0,959],
[1032,1018,1007,992,986,1015,1041,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 61, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1016,1025,1025,1041,973,1019,1020],
[984,0,997,1080,1033,1036,1010,1025],
[975,1003,0,1017,1027,999,964,1007],
[975,920,983,0,990,985,978,967],
[959,967,973,1010,0,1010,982,1018],
[1027,964,1001,1015,990,0,1026,1007],
[981,990,1036,1022,1018,974,0,998],
[980,975,993,1033,982,993,1002,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 62, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,941,946,908,935,856,990,1109],
[1059,0,974,863,965,948,1050,1046],
[1054,1026,0,1027,880,1008,1053,1028],
[1092,1137,973,0,1032,988,1086,1015],
[1065,1035,1120,968,0,1025,1089,1060],
[1144,1052,992,1012,975,0,1085,1018],
[1010,950,947,914,911,915,0,982],
[891,954,972,985,940,982,1018,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 63, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1066,988,970,1038,1004,1032,1017],
[934,0,940,975,999,956,992,987],
[1012,1060,0,969,1003,1017,998,1015],
[1030,1025,1031,0,1012,1010,972,949],
[962,1001,997,988,0,1014,976,994],
[996,1044,983,990,986,0,1005,994],
[968,1008,1002,1028,1024,995,0,981],
[983,1013,985,1051,1006,1006,1019,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 64, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1018,994,1015,1007,1023,1035,998],
[982,0,974,1019,1004,1013,1041,1015],
[1006,1026,0,998,978,1022,1006,1013],
[985,981,1002,0,985,1000,995,1008],
[993,996,1022,1015,0,991,1024,1009],
[977,987,978,1000,1009,0,1008,992],
[965,959,994,1005,976,992,0,980],
[1002,985,987,992,991,1008,1020,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 65, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1255,883,1165,1029,1098,942,1124],
[745,0,743,901,859,926,802,952],
[1117,1257,0,1293,1078,1095,956,1170],
[835,1099,707,0,774,1052,829,975],
[971,1141,922,1226,0,1052,1017,1138],
[902,1074,905,948,948,0,905,1072],
[1058,1198,1044,1171,983,1095,0,1084],
[876,1048,830,1025,862,928,916,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 66, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1028,994,1003,993,1010,993,1017],
[972,0,1003,996,1015,999,1001,1019],
[1006,997,0,976,972,1002,967,987],
[997,1004,1024,0,975,1006,1016,1005],
[1007,985,1028,1025,0,1047,999,1009],
[990,1001,998,994,953,0,1007,1013],
[1007,999,1033,984,1001,993,0,998],
[983,981,1013,995,991,987,1002,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 67, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,997,1015,987,978,1037,984,985],
[1003,0,992,987,1013,1022,974,1017],
[985,1008,0,1007,1009,1024,987,998],
[1013,1013,993,0,1029,1050,1005,985],
[1022,987,991,971,0,1013,974,1011],
[963,978,976,950,987,0,951,996],
[1016,1026,1013,995,1026,1049,0,1009],
[1015,983,1002,1015,989,1004,991,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 68, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,943,964,1012,950,982,986,1012],
[1057,0,1025,1065,992,1001,1001,1000],
[1036,975,0,1053,995,959,988,1064],
[988,935,947,0,953,961,901,942],
[1050,1008,1005,1047,0,997,984,1053],
[1018,999,1041,1039,1003,0,972,1027],
[1014,999,1012,1099,1016,1028,0,1042],
[988,1000,936,1058,947,973,958,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 69, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1015,925,1042,1015,1049,1087,982],
[985,0,948,1028,1025,992,1063,971],
[1075,1052,0,1072,1052,999,1054,1009],
[958,972,928,0,969,1023,1047,980],
[985,975,948,1031,0,1017,1004,1014],
[951,1008,1001,977,983,0,1031,1007],
[913,937,946,953,996,969,0,1012],
[1018,1029,991,1020,986,993,988,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 70, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1069,981,990,977,926,1033,1096],
[931,0,960,1050,976,966,1031,1033],
[1019,1040,0,1013,1031,1028,976,1180],
[1010,950,987,0,934,958,955,1167],
[1023,1024,969,1066,0,1011,950,1180],
[1074,1034,972,1042,989,0,1066,1154],
[967,969,1024,1045,1050,934,0,1134],
[904,967,820,833,820,846,866,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 71, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,973,1013,1009,1055,926,1023,967],
[1027,0,1027,967,1009,1014,1035,1017],
[987,973,0,989,1078,973,1044,987],
[991,1033,1011,0,1016,1001,1054,1021],
[945,991,922,984,0,928,1001,926],
[1074,986,1027,999,1072,0,1030,1027],
[977,965,956,946,999,970,0,970],
[1033,983,1013,979,1074,973,1030,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 72, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1009,975,975,971,955,1001,987],
[991,0,1002,964,962,959,992,972],
[1025,998,0,1001,987,987,1025,1003],
[1025,1036,999,0,976,1018,1044,993],
[1029,1038,1013,1024,0,980,1057,1041],
[1045,1041,1013,982,1020,0,1016,1013],
[999,1008,975,956,943,984,0,954],
[1013,1028,997,1007,959,987,1046,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 73, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,965,955,932,950,991,1015,1066],
[1035,0,1011,949,932,958,991,996],
[1045,989,0,894,917,1010,1022,1049],
[1068,1051,1106,0,1011,983,1092,1085],
[1050,1068,1083,989,0,977,1081,1057],
[1009,1042,990,1017,1023,0,1037,1077],
[985,1009,978,908,919,963,0,1065],
[934,1004,951,915,943,923,935,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 74, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1010,1074,1047,972,975,1016,948],
[990,0,1032,993,1023,998,993,998],
[926,968,0,996,936,965,978,969],
[953,1007,1004,0,927,998,994,959],
[1028,977,1064,1073,0,1054,992,989],
[1025,1002,1035,1002,946,0,1051,1002],
[984,1007,1022,1006,1008,949,0,934],
[1052,1002,1031,1041,1011,998,1066,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 75, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,967,1046,1028,1083,1040,1098,1041],
[1033,0,978,1022,985,1017,1093,1040],
[954,1022,0,968,1075,953,1078,1020],
[972,978,1032,0,996,917,1147,1024],
[917,1015,925,1004,0,936,1034,989],
[960,983,1047,1083,1064,0,1084,1041],
[902,907,922,853,966,916,0,881],
[959,960,980,976,1011,959,1119,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 76, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,977,1010,973,971,973,1015,1009],
[1023,0,971,992,1007,1005,1015,983],
[990,1029,0,1004,1043,1015,1017,1003],
[1027,1008,996,0,1016,1043,1029,1039],
[1029,993,957,984,0,1014,1015,1027],
[1027,995,985,957,986,0,1023,1013],
[985,985,983,971,985,977,0,999],
[991,1017,997,961,973,987,1001,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 77, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,989,995,1044,1006,1013,994,1022],
[1011,0,997,1029,1036,1020,1005,1004],
[1005,1003,0,1029,978,1000,995,1023],
[956,971,971,0,979,988,990,1020],
[994,964,1022,1021,0,996,1008,1029],
[987,980,1000,1012,1004,0,979,1019],
[1006,995,1005,1010,992,1021,0,1014],
[978,996,977,980,971,981,986,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 78, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1041,1041,1010,990,1021,996,996],
[959,0,1008,963,989,988,982,967],
[959,992,0,986,946,956,960,943],
[990,1037,1014,0,965,1002,1020,1032],
[1010,1011,1054,1035,0,1018,1007,977],
[979,1012,1044,998,982,0,1010,993],
[1004,1018,1040,980,993,990,0,997],
[1004,1033,1057,968,1023,1007,1003,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 79, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,950,926,974,956,945,964,976],
[1050,0,996,1031,928,978,978,967],
[1074,1004,0,1094,971,1014,1126,1045],
[1026,969,906,0,895,932,1029,989],
[1044,1072,1029,1105,0,986,1039,1060],
[1055,1022,986,1068,1014,0,987,1040],
[1036,1022,874,971,961,1013,0,976],
[1024,1033,955,1011,940,960,1024,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 80, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,993,999,993,978,993,998,1010],
[1007,0,1004,1005,982,1004,1012,1015],
[1001,996,0,963,983,1003,1003,1035],
[1007,995,1037,0,1009,1030,1013,1054],
[1022,1018,1017,991,0,1021,1054,1053],
[1007,996,997,970,979,0,1032,1035],
[1002,988,997,987,946,968,0,1023],
[990,985,965,946,947,965,977,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 81, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,971,1019,1053,999,1025,1114,1069],
[1029,0,1009,1011,986,1078,1083,1036],
[981,991,0,1014,981,1029,1034,969],
[947,989,986,0,998,1042,1090,1032],
[1001,1014,1019,1002,0,1034,1047,998],
[975,922,971,958,966,0,1084,968],
[886,917,966,910,953,916,0,928],
[931,964,1031,968,1002,1032,1072,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 82, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1007,1018,1053,1052,990,971,1055],
[993,0,960,1027,995,953,960,1016],
[982,1040,0,1018,1051,1001,1016,1061],
[947,973,982,0,958,953,909,979],
[948,1005,949,1042,0,980,945,997],
[1010,1047,999,1047,1020,0,1051,1006],
[1029,1040,984,1091,1055,949,0,1022],
[945,984,939,1021,1003,994,978,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 83, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1036,989,1007,975,1046,992,980],
[964,0,987,983,986,978,971,948],
[1011,1013,0,1015,1010,1019,976,999],
[993,1017,985,0,965,990,1021,991],
[1025,1014,990,1035,0,1025,985,1012],
[954,1022,981,1010,975,0,1002,982],
[1008,1029,1024,979,1015,998,0,956],
[1020,1052,1001,1009,988,1018,1044,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 84, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,992,1000,1043,995,1070,1026,1022],
[1008,0,997,1085,1028,1108,1013,1004],
[1000,1003,0,1038,1029,1067,982,978],
[957,915,962,0,966,1020,933,899],
[1005,972,971,1034,0,1057,979,993],
[930,892,933,980,943,0,903,945],
[974,987,1018,1067,1021,1097,0,1041],
[978,996,1022,1101,1007,1055,959,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 85, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1013,989,984,996,962,936,1002],
[987,0,1005,977,933,963,963,985],
[1011,995,0,1011,1046,1006,1010,1020],
[1016,1023,989,0,1000,1004,979,985],
[1004,1067,954,1000,0,1006,985,977],
[1038,1037,994,996,994,0,987,1001],
[1064,1037,990,1021,1015,1013,0,993],
[998,1015,980,1015,1023,999,1007,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 86, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1000,1001,1052,1031,940,1049,1011],
[1000,0,1053,1075,1050,1038,1017,1000],
[999,947,0,1000,958,905,976,995],
[948,925,1000,0,944,953,953,982],
[969,950,1042,1056,0,985,1040,1075],
[1060,962,1095,1047,1015,0,1039,1031],
[951,983,1024,1047,960,961,0,1011],
[989,1000,1005,1018,925,969,989,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 87, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,976,943,968,963,995,987,950],
[1024,0,957,977,986,1030,1006,967],
[1057,1043,0,1000,1003,1048,1062,1001],
[1032,1023,1000,0,1022,1040,1042,982],
[1037,1014,997,978,0,1043,1016,1011],
[1005,970,952,960,957,0,960,931],
[1013,994,938,958,984,1040,0,1004],
[1050,1033,999,1018,989,1069,996,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 88, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1023,981,1005,1018,998,963,993],
[977,0,960,976,995,973,952,981],
[1019,1040,0,972,1011,1025,1004,993],
[995,1024,1028,0,1028,1001,1003,1014],
[982,1005,989,972,0,1008,988,1005],
[1002,1027,975,999,992,0,1003,1013],
[1037,1048,996,997,1012,997,0,1018],
[1007,1019,1007,986,995,987,982,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 89, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,980,995,998,1001,971,987,999],
[1020,0,1036,987,1003,1006,1023,1018],
[1005,964,0,969,963,991,1000,989],
[1002,1013,1031,0,969,1016,994,1015],
[999,997,1037,1031,0,1032,995,1015],
[1029,994,1009,984,968,0,998,1012],
[1013,977,1000,1006,1005,1002,0,1002],
[1001,982,1011,985,985,988,998,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 90, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,966,1076,955,1017,1008,960,976],
[1034,0,1042,1008,1031,1024,987,1004],
[924,958,0,899,970,948,944,979],
[1045,992,1101,0,1032,1035,1004,1018],
[983,969,1030,968,0,1012,942,987],
[992,976,1052,965,988,0,966,959],
[1040,1013,1056,996,1058,1034,0,1029],
[1024,996,1021,982,1013,1041,971,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 91, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1011,986,992,1001,1011,996,967],
[989,0,1012,983,993,1032,1012,996],
[1014,988,0,975,971,1009,983,958],
[1008,1017,1025,0,990,1045,999,1018],
[999,1007,1029,1010,0,1007,1013,996],
[989,968,991,955,993,0,1017,986],
[1004,988,1017,1001,987,983,0,994],
[1033,1004,1042,982,1004,1014,1006,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 92, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1019,964,984,988,947,953,961],
[981,0,985,974,941,938,951,937],
[1036,1015,0,983,1016,972,975,976],
[1016,1026,1017,0,1020,986,974,1006],
[1012,1059,984,980,0,968,969,983],
[1053,1062,1028,1014,1032,0,1064,987],
[1047,1049,1025,1026,1031,936,0,990],
[1039,1063,1024,994,1017,1013,1010,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 93, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,974,953,973,1015,996,986,999],
[1026,0,997,1012,1007,1001,1037,1006],
[1047,1003,0,1001,1009,1003,1027,992],
[1027,988,999,0,1007,1004,1041,986],
[985,993,991,993,0,987,1015,1016],
[1004,999,997,996,1013,0,986,1008],
[1014,963,973,959,985,1014,0,996],
[1001,994,1008,1014,984,992,1004,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 94, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,962,1020,986,975,974,973,1021],
[1038,0,1023,994,1037,1041,1010,1053],
[980,977,0,979,1006,987,985,1046],
[1014,1006,1021,0,1015,1015,999,1020],
[1025,963,994,985,0,1009,969,1032],
[1026,959,1013,985,991,0,1002,1045],
[1027,990,1015,1001,1031,998,0,1020],
[979,947,954,980,968,955,980,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 95, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,986,1022,1000,1009,984,1017,978],
[1014,0,1013,994,1029,1005,1041,1012],
[978,987,0,993,1040,1006,1012,1000],
[1000,1006,1007,0,1029,1002,1006,1025],
[991,971,960,971,0,987,957,952],
[1016,995,994,998,1013,0,1047,1004],
[983,959,988,994,1043,953,0,970],
[1022,988,1000,975,1048,996,1030,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 96, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,968,980,997,1010,1004,1041,998],
[1032,0,1007,1012,1030,999,1062,1007],
[1020,993,0,1029,1021,983,1117,1040],
[1003,988,971,0,987,1000,1023,996],
[990,970,979,1013,0,969,1027,949],
[996,1001,1017,1000,1031,0,1055,1009],
[959,938,883,977,973,945,0,972],
[1002,993,960,1004,1051,991,1028,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 97, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1006,991,1005,992,978,1015,1001],
[994,0,1012,1015,999,1003,1012,982],
[1009,988,0,987,968,965,976,973],
[995,985,1013,0,1010,1021,1012,990],
[1008,1001,1032,990,0,998,1033,1032],
[1022,997,1035,979,1002,0,1006,982],
[985,988,1024,988,967,994,0,993],
[999,1018,1027,1010,968,1018,1007,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 98, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,912,1036,1029,970,962,1038,974],
[1088,0,1059,1019,975,1037,1023,1010],
[964,941,0,1051,1033,937,986,1014],
[971,981,949,0,1011,1006,1038,1011],
[1030,1025,967,989,0,1060,1021,1102],
[1038,963,1063,994,940,0,971,1025],
[962,977,1014,962,979,1029,0,1046],
[1026,990,986,989,898,975,954,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 99, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1154,970,1072,989,1077,1083,1024],
[846,0,890,990,747,1089,1020,886],
[1030,1110,0,987,1057,983,1054,922],
[928,1010,1013,0,788,973,938,1030],
[1011,1253,943,1212,0,1069,1080,1138],
[923,911,1017,1027,931,0,1024,950],
[917,980,946,1062,920,976,0,904],
[976,1114,1078,970,862,1050,1096,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 100, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,944,993,977,982,1011,1053,983],
[1056,0,1073,998,1038,1008,1083,1024],
[1007,927,0,1010,989,990,1054,958],
[1023,1002,990,0,949,1033,986,1033],
[1018,962,1011,1051,0,1003,1052,997],
[989,992,1010,967,997,0,1032,1010],
[947,917,946,1014,948,968,0,994],
[1017,976,1042,967,1003,990,1006,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 101, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,930,916,975,1065,1047,1081,1025],
[1070,0,962,937,944,1044,1056,967],
[1084,1038,0,990,1009,1118,1096,1048],
[1025,1063,1010,0,949,1172,1100,1009],
[935,1056,991,1051,0,1038,1063,1025],
[953,956,882,828,962,0,966,893],
[919,944,904,900,937,1034,0,870],
[975,1033,952,991,975,1107,1130,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 102, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,941,1052,1002,994,1029,978,1016],
[1059,0,1043,1048,998,1015,1042,1011],
[948,957,0,972,964,1023,1005,966],
[998,952,1028,0,946,950,970,968],
[1006,1002,1036,1054,0,1041,999,995],
[971,985,977,1050,959,0,1005,1002],
[1022,958,995,1030,1001,995,0,980],
[984,989,1034,1032,1005,998,1020,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 103, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1002,994,1002,1024,924,1003,1006],
[998,0,1061,1017,1030,966,960,963],
[1006,939,0,1033,1087,1034,1030,1044],
[998,983,967,0,1019,970,1000,952],
[976,970,913,981,0,924,979,1045],
[1076,1034,966,1030,1076,0,983,1062],
[997,1040,970,1000,1021,1017,0,1099],
[994,1037,956,1048,955,938,901,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 104, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1043,1015,1012,1061,1003,1091,995],
[957,0,1004,985,1034,965,1040,1040],
[985,996,0,1018,1005,914,1004,993],
[988,1015,982,0,970,975,1030,1038],
[939,966,995,1030,0,948,1044,954],
[997,1035,1086,1025,1052,0,1086,1070],
[909,960,996,970,956,914,0,930],
[1005,960,1007,962,1046,930,1070,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 105, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1040,1023,1037,1020,1008,1039,1000],
[960,0,985,977,981,966,971,1003],
[977,1015,0,1024,992,1004,1008,1025],
[963,1023,976,0,988,1002,993,989],
[980,1019,1008,1012,0,987,1027,1014],
[992,1034,996,998,1013,0,1008,1003],
[961,1029,992,1007,973,992,0,986],
[1000,997,975,1011,986,997,1014,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 106, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,958,951,980,953,966,960,964],
[1042,0,1008,1029,980,976,1018,1046],
[1049,992,0,1043,999,1001,1008,1029],
[1020,971,957,0,962,966,986,982],
[1047,1020,1001,1038,0,988,1020,1022],
[1034,1024,999,1034,1012,0,1038,1034],
[1040,982,992,1014,980,962,0,1013],
[1036,954,971,1018,978,966,987,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 107, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1019,1003,1012,969,1019,990,971],
[981,0,996,1023,987,982,1003,998],
[997,1004,0,990,980,1008,945,1007],
[988,977,1010,0,982,976,974,983],
[1031,1013,1020,1018,0,998,958,1007],
[981,1018,992,1024,1002,0,972,966],
[1010,997,1055,1026,1042,1028,0,1018],
[1029,1002,993,1017,993,1034,982,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 108, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,964,987,974,968,968,982,986],
[1036,0,1024,1021,976,1030,987,989],
[1013,976,0,986,992,1034,999,1013],
[1026,979,1014,0,1005,1020,1019,1009],
[1032,1024,1008,995,0,1015,963,980],
[1032,970,966,980,985,0,1007,996],
[1018,1013,1001,981,1037,993,0,1032],
[1014,1011,987,991,1020,1004,968,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 109, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,975,1016,992,972,1046,989,1034],
[1025,0,996,997,974,1025,939,986],
[984,1004,0,980,956,1099,938,986],
[1008,1003,1020,0,999,1048,1001,1032],
[1028,1026,1044,1001,0,1024,995,1058],
[954,975,901,952,976,0,929,950],
[1011,1061,1062,999,1005,1071,0,1054],
[966,1014,1014,968,942,1050,946,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 110, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1073,1013,953,963,1031,949,1031],
[927,0,994,990,994,972,900,981],
[987,1006,0,977,1006,1001,971,1023],
[1047,1010,1023,0,1041,976,1050,997],
[1037,1006,994,959,0,1020,960,983],
[969,1028,999,1024,980,0,947,1082],
[1051,1100,1029,950,1040,1053,0,1026],
[969,1019,977,1003,1017,918,974,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 111, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1020,1017,1019,1043,1040,985,984],
[980,0,1034,1002,1021,1042,972,1000],
[983,966,0,976,975,1013,1003,989],
[981,998,1024,0,1045,1058,976,946],
[957,979,1025,955,0,1033,959,966],
[960,958,987,942,967,0,933,967],
[1015,1028,997,1024,1041,1067,0,982],
[1016,1000,1011,1054,1034,1033,1018,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 112, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1014,1008,1002,982,1024,1022,1004],
[986,0,982,1016,990,1038,1035,1029],
[992,1018,0,993,996,1021,1016,1009],
[998,984,1007,0,1002,992,999,1007],
[1018,1010,1004,998,0,1015,1028,1006],
[976,962,979,1008,985,0,1015,986],
[978,965,984,1001,972,985,0,957],
[996,971,991,993,994,1014,1043,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 113, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,947,998,1050,1056,1015,962,982],
[1053,0,1015,1072,1088,1017,1032,973],
[1002,985,0,1021,1041,1090,991,1001],
[950,928,979,0,959,980,960,943],
[944,912,959,1041,0,998,970,925],
[985,983,910,1020,1002,0,1025,977],
[1038,968,1009,1040,1030,975,0,905],
[1018,1027,999,1057,1075,1023,1095,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 114, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1001,1022,1006,1020,1000,963,1009],
[999,0,1016,988,1013,1000,978,965],
[978,984,0,959,989,984,985,985],
[994,1012,1041,0,923,955,980,981],
[980,987,1011,1077,0,1016,995,1007],
[1000,1000,1016,1045,984,0,964,993],
[1037,1022,1015,1020,1005,1036,0,998],
[991,1035,1015,1019,993,1007,1002,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 115, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1016,1030,1020,1035,992,1004,1026],
[984,0,1036,1029,1011,1006,985,982],
[970,964,0,1003,1009,988,974,996],
[980,971,997,0,1010,982,983,982],
[965,989,991,990,0,994,993,1005],
[1008,994,1012,1018,1006,0,984,1010],
[996,1015,1026,1017,1007,1016,0,1026],
[974,1018,1004,1018,995,990,974,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 116, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1024,1038,994,972,989,941,994],
[976,0,1033,995,970,972,968,999],
[962,967,0,953,956,965,953,976],
[1006,1005,1047,0,994,984,961,1014],
[1028,1030,1044,1006,0,1034,1007,998],
[1011,1028,1035,1016,966,0,961,984],
[1059,1032,1047,1039,993,1039,0,1003],
[1006,1001,1024,986,1002,1016,997,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 117, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1035,1016,979,993,968,1011,1015],
[965,0,970,977,990,945,986,985],
[984,1030,0,1013,1014,989,1008,1011],
[1021,1023,987,0,998,1004,999,1008],
[1007,1010,986,1002,0,969,988,1014],
[1032,1055,1011,996,1031,0,1026,1012],
[989,1014,992,1001,1012,974,0,1023],
[985,1015,989,992,986,988,977,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 118, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1174,899,922,977,1004,1161,1140],
[826,0,1035,706,1003,1025,1014,889],
[1101,965,0,901,1088,1001,1083,1066],
[1078,1294,1099,0,1131,976,1079,1186],
[1023,997,912,869,0,1018,1148,1190],
[996,975,999,1024,982,0,1082,998],
[839,986,917,921,852,918,0,931],
[860,1111,934,814,810,1002,1069,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 119, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1033,957,940,965,963,952,973],
[967,0,973,906,944,903,980,910],
[1043,1027,0,972,1008,999,997,951],
[1060,1094,1028,0,1031,1044,1051,992],
[1035,1056,992,969,0,1002,1013,1018],
[1037,1097,1001,956,998,0,977,970],
[1048,1020,1003,949,987,1023,0,998],
[1027,1090,1049,1008,982,1030,1002,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 120, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1042,974,1042,871,991,984,898],
[958,0,902,902,969,960,905,918],
[1026,1098,0,1054,929,911,965,914],
[958,1098,946,0,881,880,907,880],
[1129,1031,1071,1119,0,1032,972,1005],
[1009,1040,1089,1120,968,0,956,964],
[1016,1095,1035,1093,1028,1044,0,972],
[1102,1082,1086,1120,995,1036,1028,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 121, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1034,1015,983,1005,997,1001,994],
[966,0,1005,971,991,1018,1044,1031],
[985,995,0,957,975,1012,994,994],
[1017,1029,1043,0,1000,1004,1047,1025],
[995,1009,1025,1000,0,1020,1067,1051],
[1003,982,988,996,980,0,1060,1056],
[999,956,1006,953,933,940,0,1020],
[1006,969,1006,975,949,944,980,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 122, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1070,1031,982,1040,1018,976,1051],
[930,0,984,991,942,944,941,974],
[969,1016,0,992,986,1036,988,1049],
[1018,1009,1008,0,953,1008,1007,1036],
[960,1058,1014,1047,0,1023,975,1006],
[982,1056,964,992,977,0,979,1007],
[1024,1059,1012,993,1025,1021,0,1025],
[949,1026,951,964,994,993,975,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 123, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,979,961,1007,1023,1004,1040,1044],
[1021,0,975,1110,961,986,995,1041],
[1039,1025,0,1071,997,1011,1099,1083],
[993,890,929,0,915,985,1030,980],
[977,1039,1003,1085,0,1058,1054,1058],
[996,1014,989,1015,942,0,972,1029],
[960,1005,901,970,946,1028,0,965],
[956,959,917,1020,942,971,1035,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 124, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1001,951,974,986,977,991,1020],
[999,0,936,989,960,989,985,1005],
[1049,1064,0,973,974,1053,1045,1049],
[1026,1011,1027,0,1038,1012,944,1087],
[1014,1040,1026,962,0,988,1009,1031],
[1023,1011,947,988,1012,0,981,1057],
[1009,1015,955,1056,991,1019,0,1043],
[980,995,951,913,969,943,957,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 125, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1006,1032,1017,1023,995,1041,998],
[994,0,964,1008,1005,1016,1033,942],
[968,1036,0,1007,1013,973,1038,966],
[983,992,993,0,1001,971,1045,1009],
[977,995,987,999,0,995,1063,1011],
[1005,984,1027,1029,1005,0,1047,1031],
[959,967,962,955,937,953,0,943],
[1002,1058,1034,991,989,969,1057,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 126, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1005,1014,956,1039,1001,972,973],
[995,0,998,932,987,976,925,948],
[986,1002,0,980,1027,960,905,996],
[1044,1068,1020,0,1048,1000,943,1045],
[961,1013,973,952,0,934,873,951],
[999,1024,1040,1000,1066,0,1026,1008],
[1028,1075,1095,1057,1127,974,0,1030],
[1027,1052,1004,955,1049,992,970,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 127, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1007,982,1025,1000,994,1047,1021],
[993,0,973,975,983,991,1007,986],
[1018,1027,0,995,988,1030,1028,1014],
[975,1025,1005,0,1001,1010,1021,1012],
[1000,1017,1012,999,0,1009,1036,1029],
[1006,1009,970,990,991,0,1009,1011],
[953,993,972,979,964,991,0,1015],
[979,1014,986,988,971,989,985,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 128, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1013,1059,997,1040,1040,1031,1020],
[987,0,1018,973,977,995,1022,1017],
[941,982,0,969,985,994,998,970],
[1003,1027,1031,0,1062,1024,1058,999],
[960,1023,1015,938,0,997,1000,977],
[960,1005,1006,976,1003,0,1041,1002],
[969,978,1002,942,1000,959,0,983],
[980,983,1030,1001,1023,998,1017,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 129, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,959,953,1040,903,955,916,832],
[1041,0,942,1016,860,968,890,829],
[1047,1058,0,1039,981,1014,993,871],
[960,984,961,0,811,957,949,839],
[1097,1140,1019,1189,0,1102,917,957],
[1045,1032,986,1043,898,0,882,851],
[1084,1110,1007,1051,1083,1118,0,1000],
[1168,1171,1129,1161,1043,1149,1000,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 130, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1008,986,1048,1039,1033,1038,1044],
[992,0,1008,1032,1013,1062,1048,1048],
[1014,992,0,1020,1006,1052,1021,1047],
[952,968,980,0,978,1012,992,1018],
[961,987,994,1022,0,1005,972,1002],
[967,938,948,988,995,0,975,969],
[962,952,979,1008,1028,1025,0,1049],
[956,952,953,982,998,1031,951,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 131, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1070,1024,986,970,980,1024,1006],
[930,0,956,966,938,945,962,930],
[976,1044,0,1016,978,1032,1045,1037],
[1014,1034,984,0,999,990,998,1018],
[1030,1062,1022,1001,0,966,1044,1013],
[1020,1055,968,1010,1034,0,1022,1042],
[976,1038,955,1002,956,978,0,1009],
[994,1070,963,982,987,958,991,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 132, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1011,1006,1004,1057,983,1019,990],
[989,0,1065,954,1029,953,1011,955],
[994,935,0,957,984,928,947,925],
[996,1046,1043,0,1045,1009,988,1000],
[943,971,1016,955,0,879,964,936],
[1017,1047,1072,991,1121,0,1056,1013],
[981,989,1053,1012,1036,944,0,957],
[1010,1045,1075,1000,1064,987,1043,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 133, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,952,986,959,1008,978,997,988],
[1048,0,999,1025,1021,976,1046,1009],
[1014,1001,0,951,1001,1021,967,1013],
[1041,975,1049,0,1074,1018,1023,988],
[992,979,999,926,0,998,968,984],
[1022,1024,979,982,1002,0,1057,1057],
[1003,954,1033,977,1032,943,0,996],
[1012,991,987,1012,1016,943,1004,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 134, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1011,994,1018,1004,1030,1002,1008],
[989,0,1001,1030,997,996,998,1005],
[1006,999,0,1036,1004,1023,1010,1018],
[982,970,964,0,981,975,965,992],
[996,1003,996,1019,0,1007,1018,1009],
[970,1004,977,1025,993,0,993,990],
[998,1002,990,1035,982,1007,0,1018],
[992,995,982,1008,991,1010,982,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 135, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1084,1074,998,1043,988,1054,987],
[916,0,1001,861,973,942,979,927],
[926,999,0,953,938,933,955,963],
[1002,1139,1047,0,1037,978,1057,1019],
[957,1027,1062,963,0,1023,972,1007],
[1012,1058,1067,1022,977,0,1053,1018],
[946,1021,1045,943,1028,947,0,995],
[1013,1073,1037,981,993,982,1005,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 136, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1035,1179,995,1572,960,1329,1115],
[965,0,1382,774,970,1161,1398,1230],
[821,618,0,1058,1173,1364,1305,1086],
[1005,1226,942,0,1185,942,942,1225],
[428,1030,827,815,0,695,1398,1000],
[1040,839,636,1058,1305,0,1450,786],
[671,602,695,1058,602,550,0,642],
[885,770,914,775,1000,1214,1358,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 137, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1005,1014,989,987,1011,1037,1021],
[995,0,1002,1009,1052,963,1039,1004],
[986,998,0,946,963,993,992,1020],
[1011,991,1054,0,984,1014,1036,1027],
[1013,948,1037,1016,0,1001,1021,1064],
[989,1037,1007,986,999,0,969,1007],
[963,961,1008,964,979,1031,0,1015],
[979,996,980,973,936,993,985,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 138, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1010,1064,972,1013,988,1011,1035],
[990,0,992,943,962,996,992,886],
[936,1008,0,946,898,944,966,883],
[1028,1057,1054,0,997,1033,1009,996],
[987,1038,1102,1003,0,1105,1037,1030],
[1012,1004,1056,967,895,0,960,990],
[989,1008,1034,991,963,1040,0,967],
[965,1114,1117,1004,970,1010,1033,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 139, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1007,948,1019,1020,1000,996,1025],
[993,0,983,990,1012,979,1017,1027],
[1052,1017,0,991,1041,1028,1038,1055],
[981,1010,1009,0,1012,981,978,1008],
[980,988,959,988,0,962,974,991],
[1000,1021,972,1019,1038,0,1022,1026],
[1004,983,962,1022,1026,978,0,1028],
[975,973,945,992,1009,974,972,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 140, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,989,1019,988,974,981,987,1023],
[1011,0,1018,986,982,993,970,1024],
[981,982,0,1011,1003,991,983,1003],
[1012,1014,989,0,990,1005,1005,1000],
[1026,1018,997,1010,0,999,975,1018],
[1019,1007,1009,995,1001,0,987,1006],
[1013,1030,1017,995,1025,1013,0,1031],
[977,976,997,1000,982,994,969,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 141, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1010,1022,1000,992,1053,1019,1016],
[990,0,1006,978,980,1035,1017,987],
[978,994,0,1044,1000,1040,1027,1009],
[1000,1022,956,0,1033,1027,1018,1016],
[1008,1020,1000,967,0,1031,1007,1017],
[947,965,960,973,969,0,978,961],
[981,983,973,982,993,1022,0,988],
[984,1013,991,984,983,1039,1012,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 142, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1000,1138,1018,1072,1087,1090,973],
[1000,0,950,854,982,971,1032,854],
[862,1050,0,920,1000,976,1055,868],
[982,1146,1080,0,1168,1093,1085,992],
[928,1018,1000,832,0,899,978,887],
[913,1029,1024,907,1101,0,1081,1010],
[910,968,945,915,1022,919,0,901],
[1027,1146,1132,1008,1113,990,1099,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 143, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1000,1044,1004,1030,995,1007,1001],
[1000,0,998,995,977,989,1013,969],
[956,1002,0,998,997,971,972,991],
[996,1005,1002,0,1031,1002,992,996],
[970,1023,1003,969,0,1017,958,981],
[1005,1011,1029,998,983,0,996,1010],
[993,987,1028,1008,1042,1004,0,977],
[999,1031,1009,1004,1019,990,1023,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 144, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,997,974,970,970,975,1014,984],
[1003,0,1022,1002,1017,998,1003,1021],
[1026,978,0,1022,971,1046,1031,972],
[1030,998,978,0,963,988,1023,966],
[1030,983,1029,1037,0,1019,1031,1003],
[1025,1002,954,1012,981,0,1043,943],
[986,997,969,977,969,957,0,948],
[1016,979,1028,1034,997,1057,1052,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 145, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1009,985,983,1005,1022,948,1040],
[991,0,944,926,1026,1006,945,1024],
[1015,1056,0,994,1090,1014,1019,990],
[1017,1074,1006,0,1044,996,983,1019],
[995,974,910,956,0,919,932,983],
[978,994,986,1004,1081,0,1009,1034],
[1052,1055,981,1017,1068,991,0,1013],
[960,976,1010,981,1017,966,987,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 146, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1028,966,1024,974,1009,966,1009],
[972,0,999,1006,1004,997,1000,966],
[1034,1001,0,1025,1044,1019,1010,968],
[976,994,975,0,981,987,973,965],
[1026,996,956,1019,0,1002,1001,1000],
[991,1003,981,1013,998,0,1009,1008],
[1034,1000,990,1027,999,991,0,1011],
[991,1034,1032,1035,1000,992,989,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 147, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,928,998,1088,951,979,1001,1009],
[1072,0,1000,1049,1004,1064,1006,1049],
[1002,1000,0,1036,979,1043,1009,1004],
[912,951,964,0,888,922,997,951],
[1049,996,1021,1112,0,1012,1034,1032],
[1021,936,957,1078,988,0,1012,971],
[999,994,991,1003,966,988,0,961],
[991,951,996,1049,968,1029,1039,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 148, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1017,1022,1001,991,983,1031,1023],
[983,0,1008,978,1032,1003,1001,978],
[978,992,0,953,992,991,994,977],
[999,1022,1047,0,1028,995,1011,1013],
[1009,968,1008,972,0,994,1015,996],
[1017,997,1009,1005,1006,0,1049,984],
[969,999,1006,989,985,951,0,955],
[977,1022,1023,987,1004,1016,1045,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 149, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1002,995,947,1012,1022,946,941],
[998,0,1042,997,1035,1036,987,978],
[1005,958,0,1006,1028,1019,945,974],
[1053,1003,994,0,1037,1063,1000,984],
[988,965,972,963,0,1050,962,942],
[978,964,981,937,950,0,914,949],
[1054,1013,1055,1000,1038,1086,0,1008],
[1059,1022,1026,1016,1058,1051,992,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 150, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,994,1021,1026,1016,986,992,1033],
[1006,0,1011,997,989,950,996,974],
[979,989,0,1001,1012,985,1007,980],
[974,1003,999,0,949,982,1021,982],
[984,1011,988,1051,0,942,1011,1021],
[1014,1050,1015,1018,1058,0,1017,978],
[1008,1004,993,979,989,983,0,1030],
[967,1026,1020,1018,979,1022,970,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 151, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1020,1018,1024,1032,1000,1031,1015],
[980,0,977,962,994,966,927,972],
[982,1023,0,979,1018,1002,969,1013],
[976,1038,1021,0,1015,984,972,978],
[968,1006,982,985,0,1014,972,1005],
[1000,1034,998,1016,986,0,989,1000],
[969,1073,1031,1028,1028,1011,0,1046],
[985,1028,987,1022,995,1000,954,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 152, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1067,993,1014,1055,986,1088,1089],
[933,0,967,906,943,1105,903,896],
[1007,1033,0,967,1045,1119,1087,909],
[986,1094,1033,0,1155,1063,1112,1017],
[945,1057,955,845,0,1012,1117,971],
[1014,895,881,937,988,0,992,873],
[912,1097,913,888,883,1008,0,918],
[911,1104,1091,983,1029,1127,1082,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 153, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1004,997,1016,1038,1009,997,1012],
[996,0,1036,1000,1002,998,1009,1029],
[1003,964,0,960,1009,1018,1001,960],
[984,1000,1040,0,992,1018,996,1012],
[962,998,991,1008,0,1017,978,959],
[991,1002,982,982,983,0,969,1008],
[1003,991,999,1004,1022,1031,0,988],
[988,971,1040,988,1041,992,1012,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 154, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1020,1024,1000,1020,1050,1023,996],
[980,0,1043,1003,998,1012,1032,985],
[976,957,0,970,956,994,1041,955],
[1000,997,1030,0,1025,1071,1037,1031],
[980,1002,1044,975,0,1034,1006,1010],
[950,988,1006,929,966,0,983,984],
[977,968,959,963,994,1017,0,965],
[1004,1015,1045,969,990,1016,1035,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 155, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,981,1026,984,1016,1000,1015,1002],
[1019,0,1005,999,1030,986,1003,1029],
[974,995,0,986,1006,954,983,993],
[1016,1001,1014,0,1015,980,996,1040],
[984,970,994,985,0,972,1023,1006],
[1000,1014,1046,1020,1028,0,1041,1029],
[985,997,1017,1004,977,959,0,960],
[998,971,1007,960,994,971,1040,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 156, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1005,1008,1044,1003,1017,1005,992],
[995,0,1022,1003,978,1006,993,990],
[992,978,0,978,997,1016,977,983],
[956,997,1022,0,1012,992,983,963],
[997,1022,1003,988,0,1017,957,988],
[983,994,984,1008,983,0,1000,965],
[995,1007,1023,1017,1043,1000,0,1009],
[1008,1010,1017,1037,1012,1035,991,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 157, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,965,1061,994,948,1021,948,984],
[1035,0,1001,1005,961,1019,966,963],
[939,999,0,1000,936,983,979,981],
[1006,995,1000,0,943,997,1010,1004],
[1052,1039,1064,1057,0,1076,1073,997],
[979,981,1017,1003,924,0,969,991],
[1052,1034,1021,990,927,1031,0,1026],
[1016,1037,1019,996,1003,1009,974,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 158, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1011,1029,996,1035,1048,1003,1048],
[989,0,1013,1022,999,1037,985,1031],
[971,987,0,1005,1016,1022,984,999],
[1004,978,995,0,979,1027,1002,1006],
[965,1001,984,1021,0,1028,982,1003],
[952,963,978,973,972,0,956,948],
[997,1015,1016,998,1018,1044,0,1008],
[952,969,1001,994,997,1052,992,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 159, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,992,971,991,969,943,981,993],
[1008,0,1016,994,1006,987,960,983],
[1029,984,0,981,1030,1059,1022,954],
[1009,1006,1019,0,1025,987,1052,998],
[1031,994,970,975,0,1039,997,1002],
[1057,1013,941,1013,961,0,1024,999],
[1019,1040,978,948,1003,976,0,989],
[1007,1017,1046,1002,998,1001,1011,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 160, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1018,997,987,1002,983,973,1019],
[982,0,1027,1009,1037,968,1007,1003],
[1003,973,0,997,984,971,978,1015],
[1013,991,1003,0,1004,967,990,1019],
[998,963,1016,996,0,951,965,975],
[1017,1032,1029,1033,1049,0,950,1036],
[1027,993,1022,1010,1035,1050,0,1015],
[981,997,985,981,1025,964,985,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 161, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,974,975,1049,997,1001,988,991],
[1026,0,952,1042,939,941,925,940],
[1025,1048,0,1084,1016,981,995,971],
[951,958,916,0,950,906,867,895],
[1003,1061,984,1050,0,1020,933,1059],
[999,1059,1019,1094,980,0,1009,1035],
[1012,1075,1005,1133,1067,991,0,1015],
[1009,1060,1029,1105,941,965,985,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 162, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1052,1043,1075,1000,1039,969,1039],
[948,0,1016,1036,979,1043,982,987],
[957,984,0,1001,960,1027,941,988],
[925,964,999,0,992,1006,988,1012],
[1000,1021,1040,1008,0,1043,1019,1033],
[961,957,973,994,957,0,926,1025],
[1031,1018,1059,1012,981,1074,0,1049],
[961,1013,1012,988,967,975,951,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 163, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,992,991,993,1004,1015,984,985],
[1008,0,993,999,1025,1035,1056,1047],
[1009,1007,0,999,1010,1010,1015,1010],
[1007,1001,1001,0,1020,989,1000,1019],
[996,975,990,980,0,1005,1010,1000],
[985,965,990,1011,995,0,980,1003],
[1016,944,985,1000,990,1020,0,1007],
[1015,953,990,981,1000,997,993,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 164, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,933,949,955,993,1088,955,1005],
[1067,0,1040,1098,1004,1061,994,1067],
[1051,960,0,1053,1044,1062,955,899],
[1045,902,947,0,979,1034,996,870],
[1007,996,956,1021,0,1087,1012,996],
[912,939,938,966,913,0,926,851],
[1045,1006,1045,1004,988,1074,0,931],
[995,933,1101,1130,1004,1149,1069,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 165, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1000,998,991,976,951,976,944],
[1000,0,976,976,1001,990,1004,973],
[1002,1024,0,989,1034,971,974,984],
[1009,1024,1011,0,1031,965,993,1006],
[1024,999,966,969,0,928,967,932],
[1049,1010,1029,1035,1072,0,1020,988],
[1024,996,1026,1007,1033,980,0,981],
[1056,1027,1016,994,1068,1012,1019,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 166, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1046,981,1000,1001,1001,1030,1019],
[954,0,1000,1013,990,983,1009,1013],
[1019,1000,0,1020,1019,1002,1011,1004],
[1000,987,980,0,1005,1008,1016,1005],
[999,1010,981,995,0,1005,991,991],
[999,1017,998,992,995,0,1012,986],
[970,991,989,984,1009,988,0,978],
[981,987,996,995,1009,1014,1022,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 167, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1004,1008,1034,958,1004,1064,1023],
[996,0,1011,1017,934,958,934,918],
[992,989,0,1058,1038,1035,976,956],
[966,983,942,0,966,986,998,994],
[1042,1066,962,1034,0,994,1045,1050],
[996,1042,965,1014,1006,0,950,982],
[936,1066,1024,1002,955,1050,0,999],
[977,1082,1044,1006,950,1018,1001,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 168, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,992,1008,1032,1023,1024,1037,1036],
[1008,0,976,1015,1030,965,990,1009],
[992,1024,0,1004,1008,990,1037,1005],
[968,985,996,0,1033,981,1044,1000],
[977,970,992,967,0,963,970,989],
[976,1035,1010,1019,1037,0,1035,1046],
[963,1010,963,956,1030,965,0,992],
[964,991,995,1000,1011,954,1008,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 169, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,983,1001,983,1015,1016,1013,1019],
[1017,0,988,1004,1021,992,1033,1012],
[999,1012,0,994,999,1024,1017,979],
[1017,996,1006,0,1032,1010,1045,1007],
[985,979,1001,968,0,995,962,968],
[984,1008,976,990,1005,0,973,978],
[987,967,983,955,1038,1027,0,1016],
[981,988,1021,993,1032,1022,984,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 170, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,976,988,969,1003,984,1007,929],
[1024,0,975,983,957,984,996,959],
[1012,1025,0,986,1012,1012,1008,964],
[1031,1017,1014,0,1009,984,1026,987],
[997,1043,988,991,0,987,1008,982],
[1016,1016,988,1016,1013,0,1042,1007],
[993,1004,992,974,992,958,0,958],
[1071,1041,1036,1013,1018,993,1042,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 171, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,983,971,1040,1030,1052,1005,999],
[1017,0,1006,1095,1002,1014,985,1016],
[1029,994,0,1048,1003,1003,987,1023],
[960,905,952,0,952,1016,980,967],
[970,998,997,1048,0,1037,994,1042],
[948,986,997,984,963,0,1010,1015],
[995,1015,1013,1020,1006,990,0,990],
[1001,984,977,1033,958,985,1010,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 172, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,906,917,908,960,920,948,859],
[1094,0,1071,1136,1149,1038,981,1054],
[1083,929,0,1027,1033,1017,968,974],
[1092,864,973,0,997,958,914,903],
[1040,851,967,1003,0,975,921,909],
[1080,962,983,1042,1025,0,1027,961],
[1052,1019,1032,1086,1079,973,0,1009],
[1141,946,1026,1097,1091,1039,991,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 173, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,977,992,1000,1010,969,1006,1004],
[1023,0,982,969,977,958,993,953],
[1008,1018,0,1019,998,984,1009,994],
[1000,1031,981,0,1029,979,1026,1018],
[990,1023,1002,971,0,935,956,947],
[1031,1042,1016,1021,1065,0,1038,968],
[994,1007,991,974,1044,962,0,979],
[996,1047,1006,982,1053,1032,1021,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 174, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,953,930,852,931,942,952,779],
[1047,0,951,791,1028,926,965,904],
[1070,1049,0,999,1009,989,1025,1018],
[1148,1209,1001,0,1061,1108,1104,993],
[1069,972,991,939,0,1042,948,893],
[1058,1074,1011,892,958,0,1029,877],
[1048,1035,975,896,1052,971,0,898],
[1221,1096,982,1007,1107,1123,1102,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 175, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,962,943,942,943,965,977,960],
[1038,0,1002,986,1009,1037,1008,998],
[1057,998,0,1034,1001,1037,1011,999],
[1058,1014,966,0,994,1043,1015,1003],
[1057,991,999,1006,0,1019,1052,1005],
[1035,963,963,957,981,0,1011,957],
[1023,992,989,985,948,989,0,974],
[1040,1002,1001,997,995,1043,1026,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 176, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1014,1006,1001,1040,1015,984,994],
[986,0,1015,1013,993,1001,980,975],
[994,985,0,1002,1021,961,962,1006],
[999,987,998,0,1004,973,996,974],
[960,1007,979,996,0,954,974,977],
[985,999,1039,1027,1046,0,1002,976],
[1016,1020,1038,1004,1026,998,0,995],
[1006,1025,994,1026,1023,1024,1005,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 177, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,982,968,941,949,961,937,938],
[1018,0,983,993,982,1004,967,987],
[1032,1017,0,1017,1010,1012,981,1012],
[1059,1007,983,0,1012,998,972,997],
[1051,1018,990,988,0,991,979,994],
[1039,996,988,1002,1009,0,998,996],
[1063,1033,1019,1028,1021,1002,0,994],
[1062,1013,988,1003,1006,1004,1006,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 178, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,980,988,966,1020,989,1002,968],
[1020,0,1007,1006,1004,989,1011,989],
[1012,993,0,988,1020,1002,990,985],
[1034,994,1012,0,1020,982,1003,994],
[980,996,980,980,0,973,1002,976],
[1011,1011,998,1018,1027,0,1012,1000],
[998,989,1010,997,998,988,0,995],
[1032,1011,1015,1006,1024,1000,1005,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 179, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1027,983,980,1002,1127,1070,1114],
[973,0,1010,1092,1023,1086,1103,1048],
[1017,990,0,1040,1017,1120,1090,1017],
[1020,908,960,0,951,954,1107,991],
[998,977,983,1049,0,1012,1025,1006],
[873,914,880,1046,988,0,949,1023],
[930,897,910,893,975,1051,0,1038],
[886,952,983,1009,994,977,962,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 180, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1051,1005,1013,1041,1019,921,1004],
[949,0,993,951,951,952,950,977],
[995,1007,0,962,992,1002,969,1023],
[987,1049,1038,0,1024,1026,1016,992],
[959,1049,1008,976,0,1011,978,977],
[981,1048,998,974,989,0,919,987],
[1079,1050,1031,984,1022,1081,0,1065],
[996,1023,977,1008,1023,1013,935,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 181, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1009,1012,1025,1002,1013,1001,983],
[991,0,1014,1007,1008,982,993,1007],
[988,986,0,964,967,988,949,957],
[975,993,1036,0,990,988,994,968],
[998,992,1033,1010,0,999,977,982],
[987,1018,1012,1012,1001,0,983,983],
[999,1007,1051,1006,1023,1017,0,1002],
[1017,993,1043,1032,1018,1017,998,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 182, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1068,1078,1169,1073,1239,925,955],
[932,0,351,800,1271,681,821,745],
[922,1649,0,1123,1446,1206,1150,1192],
[831,1200,877,0,993,843,776,1118],
[927,729,554,1007,0,870,899,800],
[761,1319,794,1157,1130,0,810,1080],
[1075,1179,850,1224,1101,1190,0,1319],
[1045,1255,808,882,1200,920,681,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 183, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,986,1009,1043,1023,1027,1004,1022],
[1014,0,977,1033,1021,968,990,979],
[991,1023,0,1059,1030,1012,1039,1024],
[957,967,941,0,969,978,995,992],
[977,979,970,1031,0,974,988,1010],
[973,1032,988,1022,1026,0,1030,988],
[996,1010,961,1005,1012,970,0,994],
[978,1021,976,1008,990,1012,1006,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 184, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,977,989,979,1020,993,986,999],
[1023,0,1021,1017,1006,1016,993,994],
[1011,979,0,984,1021,993,1013,987],
[1021,983,1016,0,1046,1022,1002,1015],
[980,994,979,954,0,982,952,984],
[1007,984,1007,978,1018,0,974,985],
[1014,1007,987,998,1048,1026,0,1023],
[1001,1006,1013,985,1016,1015,977,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 185, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1040,993,1018,1050,1000,942,1047],
[960,0,992,922,972,992,910,1055],
[1007,1008,0,990,1031,965,927,1084],
[982,1078,1010,0,1041,999,964,1072],
[950,1028,969,959,0,910,975,1016],
[1000,1008,1035,1001,1090,0,1011,1075],
[1058,1090,1073,1036,1025,989,0,1086],
[953,945,916,928,984,925,914,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 186, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,949,948,982,1020,1007,981,984],
[1051,0,1001,989,1026,1017,1016,1019],
[1052,999,0,1012,1068,1059,1024,1004],
[1018,1011,988,0,1041,1012,1032,987],
[980,974,932,959,0,987,972,962],
[993,983,941,988,1013,0,988,970],
[1019,984,976,968,1028,1012,0,987],
[1016,981,996,1013,1038,1030,1013,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 187, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,986,979,1054,982,986,982,1009],
[1014,0,994,1009,1002,987,956,1025],
[1021,1006,0,1027,982,995,951,1001],
[946,991,973,0,962,979,968,1003],
[1018,998,1018,1038,0,1035,1009,1019],
[1014,1013,1005,1021,965,0,984,973],
[1018,1044,1049,1032,991,1016,0,1040],
[991,975,999,997,981,1027,960,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 188, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1022,984,983,1007,1024,1037,1046],
[978,0,1005,992,981,978,1010,984],
[1016,995,0,1013,1024,1007,1045,1025],
[1017,1008,987,0,1014,995,991,1013],
[993,1019,976,986,0,984,1031,1001],
[976,1022,993,1005,1016,0,1019,1011],
[963,990,955,1009,969,981,0,1018],
[954,1016,975,987,999,989,982,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 189, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1005,1024,1004,1041,1016,1030,1000],
[995,0,1019,1016,1022,1026,1053,1007],
[976,981,0,1007,1007,1002,1037,998],
[996,984,993,0,1009,1010,1008,1018],
[959,978,993,991,0,980,983,975],
[984,974,998,990,1020,0,1023,1012],
[970,947,963,992,1017,977,0,996],
[1000,993,1002,982,1025,988,1004,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 190, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,960,1046,991,975,1008,1014,977],
[1040,0,1012,974,1004,997,1032,1018],
[954,988,0,941,993,987,979,1002],
[1009,1026,1059,0,1039,1042,991,1017],
[1025,996,1007,961,0,1000,998,956],
[992,1003,1013,958,1000,0,988,962],
[986,968,1021,1009,1002,1012,0,1015],
[1023,982,998,983,1044,1038,985,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 191, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,976,986,974,1003,994,1027,983],
[1024,0,1004,993,1028,1013,1025,1011],
[1014,996,0,1002,1040,1026,1043,1002],
[1026,1007,998,0,1009,1011,1032,1015],
[997,972,960,991,0,994,1026,980],
[1006,987,974,989,1006,0,998,981],
[973,975,957,968,974,1002,0,957],
[1017,989,998,985,1020,1019,1043,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 192, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1028,1037,1001,1043,1048,1069,1000],
[972,0,1027,988,991,1023,996,995],
[963,973,0,1000,987,999,1028,989],
[999,1012,1000,0,1033,1008,1027,946],
[957,1009,1013,967,0,997,997,988],
[952,977,1001,992,1003,0,1008,1000],
[931,1004,972,973,1003,992,0,978],
[1000,1005,1011,1054,1012,1000,1022,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 193, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,946,955,1045,984,1008,1008,980],
[1054,0,981,1087,1016,1071,1059,1058],
[1045,1019,0,1067,997,1064,1026,1030],
[955,913,933,0,927,937,937,970],
[1016,984,1003,1073,0,1061,1049,1063],
[992,929,936,1063,939,0,988,1017],
[992,941,974,1063,951,1012,0,979],
[1020,942,970,1030,937,983,1021,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 194, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,985,972,1027,1059,1001,989,1014],
[1015,0,998,1003,1019,973,1000,1003],
[1028,1002,0,1001,1039,1008,1000,1017],
[973,997,999,0,959,1011,984,1023],
[941,981,961,1041,0,944,916,1027],
[999,1027,992,989,1056,0,1021,1057],
[1011,1000,1000,1016,1084,979,0,1020],
[986,997,983,977,973,943,980,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 195, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1048,1043,1040,1000,1024,974,992],
[952,0,1006,963,989,986,983,1009],
[957,994,0,1018,994,1019,1000,959],
[960,1037,982,0,964,1020,981,1000],
[1000,1011,1006,1036,0,1008,1016,1009],
[976,1014,981,980,992,0,972,967],
[1026,1017,1000,1019,984,1028,0,999],
[1008,991,1041,1000,991,1033,1001,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 196, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,965,1038,961,985,1010,989,949],
[1035,0,1159,1100,1167,1178,1102,993],
[962,841,0,851,1005,868,900,775],
[1039,900,1149,0,995,1071,1052,957],
[1015,833,995,1005,0,1037,1087,957],
[990,822,1132,929,963,0,944,982],
[1011,898,1100,948,913,1056,0,1012],
[1051,1007,1225,1043,1043,1018,988,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 197, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,977,1004,980,1059,1048,1047,994],
[1023,0,973,1012,1012,994,1021,1009],
[996,1027,0,1008,1086,980,1059,998],
[1020,988,992,0,1051,965,1007,1007],
[941,988,914,949,0,914,978,979],
[952,1006,1020,1035,1086,0,1056,1011],
[953,979,941,993,1022,944,0,992],
[1006,991,1002,993,1021,989,1008,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 198, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1030,988,1023,988,1013,1040,1011],
[970,0,1009,1005,1009,1009,990,975],
[1012,991,0,980,1004,963,970,969],
[977,995,1020,0,990,949,986,1028],
[1012,991,996,1010,0,983,971,972],
[987,991,1037,1051,1017,0,993,985],
[960,1010,1030,1014,1029,1007,0,1009],
[989,1025,1031,972,1028,1015,991,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 199, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1010,975,1013,956,959,1001,994],
[990,0,968,1020,996,970,986,947],
[1025,1032,0,1047,995,1000,1029,1036],
[987,980,953,0,951,966,974,968],
[1044,1004,1005,1049,0,999,1037,1034],
[1041,1030,1000,1034,1001,0,1045,1002],
[999,1014,971,1026,963,955,0,994],
[1006,1053,964,1032,966,998,1006,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2000, 200, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/mebb/mebb_8_2000.csv", index=False, header=False)