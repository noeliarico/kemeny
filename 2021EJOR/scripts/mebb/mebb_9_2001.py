
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg

rep = 3
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,1096,1049,1065,1073,1057,1113,1044,974],
[905,0,943,981,950,923,948,1021,905],
[952,1058,0,1050,988,961,1004,1063,934],
[936,1020,951,0,933,1027,967,1020,984],
[928,1051,1013,1068,0,1008,1017,1019,959],
[944,1078,1040,974,993,0,995,1032,998],
[888,1053,997,1034,984,1006,0,989,1010],
[957,980,938,981,982,969,1012,0,912],
[1027,1096,1067,1017,1042,1003,991,1089,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 1, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1104,1181,1197,1045,947,1109,860,1150],
[897,0,1032,1014,884,855,895,1012,920],
[820,969,0,915,920,875,960,735,1036],
[804,987,1086,0,1042,991,1062,1000,1003],
[956,1117,1081,959,0,1002,1068,984,1133],
[1054,1146,1126,1010,999,0,1054,1005,1113],
[892,1106,1041,939,933,947,0,967,1141],
[1141,989,1266,1001,1017,996,1034,0,1109],
[851,1081,965,998,868,888,860,892,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 2, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,984,1123,1059,1058,1038,1074,1034,1018],
[1017,0,1102,1093,1033,977,1071,1077,1054],
[878,899,0,956,857,857,1039,1051,990],
[942,908,1045,0,955,975,1039,996,1040],
[943,968,1144,1046,0,1062,1072,1110,1104],
[963,1024,1144,1026,939,0,1073,980,1097],
[927,930,962,962,929,928,0,983,947],
[967,924,950,1005,891,1021,1018,0,1037],
[983,947,1011,961,897,904,1054,964,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 3, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1041,982,1028,1026,1051,1060,1017,1043],
[960,0,959,982,993,1014,990,1017,965],
[1019,1042,0,1033,994,1057,1024,1054,1073],
[973,1019,968,0,999,988,989,1044,1006],
[975,1008,1007,1002,0,972,971,994,1027],
[950,987,944,1013,1029,0,1010,1015,1015],
[941,1011,977,1012,1030,991,0,1020,999],
[984,984,947,957,1007,986,981,0,999],
[958,1036,928,995,974,986,1002,1002,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 4, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1019,1042,1004,1049,1039,1028,997,1010],
[982,0,941,967,983,1053,967,985,960],
[959,1060,0,976,974,1001,1004,968,948],
[997,1034,1025,0,1024,1055,1010,1061,990],
[952,1018,1027,977,0,1025,974,979,1014],
[962,948,1000,946,976,0,957,1004,964],
[973,1034,997,991,1027,1044,0,976,986],
[1004,1016,1033,940,1022,997,1025,0,1027],
[991,1041,1053,1011,987,1037,1015,974,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 5, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1030,1002,994,1025,1025,994,1054,1011],
[971,0,973,978,975,968,969,971,1002],
[999,1028,0,989,996,973,970,1005,970],
[1007,1023,1012,0,1053,1017,977,1031,1006],
[976,1026,1005,948,0,995,978,963,984],
[976,1033,1028,984,1006,0,983,1013,973],
[1007,1032,1031,1024,1023,1018,0,1013,987],
[947,1030,996,970,1038,988,988,0,992],
[990,999,1031,995,1017,1028,1014,1009,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 6, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1013,987,1023,1091,1028,1033,1075,1014],
[988,0,1013,1026,1001,948,1002,1023,988],
[1014,988,0,1058,1057,1020,986,1059,952],
[978,975,943,0,993,956,962,1001,982],
[910,1000,944,1008,0,945,994,1020,964],
[973,1053,981,1045,1056,0,1020,1055,994],
[968,999,1015,1039,1007,981,0,1042,969],
[926,978,942,1000,981,946,959,0,963],
[987,1013,1049,1019,1037,1007,1032,1038,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 7, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1006,990,1019,1071,1002,986,1086,937],
[995,0,1016,998,973,974,1007,1058,972],
[1011,985,0,1030,1039,1024,1045,1117,1019],
[982,1003,971,0,984,995,965,1103,973],
[930,1028,962,1017,0,1000,985,1050,960],
[999,1027,977,1006,1001,0,1027,1045,934],
[1015,994,956,1036,1016,974,0,1061,966],
[915,943,884,898,951,956,940,0,867],
[1064,1029,982,1028,1041,1067,1035,1134,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 8, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,982,1026,994,1005,1022,1029,1052,1044],
[1019,0,1023,984,1035,1033,1025,1001,1026],
[975,978,0,1015,994,1011,1026,1020,1005],
[1007,1017,986,0,997,1035,1030,1006,1029],
[996,966,1007,1004,0,997,1002,983,978],
[979,968,990,966,1004,0,1015,1010,1015],
[972,976,975,971,999,986,0,954,997],
[949,1000,981,995,1018,991,1047,0,1025],
[957,975,996,972,1023,986,1004,976,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 9, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1042,962,916,935,972,992,940,966],
[959,0,940,884,916,977,888,905,917],
[1039,1061,0,950,977,1019,934,959,965],
[1085,1117,1051,0,986,1062,1012,959,1004],
[1066,1085,1024,1015,0,1048,1020,979,1009],
[1029,1024,982,939,953,0,972,953,940],
[1009,1113,1067,989,981,1029,0,968,1018],
[1061,1096,1042,1042,1022,1048,1033,0,1000],
[1035,1084,1036,997,992,1061,983,1001,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 10, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1074,1010,1021,956,1095,1042,985,1073],
[927,0,988,997,896,961,1016,993,969],
[991,1013,0,1023,958,958,979,894,996],
[980,1004,978,0,898,897,1022,916,1062],
[1045,1105,1043,1103,0,1040,1094,983,1007],
[906,1040,1043,1104,961,0,1046,1025,1076],
[959,985,1022,979,907,955,0,993,1054],
[1016,1008,1107,1085,1018,976,1008,0,1041],
[928,1032,1005,939,994,925,947,960,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 11, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1001,990,1002,972,999,1005,1032,992],
[1000,0,1007,985,1001,996,975,982,999],
[1011,994,0,966,963,1004,971,977,970],
[999,1016,1035,0,1015,1000,976,1037,988],
[1029,1000,1038,986,0,989,983,1011,1028],
[1002,1005,997,1001,1012,0,954,980,1008],
[996,1026,1030,1025,1018,1047,0,1006,1007],
[969,1019,1024,964,990,1021,995,0,952],
[1009,1002,1031,1013,973,993,994,1049,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 12, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1002,1016,951,983,966,1014,980,1024],
[999,0,1010,969,1035,993,968,964,1000],
[985,991,0,1018,976,988,933,964,1015],
[1050,1032,983,0,1045,1049,1027,1028,1010],
[1018,966,1025,956,0,1044,1012,1012,1006],
[1035,1008,1013,952,957,0,990,938,965],
[987,1033,1068,974,989,1011,0,991,1046],
[1021,1037,1037,973,989,1063,1010,0,1019],
[977,1001,986,991,995,1036,955,982,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 13, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,991,1003,1039,1017,1001,1001,1002,989],
[1010,0,995,1011,1027,944,987,1001,981],
[998,1006,0,998,996,989,983,993,984],
[962,990,1003,0,1009,961,1004,1013,1003],
[984,974,1005,992,0,935,978,1018,972],
[1000,1057,1012,1040,1066,0,1027,1040,1031],
[1000,1014,1018,997,1023,974,0,979,1020],
[999,1000,1008,988,983,961,1022,0,993],
[1012,1020,1017,998,1029,970,981,1008,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 14, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1026,1050,1035,978,1017,1009,1001,971],
[975,0,1089,1046,957,1085,1004,1047,1022],
[951,912,0,934,945,946,975,968,939],
[966,955,1067,0,1005,1016,1026,1016,999],
[1023,1044,1056,996,0,1032,1078,1028,1015],
[984,916,1055,985,969,0,985,998,983],
[992,997,1026,975,923,1016,0,980,944],
[1000,954,1033,985,973,1003,1021,0,1025],
[1030,979,1062,1002,986,1018,1057,976,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 15, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1048,974,1016,974,960,966,974,1030],
[953,0,989,989,951,990,923,963,956],
[1027,1012,0,1030,990,946,1008,985,1027],
[985,1012,971,0,967,1015,951,978,954],
[1027,1050,1011,1034,0,993,948,997,1009],
[1041,1011,1055,986,1008,0,962,989,999],
[1035,1078,993,1050,1053,1039,0,1033,1015],
[1027,1038,1016,1023,1004,1012,968,0,1015],
[971,1045,974,1047,992,1002,986,986,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 16, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1007,1019,1007,927,990,995,954,949],
[994,0,1023,1017,987,985,986,1002,1000],
[982,978,0,1011,979,981,997,976,974],
[994,984,990,0,983,971,973,976,973],
[1074,1014,1022,1018,0,1000,1010,998,953],
[1011,1016,1020,1030,1001,0,1012,993,973],
[1006,1015,1004,1028,991,989,0,987,988],
[1047,999,1025,1025,1003,1008,1014,0,1024],
[1052,1001,1027,1028,1048,1028,1013,977,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 17, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,998,1003,1040,1033,1062,959,1050,1030],
[1003,0,993,1009,1026,1082,1048,1012,960],
[998,1008,0,1140,1013,1093,975,992,1021],
[961,992,861,0,1013,1006,902,969,928],
[968,975,988,988,0,1019,1020,1008,1023],
[939,919,908,995,982,0,993,969,1007],
[1042,953,1026,1099,981,1008,0,1002,1008],
[951,989,1009,1032,993,1032,999,0,996],
[971,1041,980,1073,978,994,993,1005,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 18, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1009,1010,1006,966,976,984,981,963],
[992,0,1021,1022,1016,973,1008,952,981],
[991,980,0,997,1001,977,1005,989,975],
[995,979,1004,0,993,993,1000,971,980],
[1035,985,1000,1008,0,959,1000,978,946],
[1025,1028,1024,1008,1042,0,1033,978,1022],
[1017,993,996,1001,1001,968,0,968,981],
[1020,1049,1012,1030,1023,1023,1033,0,998],
[1038,1020,1026,1021,1055,979,1020,1003,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 19, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,980,1001,1024,1035,990,1030,1033,1024],
[1021,0,987,1045,1042,1016,1038,1053,994],
[1000,1014,0,1018,1022,1041,1019,1045,1001],
[977,956,983,0,1016,991,981,1027,976],
[966,959,979,985,0,951,957,984,974],
[1011,985,960,1010,1050,0,1020,1037,1003],
[971,963,982,1020,1044,981,0,1004,975],
[968,948,956,974,1017,964,997,0,963],
[977,1007,1000,1025,1027,998,1026,1038,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 20, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,966,1001,955,965,983,1011,967,977],
[1035,0,1029,1023,999,1020,1021,1022,1026],
[1000,972,0,994,991,977,1004,993,1017],
[1046,978,1007,0,998,979,1012,1027,1008],
[1036,1002,1010,1003,0,1012,1019,1045,992],
[1018,981,1024,1022,989,0,1050,1013,999],
[990,980,997,989,982,951,0,1007,984],
[1034,979,1008,974,956,988,994,0,995],
[1024,975,984,993,1009,1002,1017,1006,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 21, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,929,1011,1040,989,1012,936,1016,1059],
[1072,0,1055,974,1024,1006,1041,1018,1020],
[990,946,0,1004,1038,1017,1049,1054,1025],
[961,1027,997,0,1039,1050,1050,1064,1017],
[1012,977,963,962,0,935,1017,1055,1002],
[989,995,984,951,1066,0,976,982,1069],
[1065,960,952,951,984,1025,0,1080,1025],
[985,983,947,937,946,1019,921,0,958],
[942,981,976,984,999,932,976,1043,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 22, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,971,1021,1048,1010,970,979,961,994],
[1030,0,1042,1033,1041,988,1037,995,1054],
[980,959,0,1026,1021,995,926,938,926],
[953,968,975,0,1087,990,1004,936,981],
[991,960,980,914,0,957,936,907,930],
[1031,1013,1006,1011,1044,0,1047,1010,973],
[1022,964,1075,997,1065,954,0,952,1004],
[1040,1006,1063,1065,1094,991,1049,0,1054],
[1007,947,1075,1020,1071,1028,997,947,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 23, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1035,1027,1005,999,1037,1048,1028,1052],
[966,0,999,968,995,999,1005,981,1016],
[974,1002,0,975,964,997,991,989,980],
[996,1033,1026,0,1016,1032,1030,1012,1023],
[1002,1006,1037,985,0,1007,968,1003,1028],
[964,1002,1004,969,994,0,990,989,981],
[953,996,1010,971,1033,1011,0,988,998],
[973,1020,1012,989,998,1012,1013,0,1009],
[949,985,1021,978,973,1020,1003,992,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 24, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,959,1001,968,950,998,980,960,998],
[1042,0,1054,1025,1018,1048,997,981,1014],
[1000,947,0,993,947,1024,972,985,965],
[1033,976,1008,0,970,1051,979,958,1006],
[1051,983,1054,1031,0,1049,1021,987,1016],
[1003,953,977,950,952,0,937,940,981],
[1021,1004,1029,1022,980,1064,0,1004,996],
[1041,1020,1016,1043,1014,1061,997,0,1023],
[1003,987,1036,995,985,1020,1005,978,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 25, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,823,1090,690,655,913,1270,1155,581],
[1178,0,1009,999,1167,1227,1370,1231,921],
[911,992,0,1011,846,1168,1157,1189,1028],
[1311,1002,990,0,950,1173,1087,1323,966],
[1346,834,1155,1051,0,1198,1331,1221,969],
[1088,774,833,828,803,0,714,1164,871],
[731,631,844,914,670,1287,0,1066,723],
[846,770,812,678,780,837,935,0,728],
[1420,1080,973,1035,1032,1130,1278,1273,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 26, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,975,954,985,969,987,946,1062,1019],
[1026,0,918,1018,979,1017,930,1069,1005],
[1047,1083,0,1074,1007,1075,990,1095,1060],
[1016,983,927,0,993,1010,973,1019,1011],
[1032,1022,994,1008,0,1011,1021,1054,1064],
[1014,984,926,991,990,0,994,1065,969],
[1055,1071,1011,1028,980,1007,0,1045,1028],
[939,932,906,982,947,936,956,0,1046],
[982,996,941,990,937,1032,973,955,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 27, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,989,938,984,956,1008,993,1030,1017],
[1012,0,983,1000,971,966,1015,1073,1036],
[1063,1018,0,1019,971,1043,1072,1074,1048],
[1017,1001,982,0,1010,1041,1015,1045,1007],
[1045,1030,1030,991,0,1042,1008,1039,1078],
[993,1035,958,960,959,0,995,1032,991],
[1008,986,929,986,993,1006,0,1029,1006],
[971,928,927,956,962,969,972,0,1004],
[984,965,953,994,923,1010,995,997,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 28, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1117,997,1111,1451,1206,1179,1011,1242],
[884,0,996,1049,1158,1105,1243,819,1121],
[1004,1005,0,1163,1295,1197,1156,918,1107],
[890,952,838,0,1216,1070,820,947,1105],
[550,843,706,785,0,807,885,710,803],
[795,896,804,931,1194,0,941,849,1055],
[822,758,845,1181,1116,1060,0,725,895],
[990,1182,1083,1054,1291,1152,1276,0,1146],
[759,880,894,896,1198,946,1106,855,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 29, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,996,1004,1026,996,993,997,1023,994],
[1005,0,1015,1003,1002,994,1010,1014,994],
[997,986,0,1025,968,1009,1018,1019,1033],
[975,998,976,0,989,988,982,1010,1005],
[1005,999,1033,1012,0,1010,1033,1002,1003],
[1008,1007,992,1013,991,0,1025,1010,1016],
[1004,991,983,1019,968,976,0,1008,989],
[978,987,982,991,999,991,993,0,1001],
[1007,1007,968,996,998,985,1012,1000,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 30, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1001,1050,998,1005,984,1044,1032,1047],
[1000,0,1031,999,1002,1006,1041,1030,1052],
[951,970,0,977,1002,1014,1005,1015,995],
[1003,1002,1024,0,1045,990,1034,1047,1014],
[996,999,999,956,0,967,991,1041,1013],
[1017,995,987,1011,1034,0,1018,1029,1050],
[957,960,996,967,1010,983,0,995,998],
[969,971,986,954,960,972,1006,0,984],
[954,949,1006,987,988,951,1003,1017,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 31, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1004,1006,1012,994,980,1065,979,1002],
[997,0,1011,990,981,945,985,967,952],
[995,990,0,968,971,968,959,971,981],
[989,1011,1033,0,971,975,1006,989,1006],
[1007,1020,1030,1030,0,1024,1019,1062,973],
[1021,1056,1033,1026,977,0,1030,1032,1016],
[936,1016,1042,995,982,971,0,1058,1016],
[1022,1034,1030,1012,939,969,943,0,954],
[999,1049,1020,995,1028,985,985,1047,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 32, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,972,1015,988,961,1009,1005,1003,993],
[1029,0,1029,996,988,1004,974,984,965],
[986,972,0,960,1004,985,991,943,980],
[1013,1005,1041,0,979,1028,1001,1032,988],
[1040,1013,997,1022,0,1017,1013,999,1027],
[992,997,1016,973,984,0,1030,993,976],
[996,1027,1010,1000,988,971,0,977,979],
[998,1017,1058,969,1002,1008,1024,0,994],
[1008,1036,1021,1013,974,1025,1022,1007,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 33, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,942,1030,1007,965,952,962,1010,974],
[1059,0,1091,997,976,1066,1017,1077,982],
[971,910,0,967,923,954,939,964,921],
[994,1004,1034,0,1004,1026,977,985,966],
[1036,1025,1078,997,0,1046,990,1035,997],
[1049,935,1047,975,955,0,936,957,979],
[1039,984,1062,1024,1011,1065,0,1057,970],
[991,924,1037,1016,966,1044,944,0,1017],
[1027,1019,1080,1035,1004,1022,1031,984,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 34, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1013,1037,993,1039,1008,1025,996,1014],
[988,0,1002,1007,1011,1029,966,988,976],
[964,999,0,969,1013,1010,977,976,994],
[1008,994,1032,0,1045,1018,999,987,998],
[962,990,988,956,0,968,976,976,995],
[993,972,991,983,1033,0,978,985,1000],
[976,1035,1024,1002,1025,1023,0,1010,1015],
[1005,1013,1025,1014,1025,1016,991,0,1033],
[987,1025,1007,1003,1006,1001,986,968,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 35, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1077,996,1029,1151,1043,929,1057,1047],
[924,0,1093,937,826,998,914,998,841],
[1005,908,0,911,947,913,927,1048,952],
[972,1064,1090,0,1056,1106,1026,1072,1021],
[850,1175,1054,945,0,1040,1011,1024,863],
[958,1003,1088,895,961,0,874,1018,1077],
[1072,1087,1074,975,990,1127,0,1005,982],
[944,1003,953,929,977,983,996,0,995],
[954,1160,1049,980,1138,924,1019,1006,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 36, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,977,995,1082,967,973,1009,1031,1046],
[1024,0,991,1087,1022,989,1011,1002,1048],
[1006,1010,0,1043,990,1020,1015,978,1036],
[919,914,958,0,926,935,1007,949,1014],
[1034,979,1011,1075,0,961,1038,1022,1030],
[1028,1012,981,1066,1040,0,1051,1008,1090],
[992,990,986,994,963,950,0,967,1009],
[970,999,1023,1052,979,993,1034,0,1042],
[955,953,965,987,971,911,992,959,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 37, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,928,960,939,1014,1039,1036,949,937],
[1073,0,983,1084,1090,1031,1105,1089,1023],
[1041,1018,0,981,984,1084,973,1005,984],
[1062,917,1020,0,1098,1032,990,1065,961],
[987,911,1017,903,0,952,888,914,886],
[962,970,917,969,1049,0,941,1004,966],
[965,896,1028,1011,1113,1060,0,1057,1041],
[1052,912,996,936,1087,997,944,0,937],
[1064,978,1017,1040,1115,1035,960,1064,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 38, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1030,988,1062,1077,1086,1016,1007,1042],
[971,0,1034,1071,1011,1027,1019,994,1028],
[1013,967,0,1024,1013,1003,1036,938,960],
[939,930,977,0,965,1019,934,915,960],
[924,990,988,1036,0,993,963,963,986],
[915,974,998,982,1008,0,953,969,993],
[985,982,965,1067,1038,1048,0,1024,1046],
[994,1007,1063,1086,1038,1032,977,0,1046],
[959,973,1041,1041,1015,1008,955,955,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 39, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,937,985,963,934,977,993,947,932],
[1064,0,1027,947,982,986,1009,985,965],
[1016,974,0,1012,1012,967,1036,1012,994],
[1038,1054,989,0,1059,1068,1078,1024,1060],
[1067,1019,989,942,0,1011,1004,975,1045],
[1024,1015,1034,933,990,0,1042,978,972],
[1008,992,965,923,997,959,0,957,967],
[1054,1016,989,977,1026,1023,1044,0,975],
[1069,1036,1007,941,956,1029,1034,1026,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 40, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1008,1029,984,1051,989,1019,988,951],
[993,0,1015,960,1034,980,953,1010,1002],
[972,986,0,931,984,978,970,989,934],
[1017,1041,1070,0,981,1019,986,944,973],
[950,967,1017,1020,0,1028,1003,994,896],
[1012,1021,1023,982,973,0,972,969,936],
[982,1048,1031,1015,998,1029,0,1013,935],
[1013,991,1012,1057,1007,1032,988,0,960],
[1050,999,1067,1028,1105,1065,1066,1041,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 41, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1025,1190,983,965,1080,1022,1007,970],
[976,0,994,1022,1027,996,995,979,859],
[811,1007,0,952,1001,990,929,1002,878],
[1018,979,1049,0,908,994,991,971,929],
[1036,974,1000,1093,0,1023,1032,1044,953],
[921,1005,1011,1007,978,0,966,1020,957],
[979,1006,1072,1010,969,1035,0,1036,1092],
[994,1022,999,1030,957,981,965,0,1125],
[1031,1142,1123,1072,1048,1044,909,876,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 42, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,993,1037,973,1015,1009,987,1016,1006],
[1008,0,1017,1005,990,995,1024,987,995],
[964,984,0,995,1010,956,997,971,981],
[1028,996,1006,0,988,1004,1024,1022,1026],
[986,1011,991,1013,0,992,1024,1026,1032],
[992,1006,1045,997,1009,0,1028,1025,1026],
[1014,977,1004,977,977,973,0,1000,999],
[985,1014,1030,979,975,976,1001,0,1006],
[995,1006,1020,975,969,975,1002,995,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 43, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1001,966,1004,1037,1029,984,976,994],
[1000,0,1004,1003,1039,1027,1008,1042,997],
[1035,997,0,980,1013,1011,981,1077,1023],
[997,998,1021,0,1109,1028,1014,1013,1011],
[964,962,988,892,0,986,921,1014,961],
[972,974,990,973,1015,0,978,1061,927],
[1017,993,1020,987,1080,1023,0,1023,1033],
[1025,959,924,988,987,940,978,0,932],
[1007,1004,978,990,1040,1074,968,1069,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 44, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,949,970,988,931,1013,1039,951,954],
[1052,0,1031,995,983,1037,1073,1014,957],
[1031,970,0,1030,1031,1076,1067,999,1004],
[1013,1006,971,0,971,1080,1027,932,944],
[1070,1018,970,1030,0,1075,1051,997,998],
[988,964,925,921,926,0,981,903,941],
[962,928,934,974,950,1020,0,955,947],
[1050,987,1002,1069,1004,1098,1046,0,1003],
[1047,1044,997,1057,1003,1060,1054,998,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 45, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1033,951,1060,960,988,1025,997,1019],
[968,0,977,1019,921,993,983,948,996],
[1050,1024,0,1041,1037,1004,1085,990,1031],
[941,982,960,0,954,939,932,940,989],
[1041,1080,964,1047,0,979,977,985,1003],
[1013,1008,997,1062,1022,0,1020,1007,1042],
[976,1018,916,1069,1024,981,0,1007,1030],
[1004,1053,1011,1061,1016,994,994,0,973],
[982,1005,970,1012,998,959,971,1028,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 46, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,988,1032,1053,1028,993,991,1039,998],
[1013,0,1039,1060,1044,1011,1021,1044,999],
[969,962,0,1035,1012,970,987,991,971],
[948,941,966,0,990,966,971,962,968],
[973,957,989,1011,0,958,994,995,943],
[1008,990,1031,1035,1043,0,1009,1035,1011],
[1010,980,1014,1030,1007,992,0,1009,967],
[962,957,1010,1039,1006,966,992,0,957],
[1003,1002,1030,1033,1058,990,1034,1044,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 47, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,955,979,968,969,977,992,1008,971],
[1046,0,958,997,998,1003,977,1029,996],
[1022,1043,0,994,1039,1009,1013,1029,1006],
[1033,1004,1007,0,1043,1006,991,1030,1010],
[1032,1003,962,958,0,979,979,977,988],
[1024,998,992,995,1022,0,997,1007,1029],
[1009,1024,988,1010,1022,1004,0,1044,1010],
[993,972,972,971,1024,994,957,0,965],
[1030,1005,995,991,1013,972,991,1036,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 48, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,993,1021,1007,1026,1000,1001,1015,1024],
[1008,0,986,972,972,984,969,1009,984],
[980,1015,0,992,983,996,982,1012,1014],
[994,1029,1009,0,1040,1015,987,1001,1036],
[975,1029,1018,961,0,992,997,1017,998],
[1001,1017,1005,986,1009,0,991,1031,1037],
[1000,1032,1019,1014,1004,1010,0,998,1022],
[986,992,989,1000,984,970,1003,0,997],
[977,1017,987,965,1003,964,979,1004,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 49, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1011,977,974,1016,949,979,955,1021],
[990,0,945,979,1010,996,977,1012,1025],
[1024,1056,0,1042,1048,1010,970,1015,1064],
[1027,1022,959,0,1026,986,959,1006,991],
[985,991,953,975,0,942,967,986,1004],
[1052,1005,991,1015,1059,0,1015,1042,1047],
[1022,1024,1031,1042,1034,986,0,1002,967],
[1046,989,986,995,1015,959,999,0,982],
[980,976,937,1010,997,954,1034,1019,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 50, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1018,1021,1033,1009,1036,1024,965,1000],
[983,0,1004,989,996,1054,952,947,1012],
[980,997,0,1011,989,1012,990,1009,999],
[968,1012,990,0,1003,1032,958,940,973],
[992,1005,1012,998,0,1026,987,981,967],
[965,947,989,969,975,0,988,948,985],
[977,1049,1011,1043,1014,1013,0,987,1045],
[1036,1054,992,1061,1020,1053,1014,0,1034],
[1001,989,1002,1028,1034,1016,956,967,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 51, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,974,936,1012,1021,1068,953,1045,1040],
[1027,0,1010,1028,1022,1081,990,928,1082],
[1065,991,0,1050,985,1063,1012,1004,1013],
[989,973,951,0,984,1075,961,979,1023],
[980,979,1016,1017,0,1078,1007,999,1054],
[933,920,938,926,923,0,941,926,971],
[1048,1011,989,1040,994,1060,0,1001,1012],
[956,1073,997,1022,1002,1075,1000,0,1041],
[961,919,988,978,947,1030,989,960,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 52, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,959,977,997,987,1031,987,981,1003],
[1042,0,995,1024,1015,1057,1037,1038,1064],
[1024,1006,0,1024,1006,1055,975,1029,1024],
[1004,977,977,0,966,1046,1010,1061,1027],
[1014,986,995,1035,0,1025,1013,1014,1069],
[970,944,946,955,976,0,968,995,975],
[1014,964,1026,991,988,1033,0,1027,1039],
[1020,963,972,940,987,1006,974,0,1017],
[998,937,977,974,932,1026,962,984,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 53, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1017,1067,1003,992,1065,1025,1078,1037],
[984,0,989,1004,1026,1041,1004,1012,1005],
[934,1012,0,943,917,1024,1001,985,1004],
[998,997,1058,0,985,1094,1042,1042,1037],
[1009,975,1084,1016,0,1050,1020,1031,1037],
[936,960,977,907,951,0,942,936,966],
[976,997,1000,959,981,1059,0,1000,1040],
[923,989,1016,959,970,1065,1001,0,959],
[964,996,997,964,964,1035,961,1042,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 54, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,988,1017,1016,1033,1015,1055,1046,1010],
[1013,0,1035,973,1037,1027,994,966,967],
[984,966,0,1007,997,1018,1013,1000,1000],
[985,1028,994,0,1018,1028,1012,1011,1035],
[968,964,1004,983,0,1021,996,995,991],
[986,974,983,973,980,0,967,988,976],
[946,1007,988,989,1005,1034,0,1038,981],
[955,1035,1001,990,1006,1013,963,0,1023],
[991,1034,1001,966,1010,1025,1020,978,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 55, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,986,1043,1094,1027,1020,981,1036,1011],
[1015,0,1052,1118,1024,1054,996,1007,1016],
[958,949,0,1051,988,963,891,941,934],
[907,883,950,0,936,921,926,925,895],
[974,977,1013,1065,0,1036,1044,1023,1017],
[981,947,1038,1080,965,0,975,1013,1008],
[1020,1005,1110,1075,957,1026,0,981,938],
[965,994,1060,1076,978,988,1020,0,997],
[990,985,1067,1106,984,993,1063,1004,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 56, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,969,1065,1035,981,1002,1053,1043,969],
[1032,0,1025,964,1004,997,998,1079,993],
[936,976,0,994,982,970,1031,1055,992],
[966,1037,1007,0,932,934,967,1036,960],
[1020,997,1019,1069,0,932,1004,1013,1014],
[999,1004,1031,1067,1069,0,1104,1090,1045],
[948,1003,970,1034,997,897,0,1007,978],
[958,922,946,965,988,911,994,0,992],
[1032,1008,1009,1041,987,956,1023,1009,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 57, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1085,990,976,1075,1056,1024,1022,958],
[916,0,945,892,981,972,1023,954,839],
[1011,1056,0,970,1024,953,1014,961,894],
[1025,1109,1031,0,1105,1043,1083,1084,896],
[926,1020,977,896,0,990,907,975,901],
[945,1029,1048,958,1011,0,947,937,921],
[977,978,987,918,1094,1054,0,971,1034],
[979,1047,1040,917,1026,1064,1030,0,939],
[1043,1162,1107,1105,1100,1080,967,1062,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 58, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,990,954,979,976,957,982,993,977],
[1011,0,1001,970,1006,1017,980,1003,967],
[1047,1000,0,989,997,978,992,977,986],
[1022,1031,1012,0,973,1012,1034,981,1016],
[1025,995,1004,1028,0,1033,979,1003,993],
[1044,984,1023,989,968,0,1006,1000,1009],
[1019,1021,1009,967,1022,995,0,1030,1010],
[1008,998,1024,1020,998,1001,971,0,1005],
[1024,1034,1015,985,1008,992,991,996,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 59, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1003,1004,1026,1005,999,1037,1013,1025],
[998,0,1010,1019,994,993,1024,1010,994],
[997,991,0,969,1017,981,1009,1015,992],
[975,982,1032,0,992,998,998,979,983],
[996,1007,984,1009,0,987,1036,990,979],
[1002,1008,1020,1003,1014,0,986,994,1009],
[964,977,992,1003,965,1015,0,1008,994],
[988,991,986,1022,1011,1007,993,0,996],
[976,1007,1009,1018,1022,992,1007,1005,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 60, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1024,1011,982,999,1010,1002,988,1010],
[977,0,988,967,1002,973,1003,949,994],
[990,1013,0,994,1010,1021,1009,1005,1000],
[1019,1034,1007,0,1026,991,1002,1008,1003],
[1002,999,991,975,0,970,1002,971,1006],
[991,1028,980,1010,1031,0,1011,991,1008],
[999,998,992,999,999,990,0,978,959],
[1013,1052,996,993,1030,1010,1023,0,1018],
[991,1007,1001,998,995,993,1042,983,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 61, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,987,1053,1032,991,1011,1012,1042,1011],
[1014,0,1058,1033,990,981,1014,1017,1008],
[948,943,0,953,954,951,995,958,981],
[969,968,1048,0,985,970,1026,1005,1001],
[1010,1011,1047,1016,0,978,1074,1021,1016],
[990,1020,1050,1031,1023,0,1041,1018,1031],
[989,987,1006,975,927,960,0,989,963],
[959,984,1043,996,980,983,1012,0,970],
[990,993,1020,1000,985,970,1038,1031,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 62, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1060,1033,995,1023,1006,995,1012,1003],
[941,0,988,1006,1016,1022,980,973,1065],
[968,1013,0,998,988,997,963,1030,989],
[1006,995,1003,0,1011,1013,1005,973,1008],
[978,985,1013,990,0,1017,974,976,992],
[995,979,1004,988,984,0,940,968,1001],
[1006,1021,1038,996,1027,1061,0,1006,1006],
[989,1028,971,1028,1025,1033,995,0,1002],
[998,936,1012,993,1009,1000,995,999,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 63, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,981,1102,994,1089,1107,1015,1135,1056],
[1020,0,997,975,1066,1052,1023,1041,953],
[899,1004,0,966,988,1073,990,1062,959],
[1007,1026,1035,0,998,1003,949,1075,947],
[912,935,1013,1003,0,1044,962,1055,930],
[894,949,928,998,957,0,897,1016,938],
[986,978,1011,1052,1039,1104,0,1105,1015],
[866,960,939,926,946,985,896,0,965],
[945,1048,1042,1054,1071,1063,986,1036,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 64, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,949,1026,968,984,990,988,998,965],
[1052,0,988,1014,981,995,1009,974,988],
[975,1013,0,1001,1044,993,1035,967,900],
[1033,987,1000,0,1006,1013,959,993,960],
[1017,1020,957,995,0,1026,980,962,1003],
[1011,1006,1008,988,975,0,1023,984,935],
[1013,992,966,1042,1021,978,0,1029,978],
[1003,1027,1034,1008,1039,1017,972,0,1002],
[1036,1013,1101,1041,998,1066,1023,999,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 65, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,947,934,990,1009,964,980,1020,981],
[1054,0,1029,1027,1025,1029,1020,1036,992],
[1067,972,0,1051,1024,981,1007,1045,1025],
[1011,974,950,0,991,949,993,1027,965],
[992,976,977,1010,0,960,977,1045,979],
[1037,972,1020,1052,1041,0,999,1066,1024],
[1021,981,994,1008,1024,1002,0,1020,1003],
[981,965,956,974,956,935,981,0,965],
[1020,1009,976,1036,1022,977,998,1036,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 66, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1000,979,989,987,998,960,1005,990],
[1001,0,1024,1011,993,1000,938,1007,974],
[1022,977,0,991,989,1000,959,979,954],
[1012,990,1010,0,1011,1008,974,1032,978],
[1014,1008,1012,990,0,1006,975,1026,987],
[1003,1001,1001,993,995,0,975,992,1016],
[1041,1063,1042,1027,1026,1026,0,1017,965],
[996,994,1022,969,975,1009,984,0,943],
[1011,1027,1047,1023,1014,985,1036,1058,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 67, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1014,994,1107,1005,1021,980,1020,1002],
[987,0,932,1063,1005,1017,982,1033,972],
[1007,1069,0,1062,1021,1092,1002,992,990],
[894,938,939,0,1009,955,964,948,947],
[996,996,980,992,0,1075,972,1054,962],
[980,984,909,1046,926,0,918,973,891],
[1021,1019,999,1037,1029,1083,0,1027,1013],
[981,968,1009,1053,947,1028,974,0,983],
[999,1029,1011,1054,1039,1110,988,1018,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 68, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1004,971,960,1007,984,1019,997,983],
[997,0,946,969,1017,1004,1018,960,968],
[1030,1055,0,1024,1036,1042,1061,998,1002],
[1041,1032,977,0,1021,1026,1036,981,975],
[994,984,965,980,0,993,1033,994,970],
[1017,997,959,975,1008,0,1024,966,968],
[982,983,940,965,968,977,0,971,981],
[1004,1041,1003,1020,1007,1035,1030,0,1000],
[1018,1033,999,1026,1031,1033,1020,1001,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 69, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1007,991,1032,1002,982,1007,1084,1045],
[994,0,1020,993,957,1043,1059,1053,1052],
[1010,981,0,999,1016,1024,964,1081,1022],
[969,1008,1002,0,1069,1018,1062,1082,1028],
[999,1044,985,932,0,960,1015,1089,1027],
[1019,958,977,983,1041,0,977,1052,1055],
[994,942,1037,939,986,1024,0,1011,1033],
[917,948,920,919,912,949,990,0,973],
[956,949,979,973,974,946,968,1028,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 70, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1007,1034,1106,998,1091,995,996,1054],
[994,0,1011,963,971,989,1051,1017,1031],
[967,990,0,1017,971,934,1055,913,969],
[895,1038,984,0,983,962,986,844,940],
[1003,1030,1030,1018,0,976,1008,869,891],
[910,1012,1067,1039,1025,0,975,925,932],
[1006,950,946,1015,993,1026,0,964,970],
[1005,984,1088,1157,1132,1076,1037,0,1095],
[947,970,1032,1061,1110,1069,1031,906,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 71, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1067,1019,1026,1030,1054,1005,939,1061],
[934,0,918,962,1010,1014,952,931,1019],
[982,1083,0,984,1067,1009,1052,1061,1092],
[975,1039,1017,0,1056,1002,1039,1006,1065],
[971,991,934,945,0,992,972,984,1036],
[947,987,992,999,1009,0,1026,995,1045],
[996,1049,949,962,1029,975,0,997,1068],
[1062,1070,940,995,1017,1006,1004,0,1021],
[940,982,909,936,965,956,933,980,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 72, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1055,1040,1047,1021,1040,1046,981,1066],
[946,0,1031,1054,999,1016,1012,1022,1033],
[961,970,0,992,997,993,986,947,1033],
[954,947,1009,0,981,980,1022,947,1012],
[980,1002,1004,1020,0,1020,1007,947,1035],
[961,985,1008,1021,981,0,1004,969,990],
[955,989,1015,979,994,997,0,951,1000],
[1020,979,1054,1054,1054,1032,1050,0,1027],
[935,968,968,989,966,1011,1001,974,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 73, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1006,997,1006,1000,984,1003,1020,1004],
[995,0,988,987,984,968,988,990,975],
[1004,1013,0,1023,979,985,1016,983,985],
[995,1014,978,0,964,958,974,990,994],
[1001,1017,1022,1037,0,970,1041,1002,1028],
[1017,1033,1016,1043,1031,0,1017,987,977],
[998,1013,985,1027,960,984,0,996,982],
[981,1011,1018,1011,999,1014,1005,0,994],
[997,1026,1016,1007,973,1024,1019,1007,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 74, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,993,1050,995,1002,1011,1014,982,1007],
[1008,0,1015,1003,1026,880,1055,1052,1048],
[951,986,0,953,1008,967,1004,1075,1063],
[1006,998,1048,0,1094,944,1019,1086,1076],
[999,975,993,907,0,982,1093,1037,1098],
[990,1121,1034,1057,1019,0,1029,1089,1021],
[987,946,997,982,908,972,0,1057,1022],
[1019,949,926,915,964,912,944,0,985],
[994,953,938,925,903,980,979,1016,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 75, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,958,964,966,934,1010,909,985,969],
[1043,0,992,993,984,1041,941,1003,1058],
[1037,1009,0,995,990,1011,954,977,1060],
[1035,1008,1006,0,999,1025,953,961,1035],
[1067,1017,1011,1002,0,1063,1016,990,1030],
[991,960,990,976,938,0,914,1002,1010],
[1092,1060,1047,1048,985,1087,0,1031,1076],
[1016,998,1024,1040,1011,999,970,0,1002],
[1032,943,941,966,971,991,925,999,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 76, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1103,1011,971,1021,1074,1174,1172,1071],
[898,0,978,1001,952,972,1095,1067,1020],
[990,1023,0,943,958,948,1070,1058,1069],
[1030,1000,1058,0,884,985,1165,1164,1099],
[980,1049,1043,1117,0,1039,1044,1151,1110],
[927,1029,1053,1016,962,0,1163,1113,1116],
[827,906,931,836,957,838,0,930,903],
[829,934,943,837,850,888,1071,0,869],
[930,981,932,902,891,885,1098,1132,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 77, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1035,1042,1025,1062,989,1030,1033,1007],
[966,0,1035,1003,1020,995,1011,1009,970],
[959,966,0,1005,989,1002,977,982,963],
[976,998,996,0,1007,982,958,995,1005],
[939,981,1012,994,0,983,970,989,976],
[1012,1006,999,1019,1018,0,997,985,996],
[971,990,1024,1043,1031,1004,0,1000,990],
[968,992,1019,1006,1012,1016,1001,0,999],
[994,1031,1038,996,1025,1005,1011,1002,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 78, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,979,998,997,951,955,976,994,1007],
[1022,0,1010,995,990,1004,1037,1028,1017],
[1003,991,0,965,991,988,966,1010,974],
[1004,1006,1036,0,981,993,1011,980,987],
[1050,1011,1010,1020,0,996,1013,1040,1001],
[1046,997,1013,1008,1005,0,1034,1080,1002],
[1025,964,1035,990,988,967,0,1038,979],
[1007,973,991,1021,961,921,963,0,1001],
[994,984,1027,1014,1000,999,1022,1000,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 79, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,996,1017,994,962,978,976,982,966],
[1005,0,1032,990,975,997,961,1041,987],
[984,969,0,984,970,987,1019,1007,986],
[1007,1011,1017,0,1009,977,1011,1034,974],
[1039,1026,1031,992,0,963,1033,993,974],
[1023,1004,1014,1024,1038,0,1037,1021,991],
[1025,1040,982,990,968,964,0,1000,987],
[1019,960,994,967,1008,980,1001,0,1014],
[1035,1014,1015,1027,1027,1010,1014,987,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 80, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,969,1054,1048,1028,1020,1035,1052,1028],
[1032,0,1029,1046,1017,984,1047,1053,1002],
[947,972,0,1010,962,965,997,985,964],
[953,955,991,0,981,967,980,1003,966],
[973,984,1039,1020,0,1028,1001,1010,1034],
[981,1017,1036,1034,973,0,1014,1030,996],
[966,954,1004,1021,1000,987,0,972,987],
[949,948,1016,998,991,971,1029,0,966],
[973,999,1037,1035,967,1005,1014,1035,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 81, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1035,1066,1019,1030,993,1009,992,1020],
[966,0,1022,971,966,942,974,956,956],
[935,979,0,986,981,972,976,952,945],
[982,1030,1015,0,990,966,972,1009,997],
[971,1035,1020,1011,0,979,987,986,994],
[1008,1059,1029,1035,1022,0,1008,1019,995],
[992,1027,1025,1029,1014,993,0,981,975],
[1009,1045,1049,992,1015,982,1020,0,979],
[981,1045,1056,1004,1007,1006,1026,1022,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 82, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1037,930,871,1022,1020,945,932,963],
[964,0,1042,926,1036,1064,1026,993,1007],
[1071,959,0,908,947,997,1034,998,961],
[1130,1075,1093,0,986,1127,1058,1002,1010],
[979,965,1054,1015,0,1056,1086,913,1011],
[981,937,1004,874,945,0,1012,933,910],
[1056,975,967,943,915,989,0,902,942],
[1069,1008,1003,999,1088,1068,1099,0,1024],
[1038,994,1040,991,990,1091,1059,977,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 83, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,926,1077,1099,1095,947,1130,1039,967],
[1075,0,937,1022,1153,1148,1075,1042,1033],
[924,1064,0,853,1062,1031,1083,1104,1012],
[902,979,1148,0,1061,993,1128,1065,1078],
[906,848,939,940,0,866,938,1023,924],
[1054,853,970,1008,1135,0,1084,1108,1099],
[871,926,918,873,1063,917,0,1022,906],
[962,959,897,936,978,893,979,0,907],
[1034,968,989,923,1077,902,1095,1094,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 84, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1081,1010,921,966,943,1015,958,1072],
[920,0,986,945,961,984,961,953,995],
[991,1015,0,925,1015,1042,869,903,1085],
[1080,1056,1076,0,1059,974,991,1110,1111],
[1035,1040,986,942,0,977,921,943,1043],
[1058,1017,959,1027,1024,0,965,977,995],
[986,1040,1132,1010,1080,1036,0,1031,1105],
[1043,1048,1098,891,1058,1024,970,0,1114],
[929,1006,916,890,958,1006,896,887,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 85, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1052,1034,1016,1048,985,965,1004,1033],
[949,0,1069,1048,985,1035,1027,1010,1004],
[967,932,0,958,964,936,950,982,987],
[985,953,1043,0,1040,1003,993,983,999],
[953,1016,1037,961,0,981,926,942,980],
[1016,966,1065,998,1020,0,980,962,1010],
[1036,974,1051,1008,1075,1021,0,1002,1014],
[997,991,1019,1018,1059,1039,999,0,1026],
[968,997,1014,1002,1021,991,987,975,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 86, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,974,957,1013,1011,953,979,1030,996],
[1027,0,958,1022,979,970,1006,1000,942],
[1044,1043,0,1044,996,1017,1040,972,954],
[988,979,957,0,927,941,949,1039,908],
[990,1022,1005,1074,0,977,1020,1002,956],
[1048,1031,984,1060,1024,0,1033,1045,978],
[1022,995,961,1052,981,968,0,1022,1001],
[971,1001,1029,962,999,956,979,0,1024],
[1005,1059,1047,1093,1045,1023,1000,977,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 87, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1050,986,1082,950,1115,1128,966,990],
[951,0,941,990,953,1011,1008,944,931],
[1015,1060,0,985,975,1033,1082,1019,1047],
[919,1011,1016,0,999,989,1100,956,1026],
[1051,1048,1026,1002,0,970,1128,981,961],
[886,990,968,1012,1031,0,994,990,895],
[873,993,919,901,873,1007,0,942,911],
[1035,1057,982,1045,1020,1011,1059,0,1016],
[1011,1070,954,975,1040,1106,1090,985,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 88, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1064,1007,1000,1028,998,980,1020,1007],
[937,0,941,983,1025,981,942,978,990],
[994,1060,0,990,1041,1015,972,1017,1024],
[1001,1018,1011,0,1029,974,1001,1021,996],
[973,976,960,972,0,968,954,1017,935],
[1003,1020,986,1027,1033,0,964,964,1010],
[1021,1059,1029,1000,1047,1037,0,1038,1040],
[981,1023,984,980,984,1037,963,0,993],
[994,1011,977,1005,1066,991,961,1008,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 89, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,973,971,1052,968,868,974,867,952],
[1028,0,940,1069,984,1034,946,916,1066],
[1030,1061,0,1216,982,1179,1082,1112,1013],
[949,932,785,0,844,912,938,828,992],
[1033,1017,1019,1157,0,1064,973,1118,981],
[1133,967,822,1089,937,0,1106,913,988],
[1027,1055,919,1063,1028,895,0,1078,1152],
[1134,1085,889,1173,883,1088,923,0,1102],
[1049,935,988,1009,1020,1013,849,899,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 90, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1057,996,916,921,981,830,1043,1087],
[944,0,948,1046,952,872,795,1019,1132],
[1005,1053,0,1016,1009,1035,906,1123,1133],
[1085,955,985,0,931,1018,849,1049,1081],
[1080,1049,992,1070,0,1052,897,1052,1095],
[1020,1129,966,983,949,0,1014,1029,1140],
[1171,1206,1095,1152,1104,987,0,1228,1295],
[958,982,878,952,949,972,773,0,1098],
[914,869,868,920,906,861,706,903,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 91, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1009,1008,1009,993,988,977,1014,1017],
[992,0,966,969,1008,969,931,997,957],
[993,1035,0,1036,958,992,1006,999,953],
[992,1032,965,0,1008,999,998,1046,1004],
[1008,993,1043,993,0,975,992,1006,976],
[1013,1032,1009,1002,1026,0,1001,1023,987],
[1024,1070,995,1003,1009,1000,0,1029,975],
[987,1004,1002,955,995,978,972,0,964],
[984,1044,1048,997,1025,1014,1026,1037,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 92, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1017,1033,968,1015,965,1020,978,977],
[984,0,1038,971,1004,981,1054,957,997],
[968,963,0,944,997,970,1005,955,943],
[1033,1030,1057,0,1033,1040,1037,985,1014],
[986,997,1004,968,0,961,1009,962,1029],
[1036,1020,1031,961,1040,0,1053,1040,1024],
[981,947,996,964,992,948,0,968,957],
[1023,1044,1046,1016,1039,961,1033,0,1063],
[1024,1004,1058,987,972,977,1044,938,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 93, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1009,1038,966,987,991,962,1013,982],
[992,0,977,994,1001,1057,1016,966,1040],
[963,1024,0,996,995,1043,1005,1037,1011],
[1035,1007,1005,0,1013,1021,1008,986,985],
[1014,1000,1006,988,0,1029,952,969,967],
[1010,944,958,980,972,0,933,982,1008],
[1039,985,996,993,1049,1068,0,1015,1029],
[988,1035,964,1015,1032,1019,986,0,1032],
[1019,961,990,1016,1034,993,972,969,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 94, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1010,999,982,975,1032,1005,979,1018],
[991,0,987,978,943,1009,993,973,1009],
[1002,1014,0,993,964,992,993,983,1004],
[1019,1023,1008,0,966,989,994,967,1009],
[1026,1058,1037,1035,0,1073,1030,991,1061],
[969,992,1009,1012,928,0,984,976,1010],
[996,1008,1008,1007,971,1017,0,1011,1003],
[1022,1028,1018,1034,1010,1025,990,0,1009],
[983,992,997,992,940,991,998,992,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 95, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1025,1027,998,1080,1054,1024,1026,1004],
[976,0,1035,974,1055,1015,987,1042,992],
[974,966,0,1034,1019,981,997,1054,928],
[1003,1027,967,0,1022,999,1012,1059,916],
[921,946,982,979,0,991,953,1017,942],
[947,986,1020,1002,1010,0,1026,1030,991],
[977,1014,1004,989,1048,975,0,1041,991],
[975,959,947,942,984,971,960,0,907],
[997,1009,1073,1085,1059,1010,1010,1094,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 96, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1031,1019,1053,1012,1031,987,1017,1032],
[970,0,1000,1021,1009,1007,980,981,1006],
[982,1001,0,997,1002,1006,982,998,976],
[948,980,1004,0,977,984,974,979,987],
[989,992,999,1024,0,992,977,979,998],
[970,994,995,1017,1009,0,992,984,1018],
[1014,1021,1019,1027,1024,1009,0,997,1015],
[984,1020,1003,1022,1022,1017,1004,0,1015],
[969,995,1025,1014,1003,983,986,986,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 97, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1007,1015,988,1020,992,964,961,969],
[994,0,1028,1015,998,979,990,982,982],
[986,973,0,1001,976,954,998,1028,952],
[1013,986,1000,0,999,934,966,955,982],
[981,1003,1025,1002,0,975,1003,994,976],
[1009,1022,1047,1067,1026,0,1049,1000,1004],
[1037,1011,1003,1035,998,952,0,974,996],
[1040,1019,973,1046,1007,1001,1027,0,980],
[1032,1019,1049,1019,1025,997,1005,1021,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 98, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1026,1053,1037,1009,1013,998,1007,1003],
[975,0,994,989,996,981,976,955,931],
[948,1007,0,966,986,983,984,1017,952],
[964,1012,1035,0,1036,986,992,1028,957],
[992,1005,1015,965,0,985,986,999,958],
[988,1020,1018,1015,1016,0,996,987,965],
[1003,1025,1017,1009,1015,1005,0,1012,972],
[994,1046,984,973,1002,1014,989,0,985],
[998,1070,1049,1044,1043,1036,1029,1016,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 99, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1012,979,979,953,979,975,952,995],
[989,0,974,973,974,979,1021,1002,1016],
[1022,1027,0,994,1013,998,981,988,1003],
[1022,1028,1007,0,1012,1017,997,1018,1022],
[1048,1027,988,989,0,1030,1020,997,1006],
[1022,1022,1003,984,971,0,991,993,969],
[1026,980,1020,1004,981,1010,0,1006,1018],
[1049,999,1013,983,1004,1008,995,0,990],
[1006,985,998,979,995,1032,983,1011,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 100, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,912,877,833,945,867,919,962,1033],
[1089,0,924,1019,993,1036,1068,1085,1084],
[1124,1077,0,993,1103,952,1031,1107,1113],
[1168,982,1008,0,1024,980,1041,1088,1072],
[1056,1008,898,977,0,968,1045,1079,1095],
[1134,965,1049,1021,1033,0,1130,1065,1153],
[1082,933,970,960,956,871,0,1015,967],
[1039,916,894,913,922,936,986,0,1017],
[968,917,888,929,906,848,1034,984,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 101, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1021,1010,1024,1060,1063,1022,1016,996],
[980,0,1005,1047,993,1044,1024,1014,976],
[991,996,0,988,962,1055,1032,1011,967],
[977,954,1013,0,1008,1017,1005,969,1017],
[941,1008,1039,993,0,1027,1010,1019,986],
[938,957,946,984,974,0,1007,934,930],
[979,977,969,996,991,994,0,975,938],
[985,987,990,1032,982,1067,1026,0,977],
[1005,1025,1034,984,1015,1071,1063,1024,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 102, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1006,1030,982,1068,983,953,1038,960],
[995,0,1011,1010,1032,971,1005,998,1047],
[971,990,0,977,997,980,1034,1003,1029],
[1019,991,1024,0,1005,1007,1055,1024,1018],
[933,969,1004,996,0,957,924,999,995],
[1018,1030,1021,994,1044,0,1051,986,1025],
[1048,996,967,946,1077,950,0,952,1091],
[963,1003,998,977,1002,1015,1049,0,1041],
[1041,954,972,983,1006,976,910,960,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 103, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1018,1036,999,1030,1017,1001,1007,1005],
[983,0,1002,1018,1016,988,1002,1009,1012],
[965,999,0,1004,1005,983,976,1001,971],
[1002,983,997,0,987,1005,972,989,982],
[971,985,996,1014,0,992,982,987,971],
[984,1013,1018,996,1009,0,990,997,963],
[1000,999,1025,1029,1019,1011,0,1006,1001],
[994,992,1000,1012,1014,1004,995,0,993],
[996,989,1030,1019,1030,1038,1000,1008,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 104, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1003,999,1035,986,1016,986,1025,1005],
[998,0,1015,1028,1002,1016,999,1015,993],
[1002,986,0,1047,997,1015,989,1035,1021],
[966,973,954,0,971,998,962,963,986],
[1015,999,1004,1030,0,1033,1004,1036,1003],
[985,985,986,1003,968,0,995,1002,1021],
[1015,1002,1012,1039,997,1006,0,1019,1000],
[976,986,966,1038,965,999,982,0,998],
[996,1008,980,1015,998,980,1001,1003,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 105, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1000,1005,1001,984,995,1024,1061,995],
[1001,0,987,976,935,978,996,1013,963],
[996,1014,0,986,994,993,1001,1031,976],
[1000,1025,1015,0,1007,988,1019,1067,997],
[1017,1066,1007,994,0,1005,1015,1063,1008],
[1006,1023,1008,1013,996,0,1028,1049,1030],
[977,1005,1000,982,986,973,0,1041,1030],
[940,988,970,934,938,952,960,0,941],
[1006,1038,1025,1004,993,971,971,1060,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 106, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1026,993,1038,1063,1050,985,995,1019],
[975,0,980,991,1035,986,987,998,1004],
[1008,1021,0,1031,1049,1045,1029,986,1013],
[963,1010,970,0,1039,1017,997,1042,1003],
[938,966,952,962,0,983,989,983,976],
[951,1015,956,984,1018,0,990,1000,1017],
[1016,1014,972,1004,1012,1011,0,1016,1016],
[1006,1003,1015,959,1018,1001,985,0,1021],
[982,997,988,998,1025,984,985,980,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 107, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1027,1022,990,1015,1028,1020,1003,980],
[974,0,993,980,965,993,1003,1020,975],
[979,1008,0,982,995,996,1021,1010,1013],
[1011,1021,1019,0,1021,1002,1044,996,1013],
[986,1036,1006,980,0,1005,1060,1037,1014],
[973,1008,1005,999,996,0,1040,1017,1023],
[981,998,980,957,941,961,0,984,992],
[998,981,991,1005,964,984,1017,0,993],
[1021,1026,988,988,987,978,1009,1008,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 108, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,992,998,929,1017,1028,994,1010,1023],
[1009,0,1020,987,1021,1047,1020,1024,1007],
[1003,981,0,992,1015,1052,1026,1008,1006],
[1072,1014,1009,0,1035,1036,1040,996,1045],
[984,980,986,966,0,1044,1015,992,998],
[973,954,949,965,957,0,988,974,988],
[1007,981,975,961,986,1013,0,975,997],
[991,977,993,1005,1009,1027,1026,0,1003],
[978,994,995,956,1003,1013,1004,998,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 109, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1024,1023,1020,996,1022,959,1035,1019],
[977,0,997,1002,969,998,974,1013,970],
[978,1004,0,1014,975,997,962,1025,992],
[981,999,987,0,982,998,972,1021,1012],
[1005,1032,1026,1019,0,1007,987,1037,1025],
[979,1003,1004,1003,994,0,959,1037,981],
[1042,1027,1039,1029,1014,1042,0,1080,999],
[966,988,976,980,964,964,921,0,993],
[982,1031,1009,989,976,1020,1002,1008,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 110, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,968,1084,999,953,987,978,887,919],
[1033,0,1113,1006,971,984,970,1002,956],
[917,888,0,924,922,869,937,946,910],
[1002,995,1077,0,920,981,904,921,933],
[1048,1030,1079,1081,0,987,996,1029,968],
[1014,1017,1132,1020,1014,0,996,1000,979],
[1023,1031,1064,1097,1005,1005,0,1010,974],
[1114,999,1055,1080,972,1001,991,0,1014],
[1082,1045,1091,1068,1033,1022,1027,987,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 111, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1009,1024,989,1011,986,979,1032,983],
[992,0,965,998,1033,1043,999,1073,956],
[977,1036,0,984,1060,1005,1022,1055,987],
[1012,1003,1017,0,1028,958,1008,1006,1011],
[990,968,941,973,0,951,964,962,972],
[1015,958,996,1043,1050,0,1008,1006,981],
[1022,1002,979,993,1037,993,0,1028,955],
[969,928,946,995,1039,995,973,0,960],
[1018,1045,1014,990,1029,1020,1046,1041,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 112, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,998,1043,1010,995,1006,1039,1028,1010],
[1003,0,1009,987,966,987,1014,1000,991],
[958,992,0,984,953,979,1000,1028,996],
[991,1014,1017,0,972,996,1016,1003,978],
[1006,1035,1048,1029,0,996,1031,1045,1024],
[995,1014,1022,1005,1005,0,1004,1018,993],
[962,987,1001,985,970,997,0,1018,1005],
[973,1001,973,998,956,983,983,0,991],
[991,1010,1005,1023,977,1008,996,1010,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 113, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,963,886,960,962,906,950,1016,1013],
[1038,0,984,947,926,943,929,1073,1015],
[1115,1017,0,1045,961,971,995,1048,1065],
[1041,1054,956,0,1000,1001,1005,1043,1168],
[1039,1075,1040,1001,0,963,971,981,1102],
[1095,1058,1030,1000,1038,0,962,993,1068],
[1051,1072,1006,996,1030,1039,0,1022,1054],
[985,928,953,958,1020,1008,979,0,993],
[988,986,936,833,899,933,947,1008,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 114, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,967,955,949,979,1005,928,981,973],
[1034,0,999,973,1036,1000,973,1033,1003],
[1046,1002,0,991,1001,1047,1018,1015,1007],
[1052,1028,1010,0,1006,1075,978,1059,1036],
[1022,965,1000,995,0,1014,948,1001,984],
[996,1001,954,926,987,0,936,924,1014],
[1073,1028,983,1023,1053,1065,0,1045,1059],
[1020,968,986,942,1000,1077,956,0,997],
[1028,998,994,965,1017,987,942,1004,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 115, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,941,993,899,987,1021,1006,1031,917],
[1060,0,1010,964,927,1031,1005,1016,931],
[1008,991,0,944,915,952,1010,1011,964],
[1102,1037,1057,0,1000,1005,1028,1129,1017],
[1014,1074,1086,1001,0,988,997,1027,1038],
[980,970,1049,996,1013,0,1013,1056,998],
[995,996,991,973,1004,988,0,1062,965],
[970,985,990,872,974,945,939,0,912],
[1084,1070,1037,984,963,1003,1036,1089,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 116, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,934,959,976,987,968,960,941,974],
[1067,0,1029,1044,994,1008,991,993,976],
[1042,972,0,964,996,980,963,993,991],
[1025,957,1037,0,1008,982,1009,995,1008],
[1014,1007,1005,993,0,1006,1007,1013,1010],
[1033,993,1021,1019,995,0,991,995,1001],
[1041,1010,1038,992,994,1010,0,977,1023],
[1060,1008,1008,1006,988,1006,1024,0,1010],
[1027,1025,1010,993,991,1000,978,991,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 117, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,977,1028,1032,1032,1008,982,950,1048],
[1024,0,1044,1088,1049,1094,1035,991,1123],
[973,957,0,1002,945,1031,965,954,992],
[969,913,999,0,991,969,913,921,1031],
[969,952,1056,1010,0,1049,1009,1014,1048],
[993,907,970,1032,952,0,919,911,993],
[1019,966,1036,1088,992,1082,0,1007,1110],
[1051,1010,1047,1080,987,1090,994,0,1062],
[953,878,1009,970,953,1008,891,939,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 118, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,991,944,1001,975,1003,914,959,1005],
[1010,0,969,941,969,981,1008,979,1046],
[1057,1032,0,1030,989,1021,1012,1005,1055],
[1000,1060,971,0,957,1004,970,968,986],
[1026,1032,1012,1044,0,1036,964,993,990],
[998,1020,980,997,965,0,984,958,1005],
[1087,993,989,1031,1037,1017,0,1003,1032],
[1042,1022,996,1033,1008,1043,998,0,1061],
[996,955,946,1015,1011,996,969,940,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 119, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,998,985,1032,906,955,887,1010,951],
[1003,0,859,1054,945,1011,945,1029,932],
[1016,1142,0,1006,981,1065,1053,1079,965],
[969,947,995,0,902,1015,983,959,943],
[1095,1056,1020,1099,0,1033,1037,978,973],
[1046,990,936,986,968,0,896,955,930],
[1114,1056,948,1018,964,1105,0,1050,1020],
[991,972,922,1042,1023,1046,951,0,920],
[1050,1069,1036,1058,1028,1071,981,1081,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 120, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1048,1066,1029,1035,1036,1025,1058,988],
[953,0,990,961,999,982,958,1013,926],
[935,1011,0,968,979,996,991,1019,984],
[972,1040,1033,0,1039,991,1014,1031,1037],
[966,1002,1022,962,0,1019,1014,1026,989],
[965,1019,1005,1010,982,0,963,1010,1015],
[976,1043,1010,987,987,1038,0,1002,1031],
[943,988,982,970,975,991,999,0,981],
[1013,1075,1017,964,1012,986,970,1020,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 121, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1029,1029,1003,1040,1021,1019,982,1054],
[972,0,964,981,1005,973,999,985,1000],
[972,1037,0,990,988,981,995,968,1015],
[998,1020,1011,0,1022,1007,990,1001,1052],
[961,996,1013,979,0,1016,989,981,1018],
[980,1028,1020,994,985,0,1030,971,1028],
[982,1002,1006,1011,1012,971,0,997,1040],
[1019,1016,1033,1000,1020,1030,1004,0,1026],
[947,1001,986,949,983,973,961,975,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 122, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1016,914,1049,940,998,948,1041,979],
[985,0,964,1057,967,1090,991,1032,1022],
[1087,1037,0,1013,1010,1055,994,1036,1071],
[952,944,988,0,943,979,995,1048,998],
[1061,1034,991,1058,0,1060,997,1075,1055],
[1003,911,946,1022,941,0,1037,1008,1072],
[1053,1010,1007,1006,1004,964,0,1020,1035],
[960,969,965,953,926,993,981,0,992],
[1022,979,930,1003,946,929,966,1009,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 123, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,854,965,960,1126,1054,1009,934,962],
[1147,0,959,1072,1137,1009,1017,953,1092],
[1036,1042,0,1052,1104,1036,1078,985,1070],
[1041,929,949,0,1055,957,1003,949,956],
[875,864,897,946,0,957,930,867,918],
[947,992,965,1044,1044,0,1064,926,871],
[992,984,923,998,1071,937,0,914,960],
[1067,1048,1016,1052,1134,1075,1087,0,990],
[1039,909,931,1045,1083,1130,1041,1011,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 124, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1041,1074,1106,1079,1060,1040,1018,974],
[960,0,1084,1065,937,959,1023,957,964],
[927,917,0,1043,958,1005,982,1017,951],
[895,936,958,0,982,941,939,869,948],
[922,1064,1043,1019,0,1073,1061,1012,973],
[941,1042,996,1060,928,0,973,985,904],
[961,978,1019,1062,940,1028,0,996,988],
[983,1044,984,1132,989,1016,1005,0,1020],
[1027,1037,1050,1053,1028,1097,1013,981,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 125, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,945,1096,962,1099,1043,1122,1032,954],
[1056,0,1184,1094,1105,1018,1123,962,964],
[905,817,0,992,891,894,940,870,827],
[1039,907,1009,0,997,982,1042,996,878],
[902,896,1110,1004,0,981,1162,1041,1002],
[958,983,1107,1019,1020,0,1143,984,944],
[879,878,1061,959,839,858,0,790,887],
[969,1039,1131,1005,960,1017,1211,0,970],
[1047,1037,1174,1123,999,1057,1114,1031,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 126, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,986,981,989,1013,977,1041,1011,955],
[1015,0,1001,952,1023,966,1077,1037,1001],
[1020,1000,0,1018,1067,975,1024,1009,988],
[1012,1049,983,0,1046,1027,1059,1023,1048],
[988,978,934,955,0,977,1058,1012,1007],
[1024,1035,1026,974,1024,0,1044,990,1002],
[960,924,977,942,943,957,0,944,972],
[990,964,992,978,989,1011,1057,0,1035],
[1046,1000,1013,953,994,999,1029,966,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 127, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1154,992,957,907,879,971,1161,1038],
[847,0,536,726,553,935,1019,825,781],
[1009,1465,0,1058,697,1016,1221,1116,1113],
[1044,1275,943,0,627,1107,953,1168,814],
[1094,1448,1304,1374,0,775,1172,1151,1102],
[1122,1066,985,894,1226,0,1124,1161,840],
[1030,982,780,1048,829,877,0,1162,823],
[840,1176,885,833,850,840,839,0,1050],
[963,1220,888,1187,899,1161,1178,951,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 128, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,968,1009,1012,1002,1019,1020,987,1033],
[1033,0,1037,978,1052,1043,1036,1010,1073],
[992,964,0,1023,1028,926,1000,1012,1018],
[989,1023,978,0,999,1030,988,1028,1025],
[999,949,973,1002,0,1010,998,979,1003],
[982,958,1075,971,991,0,1039,967,976],
[981,965,1001,1013,1003,962,0,923,992],
[1014,991,989,973,1022,1034,1078,0,1054],
[968,928,983,976,998,1025,1009,947,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 129, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,900,972,916,924,911,959,950,1001],
[1101,0,1044,1035,1042,1059,1041,1065,988],
[1029,957,0,967,944,1018,962,1006,977],
[1085,966,1034,0,998,982,1035,1023,1010],
[1077,959,1057,1003,0,1077,989,1023,991],
[1090,942,983,1019,924,0,1009,989,948],
[1042,960,1039,966,1012,992,0,1004,983],
[1051,936,995,978,978,1012,997,0,968],
[1000,1013,1024,991,1010,1053,1018,1033,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 130, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,993,1008,1020,972,974,962,1028,1005],
[1008,0,976,1012,1029,970,975,974,998],
[993,1025,0,1024,1016,1006,979,1014,1026],
[981,989,977,0,1032,950,968,951,981],
[1029,972,985,969,0,967,965,968,1009],
[1027,1031,995,1051,1034,0,1004,1004,1017],
[1039,1026,1022,1033,1036,997,0,977,1040],
[973,1027,987,1050,1033,997,1024,0,1051],
[996,1003,975,1020,992,984,961,950,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 131, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,996,1053,1108,1104,998,1054,1078,1056],
[1005,0,962,973,1086,977,1029,948,944],
[948,1039,0,985,1157,1121,1077,1108,1110],
[893,1028,1016,0,1041,981,988,1051,1135],
[897,915,844,960,0,901,825,982,1084],
[1003,1024,880,1020,1100,0,999,1124,1065],
[947,972,924,1013,1176,1002,0,1050,1045],
[923,1053,893,950,1019,877,951,0,933],
[945,1057,891,866,917,936,956,1068,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 132, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,975,1060,1018,962,1125,1059,1075,956],
[1026,0,953,845,978,1057,876,997,893],
[941,1048,0,967,995,1077,995,966,901],
[983,1156,1034,0,1053,1156,962,1076,1008],
[1039,1023,1006,948,0,1033,953,1023,964],
[876,944,924,845,968,0,906,900,937],
[942,1125,1006,1039,1048,1095,0,1008,1045],
[926,1004,1035,925,978,1101,993,0,944],
[1045,1108,1100,993,1037,1064,956,1057,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 133, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1016,1016,1008,1031,1028,1007,1023,997],
[985,0,1025,998,1043,1020,996,1035,1023],
[985,976,0,964,1004,988,975,989,962],
[993,1003,1037,0,1061,1033,1013,1002,1011],
[970,958,997,940,0,973,961,975,948],
[973,981,1013,968,1028,0,983,983,995],
[994,1005,1026,988,1040,1018,0,1012,998],
[978,966,1012,999,1026,1018,989,0,979],
[1004,978,1039,990,1053,1006,1003,1022,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 134, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1005,989,970,997,990,969,977,974],
[996,0,971,985,984,947,956,956,986],
[1012,1030,0,1001,1021,981,1015,1024,967],
[1031,1016,1000,0,1030,981,1017,1005,1013],
[1004,1017,980,971,0,948,972,994,974],
[1011,1054,1020,1020,1053,0,996,1019,1023],
[1032,1045,986,984,1029,1005,0,1001,1022],
[1024,1045,977,996,1007,982,1000,0,1000],
[1027,1015,1034,988,1027,978,979,1001,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 135, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,996,1021,1024,983,993,982,977,993],
[1005,0,1007,994,974,997,977,965,997],
[980,994,0,973,990,957,974,979,985],
[977,1007,1028,0,980,1003,995,984,996],
[1018,1027,1011,1021,0,1005,1008,996,998],
[1008,1004,1044,998,996,0,982,966,1001],
[1019,1024,1027,1006,993,1019,0,999,1013],
[1024,1036,1022,1017,1005,1035,1002,0,997],
[1008,1004,1016,1005,1003,1000,988,1004,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 136, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,961,1039,994,1008,1006,994,989,1005],
[1040,0,1056,1025,1000,1010,997,992,1004],
[962,945,0,970,973,969,955,962,962],
[1007,976,1031,0,1039,1022,1019,985,978],
[993,1001,1028,962,0,1012,1027,985,996],
[995,991,1032,979,989,0,1008,980,1016],
[1007,1004,1046,982,974,993,0,940,986],
[1012,1009,1039,1016,1016,1021,1061,0,998],
[996,997,1039,1023,1005,985,1015,1003,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 137, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,996,843,981,972,1019,985,1039,912],
[1005,0,861,979,981,975,1034,1000,983],
[1158,1140,0,1074,1036,1076,1000,1044,963],
[1020,1022,927,0,960,960,1003,1001,942],
[1029,1020,965,1041,0,1073,976,954,1014],
[982,1026,925,1041,928,0,932,913,983],
[1016,967,1001,998,1025,1069,0,1052,944],
[962,1001,957,1000,1047,1088,949,0,921],
[1089,1018,1038,1059,987,1018,1057,1080,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 138, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,996,964,964,982,985,987,970,956],
[1005,0,1014,1045,986,1047,1004,1002,1003],
[1037,987,0,1005,1001,1002,1004,997,1002],
[1037,956,996,0,975,1011,977,995,1002],
[1019,1015,1000,1026,0,1010,1001,983,992],
[1016,954,999,990,991,0,980,964,992],
[1014,997,997,1024,1000,1021,0,979,1029],
[1031,999,1004,1006,1018,1037,1022,0,1034],
[1045,998,999,999,1009,1009,972,967,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 139, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,969,1010,965,1003,1054,1017,1029,1025],
[1032,0,956,929,1030,975,997,1012,1022],
[991,1045,0,1032,1027,984,985,1063,1008],
[1036,1072,969,0,968,1013,1016,1050,1052],
[998,971,974,1033,0,1031,993,1052,1038],
[947,1026,1017,988,970,0,996,1016,1022],
[984,1004,1016,985,1008,1005,0,1070,1071],
[972,989,938,951,949,985,931,0,986],
[976,979,993,949,963,979,930,1015,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 140, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,971,984,1062,983,987,952,981,977],
[1030,0,1016,1039,990,994,978,1010,1022],
[1017,985,0,1068,992,991,1001,995,1011],
[939,962,933,0,992,966,970,965,987],
[1018,1011,1009,1009,0,955,965,991,1018],
[1014,1007,1010,1035,1046,0,993,1003,1014],
[1049,1023,1000,1031,1036,1008,0,1027,1019],
[1020,991,1006,1036,1010,998,974,0,1007],
[1024,979,990,1014,983,987,982,994,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 141, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,960,1005,960,997,1013,965,1002,972],
[1041,0,1020,999,985,989,1021,972,980],
[996,981,0,988,960,982,992,975,992],
[1041,1002,1013,0,1003,1019,962,1027,984],
[1004,1016,1041,998,0,993,938,994,1002],
[988,1012,1019,982,1008,0,967,995,989],
[1036,980,1009,1039,1063,1034,0,1028,1000],
[999,1029,1026,974,1007,1006,973,0,1007],
[1029,1021,1009,1017,999,1012,1001,994,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 142, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1038,982,989,939,1008,1003,1001,1004],
[963,0,981,984,953,971,991,980,957],
[1019,1020,0,1028,992,1018,1033,1025,1022],
[1012,1017,973,0,978,997,1029,992,990],
[1062,1048,1009,1023,0,1019,1031,1029,993],
[993,1030,983,1004,982,0,1032,1038,988],
[998,1010,968,972,970,969,0,970,984],
[1000,1021,976,1009,972,963,1031,0,990],
[997,1044,979,1011,1008,1013,1017,1011,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 143, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1023,980,992,988,1031,970,1015,1007],
[978,0,971,1001,945,999,977,984,980],
[1021,1030,0,1008,964,1020,1008,1029,1018],
[1009,1000,993,0,1001,1002,998,1029,989],
[1013,1056,1037,1000,0,1036,997,1033,1016],
[970,1002,981,999,965,0,977,1008,965],
[1031,1024,993,1003,1004,1024,0,1061,1003],
[986,1017,972,972,968,993,940,0,962],
[994,1021,983,1012,985,1036,998,1039,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 144, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,987,980,967,988,972,980,966,991],
[1014,0,1014,1003,1001,988,1027,973,1006],
[1021,987,0,948,984,981,976,980,952],
[1034,998,1053,0,1014,993,1018,990,997],
[1013,1000,1017,987,0,970,1020,1006,1011],
[1029,1013,1020,1008,1031,0,1030,992,1018],
[1021,974,1025,983,981,971,0,983,988],
[1035,1028,1021,1011,995,1009,1018,0,1020],
[1010,995,1049,1004,990,983,1013,981,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 145, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1060,985,985,1007,1017,1043,1020,966],
[941,0,976,987,1027,1039,1012,1014,1019],
[1016,1025,0,1001,1010,1038,982,994,977],
[1016,1014,1000,0,1003,1012,1020,1007,1019],
[994,974,991,998,0,1017,1022,1024,955],
[984,962,963,989,984,0,973,916,957],
[958,989,1019,981,979,1028,0,1000,1002],
[981,987,1007,994,977,1085,1001,0,1011],
[1035,982,1024,982,1046,1044,999,990,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 146, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,966,950,944,986,1025,942,966,951],
[1035,0,1027,981,1008,1014,988,1017,1006],
[1051,974,0,996,1003,1024,996,1001,1010],
[1057,1020,1005,0,1019,1054,1011,1015,997],
[1015,993,998,982,0,1010,977,1012,975],
[976,987,977,947,991,0,975,1002,973],
[1059,1013,1005,990,1024,1026,0,1016,974],
[1035,984,1000,986,989,999,985,0,993],
[1050,995,991,1004,1026,1028,1027,1008,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 147, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,986,1032,953,1006,1023,1004,1031,1006],
[1015,0,1028,1009,1027,1026,978,1074,1040],
[969,973,0,935,958,991,951,1024,997],
[1048,992,1066,0,1010,1036,993,1016,1014],
[995,974,1043,991,0,984,1018,1030,1026],
[978,975,1010,965,1017,0,928,995,1018],
[997,1023,1050,1008,983,1073,0,1042,1061],
[970,927,977,985,971,1006,959,0,972],
[995,961,1004,987,975,983,940,1029,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 148, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1003,1001,1042,963,1004,995,1020,988],
[998,0,1007,1044,976,1021,1002,1014,989],
[1000,994,0,978,997,1015,994,1017,996],
[959,957,1023,0,982,1017,972,1012,959],
[1038,1025,1004,1019,0,1041,990,1032,1029],
[997,980,986,984,960,0,983,990,988],
[1006,999,1007,1029,1011,1018,0,970,995],
[981,987,984,989,969,1011,1031,0,1009],
[1013,1012,1005,1042,972,1013,1006,992,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 149, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1030,964,934,942,943,978,875,900],
[971,0,999,958,945,1007,945,961,960],
[1037,1002,0,1024,980,1044,990,948,988],
[1067,1043,977,0,1001,1033,1021,1024,1012],
[1059,1056,1021,1000,0,1020,993,959,995],
[1058,994,957,968,981,0,1016,937,945],
[1023,1056,1011,980,1008,985,0,969,987],
[1126,1040,1053,977,1042,1064,1032,0,1006],
[1101,1041,1013,989,1006,1056,1014,995,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 150, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1020,1009,1028,993,993,1005,960,993],
[981,0,1026,956,1006,968,974,951,1003],
[992,975,0,977,1015,1010,966,967,980],
[973,1045,1024,0,1009,1016,1022,1024,1009],
[1008,995,986,992,0,1002,992,964,981],
[1008,1033,991,985,999,0,999,954,997],
[996,1027,1035,979,1009,1002,0,984,1020],
[1041,1050,1034,977,1037,1047,1017,0,1031],
[1008,998,1021,992,1020,1004,981,970,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 151, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1047,917,1015,1052,1002,1136,867,899],
[954,0,951,802,904,902,960,741,863],
[1084,1050,0,957,1039,1003,1169,801,908],
[986,1199,1044,0,1159,1100,1092,1042,979],
[949,1097,962,842,0,982,1127,854,814],
[999,1099,998,901,1019,0,1106,883,974],
[865,1041,832,909,874,895,0,846,789],
[1134,1260,1200,959,1147,1118,1155,0,1020],
[1102,1138,1093,1022,1187,1027,1212,981,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 152, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1041,1011,1042,1011,1010,1010,1047,995],
[960,0,1009,975,1013,1003,1002,1021,1033],
[990,992,0,1017,974,992,1024,994,1003],
[959,1026,984,0,976,983,981,1002,953],
[990,988,1027,1025,0,976,1017,1040,1017],
[991,998,1009,1018,1025,0,1011,1028,1015],
[991,999,977,1020,984,990,0,1009,998],
[954,980,1007,999,961,973,992,0,994],
[1006,968,998,1048,984,986,1003,1007,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 153, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1040,1013,1000,953,1001,1070,1049,977],
[961,0,1030,1008,990,986,1053,1008,987],
[988,971,0,927,980,958,1008,981,929],
[1001,993,1074,0,1020,1041,1067,1101,972],
[1048,1011,1021,981,0,984,1050,1092,1038],
[1000,1015,1043,960,1017,0,994,1074,936],
[931,948,993,934,951,1007,0,1012,932],
[952,993,1020,900,909,927,989,0,928],
[1024,1014,1072,1029,963,1065,1069,1073,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 154, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1001,1051,1009,1029,1044,1005,987,1041],
[1000,0,1049,1000,1039,1036,1032,1006,1018],
[950,952,0,976,1019,997,985,952,1023],
[992,1001,1025,0,1031,1028,1001,984,999],
[972,962,982,970,0,974,975,931,952],
[957,965,1004,973,1027,0,999,964,993],
[996,969,1016,1000,1026,1002,0,993,1010],
[1014,995,1049,1017,1070,1037,1008,0,1016],
[960,983,978,1002,1049,1008,991,985,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 155, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,949,892,1065,1196,986,939,1078,940],
[1052,0,1007,1042,1146,1048,1034,967,1046],
[1109,994,0,1064,1162,1042,1027,895,937],
[936,959,937,0,926,945,976,872,965],
[805,855,839,1075,0,925,1009,868,784],
[1015,953,959,1056,1076,0,938,820,775],
[1062,967,974,1025,992,1063,0,958,964],
[923,1034,1106,1129,1133,1181,1043,0,1160],
[1061,955,1064,1036,1217,1226,1037,841,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 156, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,935,985,920,1072,1086,1091,1006,969],
[1066,0,895,981,925,1177,1087,1144,1046],
[1016,1106,0,955,964,1039,1008,1021,929],
[1081,1020,1046,0,980,1085,1024,1025,1058],
[929,1076,1037,1021,0,1040,1023,1099,1104],
[915,824,962,916,961,0,927,991,910],
[910,914,993,977,978,1074,0,1110,913],
[995,857,980,976,902,1010,891,0,958],
[1032,955,1072,943,897,1091,1088,1043,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 157, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1019,977,962,999,962,985,995,963],
[982,0,988,972,1009,983,979,964,977],
[1024,1013,0,966,983,937,999,998,946],
[1039,1029,1035,0,1003,1003,986,1020,944],
[1002,992,1018,998,0,1003,988,987,969],
[1039,1018,1064,998,998,0,1050,993,1018],
[1016,1022,1002,1015,1013,951,0,994,963],
[1006,1037,1003,981,1014,1008,1007,0,984],
[1038,1024,1055,1057,1032,983,1038,1017,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 158, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,990,961,996,975,950,984,964,966],
[1011,0,991,984,1008,1023,1031,974,996],
[1040,1010,0,1018,1023,996,1046,1001,1019],
[1005,1017,983,0,982,984,1016,996,984],
[1026,993,978,1019,0,1025,1032,992,998],
[1051,978,1005,1017,976,0,1012,972,982],
[1017,970,955,985,969,989,0,979,961],
[1037,1027,1000,1005,1009,1029,1022,0,1008],
[1035,1005,982,1017,1003,1019,1040,993,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 159, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,997,1015,1025,1019,1016,1054,1026,1018],
[1004,0,991,1030,1014,969,1029,996,985],
[986,1010,0,983,979,1015,1029,1023,1016],
[976,971,1018,0,984,988,1017,1017,1013],
[982,987,1022,1017,0,987,1017,1000,1003],
[985,1032,986,1013,1014,0,1019,1003,1010],
[947,972,972,984,984,982,0,988,994],
[975,1005,978,984,1001,998,1013,0,1011],
[983,1016,985,988,998,991,1007,990,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 160, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1029,974,1061,966,1023,1015,1006,1001],
[972,0,979,1028,947,918,888,964,985],
[1027,1022,0,1043,993,975,982,1059,1022],
[940,973,958,0,950,920,970,970,959],
[1035,1054,1008,1051,0,976,958,1031,985],
[978,1083,1026,1081,1025,0,987,1096,1093],
[986,1113,1019,1031,1043,1014,0,1045,1025],
[995,1037,942,1031,970,905,956,0,983],
[1000,1016,979,1042,1016,908,976,1018,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 161, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1012,991,1028,1052,1013,1027,976,1032],
[989,0,997,1011,1022,1018,1014,946,976],
[1010,1004,0,990,1027,1000,1038,1003,1010],
[973,990,1011,0,1006,985,1012,942,1006],
[949,979,974,995,0,1003,965,956,972],
[988,983,1001,1016,998,0,993,959,983],
[974,987,963,989,1036,1008,0,943,1000],
[1025,1055,998,1059,1045,1042,1058,0,1043],
[969,1025,991,995,1029,1018,1001,958,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 162, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1025,1003,1026,1038,1005,989,969,985],
[976,0,947,991,989,967,975,961,982],
[998,1054,0,1029,1045,1033,1007,1028,1051],
[975,1010,972,0,1007,990,992,955,987],
[963,1012,956,994,0,1009,939,969,983],
[996,1034,968,1011,992,0,993,981,1003],
[1012,1026,994,1009,1062,1008,0,976,996],
[1032,1040,973,1046,1032,1020,1025,0,982],
[1016,1019,950,1014,1018,998,1005,1019,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 163, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1031,1026,999,1039,1027,976,1042,1013],
[970,0,1002,998,987,1008,988,1030,994],
[975,999,0,984,1000,993,946,991,927],
[1002,1003,1017,0,1009,1047,944,1004,1018],
[962,1014,1001,992,0,975,990,1024,972],
[974,993,1008,954,1026,0,956,1003,1007],
[1025,1013,1055,1057,1011,1045,0,998,1043],
[959,971,1010,997,977,998,1003,0,984],
[988,1007,1074,983,1029,994,958,1017,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 164, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1024,980,990,961,992,994,955,1027],
[977,0,969,969,947,1020,950,970,991],
[1021,1032,0,1006,1015,1031,1023,974,1055],
[1011,1032,995,0,961,1038,997,1001,969],
[1040,1054,986,1040,0,1082,978,1032,1031],
[1009,981,970,963,919,0,967,965,985],
[1007,1051,978,1004,1023,1034,0,995,1018],
[1046,1031,1027,1000,969,1036,1006,0,1024],
[974,1010,946,1032,970,1016,983,977,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 165, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1043,1098,949,1063,1029,961,1052,1026],
[958,0,1026,927,906,962,894,941,936],
[903,975,0,967,952,947,943,993,1041],
[1052,1074,1034,0,1033,969,1021,968,1006],
[938,1095,1049,968,0,983,1024,997,952],
[972,1039,1054,1032,1018,0,998,1049,1020],
[1040,1107,1058,980,977,1003,0,955,963],
[949,1060,1008,1033,1004,952,1046,0,1003],
[975,1065,960,995,1049,981,1038,998,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 166, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1058,1030,998,1027,1008,997,1032,1034],
[943,0,912,964,938,887,863,945,889],
[971,1089,0,1017,1020,979,996,946,982],
[1003,1037,984,0,1007,987,1018,958,988],
[974,1063,981,994,0,973,1006,1024,926],
[993,1114,1022,1014,1028,0,1026,998,1012],
[1004,1138,1005,983,995,975,0,1003,1001],
[969,1056,1055,1043,977,1003,998,0,1034],
[967,1112,1019,1013,1075,989,1000,967,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 167, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1007,1031,971,965,1026,985,1010,1005],
[994,0,1051,982,1013,1007,975,990,977],
[970,950,0,970,966,980,958,970,971],
[1030,1019,1031,0,1014,1006,996,995,1006],
[1036,988,1035,987,0,1028,973,985,991],
[975,994,1021,995,973,0,981,977,998],
[1016,1026,1043,1005,1028,1020,0,1013,975],
[991,1011,1031,1006,1016,1024,988,0,999],
[996,1024,1030,995,1010,1003,1026,1002,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 168, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1013,995,1005,1049,1023,1009,1052,1026],
[988,0,993,998,1019,1040,973,1013,1015],
[1006,1008,0,999,1023,1049,998,1042,1001],
[996,1003,1002,0,1042,1033,996,1025,1010],
[952,982,978,959,0,1008,994,1012,1008],
[978,961,952,968,993,0,970,1000,973],
[992,1028,1003,1005,1007,1031,0,1039,997],
[949,988,959,976,989,1001,962,0,1017],
[975,986,1000,991,993,1028,1004,984,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 169, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1006,988,1028,1032,978,973,992,980],
[995,0,1030,1019,1064,1017,1030,1036,1028],
[1013,971,0,969,1028,967,987,980,1007],
[973,982,1032,0,1051,1022,984,1014,995],
[969,937,973,950,0,969,960,1002,963],
[1023,984,1034,979,1032,0,992,970,1010],
[1028,971,1014,1017,1041,1009,0,1018,996],
[1009,965,1021,987,999,1031,983,0,1002],
[1021,973,994,1006,1038,991,1005,999,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 170, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,993,1025,1010,1016,1018,1025,1031,1034],
[1008,0,988,1018,990,1029,999,996,1007],
[976,1013,0,1036,1001,1005,995,1011,1042],
[991,983,965,0,973,998,967,960,1001],
[985,1011,1000,1028,0,1075,993,1003,1008],
[983,972,996,1003,926,0,964,991,974],
[976,1002,1006,1034,1008,1037,0,1009,1031],
[970,1005,990,1041,998,1010,992,0,1005],
[967,994,959,1000,993,1027,970,996,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 171, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,999,985,991,958,981,957,1016,973],
[1002,0,1017,1014,983,1013,953,1027,994],
[1016,984,0,999,1036,1003,990,1036,1006],
[1010,987,1002,0,987,993,964,1016,968],
[1043,1018,965,1014,0,1040,985,1054,996],
[1020,988,998,1008,961,0,954,1029,1002],
[1044,1048,1011,1037,1016,1047,0,1039,1000],
[985,974,965,985,947,972,962,0,967],
[1028,1007,995,1033,1005,999,1001,1034,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 172, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1046,1014,1028,1016,979,1030,986,987],
[955,0,977,974,972,961,952,937,966],
[987,1024,0,1005,988,1019,974,975,1015],
[973,1027,996,0,998,1012,991,978,988],
[985,1029,1013,1003,0,1008,970,1006,980],
[1022,1040,982,989,993,0,1028,976,995],
[971,1049,1027,1010,1031,973,0,958,991],
[1015,1064,1026,1023,995,1025,1043,0,1011],
[1014,1035,986,1013,1021,1006,1010,990,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 173, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,970,1038,1040,1009,1025,1005,989,995],
[1031,0,1001,1037,1004,1007,997,982,1023],
[963,1000,0,1002,961,960,965,966,949],
[961,964,999,0,998,965,957,979,960],
[992,997,1040,1003,0,977,945,970,978],
[976,994,1041,1036,1024,0,994,987,1002],
[996,1004,1036,1044,1056,1007,0,1002,1027],
[1012,1019,1035,1022,1031,1014,999,0,1024],
[1006,978,1052,1041,1023,999,974,977,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 174, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1039,1013,1010,1025,1000,1018,1109,1017],
[962,0,1009,993,1036,1018,1037,1050,992],
[988,992,0,995,1034,1024,997,1058,1006],
[991,1008,1006,0,999,1010,1029,1042,1013],
[976,965,967,1002,0,992,974,1051,985],
[1001,983,977,991,1009,0,1012,1047,1016],
[983,964,1004,972,1027,989,0,1038,942],
[892,951,943,959,950,954,963,0,961],
[984,1009,995,988,1016,985,1059,1040,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 175, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1019,1022,1009,1008,1020,1006,981,990],
[982,0,979,997,990,1011,969,981,1006],
[979,1022,0,995,1019,1009,970,974,962],
[992,1004,1006,0,988,980,977,979,960],
[993,1011,982,1013,0,1011,994,1006,1002],
[981,990,992,1021,990,0,982,964,966],
[995,1032,1031,1024,1007,1019,0,988,1001],
[1020,1020,1027,1022,995,1037,1013,0,1015],
[1011,995,1039,1041,999,1035,1000,986,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 176, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,987,986,1007,1019,1008,1002,999,967],
[1014,0,999,1000,1023,1011,1043,1015,988],
[1015,1002,0,999,1005,1024,1011,996,1004],
[994,1001,1002,0,1020,986,1037,998,991],
[982,978,996,981,0,972,996,964,991],
[993,990,977,1015,1029,0,1024,961,970],
[999,958,990,964,1005,977,0,980,953],
[1002,986,1005,1003,1037,1040,1021,0,1013],
[1034,1013,997,1010,1010,1031,1048,988,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 177, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,931,940,1001,954,1092,987,973,903],
[1070,0,933,1011,956,1173,1062,1011,882],
[1061,1068,0,1167,1052,1168,1116,1134,967],
[1000,990,834,0,882,1031,994,1023,860],
[1047,1045,949,1119,0,1229,1091,1010,1005],
[909,828,833,970,772,0,943,915,751],
[1014,939,885,1007,910,1058,0,1021,836],
[1028,990,867,978,991,1086,980,0,948],
[1098,1119,1034,1141,996,1250,1165,1053,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 178, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1004,970,965,978,993,994,947,972],
[997,0,977,976,1008,952,963,977,1000],
[1031,1024,0,965,1000,987,1001,1009,1005],
[1036,1025,1036,0,1015,981,985,995,1002],
[1023,993,1001,986,0,986,976,981,1029],
[1008,1049,1014,1020,1015,0,1009,981,1003],
[1007,1038,1000,1016,1025,992,0,1011,1025],
[1054,1024,992,1006,1020,1020,990,0,1032],
[1029,1001,996,999,972,998,976,969,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 179, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,978,997,975,1024,967,960,944,932],
[1023,0,1026,985,1051,1014,1051,1031,1028],
[1004,975,0,978,1044,979,979,1007,1030],
[1026,1016,1023,0,1082,1041,999,1045,1031],
[977,950,957,919,0,949,1010,914,957],
[1034,987,1022,960,1052,0,1037,1008,997],
[1041,950,1022,1002,991,964,0,956,1006],
[1057,970,994,956,1087,993,1045,0,970],
[1069,973,971,970,1044,1004,995,1031,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 180, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1035,1072,1040,1093,1086,980,1091,1375],
[966,0,835,984,1107,1225,1151,910,1254],
[929,1166,0,1005,1167,1378,1108,1253,1243],
[961,1017,996,0,1009,1223,974,1074,1228],
[908,894,834,992,0,1134,1004,1103,1066],
[915,776,623,778,867,0,894,891,1092],
[1021,850,893,1027,997,1107,0,962,1312],
[910,1091,748,927,898,1110,1039,0,1218],
[626,747,758,773,935,909,689,783,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 181, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,933,873,912,996,1023,847,945,940],
[1068,0,971,942,1003,1025,962,969,989],
[1128,1030,0,1052,1057,1030,916,968,1141],
[1089,1059,949,0,1012,1050,979,1044,1046],
[1005,998,944,989,0,929,1006,977,976],
[978,976,971,951,1072,0,934,966,1000],
[1154,1039,1085,1022,995,1067,0,1083,1098],
[1056,1032,1033,957,1024,1035,918,0,931],
[1061,1012,860,955,1025,1001,903,1070,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 182, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1029,1042,910,948,1013,1064,990,955],
[972,0,1028,1008,971,986,1080,975,1006],
[959,973,0,979,930,1011,1009,1019,905],
[1091,993,1022,0,1008,1046,1055,1019,964],
[1053,1030,1071,993,0,1029,1076,1120,1028],
[988,1015,990,955,972,0,1027,932,962],
[937,921,992,946,925,974,0,959,945],
[1011,1026,982,982,881,1069,1042,0,976],
[1046,995,1096,1037,973,1039,1056,1025,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 183, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1002,972,1049,943,998,938,1005,1044],
[999,0,972,990,959,974,926,885,999],
[1029,1029,0,1022,1006,1046,942,947,1008],
[952,1011,979,0,931,992,957,962,952],
[1058,1042,995,1070,0,1008,1003,1041,1044],
[1003,1027,955,1009,993,0,959,987,988],
[1063,1075,1059,1044,998,1042,0,1009,1037],
[996,1116,1054,1039,960,1014,992,0,998],
[957,1002,993,1049,957,1013,964,1003,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 184, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,972,976,973,1074,947,962,912,928],
[1029,0,1002,1067,1088,969,978,958,1008],
[1025,999,0,1042,1102,978,1019,981,1007],
[1028,934,959,0,1092,1007,1016,976,984],
[927,913,899,909,0,882,897,866,881],
[1054,1032,1023,994,1119,0,1061,1041,1006],
[1039,1023,982,985,1104,940,0,980,1012],
[1089,1043,1020,1025,1135,960,1021,0,1117],
[1073,993,994,1017,1120,995,989,884,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 185, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1023,1004,1046,1001,983,1009,996,1020],
[978,0,998,1027,1034,1011,997,993,1026],
[997,1003,0,1034,1037,976,1036,993,1019],
[955,974,967,0,1002,976,997,967,1022],
[1000,967,964,999,0,1001,1016,999,1004],
[1018,990,1025,1025,1000,0,1051,1025,1039],
[992,1004,965,1004,985,950,0,982,1005],
[1005,1008,1008,1034,1002,976,1019,0,1005],
[981,975,982,979,997,962,996,996,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 186, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,992,990,988,1026,1008,976,1006,969],
[1009,0,1016,1002,1039,1041,988,1012,1018],
[1011,985,0,1004,1036,1022,992,1001,980],
[1013,999,997,0,1044,1039,992,977,983],
[975,962,965,957,0,988,917,991,939],
[993,960,979,962,1013,0,976,988,962],
[1025,1013,1009,1009,1084,1025,0,1021,993],
[995,989,1000,1024,1010,1013,980,0,975],
[1032,983,1021,1018,1062,1039,1008,1026,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 187, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1039,963,1025,1024,1012,1000,1060,1055],
[962,0,924,937,971,943,888,938,948],
[1038,1077,0,1034,1035,992,965,1008,1047],
[976,1064,967,0,988,1029,1004,1026,1037],
[977,1030,966,1013,0,984,928,1018,992],
[989,1058,1009,972,1017,0,982,1016,1023],
[1001,1113,1036,997,1073,1019,0,1053,1054],
[941,1063,993,975,983,985,948,0,1010],
[946,1053,954,964,1009,978,947,991,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 188, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,983,978,1008,981,961,958,950,961],
[1018,0,1006,1024,1004,989,974,994,1004],
[1023,995,0,1055,1032,1004,1032,1004,1016],
[993,977,946,0,980,961,991,962,988],
[1020,997,969,1021,0,990,988,991,978],
[1040,1012,997,1040,1011,0,1028,1000,1020],
[1043,1027,969,1010,1013,973,0,991,997],
[1051,1007,997,1039,1010,1001,1010,0,994],
[1040,997,985,1013,1023,981,1004,1007,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 189, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1001,1006,1051,1021,997,1001,1033,1011],
[1000,0,995,1031,1010,1025,997,1005,1020],
[995,1006,0,1015,991,997,974,992,984],
[950,970,986,0,994,992,972,989,987],
[980,991,1010,1007,0,1023,969,1005,990],
[1004,976,1004,1009,978,0,972,1011,1009],
[1000,1004,1027,1029,1032,1029,0,1059,1024],
[968,996,1009,1012,996,990,942,0,978],
[990,981,1017,1014,1011,992,977,1023,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 190, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1026,975,1011,1068,1027,1028,1067,1065],
[975,0,963,939,998,1011,978,1028,977],
[1026,1038,0,1003,989,1043,1037,1006,1049],
[990,1062,998,0,1038,1049,1025,1069,1044],
[933,1003,1012,963,0,1004,976,1026,980],
[974,990,958,952,997,0,972,1012,1008],
[973,1023,964,976,1025,1029,0,993,1028],
[934,973,995,932,975,989,1008,0,1009],
[936,1024,952,957,1021,993,973,992,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 191, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1013,1020,1000,1007,976,1021,1006,981],
[988,0,1016,1003,1027,993,989,1006,966],
[981,985,0,988,986,997,1034,987,973],
[1001,998,1013,0,1012,1016,1036,991,1003],
[994,974,1015,989,0,984,995,989,985],
[1025,1008,1004,985,1017,0,1027,983,1004],
[980,1012,967,965,1006,974,0,992,998],
[995,995,1014,1010,1012,1018,1009,0,982],
[1020,1035,1028,998,1016,997,1003,1019,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 192, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1023,1227,946,1034,1186,1113,982,1104],
[978,0,1103,1036,945,1128,954,1009,1081],
[774,898,0,992,863,948,834,904,974],
[1055,965,1009,0,912,1120,941,1095,1005],
[967,1056,1138,1089,0,1029,977,1009,1115],
[815,873,1053,881,972,0,835,967,859],
[888,1047,1167,1060,1024,1166,0,1008,1132],
[1019,992,1097,906,992,1034,993,0,1018],
[897,920,1027,996,886,1142,869,983,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 193, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1010,989,1008,1002,1016,983,1034,1019],
[991,0,1034,1035,985,1051,1016,1048,1040],
[1012,967,0,992,1030,1019,997,1004,997],
[993,966,1009,0,997,985,967,1009,993],
[999,1016,971,1004,0,995,1016,1000,1044],
[985,950,982,1016,1006,0,1007,1029,1021],
[1018,985,1004,1034,985,994,0,1020,1021],
[967,953,997,992,1001,972,981,0,995],
[982,961,1004,1008,957,980,980,1006,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 194, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1041,984,1014,1064,981,977,1057,999],
[960,0,997,1017,1044,1004,1011,1016,969],
[1017,1004,0,1016,1034,991,1045,1003,1005],
[987,984,985,0,1064,1035,1016,1038,1005],
[937,957,967,937,0,981,986,1009,925],
[1020,997,1010,966,1020,0,1020,1020,982],
[1024,990,956,985,1015,981,0,1033,964],
[944,985,998,963,992,981,968,0,995],
[1002,1032,996,996,1076,1019,1037,1006,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 195, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,973,969,974,959,984,1001,1012,995],
[1028,0,1005,999,988,1013,1017,1036,1039],
[1032,996,0,1031,1026,1016,1046,1028,1020],
[1027,1002,970,0,963,1008,997,1016,1013],
[1042,1013,975,1038,0,1006,1035,1029,1018],
[1017,988,985,993,995,0,1022,1012,1014],
[1000,984,955,1004,966,979,0,1030,998],
[989,965,973,985,972,989,971,0,996],
[1006,962,981,988,983,987,1003,1005,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 196, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1005,1006,997,987,986,990,982,1011],
[996,0,1032,991,1018,1000,1019,1008,1000],
[995,969,0,975,996,997,999,997,978],
[1004,1010,1026,0,991,970,1019,992,966],
[1014,983,1005,1010,0,980,1010,986,997],
[1015,1001,1004,1031,1021,0,998,988,989],
[1011,982,1002,982,991,1003,0,1015,1018],
[1019,993,1004,1009,1015,1013,986,0,1003],
[990,1001,1023,1035,1004,1012,983,998,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 197, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1033,987,1013,961,1027,1002,992,966],
[968,0,969,1003,970,1034,997,992,984],
[1014,1032,0,1019,1017,1010,1038,990,986],
[988,998,982,0,966,1001,1000,1001,970],
[1040,1031,984,1035,0,1022,1026,1017,1001],
[974,967,991,1000,979,0,988,953,993],
[999,1004,963,1001,975,1013,0,962,991],
[1009,1009,1011,1000,984,1048,1039,0,978],
[1035,1017,1015,1031,1000,1008,1010,1023,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 198, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,921,939,976,1018,976,977,940,1106],
[1080,0,1076,1110,1047,964,931,1033,1026],
[1062,925,0,978,1036,1068,1033,924,1000],
[1025,891,1023,0,1062,941,1015,1091,1132],
[983,954,965,939,0,1048,945,976,1015],
[1025,1037,933,1060,953,0,925,983,994],
[1024,1070,968,986,1056,1076,0,1003,1027],
[1061,968,1077,910,1025,1018,998,0,1059],
[895,975,1001,869,986,1007,974,942,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 199, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,869,862,994,980,855,795,802,1029],
[1132,0,995,1066,944,1075,894,1062,957],
[1139,1006,0,1119,961,1075,1056,1108,977],
[1007,935,882,0,912,1032,887,1002,877],
[1021,1057,1040,1089,0,1005,848,918,881],
[1146,926,926,969,996,0,787,875,958],
[1206,1107,945,1114,1153,1214,0,1053,1003],
[1199,939,893,999,1083,1126,948,0,1014],
[972,1044,1024,1124,1120,1043,998,987,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2001, 200, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/mebb/mebb_9_2001.csv", index=False, header=False)