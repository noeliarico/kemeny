
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg

rep = 1
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,1053,1050,1023,1060,933,962,960,999,1042,1000],
[947,0,956,964,960,899,1009,1009,979,951,959],
[950,1044,0,975,999,931,961,903,973,1031,978],
[977,1036,1025,0,1101,1031,1022,1055,1088,1042,1078],
[940,1040,1001,899,0,846,988,1003,918,998,944],
[1067,1101,1069,969,1154,0,1042,1041,1054,1115,1019],
[1038,991,1039,978,1012,958,0,976,995,992,991],
[1040,991,1097,945,997,959,1024,0,1003,1021,1001],
[1001,1021,1027,912,1082,946,1005,997,0,1020,958],
[958,1049,969,958,1002,885,1008,979,980,0,1010],
[1000,1041,1022,922,1056,981,1009,999,1042,990,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 1, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1364,542,1436,365,1364,907,614,1071,1436,1071],
[636,0,564,72,0,457,542,72,72,529,72],
[1458,1436,0,1436,894,1436,1436,894,894,894,894],
[564,1928,564,0,564,457,1106,564,564,1458,1021],
[1635,2000,1106,1436,0,1436,979,1178,1635,2000,1635],
[636,1543,564,1543,564,0,1178,636,636,1458,636],
[1093,1458,564,894,1021,822,0,636,1093,1458,1093],
[1386,1928,1106,1436,822,1364,1364,0,1458,894,894],
[929,1928,1106,1436,365,1364,907,542,0,894,529],
[564,1471,1106,542,0,542,542,1106,1106,0,0],
[929,1928,1106,979,365,1364,907,1106,1471,2000,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 2, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,987,1020,1062,1053,985,1024,983,1033,1065,1016],
[1013,0,1017,984,1012,1001,1034,1012,1014,1088,1043],
[980,983,0,979,1008,962,1026,997,1010,1072,1011],
[938,1016,1021,0,1058,1007,976,993,1021,1060,1046],
[947,988,992,942,0,1011,954,989,1008,1064,1001],
[1015,999,1038,993,989,0,1011,1011,1004,1086,1025],
[976,966,974,1024,1046,989,0,1056,994,1028,1036],
[1017,988,1003,1007,1011,989,944,0,1001,1022,1009],
[967,986,990,979,992,996,1006,999,0,1045,1032],
[935,912,928,940,936,914,972,978,955,0,927],
[984,957,989,954,999,975,964,991,968,1073,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 3, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,998,920,1007,957,1017,1077,1010,968,1046,1060],
[1002,0,999,963,994,952,952,1080,1051,1001,979],
[1080,1001,0,1165,1050,1173,1072,990,1039,1019,1100],
[993,1037,835,0,1017,1105,1031,1001,1046,933,1071],
[1043,1006,950,983,0,1115,1085,1049,1014,1036,1055],
[983,1048,827,895,885,0,940,958,820,872,922],
[923,1048,928,969,915,1060,0,984,997,988,1032],
[990,920,1010,999,951,1042,1016,0,1020,1038,1072],
[1032,949,961,954,986,1180,1003,980,0,921,1039],
[954,999,981,1067,964,1128,1012,962,1079,0,991],
[940,1021,900,929,945,1078,968,928,961,1009,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 4, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,968,1064,1021,1014,990,1058,1010,991,1027,991],
[1032,0,999,1009,1081,999,1043,959,1048,1042,966],
[936,1001,0,1065,1055,983,985,971,1005,1025,1030],
[979,991,935,0,978,975,953,915,969,940,893],
[986,919,945,1022,0,1013,986,972,976,992,974],
[1010,1001,1017,1025,987,0,969,1007,1011,978,1009],
[942,957,1015,1047,1014,1031,0,937,1016,992,959],
[990,1041,1029,1085,1028,993,1063,0,1070,1028,1035],
[1009,952,995,1031,1024,989,984,930,0,995,940],
[973,958,975,1060,1008,1022,1008,972,1005,0,1028],
[1009,1034,970,1107,1026,991,1041,965,1060,972,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 5, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1027,1012,984,1007,1020,1027,1002,1000,1027,1009],
[973,0,992,953,974,995,993,1012,948,1038,1013],
[988,1008,0,953,965,969,991,971,910,1028,976],
[1016,1047,1047,0,984,990,986,1028,1002,993,1017],
[993,1026,1035,1016,0,1005,1027,987,990,1061,1031],
[980,1005,1031,1010,995,0,1032,1010,973,1045,971],
[973,1007,1009,1014,973,968,0,950,980,1023,1021],
[998,988,1029,972,1013,990,1050,0,959,1027,1011],
[1000,1052,1090,998,1010,1027,1020,1041,0,1065,1020],
[973,962,972,1007,939,955,977,973,935,0,985],
[991,987,1024,983,969,1029,979,989,980,1015,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 6, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,956,974,1019,989,989,993,1012,972,995,997],
[1044,0,995,1013,1006,1043,1059,1029,1049,1053,1040],
[1026,1005,0,1002,946,983,975,988,960,1019,1021],
[981,987,998,0,964,987,981,1017,992,982,1017],
[1011,994,1054,1036,0,1003,1021,974,984,1001,1049],
[1011,957,1017,1013,997,0,1012,1009,1005,1030,1021],
[1007,941,1025,1019,979,988,0,1004,967,1013,958],
[988,971,1012,983,1026,991,996,0,961,984,991],
[1028,951,1040,1008,1016,995,1033,1039,0,1042,1035],
[1005,947,981,1018,999,970,987,1016,958,0,1026],
[1003,960,979,983,951,979,1042,1009,965,974,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 7, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,573,706,688,772,824,680,738,681,903,915],
[1427,0,962,1207,1143,1214,1298,1007,1125,1295,1620],
[1294,1038,0,849,1225,927,865,976,1125,1097,1047],
[1312,793,1151,0,814,817,868,774,718,919,1232],
[1228,857,775,1186,0,845,948,833,1028,1166,1327],
[1176,786,1073,1183,1155,0,1016,1216,1038,1242,1319],
[1320,702,1135,1132,1052,984,0,1179,809,965,1244],
[1262,993,1024,1226,1167,784,821,0,1028,864,1304],
[1319,875,875,1282,972,962,1191,972,0,941,1326],
[1097,705,903,1081,834,758,1035,1136,1059,0,1038],
[1085,380,953,768,673,681,756,696,674,962,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 8, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,988,983,1038,1025,978,999,1032,984,1000,1019],
[1012,0,1030,1039,1045,1028,1013,961,980,953,978],
[1017,970,0,991,1015,1007,992,967,1008,985,975],
[962,961,1009,0,1016,970,1011,983,968,974,962],
[975,955,985,984,0,932,988,1004,958,966,962],
[1022,972,993,1030,1068,0,1023,1011,992,1035,1000],
[1001,987,1008,989,1012,977,0,993,959,1025,1008],
[968,1039,1033,1017,996,989,1007,0,1019,977,938],
[1016,1020,992,1032,1042,1008,1041,981,0,1036,1028],
[1000,1047,1015,1026,1034,965,975,1023,964,0,993],
[981,1022,1025,1038,1038,1000,992,1062,972,1007,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 9, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,989,1044,1018,1019,1002,1056,1071,1025,1026,1017],
[1011,0,1003,1051,997,1061,1039,1027,1048,982,1035],
[956,997,0,1005,990,986,1011,1035,966,956,965],
[982,949,995,0,991,1017,1017,1015,975,995,1003],
[981,1003,1010,1009,0,989,1017,1022,990,1024,1031],
[998,939,1014,983,1011,0,1047,1026,1026,1003,994],
[944,961,989,983,983,953,0,1006,1021,975,1016],
[929,973,965,985,978,974,994,0,1002,947,993],
[975,952,1034,1025,1010,974,979,998,0,963,1008],
[974,1018,1044,1005,976,997,1025,1053,1037,0,1016],
[983,965,1035,997,969,1006,984,1007,992,984,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 10, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,973,992,937,907,950,978,1006,918,996,944],
[1027,0,1012,922,930,942,1016,1002,1003,971,976],
[1008,988,0,950,964,978,998,966,971,964,958],
[1063,1078,1050,0,987,1057,1048,1037,1065,1000,1035],
[1093,1070,1036,1013,0,1048,1041,1053,1012,1000,1013],
[1050,1058,1022,943,952,0,1016,1045,972,974,992],
[1022,984,1002,952,959,984,0,1038,967,978,987],
[994,998,1034,963,947,955,962,0,959,933,1007],
[1082,997,1029,935,988,1028,1033,1041,0,1011,1009],
[1004,1029,1036,1000,1000,1026,1022,1067,989,0,998],
[1056,1024,1042,965,987,1008,1013,993,991,1002,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 11, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1032,976,1039,1011,991,963,947,949,999,1084],
[968,0,1087,1005,990,995,902,991,974,854,1018],
[1024,913,0,1052,929,980,977,1006,1036,912,1023],
[961,995,948,0,951,966,933,890,927,964,1043],
[989,1010,1071,1049,0,1019,956,995,1013,950,1020],
[1009,1005,1020,1034,981,0,1005,958,1007,990,1045],
[1037,1098,1023,1067,1044,995,0,944,976,954,1070],
[1053,1009,994,1110,1005,1042,1056,0,1064,1153,1036],
[1051,1026,964,1073,987,993,1024,936,0,1021,1016],
[1001,1146,1088,1036,1050,1010,1046,847,979,0,1079],
[916,982,977,957,980,955,930,964,984,921,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 12, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1035,998,1029,1022,979,980,948,1054,1047,1045],
[965,0,1003,1000,985,957,924,986,939,982,996],
[1002,997,0,1067,927,1040,1137,1034,1036,1079,996],
[971,1000,933,0,992,1015,914,1075,925,1005,955],
[978,1015,1073,1008,0,935,1097,989,999,1133,1087],
[1021,1043,960,985,1065,0,980,1022,950,1035,1111],
[1020,1076,863,1086,903,1020,0,991,1005,1054,1061],
[1052,1014,966,925,1011,978,1009,0,1035,1043,1100],
[946,1061,964,1075,1001,1050,995,965,0,1110,1061],
[953,1018,921,995,867,965,946,957,890,0,923],
[955,1004,1004,1045,913,889,939,900,939,1077,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 13, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1030,1024,1017,1046,1016,1024,1022,1080,985,1029],
[970,0,984,1010,945,1023,980,970,1020,1028,1037],
[976,1016,0,984,982,977,1009,1005,1036,1004,984],
[983,990,1016,0,941,1027,986,994,1044,1021,995],
[954,1055,1018,1059,0,1052,1016,995,1058,1027,1046],
[984,977,1023,973,948,0,1012,947,1039,1024,1048],
[976,1020,991,1014,984,988,0,972,1049,1013,1008],
[978,1030,995,1006,1005,1053,1028,0,1026,1047,1021],
[920,980,964,956,942,961,951,974,0,941,971],
[1015,972,996,979,973,976,987,953,1059,0,1014],
[971,963,1016,1005,954,952,992,979,1029,986,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 14, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,999,901,835,1085,1021,1102,984,984,1054,1152],
[1001,0,1036,1091,1198,1090,1200,972,1128,1200,1022],
[1099,964,0,953,983,937,1103,950,783,1224,988],
[1165,909,1047,0,1029,936,1097,974,1137,1201,1081],
[915,802,1017,971,0,986,1011,983,978,1105,925],
[979,910,1063,1064,1014,0,930,962,1022,1249,964],
[898,800,897,903,989,1070,0,894,923,1094,1062],
[1016,1028,1050,1026,1017,1038,1106,0,948,1157,1109],
[1016,872,1217,863,1022,978,1077,1052,0,1072,993],
[946,800,776,799,895,751,906,843,928,0,848],
[848,978,1012,919,1075,1036,938,891,1007,1152,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 15, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1037,1004,1007,982,1025,1015,1026,1025,1034,1035],
[963,0,947,952,931,980,985,998,1008,973,978],
[996,1053,0,980,1005,1017,1013,1049,1035,989,1029],
[993,1048,1020,0,1006,1069,1035,1014,1027,1024,1046],
[1018,1069,995,994,0,1032,1022,997,1054,1036,1041],
[975,1020,983,931,968,0,1011,984,996,996,1018],
[985,1015,987,965,978,989,0,1012,1027,979,1038],
[974,1002,951,986,1003,1016,988,0,1025,974,1003],
[975,992,965,973,946,1004,973,975,0,1016,984],
[966,1027,1011,976,964,1004,1021,1026,984,0,998],
[965,1022,971,954,959,982,962,997,1016,1002,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 16, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1002,1046,1031,1020,995,1000,1007,1018,1020,1018],
[998,0,1020,997,1013,998,982,998,1002,1047,1008],
[954,980,0,976,995,969,977,944,945,989,994],
[969,1003,1024,0,1018,1000,982,1014,986,1024,1015],
[980,987,1005,982,0,980,984,976,986,1014,1016],
[1005,1002,1031,1000,1020,0,937,1006,1010,992,976],
[1000,1018,1023,1018,1016,1063,0,1008,1019,1026,1007],
[993,1002,1056,986,1024,994,992,0,993,1017,984],
[982,998,1055,1014,1014,990,981,1007,0,1020,999],
[980,953,1011,976,986,1008,974,983,980,0,995],
[982,992,1006,985,984,1024,993,1016,1001,1005,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 17, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,992,999,1000,1065,986,971,1012,986,1011,999],
[1008,0,989,1026,1025,1049,987,1027,985,975,1043],
[1001,1011,0,1001,1029,1040,1007,1049,1030,997,1020],
[1000,974,999,0,993,1012,971,1016,981,972,1018],
[935,975,971,1007,0,988,918,1018,982,970,967],
[1014,951,960,988,1012,0,922,1012,951,979,958],
[1029,1013,993,1029,1082,1078,0,1080,1030,1053,1041],
[988,973,951,984,982,988,920,0,950,946,979],
[1014,1015,970,1019,1018,1049,970,1050,0,1015,1001],
[989,1025,1003,1028,1030,1021,947,1054,985,0,1019],
[1001,957,980,982,1033,1042,959,1021,999,981,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 18, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,978,1003,1000,986,942,948,960,935,955,989],
[1022,0,1004,1035,1013,988,988,1020,999,1005,1000],
[997,996,0,977,995,947,978,974,961,991,990],
[1000,965,1023,0,987,934,991,995,984,967,968],
[1014,987,1005,1013,0,983,972,992,988,1011,986],
[1058,1012,1053,1066,1017,0,1037,1041,998,1002,994],
[1052,1012,1022,1009,1028,963,0,1002,987,1005,964],
[1040,980,1026,1005,1008,959,998,0,1008,994,987],
[1065,1001,1039,1016,1012,1002,1013,992,0,1015,1002],
[1045,995,1009,1033,989,998,995,1006,985,0,1012],
[1011,1000,1010,1032,1014,1006,1036,1013,998,988,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 19, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1114,1153,1081,907,1007,1085,1202,987,1043,1025],
[886,0,1037,1017,832,1026,1051,1036,894,1022,930],
[847,963,0,932,794,991,935,1009,910,961,872],
[919,983,1068,0,897,961,1008,1144,872,1007,1017],
[1093,1168,1206,1103,0,1056,1172,1190,1000,1165,1083],
[993,974,1009,1039,944,0,1072,1131,975,1024,987],
[915,949,1065,992,828,928,0,1115,926,931,1016],
[798,964,991,856,810,869,885,0,767,893,970],
[1013,1106,1090,1128,1000,1025,1074,1233,0,1057,1074],
[957,978,1039,993,835,976,1069,1107,943,0,1103],
[975,1070,1128,983,917,1013,984,1030,926,897,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 20, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,966,998,1065,975,1037,1023,1057,1070,972,1045],
[1034,0,1032,1075,972,1059,1015,1003,1021,1013,1056],
[1002,968,0,1023,961,1039,1015,1031,998,1011,1008],
[935,925,977,0,970,1008,963,965,980,939,998],
[1025,1028,1039,1030,0,1065,1022,1025,1037,990,1066],
[963,941,961,992,935,0,986,1027,1023,949,985],
[977,985,985,1037,978,1014,0,1017,1013,989,997],
[943,997,969,1035,975,973,983,0,1012,973,1011],
[930,979,1002,1020,963,977,987,988,0,975,992],
[1028,987,989,1061,1010,1051,1011,1027,1025,0,1007],
[955,944,992,1002,934,1015,1003,989,1008,993,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 21, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1047,1043,1006,1009,1024,1006,1054,979,1039,955],
[953,0,988,996,936,1003,1021,994,937,951,931],
[957,1012,0,969,935,980,989,1026,900,1005,946],
[994,1004,1031,0,996,995,983,1023,950,1012,953],
[991,1064,1065,1004,0,1014,1013,1072,984,1040,969],
[976,997,1020,1005,986,0,990,993,983,1016,936],
[994,979,1011,1017,987,1010,0,1054,1004,998,967],
[946,1006,974,977,928,1007,946,0,879,993,947],
[1021,1063,1100,1050,1016,1017,996,1121,0,1056,1018],
[961,1049,995,988,960,984,1002,1007,944,0,979],
[1045,1069,1054,1047,1031,1064,1033,1053,982,1021,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 22, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1003,1018,1002,985,1028,1010,1002,1026,1001,1038],
[997,0,966,1009,1006,1039,1045,1020,1054,1027,1020],
[982,1034,0,1014,1031,1044,1041,1033,1041,1019,1043],
[998,991,986,0,1001,1021,1029,995,1020,1008,1019],
[1015,994,969,999,0,1007,1001,975,1042,1063,1019],
[972,961,956,979,993,0,1029,948,1024,973,986],
[990,955,959,971,999,971,0,988,1041,1013,1025],
[998,980,967,1005,1025,1052,1012,0,1017,994,1060],
[974,946,959,980,958,976,959,983,0,981,1009],
[999,973,981,992,937,1027,987,1006,1019,0,1012],
[962,980,957,981,981,1014,975,940,991,988,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 23, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1047,992,989,1017,994,969,1021,1011,1003,1007],
[953,0,943,932,981,926,964,981,950,968,961],
[1008,1057,0,994,1046,1020,1041,1031,1007,998,1003],
[1011,1068,1006,0,1032,1007,990,982,1002,987,1012],
[983,1019,954,968,0,965,992,1010,959,996,978],
[1006,1074,980,993,1035,0,1005,1003,999,1005,960],
[1031,1036,959,1010,1008,995,0,973,1011,989,1005],
[979,1019,969,1018,990,997,1027,0,1000,1003,1004],
[989,1050,993,998,1041,1001,989,1000,0,1007,992],
[997,1032,1002,1013,1004,995,1011,997,993,0,982],
[993,1039,997,988,1022,1040,995,996,1008,1018,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 24, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,977,842,852,821,831,916,868,836,966,964],
[1023,0,904,845,901,1023,987,890,809,991,980],
[1158,1096,0,984,985,1038,1050,1033,1024,1098,964],
[1148,1155,1016,0,952,1003,1135,1002,990,1065,1126],
[1179,1099,1015,1048,0,990,1042,990,983,1096,1054],
[1169,977,962,997,1010,0,1032,975,989,1027,1052],
[1084,1013,950,865,958,968,0,970,922,935,1065],
[1132,1110,967,998,1010,1025,1030,0,1012,1117,1088],
[1164,1191,976,1010,1017,1011,1078,988,0,1070,1035],
[1034,1009,902,935,904,973,1065,883,930,0,970],
[1036,1020,1036,874,946,948,935,912,965,1030,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 25, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,976,980,1002,1023,992,1015,991,1036,1002,1013],
[1024,0,994,1027,1048,1031,1019,1038,1008,1026,989],
[1020,1006,0,1049,1023,1028,985,995,1009,1008,995],
[998,973,951,0,1008,973,991,956,943,980,964],
[977,952,977,992,0,1002,1026,975,960,1004,988],
[1008,969,972,1027,998,0,1024,999,999,1014,1022],
[985,981,1015,1009,974,976,0,974,981,1012,982],
[1009,962,1005,1044,1025,1001,1026,0,1014,1037,984],
[964,992,991,1057,1040,1001,1019,986,0,1022,992],
[998,974,992,1020,996,986,988,963,978,0,1000],
[987,1011,1005,1036,1012,978,1018,1016,1008,1000,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 26, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,952,987,1040,999,997,1006,986,1029,1036,1017],
[1048,0,1039,1080,1131,986,1004,1059,1075,1006,1074],
[1013,961,0,1048,978,947,989,986,993,1000,987],
[960,920,952,0,976,995,1014,1023,995,1006,1045],
[1001,869,1022,1024,0,941,982,976,997,996,939],
[1003,1014,1053,1005,1059,0,975,983,930,1018,1011],
[994,996,1011,986,1018,1025,0,1051,1053,1003,1066],
[1014,941,1014,977,1024,1017,949,0,945,961,1038],
[971,925,1007,1005,1003,1070,947,1055,0,1030,994],
[964,994,1000,994,1004,982,997,1039,970,0,970],
[983,926,1013,955,1061,989,934,962,1006,1030,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 27, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1053,992,1021,965,995,974,1002,966,934,926],
[947,0,983,1000,953,955,963,934,960,962,968],
[1008,1017,0,1066,1017,951,1102,1010,1017,947,1020],
[979,1000,934,0,974,962,1062,964,964,879,959],
[1035,1047,983,1026,0,1003,996,1055,1000,1007,963],
[1005,1045,1049,1038,997,0,1048,1019,1002,995,1051],
[1026,1037,898,938,1004,952,0,931,965,977,936],
[998,1066,990,1036,945,981,1069,0,999,933,994],
[1034,1040,983,1036,1000,998,1035,1001,0,960,962],
[1066,1038,1053,1121,993,1005,1023,1067,1040,0,953],
[1074,1032,980,1041,1037,949,1064,1006,1038,1047,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 28, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,999,972,985,1007,1004,1021,1006,954,1005,1015],
[1001,0,1013,1045,1005,1002,1006,1016,1019,1033,994],
[1028,987,0,1024,1017,1050,1036,1023,1017,1031,1035],
[1015,955,976,0,992,994,1003,1042,987,1019,1002],
[993,995,983,1008,0,1005,1012,991,966,996,1015],
[996,998,950,1006,995,0,1022,1017,978,1005,1030],
[979,994,964,997,988,978,0,999,971,975,990],
[994,984,977,958,1009,983,1001,0,989,986,982],
[1046,981,983,1013,1034,1022,1029,1011,0,1044,1020],
[995,967,969,981,1004,995,1025,1014,956,0,971],
[985,1006,965,998,985,970,1010,1018,980,1029,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 29, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1037,1023,1114,993,1033,1029,1012,1050,1063,1005],
[963,0,995,1067,979,1108,975,1037,1031,1001,956],
[977,1005,0,1034,945,1062,974,1080,989,963,992],
[886,933,966,0,965,997,927,999,988,1000,943],
[1007,1021,1055,1035,0,1074,963,984,1016,1016,940],
[967,892,938,1003,926,0,896,996,975,900,935],
[971,1025,1026,1073,1037,1104,0,1033,1082,1029,1035],
[988,963,920,1001,1016,1004,967,0,1006,1014,963],
[950,969,1011,1012,984,1025,918,994,0,1004,909],
[937,999,1037,1000,984,1100,971,986,996,0,930],
[995,1044,1008,1057,1060,1065,965,1037,1091,1070,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 30, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1015,961,977,972,984,956,976,980,982,976],
[985,0,969,967,956,980,925,967,985,950,991],
[1039,1031,0,1003,975,1002,957,983,1005,977,1016],
[1023,1033,997,0,987,1004,987,984,1007,974,1012],
[1028,1044,1025,1013,0,1022,1000,1030,1033,1018,1026],
[1016,1020,998,996,978,0,960,966,1008,936,1024],
[1044,1075,1043,1013,1000,1040,0,1033,1040,973,1064],
[1024,1033,1017,1016,970,1034,967,0,1013,983,1021],
[1020,1015,995,993,967,992,960,987,0,981,1020],
[1018,1050,1023,1026,982,1064,1027,1017,1019,0,1017],
[1024,1009,984,988,974,976,936,979,980,983,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 31, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1016,1029,975,988,981,1038,966,999,978,1041],
[984,0,982,987,957,994,1018,985,1025,957,1041],
[971,1018,0,1016,1058,979,1008,991,1028,980,1026],
[1025,1013,984,0,1026,1028,961,1039,1037,998,1082],
[1012,1043,942,974,0,934,933,948,1019,952,1016],
[1019,1006,1021,972,1066,0,1026,1031,1035,1007,989],
[962,982,992,1039,1067,974,0,993,1009,965,1060],
[1034,1015,1009,961,1052,969,1007,0,1060,955,1003],
[1001,975,972,963,981,965,991,940,0,917,1073],
[1022,1043,1020,1002,1048,993,1035,1045,1083,0,1068],
[959,959,974,918,984,1011,940,997,927,932,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 32, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,978,942,974,1005,1044,1053,1009,999,977,970],
[1022,0,1069,935,1038,1026,1017,1030,1005,995,1010],
[1058,931,0,1081,1054,1050,1019,1008,1046,1043,997],
[1026,1065,919,0,1092,1035,1003,949,1054,994,1002],
[995,962,946,908,0,1001,952,960,1007,962,968],
[956,974,950,965,999,0,947,967,1001,926,1004],
[947,983,981,997,1048,1053,0,958,966,954,975],
[991,970,992,1051,1040,1033,1042,0,959,1037,1014],
[1001,995,954,946,993,999,1034,1041,0,1010,988],
[1023,1005,957,1006,1038,1074,1046,963,990,0,991],
[1030,990,1003,998,1032,996,1025,986,1012,1009,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 33, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,968,957,1047,1020,1009,980,970,1041,1000,1009],
[1032,0,985,1042,1013,948,958,1009,1035,1029,1034],
[1043,1015,0,1059,975,998,1001,1038,1056,993,1071],
[953,958,941,0,929,897,956,991,981,961,979],
[980,987,1025,1071,0,963,994,1053,1031,990,1060],
[991,1052,1002,1103,1037,0,1052,1064,1068,994,1069],
[1020,1042,999,1044,1006,948,0,1055,1028,978,1050],
[1030,991,962,1009,947,936,945,0,975,956,1011],
[959,965,944,1019,969,932,972,1025,0,985,997],
[1000,971,1007,1039,1010,1006,1022,1044,1015,0,1041],
[991,966,929,1021,940,931,950,989,1003,959,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 34, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1024,1020,1057,1027,997,1030,1005,1004,1070,1004],
[976,0,1026,993,1014,1014,1020,970,1032,1034,989],
[980,974,0,988,999,987,1026,1013,1004,1037,966],
[943,1007,1012,0,992,1035,1017,992,1026,984,994],
[973,986,1001,1008,0,1018,1026,988,1012,1032,996],
[1003,986,1013,965,982,0,1010,987,1008,1020,980],
[970,980,974,983,974,990,0,940,963,1005,964],
[995,1030,987,1008,1012,1013,1060,0,1027,1029,1016],
[996,968,996,974,988,992,1037,973,0,1006,970],
[930,966,963,1016,968,980,995,971,994,0,971],
[996,1011,1034,1006,1004,1020,1036,984,1030,1029,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 35, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1010,983,1008,1000,995,1006,973,999,1006,1002],
[990,0,974,1007,992,983,1004,1002,979,1012,1042],
[1017,1026,0,992,1003,1008,994,997,1010,972,999],
[992,993,1008,0,984,1035,1020,990,1016,1005,1025],
[1000,1008,997,1016,0,1010,996,1019,1020,1005,1036],
[1005,1017,992,965,990,0,1000,991,995,997,998],
[994,996,1006,980,1004,1000,0,994,1003,977,1023],
[1027,998,1003,1010,981,1009,1006,0,1024,985,1026],
[1001,1021,990,984,980,1005,997,976,0,1009,1052],
[994,988,1028,995,995,1003,1023,1015,991,0,1012],
[998,958,1001,975,964,1002,977,974,948,988,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 36, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1030,965,1013,1007,989,972,1012,1059,1001,1045],
[970,0,940,1031,976,984,943,996,1062,975,1037],
[1035,1060,0,1048,1033,1018,1000,1096,1062,1047,1090],
[987,969,952,0,942,984,942,1042,1052,996,968],
[993,1024,967,1058,0,1011,1000,1086,1064,1023,1084],
[1011,1016,982,1016,989,0,986,1052,1060,1007,1029],
[1028,1057,1000,1058,1000,1014,0,1115,1160,1065,1048],
[988,1004,904,958,914,948,885,0,1060,977,978],
[941,938,938,948,936,940,840,940,0,946,1027],
[999,1025,953,1004,977,993,935,1023,1054,0,1007],
[955,963,910,1032,916,971,952,1022,973,993,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 37, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,970,1007,1007,981,986,1000,995,978,1002,998],
[1030,0,1027,1006,1005,1012,1024,1004,980,1059,1004],
[993,973,0,988,969,996,999,984,975,1003,1007],
[993,994,1012,0,981,1018,1019,966,993,1005,992],
[1019,995,1031,1019,0,1027,1017,1021,992,1030,1010],
[1014,988,1004,982,973,0,973,1001,964,994,980],
[1000,976,1001,981,983,1027,0,985,1005,1007,1016],
[1005,996,1016,1034,979,999,1015,0,1010,1039,994],
[1022,1020,1025,1007,1008,1036,995,990,0,1020,1005],
[998,941,997,995,970,1006,993,961,980,0,969],
[1002,996,993,1008,990,1020,984,1006,995,1031,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 38, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1038,987,1026,1006,1011,1027,1008,992,1015,1008],
[962,0,992,1027,999,1019,986,1002,987,1014,999],
[1013,1008,0,1045,1000,1034,1027,1026,1008,1024,1018],
[974,973,955,0,960,982,998,990,991,997,989],
[994,1001,1000,1040,0,1020,1028,1023,1037,991,997],
[989,981,966,1018,980,0,1023,1006,967,1004,978],
[973,1014,973,1002,972,977,0,983,974,1008,977],
[992,998,974,1010,977,994,1017,0,979,1005,999],
[1008,1013,992,1009,963,1033,1026,1021,0,999,994],
[985,986,976,1003,1009,996,992,995,1001,0,989],
[992,1001,982,1011,1003,1022,1023,1001,1006,1011,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 39, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1015,1027,1002,1001,1004,983,971,1013,1019,1040],
[985,0,1015,1014,1017,1016,1001,1022,1043,1021,988],
[973,985,0,975,994,969,947,971,1002,976,968],
[998,986,1025,0,1024,987,1004,989,996,976,1001],
[999,983,1006,976,0,999,999,947,998,1001,998],
[996,984,1031,1013,1001,0,1009,1013,992,1027,1023],
[1017,999,1053,996,1001,991,0,1021,1003,999,1026],
[1029,978,1029,1011,1053,987,979,0,1037,995,1042],
[987,957,998,1004,1002,1008,997,963,0,1003,991],
[981,979,1024,1024,999,973,1001,1005,997,0,1031],
[960,1012,1032,999,1002,977,974,958,1009,969,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 40, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1011,1037,1028,995,986,1018,1043,993,981,1026],
[989,0,1022,1000,975,1001,980,1011,976,986,1010],
[963,978,0,998,972,981,933,981,946,982,1012],
[972,1000,1002,0,994,997,957,1025,990,953,1015],
[1005,1025,1028,1006,0,988,1005,1036,1010,1015,1048],
[1014,999,1019,1003,1012,0,1015,1008,994,1004,1024],
[982,1020,1067,1043,995,985,0,1018,977,1019,1041],
[957,989,1019,975,964,992,982,0,969,958,989],
[1007,1024,1054,1010,990,1006,1023,1031,0,982,1042],
[1019,1014,1018,1047,985,996,981,1042,1018,0,1017],
[974,990,988,985,952,976,959,1011,958,983,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 41, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,993,1024,1019,1005,998,961,939,983,951,1002],
[1007,0,1016,1048,1025,1024,970,1003,1016,975,1002],
[976,984,0,979,1005,965,979,949,994,973,980],
[981,952,1021,0,998,962,1006,935,978,965,964],
[995,975,995,1002,0,963,937,944,987,956,950],
[1002,976,1035,1038,1037,0,973,991,1011,1038,1034],
[1039,1030,1021,994,1063,1027,0,1004,1019,997,1010],
[1061,997,1051,1065,1056,1009,996,0,1018,999,1008],
[1017,984,1006,1022,1013,989,981,982,0,972,982],
[1049,1025,1027,1035,1044,962,1003,1001,1028,0,997],
[998,998,1020,1036,1050,966,990,992,1018,1003,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 42, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,977,996,982,969,1032,1026,920,1015,981,933],
[1023,0,999,943,993,966,998,949,1044,988,970],
[1004,1001,0,974,1002,986,965,924,1012,942,984],
[1018,1057,1026,0,969,1037,988,970,1007,1054,1049],
[1031,1007,998,1031,0,1025,1017,944,1029,1038,1063],
[968,1034,1014,963,975,0,969,1008,982,995,989],
[974,1002,1035,1012,983,1031,0,933,1010,975,1017],
[1080,1051,1076,1030,1056,992,1067,0,1072,1040,1052],
[985,956,988,993,971,1018,990,928,0,947,989],
[1019,1012,1058,946,962,1005,1025,960,1053,0,1006],
[1067,1030,1016,951,937,1011,983,948,1011,994,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 43, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,918,949,922,953,936,1005,950,932,984,895],
[1082,0,988,1035,1069,984,1052,975,1002,991,939],
[1051,1012,0,1030,981,986,1063,1027,1001,1058,994],
[1078,965,970,0,1079,1002,1068,966,1035,983,983],
[1047,931,1019,921,0,1001,1030,970,1019,983,941],
[1064,1016,1014,998,999,0,1044,978,1000,1079,1028],
[995,948,937,932,970,956,0,952,988,950,943],
[1050,1025,973,1034,1030,1022,1048,0,1007,1011,1015],
[1068,998,999,965,981,1000,1012,993,0,1001,1012],
[1016,1009,942,1017,1017,921,1050,989,999,0,976],
[1105,1061,1006,1017,1059,972,1057,985,988,1024,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 44, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,965,958,960,1016,988,997,955,972,981,990],
[1035,0,1003,972,1002,998,1009,990,996,1008,984],
[1042,997,0,1005,1036,1002,1042,1005,997,1001,1000],
[1040,1028,995,0,1029,1014,1026,983,998,1013,1015],
[984,998,964,971,0,963,988,982,965,984,962],
[1012,1002,998,986,1037,0,1028,992,1000,1003,983],
[1003,991,958,974,1012,972,0,964,996,960,980],
[1045,1010,995,1017,1018,1008,1036,0,1024,986,999],
[1028,1004,1003,1002,1035,1000,1004,976,0,986,979],
[1019,992,999,987,1016,997,1040,1014,1014,0,1012],
[1010,1016,1000,985,1038,1017,1020,1001,1021,988,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 45, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,954,952,970,980,1000,951,1000,1019,930,1009],
[1046,0,945,953,942,1082,986,950,1049,1011,961],
[1048,1055,0,1028,1024,1054,1069,953,1070,1043,1018],
[1030,1047,972,0,1042,1186,1075,1013,1025,1031,1010],
[1020,1058,976,958,0,1070,997,1006,1027,1048,998],
[1000,918,946,814,930,0,1014,893,993,949,986],
[1049,1014,931,925,1003,986,0,969,1042,998,1014],
[1000,1050,1047,987,994,1107,1031,0,1063,1046,1012],
[981,951,930,975,973,1007,958,937,0,965,954],
[1070,989,957,969,952,1051,1002,954,1035,0,951],
[991,1039,982,990,1002,1014,986,988,1046,1049,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 46, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1035,1039,999,1018,977,1060,992,1021,1003,1016],
[965,0,989,1001,941,982,1056,994,1023,958,1011],
[961,1011,0,1020,1002,1000,1025,998,1025,977,953],
[1001,999,980,0,1007,1029,1038,996,1017,985,987],
[982,1059,998,993,0,1040,1034,1014,1021,996,1012],
[1023,1018,1000,971,960,0,1030,1003,960,970,950],
[940,944,975,962,966,970,0,998,982,968,964],
[1008,1006,1002,1004,986,997,1002,0,1016,1005,986],
[979,977,975,983,979,1040,1018,984,0,973,987],
[997,1042,1023,1015,1004,1030,1032,995,1027,0,974],
[984,989,1047,1013,988,1050,1036,1014,1013,1026,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 47, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1003,984,1073,1045,1075,924,1031,1026,999,989],
[997,0,1020,1062,1007,1054,973,1055,992,1007,976],
[1016,980,0,1079,1032,1077,1015,1016,962,1051,1027],
[927,938,921,0,991,1020,985,970,926,1008,973],
[955,993,968,1009,0,1015,952,1021,1015,1010,968],
[925,946,923,980,985,0,961,959,921,949,942],
[1076,1027,985,1015,1048,1039,0,1064,989,1031,971],
[969,945,984,1030,979,1041,936,0,951,998,948],
[974,1008,1038,1074,985,1079,1011,1049,0,1005,1020],
[1001,993,949,992,990,1051,969,1002,995,0,992],
[1011,1024,973,1027,1032,1058,1029,1052,980,1008,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 48, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,942,1006,984,1027,915,1013,911,981,995,938],
[1058,0,1049,1015,1049,998,1016,963,1009,1009,976],
[994,951,0,997,981,977,1001,970,984,987,964],
[1016,985,1003,0,1055,963,1002,1006,974,1003,919],
[973,951,1019,945,0,977,1046,938,999,1014,899],
[1085,1002,1023,1037,1023,0,1033,1039,1045,1039,983],
[987,984,999,998,954,967,0,970,1062,1021,965],
[1089,1037,1030,994,1062,961,1030,0,1043,1037,1026],
[1019,991,1016,1026,1001,955,938,957,0,915,956],
[1005,991,1013,997,986,961,979,963,1085,0,949],
[1062,1024,1036,1081,1101,1017,1035,974,1044,1051,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 49, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,952,970,967,983,973,1013,1009,1003,965,996],
[1048,0,992,985,973,997,1005,1021,1035,989,1031],
[1030,1008,0,992,966,1007,984,974,1007,1007,995],
[1033,1015,1008,0,977,1023,999,1035,1007,969,993],
[1017,1027,1034,1023,0,1001,998,1009,1046,1022,1007],
[1027,1003,993,977,999,0,1010,1009,1028,1003,1005],
[987,995,1016,1001,1002,990,0,1005,1028,993,994],
[991,979,1026,965,991,991,995,0,1029,995,1014],
[997,965,993,993,954,972,972,971,0,986,1016],
[1035,1011,993,1031,978,997,1007,1005,1014,0,1041],
[1004,969,1005,1007,993,995,1006,986,984,959,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 50, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1012,997,1010,1017,1032,1027,1022,1004,1031,1014],
[988,0,1002,996,1025,993,1000,993,980,1007,990],
[1003,998,0,1032,1010,994,993,999,1003,979,999],
[990,1004,968,0,1020,1017,1015,994,968,997,999],
[983,975,990,980,0,1017,999,980,980,985,998],
[968,1007,1006,983,983,0,980,996,989,1003,997],
[973,1000,1007,985,1001,1020,0,981,964,996,982],
[978,1007,1001,1006,1020,1004,1019,0,996,1007,995],
[996,1020,997,1032,1020,1011,1036,1004,0,1012,987],
[969,993,1021,1003,1015,997,1004,993,988,0,996],
[986,1010,1001,1001,1002,1003,1018,1005,1013,1004,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 51, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1026,980,1011,993,980,1009,1011,1016,974,1041],
[974,0,996,1017,999,967,989,1008,986,977,1007],
[1020,1004,0,988,1010,1008,991,989,998,980,989],
[989,983,1012,0,992,981,1004,994,998,983,1032],
[1007,1001,990,1008,0,985,984,1009,1010,987,1005],
[1020,1033,992,1019,1015,0,999,1031,986,1009,1023],
[991,1011,1009,996,1016,1001,0,1031,1015,987,996],
[989,992,1011,1006,991,969,969,0,985,988,1028],
[984,1014,1002,1002,990,1014,985,1015,0,1014,1013],
[1026,1023,1020,1017,1013,991,1013,1012,986,0,1049],
[959,993,1011,968,995,977,1004,972,987,951,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 52, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1018,1029,1035,1004,982,1009,1030,1025,1013,1035],
[982,0,1002,993,1001,976,1031,1023,1007,1009,1025],
[971,998,0,1012,1021,995,983,1036,986,1001,1022],
[965,1007,988,0,1014,979,1012,1052,1018,984,1017],
[996,999,979,986,0,991,987,1038,1016,964,1015],
[1018,1024,1005,1021,1009,0,989,1019,1046,990,1005],
[991,969,1017,988,1013,1011,0,1046,997,960,1023],
[970,977,964,948,962,981,954,0,974,952,1005],
[975,993,1014,982,984,954,1003,1026,0,950,1024],
[987,991,999,1016,1036,1010,1040,1048,1050,0,1036],
[965,975,978,983,985,995,977,995,976,964,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 53, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1027,1005,1018,1050,999,1022,992,1019,1074,1013],
[973,0,977,934,1048,1018,986,980,950,982,1004],
[995,1023,0,1004,1083,1021,1026,1053,1042,1052,1071],
[982,1066,996,0,1050,986,1010,1034,1042,999,1032],
[950,952,917,950,0,985,953,960,957,976,1015],
[1001,982,979,1014,1015,0,1010,1037,943,1004,1093],
[978,1014,974,990,1047,990,0,1036,982,1009,1043],
[1008,1020,947,966,1040,963,964,0,1061,991,1028],
[981,1050,958,958,1043,1057,1018,939,0,1009,1037],
[926,1018,948,1001,1024,996,991,1009,991,0,1001],
[987,996,929,968,985,907,957,972,963,999,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 54, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1014,995,989,999,1016,997,1005,1008,984,981],
[986,0,939,983,985,967,980,986,990,962,977],
[1005,1061,0,990,1011,1004,1009,1002,1014,1006,1006],
[1011,1017,1010,0,1001,999,966,1010,1005,1006,988],
[1001,1015,989,999,0,1005,974,1001,1019,992,981],
[984,1033,996,1001,995,0,987,985,1013,984,981],
[1003,1020,991,1034,1026,1013,0,1026,1017,998,1004],
[995,1014,998,990,999,1015,974,0,1022,975,1011],
[992,1010,986,995,981,987,983,978,0,987,1012],
[1016,1038,994,994,1008,1016,1002,1025,1013,0,1022],
[1019,1023,994,1012,1019,1019,996,989,988,978,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 55, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1005,1025,989,1080,1020,1013,1024,1004,1002,983],
[995,0,1025,1028,1044,1034,1062,1032,1007,1023,1047],
[975,975,0,1014,965,987,997,1047,964,1017,1046],
[1011,972,986,0,1018,984,1024,1042,1003,1019,1014],
[920,956,1035,982,0,918,991,1025,1026,951,971],
[980,966,1013,1016,1082,0,1086,1045,1025,1016,1046],
[987,938,1003,976,1009,914,0,964,1012,977,985],
[976,968,953,958,975,955,1036,0,1006,957,984],
[996,993,1036,997,974,975,988,994,0,1026,1006],
[998,977,983,981,1049,984,1023,1043,974,0,978],
[1017,953,954,986,1029,954,1015,1016,994,1022,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 56, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1020,1000,981,1018,1003,977,958,1007,993,1024],
[980,0,1002,1031,998,1013,992,1012,1000,1014,1008],
[1000,998,0,1021,993,1007,996,1022,1050,965,995],
[1019,969,979,0,1007,1036,987,953,1012,998,983],
[982,1002,1007,993,0,1014,999,986,1037,985,972],
[997,987,993,964,986,0,994,987,1021,998,1014],
[1023,1008,1004,1013,1001,1006,0,1010,1009,1029,990],
[1042,988,978,1047,1014,1013,990,0,1022,1043,1003],
[993,1000,950,988,963,979,991,978,0,983,978],
[1007,986,1035,1002,1015,1002,971,957,1017,0,971],
[976,992,1005,1017,1028,986,1010,997,1022,1029,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 57, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,917,948,1023,1019,953,981,980,1000,940,987],
[1083,0,1030,1040,1020,981,1005,1004,1007,978,1059],
[1052,970,0,1028,1023,926,978,1006,1001,988,1027],
[977,960,972,0,988,992,976,984,1011,1011,1009],
[981,980,977,1012,0,989,975,970,999,962,1012],
[1047,1019,1074,1008,1011,0,1007,990,1022,1060,1085],
[1019,995,1022,1024,1025,993,0,981,993,1015,1022],
[1020,996,994,1016,1030,1010,1019,0,999,1016,1014],
[1000,993,999,989,1001,978,1007,1001,0,981,1046],
[1060,1022,1012,989,1038,940,985,984,1019,0,1065],
[1013,941,973,991,988,915,978,986,954,935,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 58, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,992,1009,984,966,974,989,1002,967,1025,1033],
[1008,0,978,1042,967,1028,1016,1022,990,1019,1045],
[991,1022,0,958,954,1023,984,1068,971,1019,1006],
[1016,958,1042,0,1014,1029,964,1008,961,1012,1047],
[1034,1033,1046,986,0,1060,1028,1066,1017,1035,1046],
[1026,972,977,971,940,0,999,998,971,992,990],
[1011,984,1016,1036,972,1001,0,1067,991,1039,1036],
[998,978,932,992,934,1002,933,0,967,1062,936],
[1033,1010,1029,1039,983,1029,1009,1033,0,1025,1057],
[975,981,981,988,965,1008,961,938,975,0,1010],
[967,955,994,953,954,1010,964,1064,943,990,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 59, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,988,1010,1029,1027,1013,994,1038,1001,997,978],
[1012,0,1014,1007,994,1013,993,996,983,986,1004],
[990,986,0,1006,999,1022,978,998,997,990,980],
[971,993,994,0,1001,1003,974,984,973,979,982],
[973,1006,1001,999,0,1011,995,1002,976,997,1010],
[987,987,978,997,989,0,980,980,970,952,1001],
[1006,1007,1022,1026,1005,1020,0,1036,1002,985,1018],
[962,1004,1002,1016,998,1020,964,0,960,1012,976],
[999,1017,1003,1027,1024,1030,998,1040,0,1000,1013],
[1003,1014,1010,1021,1003,1048,1015,988,1000,0,997],
[1022,996,1020,1018,990,999,982,1024,987,1003,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 60, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1027,987,955,1021,988,979,1026,1017,970,969],
[973,0,995,970,981,981,979,993,950,1019,966],
[1013,1005,0,985,995,1003,945,1033,944,1019,956],
[1045,1030,1015,0,1013,990,974,1018,981,1046,997],
[979,1019,1005,987,0,1015,966,976,944,1000,968],
[1012,1019,997,1010,985,0,981,1016,987,1033,1008],
[1021,1021,1055,1026,1034,1019,0,1063,999,1025,978],
[974,1007,967,982,1024,984,937,0,971,1024,956],
[983,1050,1056,1019,1056,1013,1001,1029,0,1056,987],
[1030,981,981,954,1000,967,975,976,944,0,931],
[1031,1034,1044,1003,1032,992,1022,1044,1013,1069,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 61, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,910,963,929,1060,937,961,951,932,979,957],
[1090,0,995,1002,1090,978,993,1000,1014,1013,1037],
[1037,1005,0,943,1138,1005,979,973,1054,994,1051],
[1071,998,1057,0,1076,1066,1034,943,1038,1043,1067],
[940,910,862,924,0,920,928,860,936,912,952],
[1063,1022,995,934,1080,0,960,956,971,973,1006],
[1039,1007,1021,966,1072,1040,0,939,1037,985,1047],
[1049,1000,1027,1057,1140,1044,1061,0,1037,1083,1108],
[1068,986,946,962,1064,1029,963,963,0,958,1014],
[1021,987,1006,957,1088,1027,1015,917,1042,0,1049],
[1043,963,949,933,1048,994,953,892,986,951,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 62, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1023,931,990,882,942,997,884,893,894,1016],
[977,0,968,881,968,968,906,863,935,929,925],
[1069,1032,0,1076,984,991,1061,900,1024,930,1113],
[1010,1119,924,0,1068,1038,1021,941,982,984,1067],
[1118,1032,1016,932,0,982,1058,1001,973,1104,986],
[1058,1032,1009,962,1018,0,1076,1024,836,887,1019],
[1003,1094,939,979,942,924,0,882,927,911,1084],
[1116,1137,1100,1059,999,976,1118,0,952,1004,1166],
[1107,1065,976,1018,1027,1164,1073,1048,0,1033,1083],
[1106,1071,1070,1016,896,1113,1089,996,967,0,1036],
[984,1075,887,933,1014,981,916,834,917,964,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 63, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,983,1006,1017,1034,1058,1013,1014,1022,1049,1039],
[1017,0,1017,1070,1046,1005,1032,1042,1024,997,1009],
[994,983,0,992,975,1013,1030,1017,1006,1022,980],
[983,930,1008,0,930,1006,980,1003,1039,1017,992],
[966,954,1025,1070,0,1016,1028,976,1026,971,1028],
[942,995,987,994,984,0,971,973,1023,1002,1031],
[987,968,970,1020,972,1029,0,1031,1025,995,1017],
[986,958,983,997,1024,1027,969,0,988,1025,1005],
[978,976,994,961,974,977,975,1012,0,957,994],
[951,1003,978,983,1029,998,1005,975,1043,0,1019],
[961,991,1020,1008,972,969,983,995,1006,981,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 64, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1023,1028,1013,1042,983,1009,976,993,1004,1045],
[977,0,1016,1010,1024,981,1018,983,1001,1021,1039],
[972,984,0,970,1005,953,951,977,943,970,1027],
[987,990,1030,0,1053,1000,1013,1003,1002,1020,1042],
[958,976,995,947,0,950,993,956,936,958,1020],
[1017,1019,1047,1000,1050,0,1032,996,1004,1036,1071],
[991,982,1049,987,1007,968,0,1009,967,1006,1044],
[1024,1017,1023,997,1044,1004,991,0,1002,1020,1063],
[1007,999,1057,998,1064,996,1033,998,0,1044,1061],
[996,979,1030,980,1042,964,994,980,956,0,1042],
[955,961,973,958,980,929,956,937,939,958,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 65, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1054,1006,1019,1005,1011,1018,1016,1030,1049,993],
[946,0,989,1001,985,1009,982,993,981,969,989],
[994,1011,0,1032,1002,1054,1029,1015,1007,1028,1015],
[981,999,968,0,1009,1037,992,1000,957,1004,992],
[995,1015,998,991,0,1017,979,975,985,1018,991],
[989,991,946,963,983,0,998,979,976,1003,965],
[982,1018,971,1008,1021,1002,0,1006,1001,1021,1003],
[984,1007,985,1000,1025,1021,994,0,997,997,990],
[970,1019,993,1043,1015,1024,999,1003,0,1030,997],
[951,1031,972,996,982,997,979,1003,970,0,980],
[1007,1011,985,1008,1009,1035,997,1010,1003,1020,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 66, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,979,997,933,943,1002,987,1019,966,970,978],
[1021,0,999,979,1034,1047,989,987,981,988,976],
[1003,1001,0,1012,1012,988,976,984,1009,969,999],
[1067,1021,988,0,1012,1067,1000,992,984,983,1009],
[1057,966,988,988,0,1011,1025,956,957,1012,904],
[998,953,1012,933,989,0,998,971,969,1001,937],
[1013,1011,1024,1000,975,1002,0,944,952,927,943],
[981,1013,1016,1008,1044,1029,1056,0,1037,991,966],
[1034,1019,991,1016,1043,1031,1048,963,0,1009,1005],
[1030,1012,1031,1017,988,999,1073,1009,991,0,951],
[1022,1024,1001,991,1096,1063,1057,1034,995,1049,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 67, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,995,960,1029,1007,1023,957,965,1003,967,991],
[1005,0,970,1055,1014,1071,994,998,1009,991,976],
[1040,1030,0,1063,999,991,1002,1009,1018,1012,1035],
[971,945,937,0,983,996,919,959,983,987,939],
[993,986,1001,1017,0,1004,993,1001,1003,997,980],
[977,929,1009,1004,996,0,1000,986,1016,1017,1025],
[1043,1006,998,1081,1007,1000,0,1015,990,1001,968],
[1035,1002,991,1041,999,1014,985,0,1027,1055,978],
[997,991,982,1017,997,984,1010,973,0,1048,1014],
[1033,1009,988,1013,1003,983,999,945,952,0,974],
[1009,1024,965,1061,1020,975,1032,1022,986,1026,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 68, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,978,975,951,997,952,1002,953,1096,899,986],
[1022,0,1069,1017,999,956,1052,1022,1067,977,1017],
[1025,931,0,939,967,942,1016,992,1039,960,933],
[1049,983,1061,0,1019,1008,1042,1006,1037,936,991],
[1003,1001,1033,981,0,986,1013,1069,982,1003,970],
[1048,1044,1058,992,1014,0,1102,1013,1051,969,1067],
[998,948,984,958,987,898,0,927,976,954,930],
[1047,978,1008,994,931,987,1073,0,1027,965,953],
[904,933,961,963,1018,949,1024,973,0,914,933],
[1101,1023,1040,1064,997,1031,1046,1035,1086,0,986],
[1014,983,1067,1009,1030,933,1070,1047,1067,1014,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 69, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1012,1027,956,1025,1011,1032,1079,987,984,950],
[988,0,905,926,1007,920,945,1007,880,885,932],
[973,1095,0,1027,1029,1067,992,1041,1008,1010,953],
[1044,1074,973,0,1027,1031,1007,1049,955,1046,960],
[975,993,971,973,0,1047,970,1002,1024,984,982],
[989,1080,933,969,953,0,993,1021,899,939,928],
[968,1055,1008,993,1030,1007,0,1066,971,963,954],
[921,993,959,951,998,979,934,0,871,932,890],
[1013,1120,992,1045,976,1101,1029,1129,0,993,1006],
[1016,1115,990,954,1016,1061,1037,1068,1007,0,962],
[1050,1068,1047,1040,1018,1072,1046,1110,994,1038,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 70, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1012,1035,969,1029,1048,974,1065,1099,1055,948],
[988,0,996,918,1026,1028,1014,1047,1043,1004,963],
[965,1004,0,1023,1025,1031,935,1044,998,1055,1001],
[1031,1082,977,0,1035,1045,982,1072,1065,1031,1036],
[971,974,975,965,0,1010,938,1034,1004,961,944],
[952,972,969,955,990,0,971,992,1018,1042,968],
[1026,986,1065,1018,1062,1029,0,1085,1057,1054,994],
[935,953,956,928,966,1008,915,0,947,998,902],
[901,957,1002,935,996,982,943,1053,0,1002,956],
[945,996,945,969,1039,958,946,1002,998,0,942],
[1052,1037,999,964,1056,1032,1006,1098,1044,1058,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 71, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,988,1036,981,985,972,1015,1070,985,1061,963],
[1012,0,1085,1010,1024,1038,974,1047,997,986,992],
[964,915,0,984,1015,975,936,946,954,997,930],
[1019,990,1016,0,1062,1064,997,1026,978,1045,972],
[1015,976,985,938,0,980,1007,1027,958,1027,977],
[1028,962,1025,936,1020,0,978,1030,980,1042,958],
[985,1026,1064,1003,993,1022,0,1087,1014,1059,1004],
[930,953,1054,974,973,970,913,0,878,931,967],
[1015,1003,1046,1022,1042,1020,986,1122,0,976,1022],
[939,1014,1003,955,973,958,941,1069,1024,0,1012],
[1037,1008,1070,1028,1023,1042,996,1033,978,988,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 72, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1012,984,993,995,997,969,1025,977,993,982],
[988,0,1026,1004,1059,1015,979,1036,1005,986,969],
[1016,974,0,981,1041,1018,1028,1014,1003,1040,994],
[1007,996,1019,0,1021,1039,950,1005,987,958,1018],
[1005,941,959,979,0,970,895,988,967,1014,968],
[1003,985,982,961,1030,0,953,986,964,992,952],
[1031,1021,972,1050,1105,1047,0,1058,1028,1071,1031],
[975,964,986,995,1012,1014,942,0,972,979,998],
[1023,995,997,1013,1033,1036,972,1028,0,1050,1033],
[1007,1014,960,1042,986,1008,929,1021,950,0,997],
[1018,1031,1006,982,1032,1048,969,1002,967,1003,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 73, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1006,1017,997,1025,973,1012,985,962,1036,1012],
[994,0,1010,979,958,977,996,972,985,984,992],
[983,990,0,971,972,1003,1005,973,955,964,985],
[1003,1021,1029,0,1018,988,1012,992,1014,1013,1015],
[975,1042,1028,982,0,964,1063,972,1005,995,1001],
[1027,1023,997,1012,1036,0,1021,1002,978,981,951],
[988,1004,995,988,937,979,0,956,1002,956,973],
[1015,1028,1027,1008,1028,998,1044,0,988,1003,971],
[1038,1015,1045,986,995,1022,998,1012,0,984,997],
[964,1016,1036,987,1005,1019,1044,997,1016,0,968],
[988,1008,1015,985,999,1049,1027,1029,1003,1032,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 74, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1044,1047,1022,1050,1035,1048,989,1003,1057,1073],
[956,0,1026,1006,1042,961,981,966,1002,1007,1013],
[953,974,0,994,990,993,974,954,965,954,1033],
[978,994,1006,0,1036,978,978,966,967,1033,1042],
[950,958,1010,964,0,999,1010,973,969,992,1045],
[965,1039,1007,1022,1001,0,964,958,968,1035,1031],
[952,1019,1026,1022,990,1036,0,1004,941,992,1027],
[1011,1034,1046,1034,1027,1042,996,0,961,1014,1074],
[997,998,1035,1033,1031,1032,1059,1039,0,1020,1062],
[943,993,1046,967,1008,965,1008,986,980,0,1032],
[927,987,967,958,955,969,973,926,938,968,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 75, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,990,1201,1106,1064,1145,1190,1062,1243,1149,1020],
[1010,0,1321,1057,1303,1379,1226,927,1408,1127,1204],
[799,679,0,676,973,868,931,590,987,750,967],
[894,943,1324,0,1169,1204,1154,910,1292,1119,1283],
[936,697,1027,831,0,1198,1098,853,1140,927,1011],
[855,621,1132,796,802,0,1116,949,1099,957,1249],
[810,774,1069,846,902,884,0,788,947,945,1041],
[938,1073,1410,1090,1147,1051,1212,0,1482,1047,1179],
[757,592,1013,708,860,901,1053,518,0,990,1050],
[851,873,1250,881,1073,1043,1055,953,1010,0,1239],
[980,796,1033,717,989,751,959,821,950,761,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 76, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,987,988,1025,1036,988,1017,1012,1009,984,1007],
[1013,0,1008,1053,1030,1019,1012,1032,1023,1015,997],
[1012,992,0,992,1041,986,1001,979,999,961,967],
[975,947,1008,0,1020,950,1024,1005,1024,938,992],
[964,970,959,980,0,949,965,985,966,945,976],
[1012,981,1014,1050,1051,0,1047,1048,1032,976,1003],
[983,988,999,976,1035,953,0,978,985,937,957],
[988,968,1021,995,1015,952,1022,0,998,935,974],
[991,977,1001,976,1034,968,1015,1002,0,939,987],
[1016,985,1039,1062,1055,1024,1063,1065,1061,0,1002],
[993,1003,1033,1008,1024,997,1043,1026,1013,998,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 77, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,946,957,982,937,982,987,950,973,960,986],
[1054,0,972,984,997,981,992,962,1001,1024,983],
[1043,1028,0,1042,989,1027,986,1025,1045,1017,1040],
[1018,1016,958,0,981,980,972,1004,1015,1012,1010],
[1063,1003,1011,1019,0,999,1004,976,1031,972,1010],
[1018,1019,973,1020,1001,0,1018,1006,1014,973,1015],
[1013,1008,1014,1028,996,982,0,988,1040,994,1012],
[1050,1038,975,996,1024,994,1012,0,1012,973,1033],
[1027,999,955,985,969,986,960,988,0,979,975],
[1040,976,983,988,1028,1027,1006,1027,1021,0,1032],
[1014,1017,960,990,990,985,988,967,1025,968,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 78, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1008,979,1000,996,1008,989,992,1050,991,1011],
[992,0,984,1003,1001,993,992,937,1012,990,1038],
[1021,1016,0,1050,1014,1025,1009,990,1025,1026,1049],
[1000,997,950,0,1010,1011,1007,970,1024,1007,1016],
[1004,999,986,990,0,964,995,991,1014,977,1024],
[992,1007,975,989,1036,0,956,981,1020,1008,1013],
[1011,1008,991,993,1005,1044,0,1000,1078,997,1051],
[1008,1063,1010,1030,1009,1019,1000,0,1015,1016,1037],
[950,988,975,976,986,980,922,985,0,984,1007],
[1009,1010,974,993,1023,992,1003,984,1016,0,1022],
[989,962,951,984,976,987,949,963,993,978,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 79, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,914,1043,896,710,864,775,922,880,863,818],
[1086,0,1107,1085,1067,968,1091,1016,1041,965,1028],
[957,893,0,833,914,844,915,891,797,903,858],
[1104,915,1167,0,926,931,1037,1103,981,986,926],
[1290,933,1086,1074,0,1061,1069,1024,1024,964,904],
[1136,1032,1156,1069,939,0,873,1105,918,992,940],
[1225,909,1085,963,931,1127,0,1116,1043,1094,1035],
[1078,984,1109,897,976,895,884,0,951,896,886],
[1120,959,1203,1019,976,1082,957,1049,0,973,997],
[1137,1035,1097,1014,1036,1008,906,1104,1027,0,876],
[1182,972,1142,1074,1096,1060,965,1114,1003,1124,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 80, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,951,984,1043,991,1043,1005,1004,982,1035,1015],
[1049,0,970,1067,1048,1058,1012,1059,1069,1010,1067],
[1016,1030,0,1065,1085,1049,997,1059,1025,1042,1050],
[957,933,935,0,984,1028,879,979,981,973,980],
[1009,952,915,1016,0,1003,983,995,972,973,997],
[957,942,951,972,997,0,950,1026,985,978,1006],
[995,988,1003,1121,1017,1050,0,1053,1007,1050,1015],
[996,941,941,1021,1005,974,947,0,994,1023,990],
[1018,931,975,1019,1028,1015,993,1006,0,1022,1004],
[965,990,958,1027,1027,1022,950,977,978,0,985],
[985,933,950,1020,1003,994,985,1010,996,1015,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 81, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1091,1023,1085,1013,995,1077,1081,1019,1042,1044],
[909,0,989,960,935,962,978,843,910,953,953],
[977,1011,0,975,991,981,971,888,1076,977,930],
[915,1040,1025,0,973,962,1073,1001,981,1073,995],
[987,1065,1009,1027,0,969,1015,874,1009,1043,1029],
[1005,1038,1019,1038,1031,0,1078,967,1071,1095,958],
[923,1022,1029,927,985,922,0,937,921,1050,995],
[919,1157,1112,999,1126,1033,1063,0,1012,1084,1041],
[981,1090,924,1019,991,929,1079,988,0,1030,930],
[958,1047,1023,927,957,905,950,916,970,0,928],
[956,1047,1070,1005,971,1042,1005,959,1070,1072,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 82, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1016,1008,1096,1004,950,989,1095,1007,1090,963],
[984,0,1033,1069,1068,974,945,1077,1019,1132,961],
[992,967,0,1062,1033,1033,929,923,970,1055,983],
[904,931,938,0,999,878,989,968,1004,1034,946],
[996,932,967,1001,0,967,932,1061,996,992,994],
[1050,1026,967,1122,1033,0,948,1136,1080,1139,1008],
[1011,1055,1071,1011,1068,1052,0,1025,969,1069,990],
[905,923,1077,1032,939,864,975,0,947,951,930],
[993,981,1030,996,1004,920,1031,1053,0,1073,928],
[910,868,945,966,1008,861,931,1049,927,0,1011],
[1037,1039,1017,1054,1006,992,1010,1070,1072,989,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 83, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,998,1022,1002,1027,1000,1035,946,964,972,966],
[1002,0,1009,983,1043,1023,1001,988,996,989,987],
[978,991,0,968,969,1036,961,933,941,968,977],
[998,1017,1032,0,1064,1013,973,1010,959,982,1041],
[973,957,1031,936,0,988,988,976,972,978,988],
[1000,977,964,987,1012,0,998,978,969,984,996],
[965,999,1039,1027,1012,1002,0,957,996,1010,1002],
[1054,1012,1067,990,1024,1022,1043,0,1006,1040,1031],
[1036,1004,1059,1041,1028,1031,1004,994,0,1034,1031],
[1028,1011,1032,1018,1022,1016,990,960,966,0,1013],
[1034,1013,1023,959,1012,1004,998,969,969,987,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 84, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,987,985,959,972,957,982,1026,988,983,999],
[1013,0,960,993,969,987,1009,980,1021,942,1004],
[1015,1040,0,981,1009,1007,964,998,1018,990,1028],
[1041,1007,1019,0,986,1026,1042,1035,997,1029,1030],
[1028,1031,991,1014,0,1031,1005,997,1001,970,1028],
[1043,1013,993,974,969,0,988,1030,996,943,1026],
[1018,991,1036,958,995,1012,0,1003,1001,950,1012],
[974,1020,1002,965,1003,970,997,0,982,975,1009],
[1012,979,982,1003,999,1004,999,1018,0,1009,1013],
[1017,1058,1010,971,1030,1057,1050,1025,991,0,1032],
[1001,996,972,970,972,974,988,991,987,968,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 85, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,921,966,936,1009,1012,997,929,976,957,937],
[1079,0,991,1012,1028,1055,1038,1009,1025,1068,1007],
[1034,1009,0,959,1046,1021,998,1031,1039,1039,977],
[1064,988,1041,0,1018,1047,1053,1007,1021,975,1023],
[991,972,954,982,0,1055,1016,981,988,977,975],
[988,945,979,953,945,0,973,960,948,928,977],
[1003,962,1002,947,984,1027,0,969,994,1025,990],
[1071,991,969,993,1019,1040,1031,0,1001,984,979],
[1024,975,961,979,1012,1052,1006,999,0,994,988],
[1043,932,961,1025,1023,1072,975,1016,1006,0,1011],
[1063,993,1023,977,1025,1023,1010,1021,1012,989,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 86, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,946,1031,992,1014,1007,933,966,951,1018,1062],
[1054,0,1024,1076,965,1047,1001,999,1012,1051,1054],
[969,976,0,1023,1007,1048,989,979,1004,1013,1029],
[1008,924,977,0,999,1069,990,955,1006,1048,1027],
[986,1035,993,1001,0,1055,980,940,980,1006,1060],
[993,953,952,931,945,0,914,940,947,973,1008],
[1067,999,1011,1010,1020,1086,0,1002,1045,1037,1105],
[1034,1001,1021,1045,1060,1060,998,0,980,1054,1087],
[1049,988,996,994,1020,1053,955,1020,0,1024,1026],
[982,949,987,952,994,1027,963,946,976,0,1078],
[938,946,971,973,940,992,895,913,974,922,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 87, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,994,1020,960,821,827,961,1126,808,752,1230],
[1006,0,992,981,750,921,1048,1164,944,979,1231],
[980,1008,0,994,914,1055,1144,1136,1001,1069,1213],
[1040,1019,1006,0,894,875,1033,1159,995,992,1136],
[1179,1250,1086,1106,0,1080,1171,1219,1004,943,1130],
[1173,1079,945,1125,920,0,1020,1321,927,962,1112],
[1039,952,856,967,829,980,0,1023,857,883,1115],
[874,836,864,841,781,679,977,0,824,790,1136],
[1192,1056,999,1005,996,1073,1143,1176,0,1099,1154],
[1248,1021,931,1008,1057,1038,1117,1210,901,0,1176],
[770,769,787,864,870,888,885,864,846,824,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 88, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,942,926,966,923,941,961,973,945,917,958],
[1058,0,1042,1012,971,967,1017,1028,956,991,1018],
[1074,958,0,977,955,972,973,1001,985,958,1038],
[1034,988,1023,0,986,975,1005,1040,983,996,1033],
[1077,1029,1045,1014,0,1014,1018,1004,997,997,1031],
[1059,1033,1028,1025,986,0,1027,1030,1021,1007,1048],
[1039,983,1027,995,982,973,0,998,972,953,1029],
[1027,972,999,960,996,970,1002,0,986,944,985],
[1055,1044,1015,1017,1003,979,1028,1014,0,1028,1076],
[1083,1009,1042,1004,1003,993,1047,1056,972,0,1048],
[1042,982,962,967,969,952,971,1015,924,952,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 89, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,980,994,1027,978,1027,990,955,993,986,1018],
[1020,0,980,1022,957,1032,1016,972,954,1009,1048],
[1006,1020,0,1034,972,1067,1022,973,983,1015,997],
[973,978,966,0,971,1012,982,972,979,970,1009],
[1022,1043,1028,1029,0,1014,1024,1008,980,979,1031],
[973,968,933,988,986,0,950,995,983,996,976],
[1010,984,978,1018,976,1050,0,984,989,1001,971],
[1045,1028,1027,1028,992,1005,1016,0,997,1022,1038],
[1007,1046,1017,1021,1020,1017,1011,1003,0,993,969],
[1014,991,985,1030,1021,1004,999,978,1007,0,964],
[982,952,1003,991,969,1024,1029,962,1031,1036,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 90, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1006,1064,1018,1019,1022,1055,1066,1019,975,1041],
[994,0,963,1054,1002,1024,989,1076,1022,1031,983],
[936,1037,0,1001,999,1047,999,1014,1021,1003,996],
[982,946,999,0,1031,1006,950,1023,981,973,1008],
[981,998,1001,969,0,977,943,999,1002,956,964],
[978,976,953,994,1023,0,1004,1012,1009,1007,995],
[945,1011,1001,1050,1057,996,0,1077,1029,1015,999],
[934,924,986,977,1001,988,923,0,970,912,965],
[981,978,979,1019,998,991,971,1030,0,929,1005],
[1025,969,997,1027,1044,993,985,1088,1071,0,1023],
[959,1017,1004,992,1036,1005,1001,1035,995,977,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 91, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,925,928,1011,1012,978,1031,988,962,1060,962],
[1075,0,1034,1082,1122,1036,1050,1019,1047,1068,969],
[1072,966,0,1023,1032,952,1009,1015,1044,997,944],
[989,918,977,0,1076,961,1067,972,958,1061,976],
[988,878,968,924,0,965,978,1005,937,993,973],
[1022,964,1048,1039,1035,0,1019,991,1047,1002,1003],
[969,950,991,933,1022,981,0,942,989,1059,969],
[1012,981,985,1028,995,1009,1058,0,1007,1048,1009],
[1038,953,956,1042,1063,953,1011,993,0,980,1041],
[940,932,1003,939,1007,998,941,952,1020,0,914],
[1038,1031,1056,1024,1027,997,1031,991,959,1086,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 92, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1020,1025,1001,1025,1031,996,979,1041,991,1013],
[980,0,970,1002,994,1014,979,969,984,967,977],
[975,1030,0,998,996,983,974,950,1017,996,993],
[999,998,1002,0,943,984,934,956,992,974,942],
[975,1006,1004,1057,0,1020,1018,991,1014,993,989],
[969,986,1017,1016,980,0,974,985,1002,967,971],
[1004,1021,1026,1066,982,1026,0,978,1046,979,972],
[1021,1031,1050,1044,1009,1015,1022,0,1034,1013,984],
[959,1016,983,1008,986,998,954,966,0,951,970],
[1009,1033,1004,1026,1007,1033,1021,987,1049,0,976],
[987,1023,1007,1058,1011,1029,1028,1016,1030,1024,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 93, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,993,949,980,972,1009,1022,983,930,1012,1037],
[1007,0,978,1005,956,1002,1037,970,961,981,1056],
[1051,1022,0,1026,1005,1031,1044,1015,972,982,1015],
[1020,995,974,0,950,992,1035,975,1010,1011,1009],
[1028,1044,995,1050,0,1061,1033,1027,973,986,1010],
[991,998,969,1008,939,0,1005,1001,983,1000,1021],
[978,963,956,965,967,995,0,958,970,938,1003],
[1017,1030,985,1025,973,999,1042,0,1008,998,1022],
[1070,1039,1028,990,1027,1017,1030,992,0,1073,1006],
[988,1019,1018,989,1014,1000,1062,1002,927,0,1029],
[963,944,985,991,990,979,997,978,994,971,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 94, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,946,969,1003,980,977,983,990,986,954,968],
[1054,0,977,1013,1004,999,992,980,1001,990,991],
[1031,1023,0,1025,1008,1007,1046,989,1002,995,1031],
[997,987,975,0,979,1002,986,1022,997,1011,1007],
[1020,996,992,1021,0,1007,976,1023,997,984,1016],
[1023,1001,993,998,993,0,1005,974,977,982,1025],
[1017,1008,954,1014,1024,995,0,1009,973,992,1013],
[1010,1020,1011,978,977,1026,991,0,992,1002,1006],
[1014,999,998,1003,1003,1023,1027,1008,0,975,987],
[1046,1010,1005,989,1016,1018,1008,998,1025,0,1025],
[1032,1009,969,993,984,975,987,994,1013,975,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 95, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1066,1172,597,1011,1128,1145,1082,894,1122,928],
[934,0,790,815,1079,885,1135,1067,553,718,1213],
[828,1210,0,893,1247,1180,1205,858,804,852,956],
[1403,1185,1107,0,1165,1115,1657,1508,978,1050,1230],
[989,921,753,835,0,1144,1194,1033,926,863,941],
[872,1115,820,885,856,0,1217,1198,720,829,1054],
[855,865,795,343,806,783,0,893,649,803,945],
[918,933,1142,492,967,802,1107,0,808,882,801],
[1106,1447,1196,1022,1074,1280,1351,1192,0,1005,992],
[878,1282,1148,950,1137,1171,1197,1118,995,0,1023],
[1072,787,1044,770,1059,946,1055,1199,1008,977,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 96, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,984,997,1022,1006,980,987,1054,1011,1034,1024],
[1016,0,1002,1038,1025,986,1034,1047,1010,1031,1026],
[1003,998,0,1003,1015,975,1021,1024,1000,1025,988],
[978,962,997,0,985,987,992,1026,999,1007,1030],
[994,975,985,1015,0,1000,1030,1050,1013,1037,1050],
[1020,1014,1025,1013,1000,0,1030,1038,989,1027,1068],
[1013,966,979,1008,970,970,0,1006,999,994,1019],
[946,953,976,974,950,962,994,0,977,998,1002],
[989,990,1000,1001,987,1011,1001,1023,0,994,1009],
[966,969,975,993,963,973,1006,1002,1006,0,1010],
[976,974,1012,970,950,932,981,998,991,990,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 97, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,923,999,939,897,986,967,932,958,959,976],
[1077,0,1078,1052,1037,1070,989,1061,1070,1004,1057],
[1001,922,0,980,986,1024,960,1009,1014,934,1040],
[1061,948,1020,0,970,1032,1005,949,1032,982,1057],
[1103,963,1014,1030,0,1061,1045,968,1011,991,1049],
[1014,930,976,968,939,0,944,931,1025,867,1023],
[1033,1011,1040,995,955,1056,0,986,1016,940,1049],
[1068,939,991,1051,1032,1069,1014,0,1015,975,1068],
[1042,930,986,968,989,975,984,985,0,932,1006],
[1041,996,1066,1018,1009,1133,1060,1025,1068,0,1071],
[1024,943,960,943,951,977,951,932,994,929,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 98, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,965,869,884,913,940,882,895,944,948,917],
[1035,0,875,924,892,927,857,1012,928,845,875],
[1131,1125,0,974,1047,1054,972,1048,1007,1050,1043],
[1116,1076,1026,0,1100,1052,1028,970,984,936,972],
[1087,1108,953,900,0,1018,935,1048,988,961,984],
[1060,1073,946,948,982,0,952,1014,980,973,1016],
[1118,1143,1028,972,1065,1048,0,1087,1039,1121,1070],
[1105,988,952,1030,952,986,913,0,988,1011,942],
[1056,1072,993,1016,1012,1020,961,1012,0,1046,1008],
[1052,1155,950,1064,1039,1027,879,989,954,0,1001],
[1083,1125,957,1028,1016,984,930,1058,992,999,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 99, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1020,978,1004,1019,1043,988,960,1027,1006,1029],
[980,0,972,954,1019,996,982,949,983,996,999],
[1022,1028,0,996,1026,1063,990,998,1020,1021,1041],
[996,1046,1004,0,1032,1042,982,1025,1043,1006,1025],
[981,981,974,968,0,995,990,974,1009,969,1031],
[957,1004,937,958,1005,0,983,980,1019,993,984],
[1012,1018,1010,1018,1010,1017,0,977,1015,985,1029],
[1040,1051,1002,975,1026,1020,1023,0,1019,1012,1065],
[973,1017,980,957,991,981,985,981,0,981,1019],
[994,1004,979,994,1031,1007,1015,988,1019,0,1040],
[971,1001,959,975,969,1016,971,935,981,960,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 100, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,980,983,987,953,962,999,994,972,974,1002],
[1020,0,1016,1030,1004,1003,1029,1018,1031,993,1019],
[1017,984,0,1033,1000,1011,994,1026,1024,983,1001],
[1013,970,967,0,995,981,978,1048,976,995,1014],
[1047,996,1000,1005,0,1034,1025,1041,993,1020,1012],
[1038,997,989,1019,966,0,980,1015,1023,974,1016],
[1001,971,1006,1022,975,1020,0,1013,986,1023,1020],
[1006,982,974,952,959,985,987,0,968,953,1001],
[1028,969,976,1024,1007,977,1014,1032,0,981,991],
[1026,1007,1017,1005,980,1026,977,1047,1019,0,1012],
[998,981,999,986,988,984,980,999,1009,988,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 101, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,974,1016,976,1012,992,976,988,1020,997,1000],
[1026,0,997,1013,1010,1029,986,1000,1041,1036,1029],
[984,1003,0,1026,1027,994,978,1001,984,1037,1020],
[1024,987,974,0,1004,1005,986,998,1013,1005,1010],
[988,990,973,996,0,975,957,970,1007,1000,1007],
[1008,971,1006,995,1025,0,1015,1014,1012,1016,1012],
[1024,1014,1022,1014,1043,985,0,1010,1018,1029,1034],
[1012,1000,999,1002,1030,986,990,0,1018,1006,1016],
[980,959,1016,987,993,988,982,982,0,1025,989],
[1003,964,963,995,1000,984,971,994,975,0,977],
[1000,971,980,990,993,988,966,984,1011,1023,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 102, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1021,982,952,979,1005,1009,986,937,1015,979],
[979,0,983,992,1027,1019,1017,968,927,996,1003],
[1018,1017,0,971,1020,995,1042,974,955,1020,989],
[1048,1008,1029,0,1012,1035,1055,1016,1005,1034,997],
[1021,973,980,988,0,1018,1004,992,974,1045,1010],
[995,981,1005,965,982,0,1030,990,952,1052,1000],
[991,983,958,945,996,970,0,947,957,1002,969],
[1014,1032,1026,984,1008,1010,1053,0,971,1036,998],
[1063,1073,1045,995,1026,1048,1043,1029,0,1057,1022],
[985,1004,980,966,955,948,998,964,943,0,992],
[1021,997,1011,1003,990,1000,1031,1002,978,1008,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 103, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,989,982,1004,965,929,951,1024,998,979,981],
[1011,0,1016,1020,1006,939,983,989,1018,1005,1026],
[1018,984,0,956,1006,943,986,989,1009,995,989],
[996,980,1044,0,994,1003,977,991,1000,996,1006],
[1035,994,994,1006,0,935,950,997,1035,997,1011],
[1071,1061,1057,997,1065,0,1034,1026,1047,1079,1048],
[1049,1017,1014,1023,1050,966,0,1061,1037,1017,1022],
[976,1011,1011,1009,1003,974,939,0,966,974,982],
[1002,982,991,1000,965,953,963,1034,0,986,992],
[1021,995,1005,1004,1003,921,983,1026,1014,0,1001],
[1019,974,1011,994,989,952,978,1018,1008,999,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 104, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,914,1017,971,968,1002,903,991,960,1005,965],
[1086,0,1068,1015,1003,1015,1018,982,1050,1046,989],
[983,932,0,965,946,961,927,978,945,957,898],
[1029,985,1035,0,1002,1041,971,966,1011,1018,984],
[1032,997,1054,998,0,1021,967,991,970,1025,974],
[998,985,1039,959,979,0,977,907,1011,973,964],
[1097,982,1073,1029,1033,1023,0,1043,1053,1058,1038],
[1009,1018,1022,1034,1009,1093,957,0,1050,987,963],
[1040,950,1055,989,1030,989,947,950,0,1006,972],
[995,954,1043,982,975,1027,942,1013,994,0,949],
[1035,1011,1102,1016,1026,1036,962,1037,1028,1051,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 105, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1000,1016,1014,981,1018,1028,1029,1009,1033,1002],
[1000,0,1028,1026,997,1049,1027,1031,1017,1034,1040],
[984,972,0,1033,1005,999,1021,999,1015,972,1010],
[986,974,967,0,994,1006,999,1013,1002,984,996],
[1019,1003,995,1006,0,1003,1044,1026,1018,1000,1015],
[982,951,1001,994,997,0,1008,992,983,994,1010],
[972,973,979,1001,956,992,0,983,990,972,1003],
[971,969,1001,987,974,1008,1017,0,989,986,1013],
[991,983,985,998,982,1017,1010,1011,0,990,1014],
[967,966,1028,1016,1000,1006,1028,1014,1010,0,1037],
[998,960,990,1004,985,990,997,987,986,963,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 106, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,990,958,985,1001,974,973,966,970,988,940],
[1010,0,1001,1008,1009,1020,998,983,1027,1000,972],
[1042,999,0,1004,1000,980,1004,977,989,1020,946],
[1015,992,996,0,1006,997,1014,989,1007,1022,981],
[999,991,1000,994,0,981,1012,991,1007,1009,973],
[1026,980,1020,1003,1019,0,1022,991,1008,1003,975],
[1027,1002,996,986,988,978,0,1005,1007,994,1006],
[1034,1017,1023,1011,1009,1009,995,0,998,1028,1004],
[1030,973,1011,993,993,992,993,1002,0,1036,971],
[1012,1000,980,978,991,997,1006,972,964,0,981],
[1060,1028,1054,1019,1027,1025,994,996,1029,1019,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 107, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,996,970,983,986,921,914,988,954,972,1013],
[1004,0,971,955,965,910,998,985,942,1043,998],
[1030,1029,0,1036,958,974,1016,1006,956,1058,1044],
[1017,1045,964,0,1001,950,1026,929,960,1046,1038],
[1014,1035,1042,999,0,983,963,1048,1006,1072,983],
[1079,1090,1026,1050,1017,0,949,1026,958,1094,1038],
[1086,1002,984,974,1037,1051,0,1025,975,1024,1042],
[1012,1015,994,1071,952,974,975,0,951,1044,1015],
[1046,1058,1044,1040,994,1042,1025,1049,0,1030,1016],
[1028,957,942,954,928,906,976,956,970,0,932],
[987,1002,956,962,1017,962,958,985,984,1068,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 108, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1012,1001,1028,1010,1001,981,970,985,992,1005],
[988,0,1036,985,983,1017,995,995,1009,1017,1046],
[999,964,0,1009,972,978,970,1013,1013,997,1040],
[972,1015,991,0,1008,984,953,964,973,1008,1030],
[990,1017,1028,992,0,1009,974,1006,980,1032,1047],
[999,983,1022,1016,991,0,986,1011,980,1003,1025],
[1019,1005,1030,1047,1026,1014,0,1034,1001,995,1023],
[1030,1005,987,1036,994,989,966,0,1009,1071,1063],
[1015,991,987,1027,1020,1020,999,991,0,1003,1072],
[1008,983,1003,992,968,997,1005,929,997,0,1001],
[995,954,960,970,953,975,977,937,928,999,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 109, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,991,882,914,1105,1030,1002,981,971,1000,999],
[1009,0,947,981,1115,1025,952,1037,1034,1004,977],
[1118,1053,0,1020,1177,1046,1017,1000,1080,1059,1112],
[1086,1019,980,0,1085,1081,946,1013,1039,1082,1052],
[895,885,823,915,0,968,903,957,879,907,950],
[970,975,954,919,1032,0,920,996,858,1017,1014],
[998,1048,983,1054,1097,1080,0,1046,1034,1051,1113],
[1019,963,1000,987,1043,1004,954,0,990,1012,1046],
[1029,966,920,961,1121,1142,966,1010,0,994,1069],
[1000,996,941,918,1093,983,949,988,1006,0,942],
[1001,1023,888,948,1050,986,887,954,931,1058,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 110, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,986,1020,1034,1050,1001,1048,989,1006,1014,1036],
[1014,0,998,1052,1049,1013,1049,1018,1030,1049,1017],
[980,1002,0,1031,971,991,1025,964,982,1018,1007],
[966,948,969,0,979,963,993,956,986,983,969],
[950,951,1029,1021,0,987,989,977,996,989,999],
[999,987,1009,1037,1013,0,1012,986,1000,1014,973],
[952,951,975,1007,1011,988,0,942,984,963,995],
[1011,982,1036,1044,1023,1014,1058,0,1028,1021,1018],
[994,970,1018,1014,1004,1000,1016,972,0,1009,996],
[986,951,982,1017,1011,986,1037,979,991,0,987],
[964,983,993,1031,1001,1027,1005,982,1004,1013,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 111, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,972,1016,937,1026,1040,1052,996,966,972,1032],
[1028,0,1081,1042,1043,1124,1041,1054,968,1020,1006],
[984,919,0,1052,960,978,960,949,926,1024,998],
[1063,958,948,0,970,1039,1020,1018,952,1026,886],
[974,957,1040,1030,0,1098,1063,974,1030,970,986],
[960,876,1022,961,902,0,980,910,885,955,901],
[948,959,1040,980,937,1020,0,958,953,993,953],
[1004,946,1051,982,1026,1090,1042,0,1032,1029,999],
[1034,1032,1074,1048,970,1115,1047,968,0,1006,959],
[1028,980,976,974,1030,1045,1007,971,994,0,957],
[968,994,1002,1114,1014,1099,1047,1001,1041,1043,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 112, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1089,1058,1035,1057,1105,1004,993,1064,992,987],
[911,0,1053,1021,1020,994,999,951,1012,967,1013],
[942,947,0,978,991,954,984,917,982,930,993],
[965,979,1022,0,1051,1060,1073,1007,1043,957,1010],
[943,980,1009,949,0,949,1029,944,1020,937,973],
[895,1006,1046,940,1051,0,1001,1048,1018,994,1039],
[996,1001,1016,927,971,999,0,967,1020,943,1034],
[1007,1049,1083,993,1056,952,1033,0,998,1018,1030],
[936,988,1018,957,980,982,980,1002,0,981,977],
[1008,1033,1070,1043,1063,1006,1057,982,1019,0,1004],
[1013,987,1007,990,1027,961,966,970,1023,996,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 113, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,976,951,1007,953,955,990,944,962,971,971],
[1024,0,975,986,986,960,985,988,958,985,959],
[1049,1025,0,1029,1022,1028,1015,985,984,1035,1021],
[993,1014,971,0,978,953,967,952,927,999,965],
[1047,1014,978,1022,0,996,979,970,970,971,1024],
[1045,1040,972,1047,1004,0,1037,1027,1007,1039,1006],
[1010,1015,985,1033,1021,963,0,993,975,994,1038],
[1056,1012,1015,1048,1030,973,1007,0,1028,1020,1000],
[1038,1042,1016,1073,1030,993,1025,972,0,1030,1040],
[1029,1015,965,1001,1029,961,1006,980,970,0,963],
[1029,1041,979,1035,976,994,962,1000,960,1037,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 114, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,965,1001,1120,993,944,1078,1017,940,1005,962],
[1035,0,976,1157,1053,1042,1114,1092,1050,927,1039],
[999,1024,0,1066,1031,979,1072,1114,1012,863,1093],
[880,843,934,0,924,877,1013,904,845,738,914],
[1007,947,969,1076,0,998,1057,1062,1016,897,1050],
[1056,958,1021,1123,1002,0,1157,1125,1056,1075,1013],
[922,886,928,987,943,843,0,899,901,810,849],
[983,908,886,1096,938,875,1101,0,972,968,992],
[1060,950,988,1155,984,944,1099,1028,0,955,1083],
[995,1073,1137,1262,1103,925,1190,1032,1045,0,1057],
[1038,961,907,1086,950,987,1151,1008,917,943,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 115, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,949,1289,1012,1043,950,992,856,844,985,1134],
[1051,0,1164,1119,1079,1158,912,817,1148,1021,1069],
[711,836,0,932,1136,1008,726,773,880,984,696],
[988,881,1068,0,1354,1153,1161,922,1195,977,984],
[957,921,864,646,0,1175,791,898,1041,1057,857],
[1050,842,992,847,825,0,895,834,841,848,819],
[1008,1088,1274,839,1209,1105,0,1291,955,1136,1010],
[1144,1183,1227,1078,1102,1166,709,0,1177,919,1146],
[1156,852,1120,805,959,1159,1045,823,0,1020,1007],
[1015,979,1016,1023,943,1152,864,1081,980,0,831],
[866,931,1304,1016,1143,1181,990,854,993,1169,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 116, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1056,1000,957,1004,999,985,1050,1046,1014,975],
[944,0,951,939,940,895,955,974,1005,946,967],
[1000,1049,0,1026,995,1019,994,1031,1054,991,1000],
[1043,1061,974,0,1042,1036,1039,1055,1101,1062,1028],
[996,1060,1005,958,0,1003,996,1056,1023,971,989],
[1001,1105,981,964,997,0,969,1020,993,1020,977],
[1015,1045,1006,961,1004,1031,0,1030,1028,1016,1021],
[950,1026,969,945,944,980,970,0,999,995,1014],
[954,995,946,899,977,1007,972,1001,0,983,988],
[986,1054,1009,938,1029,980,984,1005,1017,0,1019],
[1025,1033,1000,972,1011,1023,979,986,1012,981,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 117, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1037,1051,1076,1076,1042,1031,1047,979,1072,1024],
[963,0,985,999,992,963,968,1035,976,1008,990],
[949,1015,0,1011,1013,1016,1001,996,976,1020,1008],
[924,1001,989,0,995,992,973,998,969,1007,955],
[924,1008,987,1005,0,980,995,988,950,999,978],
[958,1037,984,1008,1020,0,1009,1019,996,1037,1015],
[969,1032,999,1027,1005,991,0,1021,953,1039,993],
[953,965,1004,1002,1012,981,979,0,946,1031,975],
[1021,1024,1024,1031,1050,1004,1047,1054,0,1071,992],
[928,992,980,993,1001,963,961,969,929,0,965],
[976,1010,992,1045,1022,985,1007,1025,1008,1035,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 118, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1032,1102,1097,1061,1064,996,1214,1053,1020,1033],
[968,0,938,969,1036,1022,905,1051,993,926,952],
[898,1062,0,951,1089,979,910,1023,987,888,1047],
[903,1031,1049,0,997,922,877,993,933,909,1032],
[939,964,911,1003,0,958,956,992,951,944,971],
[936,978,1021,1078,1042,0,894,1012,1031,991,981],
[1004,1095,1090,1123,1044,1106,0,1137,1081,985,1039],
[786,949,977,1007,1008,988,863,0,942,913,977],
[947,1007,1013,1067,1049,969,919,1058,0,994,1039],
[980,1074,1112,1091,1056,1009,1015,1087,1006,0,1046],
[967,1048,953,968,1029,1019,961,1023,961,954,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 119, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,999,963,927,1055,969,1010,947,995,948,995],
[1001,0,1050,1022,1056,979,1047,1015,1105,965,1027],
[1037,950,0,959,1001,983,1070,922,1043,979,1027],
[1073,978,1041,0,1095,965,1078,1024,1067,979,1021],
[945,944,999,905,0,905,952,942,987,951,950],
[1031,1021,1017,1035,1095,0,1054,1015,1078,977,959],
[990,953,930,922,1048,946,0,914,1003,948,934],
[1053,985,1078,976,1058,985,1086,0,1126,1022,1039],
[1005,895,957,933,1013,922,997,874,0,933,920],
[1052,1035,1021,1021,1049,1023,1052,978,1067,0,1013],
[1005,973,973,979,1050,1041,1066,961,1080,987,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 120, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1003,1003,967,915,977,979,989,968,982,977],
[997,0,1018,958,942,954,973,974,984,985,967],
[997,982,0,937,948,967,998,941,968,953,982],
[1033,1042,1063,0,1000,1006,1036,1025,1041,1053,1018],
[1085,1058,1052,1000,0,1006,1049,1028,1025,1036,1020],
[1023,1046,1033,994,994,0,1023,1022,1024,997,1003],
[1021,1027,1002,964,951,977,0,999,997,968,978],
[1011,1026,1059,975,972,978,1001,0,1019,992,992],
[1032,1016,1032,959,975,976,1003,981,0,978,1009],
[1018,1015,1047,947,964,1003,1032,1008,1022,0,982],
[1023,1033,1018,982,980,997,1022,1008,991,1018,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 121, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,955,1029,1197,1040,920,1085,1110,1132,1097,1075],
[1045,0,848,932,1059,861,932,972,942,940,1002],
[971,1152,0,1095,1070,1045,1122,1061,1319,1020,1216],
[803,1068,905,0,1078,956,850,968,1062,1096,907],
[960,941,930,922,0,820,1066,1046,1058,979,1048],
[1080,1139,955,1044,1180,0,1122,969,1051,1191,957],
[915,1068,878,1150,934,878,0,1049,1056,972,1015],
[890,1028,939,1032,954,1031,951,0,1057,1007,892],
[868,1058,681,938,942,949,944,943,0,874,926],
[903,1060,980,904,1021,809,1028,993,1126,0,1136],
[925,998,784,1093,952,1043,985,1108,1074,864,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 122, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,985,1041,1002,990,1034,999,1005,1002,966,1016],
[1015,0,1028,997,970,997,1014,1023,963,1046,964],
[959,972,0,973,992,1033,978,1026,987,1017,991],
[998,1003,1027,0,1024,999,1020,1027,1026,975,1004],
[1010,1030,1008,976,0,987,1029,981,994,1024,1058],
[966,1003,967,1001,1013,0,968,994,948,960,968],
[1001,986,1022,980,971,1032,0,1055,984,986,1012],
[995,977,974,973,1019,1006,945,0,978,1007,965],
[998,1037,1013,974,1006,1052,1016,1022,0,1046,1045],
[1034,954,983,1025,976,1040,1014,993,954,0,994],
[984,1036,1009,996,942,1032,988,1035,955,1006,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 123, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,848,1104,926,1032,936,977,950,960,890,943],
[1152,0,1203,1038,1194,1018,1032,1039,1114,1063,977],
[896,797,0,882,961,831,940,883,977,899,938],
[1074,962,1118,0,1045,1008,1036,1040,981,1034,962],
[968,806,1039,955,0,917,899,868,957,933,968],
[1064,982,1169,992,1083,0,1013,979,1056,1014,1027],
[1023,968,1060,964,1101,987,0,973,1020,1045,1102],
[1050,961,1117,960,1132,1021,1027,0,1022,1009,1008],
[1040,886,1023,1019,1043,944,980,978,0,922,949],
[1110,937,1101,966,1067,986,955,991,1078,0,1042],
[1057,1023,1062,1038,1032,973,898,992,1051,958,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 124, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,978,889,995,886,953,919,941,926,1013,870],
[1022,0,928,963,979,1041,956,952,1008,1074,983],
[1111,1072,0,1055,1000,1072,996,1005,1026,1132,1014],
[1005,1037,945,0,1020,1027,971,961,975,1048,980],
[1114,1021,1000,980,0,996,1016,1056,1010,1086,1011],
[1047,959,928,973,1004,0,990,955,970,1019,927],
[1081,1044,1004,1029,984,1010,0,1010,992,1092,983],
[1059,1048,995,1039,944,1045,990,0,1029,1130,954],
[1074,992,974,1025,990,1030,1008,971,0,1118,1028],
[987,926,868,952,914,981,908,870,882,0,942],
[1130,1017,986,1020,989,1073,1017,1046,972,1058,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 125, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,975,944,1004,951,955,1031,956,1005,963,1027],
[1025,0,896,1088,1033,985,946,962,943,958,999],
[1056,1104,0,1111,1176,992,1133,1080,1143,1099,1052],
[996,912,889,0,1077,894,956,1034,997,941,932],
[1049,967,824,923,0,923,856,885,861,873,970],
[1045,1015,1008,1106,1077,0,1123,987,1035,997,998],
[969,1054,867,1044,1144,877,0,909,1027,1026,976],
[1044,1038,920,966,1115,1013,1091,0,951,986,1065],
[995,1057,857,1003,1139,965,973,1049,0,917,1037],
[1037,1042,901,1059,1127,1003,974,1014,1083,0,1028],
[973,1001,948,1068,1030,1002,1024,935,963,972,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 126, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1050,996,1016,986,979,982,1066,1021,1006,973],
[950,0,926,979,955,986,947,938,997,957,920],
[1004,1074,0,1032,1013,1059,1047,1051,1030,996,999],
[984,1021,968,0,1007,1011,995,978,948,992,952],
[1014,1045,987,993,0,1005,987,1011,1008,1013,1020],
[1021,1014,941,989,995,0,988,981,1007,971,1032],
[1018,1053,953,1005,1013,1012,0,979,988,989,1000],
[934,1062,949,1022,989,1019,1021,0,997,990,975],
[979,1003,970,1052,992,993,1012,1003,0,1014,1019],
[994,1043,1004,1008,987,1029,1011,1010,986,0,969],
[1027,1080,1001,1048,980,968,1000,1025,981,1031,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 127, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1018,1069,1025,1086,976,979,967,1065,1001,990],
[982,0,1011,989,1035,967,937,962,965,1009,969],
[931,989,0,998,1014,971,960,958,1017,1021,972],
[975,1011,1002,0,1033,961,981,922,967,1022,976],
[914,965,986,967,0,952,940,943,980,990,961],
[1024,1033,1029,1039,1048,0,965,957,987,1008,991],
[1021,1063,1040,1019,1060,1035,0,1007,1044,1051,999],
[1033,1038,1042,1078,1057,1043,993,0,1041,1085,1023],
[935,1035,983,1033,1020,1013,956,959,0,1001,959],
[999,991,979,978,1010,992,949,915,999,0,947],
[1010,1031,1028,1024,1039,1009,1001,977,1041,1053,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 128, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,943,967,955,962,1082,922,832,916,917,928],
[1057,0,1253,1058,968,1045,922,1008,1061,1068,933],
[1033,747,0,862,768,838,905,744,753,865,812],
[1045,942,1138,0,1091,1089,1010,938,957,1020,1018],
[1038,1032,1232,909,0,1063,1026,969,908,955,1039],
[918,955,1162,911,937,0,1107,989,928,1074,1009],
[1078,1078,1095,990,974,893,0,979,947,1123,981],
[1168,992,1256,1062,1031,1011,1021,0,1010,1063,1071],
[1084,939,1247,1043,1092,1072,1053,990,0,1111,967],
[1083,932,1135,980,1045,926,877,937,889,0,919],
[1072,1067,1188,982,961,991,1019,929,1033,1081,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 129, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,955,998,992,960,940,946,954,1018,980,947],
[1045,0,1009,963,953,970,962,1014,963,999,978],
[1002,991,0,976,986,998,953,931,1019,984,957],
[1008,1037,1024,0,1027,995,1000,1002,1012,1013,1000],
[1040,1047,1014,973,0,960,959,964,1043,988,945],
[1060,1030,1002,1005,1040,0,974,1048,1003,986,970],
[1054,1038,1047,1000,1041,1026,0,994,1011,1041,1047],
[1046,986,1069,998,1036,952,1006,0,1025,1039,991],
[982,1037,981,988,957,997,989,975,0,1011,991],
[1020,1001,1016,987,1012,1014,959,961,989,0,951],
[1053,1022,1043,1000,1055,1030,953,1009,1009,1049,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 130, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1032,995,1017,960,1008,1035,958,922,888,904],
[968,0,916,1026,982,985,944,965,914,918,908],
[1005,1084,0,1020,993,994,1014,1004,996,1016,1047],
[983,974,980,0,985,1011,1024,962,958,933,930],
[1040,1018,1007,1015,0,955,1010,1010,901,971,946],
[992,1015,1006,989,1045,0,1042,934,979,971,974],
[965,1056,986,976,990,958,0,943,970,998,971],
[1042,1035,996,1038,990,1066,1057,0,1032,965,981],
[1078,1086,1004,1042,1099,1021,1030,968,0,909,967],
[1112,1082,984,1067,1029,1029,1002,1035,1091,0,962],
[1096,1092,953,1070,1054,1026,1029,1019,1033,1038,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 131, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1038,996,1007,971,997,1006,1026,991,1004,973],
[962,0,1027,996,957,976,986,958,992,1014,984],
[1004,973,0,968,988,976,1006,1014,976,979,953],
[993,1004,1032,0,969,962,993,1006,981,994,1002],
[1029,1043,1012,1031,0,1016,1017,1016,1003,988,1026],
[1003,1024,1024,1038,984,0,1036,1001,1025,1023,1011],
[994,1014,994,1007,983,964,0,999,1023,989,964],
[974,1042,986,994,984,999,1001,0,1038,983,985],
[1009,1008,1024,1019,997,975,977,962,0,991,964],
[996,986,1021,1006,1012,977,1011,1017,1009,0,994],
[1027,1016,1047,998,974,989,1036,1015,1036,1006,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 132, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,999,987,1014,987,1021,1004,1007,1033,983,1003],
[1001,0,1007,1017,1002,998,995,991,1041,1005,961],
[1013,993,0,1016,1052,1007,1012,1044,1017,979,977],
[986,983,984,0,1000,968,950,997,1026,979,939],
[1013,998,948,1000,0,955,967,1005,1012,958,952],
[979,1002,993,1032,1045,0,967,1029,1020,956,965],
[996,1005,988,1050,1033,1033,0,1025,1050,1016,1001],
[993,1009,956,1003,995,971,975,0,1020,950,969],
[967,959,983,974,988,980,950,980,0,941,952],
[1017,995,1021,1021,1042,1044,984,1050,1059,0,982],
[997,1039,1023,1061,1048,1035,999,1031,1048,1018,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 133, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1265,1169,1129,1201,1059,1152,1106,1089,1237,879],
[735,0,1142,1084,920,892,879,1024,1007,1070,927],
[831,858,0,930,980,880,984,796,918,932,838],
[871,916,1070,0,986,731,981,934,988,945,785],
[799,1080,1020,1014,0,840,928,921,996,888,1003],
[941,1108,1120,1269,1160,0,1162,1084,1214,882,994],
[848,1121,1016,1019,1072,838,0,980,1075,907,937],
[894,976,1204,1066,1079,916,1020,0,1150,941,1053],
[911,993,1082,1012,1004,786,925,850,0,857,910],
[763,930,1068,1055,1112,1118,1093,1059,1143,0,973],
[1121,1073,1162,1215,997,1006,1063,947,1090,1027,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 134, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1003,1019,1008,982,995,978,991,1004,992,1005],
[997,0,1026,977,1020,1026,1009,995,1025,995,1005],
[981,974,0,951,1011,996,987,994,1011,970,976],
[992,1023,1049,0,1004,1028,1031,1012,1023,996,1006],
[1018,980,989,996,0,1015,1006,973,1004,1007,1018],
[1005,974,1004,972,985,0,975,994,989,975,993],
[1022,991,1013,969,994,1025,0,971,1013,1012,973],
[1009,1005,1006,988,1027,1006,1029,0,1015,994,1010],
[996,975,989,977,996,1011,987,985,0,973,984],
[1008,1005,1030,1004,993,1025,988,1006,1027,0,1007],
[995,995,1024,994,982,1007,1027,990,1016,993,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 135, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,964,963,988,991,975,1024,984,1002,975,992],
[1036,0,995,1015,1013,1006,1040,1021,1024,1017,1023],
[1037,1005,0,986,1028,993,1000,990,996,984,1021],
[1012,985,1014,0,1026,996,1041,989,1007,1006,1044],
[1009,987,972,974,0,963,982,972,984,984,978],
[1025,994,1007,1004,1037,0,1028,985,983,1026,1033],
[976,960,1000,959,1018,972,0,993,995,1000,1012],
[1016,979,1010,1011,1028,1015,1007,0,991,998,992],
[998,976,1004,993,1016,1017,1005,1009,0,998,1016],
[1025,983,1016,994,1016,974,1000,1002,1002,0,1012],
[1008,977,979,956,1022,967,988,1008,984,988,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 136, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1015,1019,994,1012,1005,996,999,1040,1045,1007],
[985,0,1013,993,999,1019,995,1010,1011,1029,1013],
[981,987,0,1019,994,989,963,1000,1036,1005,981],
[1006,1007,981,0,994,997,965,988,1011,1014,1025],
[988,1001,1006,1006,0,1019,998,1015,1033,1037,1021],
[995,981,1011,1003,981,0,987,1003,1013,1022,1056],
[1004,1005,1037,1035,1002,1013,0,1018,1026,1000,1013],
[1001,990,1000,1012,985,997,982,0,1034,1033,1007],
[960,989,964,989,967,987,974,966,0,992,970],
[955,971,995,986,963,978,1000,967,1008,0,1006],
[993,987,1019,975,979,944,987,993,1030,994,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 137, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1016,1033,1035,988,981,993,1077,1103,967,979],
[984,0,1026,948,1067,1007,985,1072,1090,983,1059],
[967,974,0,1004,1036,960,913,984,1102,885,990],
[965,1052,996,0,981,985,956,1028,1169,1056,1048],
[1012,933,964,1019,0,983,992,1025,1078,947,1074],
[1019,993,1040,1015,1017,0,904,1074,1086,909,1006],
[1007,1015,1087,1044,1008,1096,0,1020,1069,937,1161],
[923,928,1016,972,975,926,980,0,1078,985,1154],
[897,910,898,831,922,914,931,922,0,911,996],
[1033,1017,1115,944,1053,1091,1063,1015,1089,0,1113],
[1021,941,1010,952,926,994,839,846,1004,887,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 138, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1020,1034,968,1015,938,955,969,1005,964,1024],
[980,0,959,943,992,963,940,960,982,943,986],
[966,1041,0,968,969,1004,964,1051,982,876,998],
[1032,1057,1032,0,990,1003,957,991,959,1015,959],
[985,1008,1031,1010,0,1008,1010,1036,1023,991,1064],
[1062,1037,996,997,992,0,1011,1043,1036,1003,1050],
[1045,1060,1036,1043,990,989,0,1056,948,991,987],
[1031,1040,949,1009,964,957,944,0,1002,969,1006],
[995,1018,1018,1041,977,964,1052,998,0,970,1040],
[1036,1057,1124,985,1009,997,1009,1031,1030,0,1033],
[976,1014,1002,1041,936,950,1013,994,960,967,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 139, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1014,996,975,936,1014,1000,991,988,1040,988],
[986,0,978,998,924,992,1010,982,1010,1009,958],
[1004,1022,0,1012,949,1011,999,982,1010,999,984],
[1025,1002,988,0,963,1037,1011,983,1003,1011,1000],
[1064,1076,1051,1037,0,1048,1040,1060,1067,1044,993],
[986,1008,989,963,952,0,1022,982,957,1038,1003],
[1000,990,1001,989,960,978,0,968,1000,1013,1000],
[1009,1018,1018,1017,940,1018,1032,0,1004,1027,993],
[1012,990,990,997,933,1043,1000,996,0,1028,960],
[960,991,1001,989,956,962,987,973,972,0,994],
[1012,1042,1016,1000,1007,997,1000,1007,1040,1006,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 140, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,971,1006,1005,976,993,995,936,1013,989,991],
[1029,0,1014,1048,1007,1015,1036,1003,1017,1029,991],
[994,986,0,1023,994,1007,1044,1019,1006,1007,1002],
[995,952,977,0,967,974,1009,956,989,961,965],
[1024,993,1006,1033,0,1005,1002,962,1021,1003,1032],
[1007,985,993,1026,995,0,1016,979,1016,984,978],
[1005,964,956,991,998,984,0,968,966,984,961],
[1064,997,981,1044,1038,1021,1032,0,1029,1009,1047],
[987,983,994,1011,979,984,1034,971,0,1000,988],
[1011,971,993,1039,997,1016,1016,991,1000,0,1014],
[1009,1009,998,1035,968,1022,1039,953,1012,986,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 141, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1071,1003,1100,1137,1064,992,1068,1077,1074,1033],
[929,0,892,909,1054,887,883,937,992,924,920],
[997,1108,0,1120,1203,1083,1080,1056,1044,1050,1106],
[900,1091,880,0,1069,967,953,903,1016,1027,1011],
[863,946,797,931,0,886,884,942,893,949,921],
[936,1113,917,1033,1114,0,970,942,1042,1066,1094],
[1008,1117,920,1047,1116,1030,0,976,966,1067,1114],
[932,1063,944,1097,1058,1058,1024,0,1056,1064,1083],
[923,1008,956,984,1107,958,1034,944,0,1002,1132],
[926,1076,950,973,1051,934,933,936,998,0,1080],
[967,1080,894,989,1079,906,886,917,868,920,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 142, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1093,1139,1090,1195,992,1032,1113,1091,1082,1095],
[907,0,1043,1017,1111,939,944,1006,961,945,997],
[861,957,0,987,1029,984,946,987,892,877,937],
[910,983,1013,0,1127,934,991,987,947,965,937],
[805,889,971,873,0,897,896,894,943,893,927],
[1008,1061,1016,1066,1103,0,979,1008,1012,1003,976],
[968,1056,1054,1009,1104,1021,0,1057,985,973,951],
[887,994,1013,1013,1106,992,943,0,952,1008,1003],
[909,1039,1108,1053,1057,988,1015,1048,0,983,1000],
[918,1055,1123,1035,1107,997,1027,992,1017,0,985],
[905,1003,1063,1063,1073,1024,1049,997,1000,1015,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 143, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,995,1038,986,1074,1012,999,979,1000,1058,1001],
[1005,0,981,979,1018,1011,980,994,984,1055,1034],
[962,1019,0,980,1041,1017,982,1023,997,1031,1014],
[1014,1021,1020,0,1031,1060,1014,1026,981,1020,1007],
[926,982,959,969,0,1001,958,973,975,1050,940],
[988,989,983,940,999,0,994,936,994,1037,980],
[1001,1020,1018,986,1042,1006,0,1005,966,1050,1000],
[1021,1006,977,974,1027,1064,995,0,985,1054,982],
[1000,1016,1003,1019,1025,1006,1034,1015,0,1075,986],
[942,945,969,980,950,963,950,946,925,0,936],
[999,966,986,993,1060,1020,1000,1018,1014,1064,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 144, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,987,1049,1013,1022,1002,985,1022,995,969,976],
[1013,0,1044,982,1043,999,1039,1042,1003,1006,993],
[951,956,0,997,1013,982,964,979,994,951,975],
[987,1018,1003,0,1027,980,1011,1024,1030,993,953],
[978,957,987,973,0,976,984,977,1018,951,920],
[998,1001,1018,1020,1024,0,996,1037,1038,1014,976],
[1015,961,1036,989,1016,1004,0,1068,967,948,965],
[978,958,1021,976,1023,963,932,0,987,991,962],
[1005,997,1006,970,982,962,1033,1013,0,988,979],
[1031,994,1049,1007,1049,986,1052,1009,1012,0,1014],
[1024,1007,1025,1047,1080,1024,1035,1038,1021,986,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 145, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1060,946,1011,1008,993,911,980,953,1015,1016],
[940,0,1005,1063,981,1001,962,918,941,962,981],
[1054,995,0,1015,1034,996,1005,994,1025,939,966],
[989,937,985,0,948,933,964,979,920,918,967],
[992,1019,966,1052,0,1003,972,1019,977,974,965],
[1007,999,1004,1067,997,0,971,948,985,946,1014],
[1089,1038,995,1036,1028,1029,0,1029,966,997,1084],
[1020,1082,1006,1021,981,1052,971,0,1014,1006,1003],
[1047,1059,975,1080,1023,1015,1034,986,0,1026,1054],
[985,1038,1061,1082,1026,1054,1003,994,974,0,1086],
[984,1019,1034,1033,1035,986,916,997,946,914,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 146, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1044,1034,1058,1019,962,990,900,1008,990,915],
[956,0,961,966,1021,916,950,968,994,972,916],
[966,1039,0,995,1004,996,977,962,1017,980,1004],
[942,1034,1005,0,1008,985,998,987,998,1018,987],
[981,979,996,992,0,959,979,900,1027,964,904],
[1038,1084,1004,1015,1041,0,1019,991,1053,1065,1027],
[1010,1050,1023,1002,1021,981,0,980,995,1024,968],
[1100,1032,1038,1013,1100,1009,1020,0,1051,1070,998],
[992,1006,983,1002,973,947,1005,949,0,972,908],
[1010,1028,1020,982,1036,935,976,930,1028,0,998],
[1085,1084,996,1013,1096,973,1032,1002,1092,1002,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 147, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1021,1056,1022,1002,1019,1032,985,1075,1023,1033],
[979,0,981,999,971,1027,999,988,1056,1024,999],
[944,1019,0,1060,985,1012,1041,1000,1053,1018,967],
[978,1001,940,0,998,941,961,1013,996,1005,987],
[998,1029,1015,1002,0,1020,1016,999,1025,1041,1046],
[981,973,988,1059,980,0,1016,1004,1015,1032,1049],
[968,1001,959,1039,984,984,0,978,1063,988,989],
[1015,1012,1000,987,1001,996,1022,0,1046,1025,999],
[925,944,947,1004,975,985,937,954,0,1007,983],
[977,976,982,995,959,968,1012,975,993,0,958],
[967,1001,1033,1013,954,951,1011,1001,1017,1042,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 148, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1018,1017,1010,977,1010,1017,993,1024,1007,1038],
[982,0,1044,1032,1026,1005,1030,1038,1021,1021,1021],
[983,956,0,964,955,955,987,972,964,980,1010],
[990,968,1036,0,975,938,1028,1000,991,1000,1028],
[1023,974,1045,1025,0,947,1026,1002,976,996,1020],
[990,995,1045,1062,1053,0,1008,1024,1025,1011,1038],
[983,970,1013,972,974,992,0,1000,1005,1011,1004],
[1007,962,1028,1000,998,976,1000,0,990,990,992],
[976,979,1036,1009,1024,975,995,1010,0,980,1013],
[993,979,1020,1000,1004,989,989,1010,1020,0,1051],
[962,979,990,972,980,962,996,1008,987,949,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 149, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1025,976,1001,996,1032,992,981,1006,1009,1002],
[975,0,966,1003,1011,1006,986,985,962,984,969],
[1024,1034,0,1007,1033,1067,1008,998,1005,1023,1045],
[999,997,993,0,992,1014,988,976,970,1000,994],
[1004,989,967,1008,0,1030,982,1001,979,1006,971],
[968,994,933,986,970,0,989,957,954,994,997],
[1008,1014,992,1012,1018,1011,0,978,994,1015,1000],
[1019,1015,1002,1024,999,1043,1022,0,977,1005,1015],
[994,1038,995,1030,1021,1046,1006,1023,0,1014,1023],
[991,1016,977,1000,994,1006,985,995,986,0,1025],
[998,1031,955,1006,1029,1003,1000,985,977,975,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 150, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,982,1091,1156,990,1114,1032,1022,1124,1037,1147],
[1018,0,1069,1125,1091,1005,1003,1102,1013,983,1119],
[909,931,0,1037,1044,970,1006,1051,970,915,1078],
[844,875,963,0,922,991,892,912,961,933,984],
[1010,909,956,1078,0,1050,1106,1008,1002,843,1104],
[886,995,1030,1009,950,0,1072,1056,997,889,1076],
[968,997,994,1108,894,928,0,1009,1013,833,1019],
[978,898,949,1088,992,944,991,0,970,912,1099],
[876,987,1030,1039,998,1003,987,1030,0,968,1010],
[963,1017,1085,1067,1157,1111,1167,1088,1032,0,1140],
[853,881,922,1016,896,924,981,901,990,860,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 151, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1018,1009,956,989,982,968,1046,953,1033,1025],
[982,0,989,946,943,964,924,962,936,975,1005],
[991,1011,0,984,965,983,971,956,983,990,970],
[1044,1054,1016,0,977,1007,980,995,984,1003,1011],
[1011,1057,1035,1023,0,1005,998,1013,980,1039,1013],
[1018,1036,1017,993,995,0,980,990,984,984,1028],
[1032,1076,1029,1020,1002,1020,0,972,1010,1017,1018],
[954,1038,1044,1005,987,1010,1028,0,975,1023,1040],
[1047,1064,1017,1016,1020,1016,990,1025,0,1046,1054],
[967,1025,1010,997,961,1016,983,977,954,0,971],
[975,995,1030,989,987,972,982,960,946,1029,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 152, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,994,1067,1046,987,963,951,995,1044,1025,1034],
[1006,0,1047,1070,1046,995,978,961,933,978,980],
[933,953,0,975,930,954,940,920,963,948,981],
[954,930,1025,0,1016,990,910,947,977,1037,992],
[1013,954,1070,984,0,993,973,1005,991,1048,983],
[1037,1005,1046,1010,1007,0,1031,978,1043,1058,987],
[1049,1022,1060,1090,1027,969,0,1012,1028,1064,1060],
[1005,1039,1080,1053,995,1022,988,0,1045,1028,1042],
[956,1067,1037,1023,1009,957,972,955,0,1032,1004],
[975,1022,1052,963,952,942,936,972,968,0,911],
[966,1020,1019,1008,1017,1013,940,958,996,1089,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 153, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,977,992,947,957,982,988,965,935,940,1004],
[1023,0,1053,1025,1011,1027,1031,983,1002,980,1021],
[1008,947,0,977,965,979,1001,989,987,982,1007],
[1053,975,1023,0,994,1000,1019,977,1022,1009,1017],
[1043,989,1035,1006,0,1008,1030,1010,998,1030,1042],
[1018,973,1021,1000,992,0,1010,977,980,994,1012],
[1012,969,999,981,970,990,0,974,970,964,989],
[1035,1017,1011,1023,990,1023,1026,0,1008,982,1031],
[1065,998,1013,978,1002,1020,1030,992,0,972,1027],
[1060,1020,1018,991,970,1006,1036,1018,1028,0,1013],
[996,979,993,983,958,988,1011,969,973,987,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 154, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1012,1182,1213,1124,1043,988,1113,1080,1074,1090],
[988,0,1045,1023,1012,979,972,1059,1031,1046,999],
[818,955,0,1014,907,883,841,1020,939,1037,1053],
[787,977,986,0,895,970,872,1010,981,889,1006],
[876,988,1093,1105,0,929,973,1035,1134,1080,1035],
[957,1021,1117,1030,1071,0,1039,1116,1072,1049,1061],
[1012,1028,1159,1128,1027,961,0,1064,1115,1073,1099],
[887,941,980,990,965,884,936,0,988,967,1002],
[920,969,1061,1019,866,928,885,1012,0,931,947],
[926,954,963,1111,920,951,927,1033,1069,0,975],
[910,1001,947,994,965,939,901,998,1053,1025,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 155, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,988,1008,1009,1056,1017,1053,988,1023,998,1000],
[1012,0,1015,998,1012,1005,1050,983,1084,1027,983],
[992,985,0,1026,965,1037,998,1032,1060,1002,958],
[991,1002,974,0,1011,987,1006,976,1026,947,989],
[944,988,1035,989,0,993,1016,1003,1039,997,964],
[983,995,963,1013,1007,0,1076,1005,1034,988,984],
[947,950,1002,994,984,924,0,997,997,982,927],
[1012,1017,968,1024,997,995,1003,0,1057,997,975],
[977,916,940,974,961,966,1003,943,0,930,946],
[1002,973,998,1053,1003,1012,1018,1003,1070,0,970],
[1000,1017,1042,1011,1036,1016,1073,1025,1054,1030,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 156, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,992,1019,1014,1022,972,1048,1023,966,997,1044],
[1008,0,1008,1049,983,975,1046,1000,933,974,1003],
[981,992,0,992,1010,1040,1010,1007,955,1032,987],
[986,951,1008,0,1064,962,1060,963,970,1005,982],
[978,1017,990,936,0,938,1037,978,929,991,1037],
[1028,1025,960,1038,1062,0,1024,1018,1044,1039,986],
[952,954,990,940,963,976,0,977,891,963,923],
[977,1000,993,1037,1022,982,1023,0,1081,1041,995],
[1034,1067,1045,1030,1071,956,1109,919,0,986,1002],
[1003,1026,968,995,1009,961,1037,959,1014,0,972],
[956,997,1013,1018,963,1014,1077,1005,998,1028,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 157, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,996,1020,1055,1000,1039,989,1030,1018,1042,1033],
[1004,0,1004,1025,1013,993,1030,979,1030,1004,1019],
[980,996,0,996,994,992,1005,1008,1007,985,993],
[945,975,1004,0,994,979,985,1006,1000,983,987],
[1000,987,1006,1006,0,1026,1027,1007,1014,1010,1014],
[961,1007,1008,1021,974,0,1003,1031,1048,1011,1023],
[1011,970,995,1015,973,997,0,1014,984,1008,1001],
[970,1021,992,994,993,969,986,0,998,992,1026],
[982,970,993,1000,986,952,1016,1002,0,979,966],
[958,996,1015,1017,990,989,992,1008,1021,0,1016],
[967,981,1007,1013,986,977,999,974,1034,984,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 158, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1013,993,1006,1011,1002,1036,1008,1011,1014,1020],
[987,0,991,999,998,990,995,975,988,972,978],
[1007,1009,0,1018,999,991,1040,980,999,986,1007],
[994,1001,982,0,1027,993,1042,992,1005,1018,992],
[989,1002,1001,973,0,963,1018,979,978,1000,1004],
[998,1010,1009,1007,1037,0,1010,975,1008,1001,988],
[964,1005,960,958,982,990,0,982,980,969,986],
[992,1025,1020,1008,1021,1025,1018,0,1020,1018,987],
[989,1012,1001,995,1022,992,1020,980,0,995,961],
[986,1028,1014,982,1000,999,1031,982,1005,0,998],
[980,1022,993,1008,996,1012,1014,1013,1039,1002,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 159, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,992,1038,1008,1011,996,997,1004,978,1022,1014],
[1008,0,1011,999,997,1002,990,994,1013,994,990],
[962,989,0,978,966,976,955,1004,941,998,963],
[992,1001,1022,0,973,987,1019,1021,1005,988,997],
[989,1003,1034,1027,0,1014,997,1046,1016,1035,1031],
[1004,998,1024,1013,986,0,981,1032,1009,1022,1007],
[1003,1010,1045,981,1003,1019,0,989,1022,1059,986],
[996,1006,996,979,954,968,1011,0,981,977,972],
[1022,987,1059,995,984,991,978,1019,0,1043,1002],
[978,1006,1002,1012,965,978,941,1023,957,0,964],
[986,1010,1037,1003,969,993,1014,1028,998,1036,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 160, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1000,1024,1016,1007,1001,1041,1000,1005,1049,1037],
[1000,0,1034,1034,1036,994,1069,1016,1058,1058,1054],
[976,966,0,986,1035,1012,1037,974,1017,1066,1039],
[984,966,1014,0,981,965,1044,1011,1028,1034,1019],
[993,964,965,1019,0,995,1016,956,1018,1033,1046],
[999,1006,988,1035,1005,0,1101,1010,1067,1038,1053],
[959,931,963,956,984,899,0,961,983,974,976],
[1000,984,1026,989,1044,990,1039,0,1051,1028,1022],
[995,942,983,972,982,933,1017,949,0,994,990],
[951,942,934,966,967,962,1026,972,1006,0,997],
[963,946,961,981,954,947,1024,978,1010,1003,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 161, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,989,1003,1027,955,1031,1043,975,965,994,987],
[1011,0,988,1072,999,1044,1083,1047,1028,1026,1019],
[997,1012,0,1051,1006,1037,1064,1022,1007,1058,976],
[973,928,949,0,913,1045,1018,1009,986,975,976],
[1045,1001,994,1087,0,1083,1046,1051,991,1025,997],
[969,956,963,955,917,0,964,947,970,978,966],
[957,917,936,982,954,1036,0,946,981,963,1012],
[1025,953,978,991,949,1053,1054,0,993,1029,992],
[1035,972,993,1014,1009,1030,1019,1007,0,1037,957],
[1006,974,942,1025,975,1022,1037,971,963,0,996],
[1013,981,1024,1024,1003,1034,988,1008,1043,1004,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 162, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,978,1000,974,1035,1053,1014,995,986,992,1014],
[1022,0,1047,1009,1047,1030,1010,975,1017,1012,1016],
[1000,953,0,955,1019,1028,1031,973,951,947,999],
[1026,991,1045,0,1053,1032,1048,1023,1003,959,1048],
[965,953,981,947,0,988,1022,983,960,921,991],
[947,970,972,968,1012,0,1022,963,982,980,1007],
[986,990,969,952,978,978,0,965,972,954,964],
[1005,1025,1027,977,1017,1037,1035,0,1005,983,1045],
[1014,983,1049,997,1040,1018,1028,995,0,984,1013],
[1008,988,1053,1041,1079,1020,1046,1017,1016,0,1081],
[986,984,1001,952,1009,993,1036,955,987,919,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 163, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,927,1004,965,951,1012,928,898,946,967,939],
[1073,0,1003,975,997,1003,1097,970,967,989,994],
[996,997,0,1037,989,1035,1061,1006,992,1090,1010],
[1035,1025,963,0,974,981,1082,1016,1003,994,972],
[1049,1003,1011,1026,0,1010,1073,955,951,961,977],
[988,997,965,1019,990,0,1040,998,937,1018,951],
[1072,903,939,918,927,960,0,921,1027,1004,919],
[1102,1030,994,984,1045,1002,1079,0,992,1023,988],
[1054,1033,1008,997,1049,1063,973,1008,0,978,986],
[1033,1011,910,1006,1039,982,996,977,1022,0,968],
[1061,1006,990,1028,1023,1049,1081,1012,1014,1032,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 164, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,975,963,889,972,904,927,910,990,975,990],
[1025,0,1001,887,1015,941,1019,960,1018,959,877],
[1037,999,0,962,978,991,1054,969,964,960,1035],
[1111,1113,1038,0,1025,1013,1121,996,1050,1067,1093],
[1028,985,1022,975,0,972,1031,1004,958,965,1007],
[1096,1059,1009,987,1028,0,983,989,1012,1050,985],
[1073,981,946,879,969,1017,0,940,1002,922,1042],
[1090,1040,1031,1004,996,1011,1060,0,1010,1055,1022],
[1010,982,1036,950,1042,988,998,990,0,1048,996],
[1025,1041,1040,933,1035,950,1078,945,952,0,1023],
[1010,1123,965,907,993,1015,958,978,1004,977,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 165, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1051,971,1010,1003,996,1040,1000,1030,1040,1010],
[949,0,922,979,926,996,981,939,985,1007,976],
[1029,1078,0,965,953,993,1045,1020,1045,1053,1019],
[990,1021,1035,0,1000,1020,1023,988,1004,1036,1036],
[997,1074,1047,1000,0,997,1098,1022,1080,1030,1026],
[1004,1004,1007,980,1003,0,991,1041,1042,1024,1014],
[960,1019,955,977,902,1009,0,978,1042,1014,993],
[1000,1061,980,1012,978,959,1022,0,971,1026,1000],
[970,1015,955,996,920,958,958,1029,0,1000,981],
[960,993,947,964,970,976,986,974,1000,0,983],
[990,1024,981,964,974,986,1007,1000,1019,1017,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 166, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,947,964,981,960,1023,964,999,966,968,977],
[1053,0,1002,1026,992,1003,1004,1023,1006,975,1013],
[1036,998,0,996,984,1008,1030,1007,966,982,993],
[1019,974,1004,0,1015,1009,1026,1034,999,1021,990],
[1040,1008,1016,985,0,1022,993,1019,976,984,1039],
[977,997,992,991,978,0,981,1010,976,979,997],
[1036,996,970,974,1007,1019,0,1035,983,992,1019],
[1001,977,993,966,981,990,965,0,968,993,993],
[1034,994,1034,1001,1024,1024,1017,1032,0,998,1023],
[1032,1025,1018,979,1016,1021,1008,1007,1002,0,1008],
[1023,987,1007,1010,961,1003,981,1007,977,992,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 167, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1033,938,940,978,985,958,1068,1009,945,959],
[967,0,1009,976,1014,998,985,1027,942,985,998],
[1062,991,0,975,999,1001,1035,1063,1025,944,1058],
[1060,1024,1025,0,1065,992,982,1061,1002,967,1026],
[1022,986,1001,935,0,944,984,1062,1021,984,1038],
[1015,1002,999,1008,1056,0,999,1009,1034,1002,979],
[1042,1015,965,1018,1016,1001,0,1065,1030,991,969],
[932,973,937,939,938,991,935,0,1027,890,997],
[991,1058,975,998,979,966,970,973,0,960,959],
[1055,1015,1056,1033,1016,998,1009,1110,1040,0,986],
[1041,1002,942,974,962,1021,1031,1003,1041,1014,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 168, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1032,976,997,976,980,999,970,963,945,959],
[968,0,946,980,975,942,959,977,974,971,943],
[1024,1054,0,1008,1011,997,1025,1011,1001,1005,1002],
[1003,1020,992,0,1008,986,1016,969,1015,983,951],
[1024,1025,989,992,0,996,990,994,964,991,973],
[1020,1058,1003,1014,1004,0,988,969,1027,1009,975],
[1001,1041,975,984,1010,1012,0,969,1001,1000,955],
[1030,1023,989,1031,1006,1031,1031,0,1037,1034,999],
[1037,1026,999,985,1036,973,999,963,0,985,973],
[1055,1029,995,1017,1009,991,1000,966,1015,0,978],
[1041,1057,998,1049,1027,1025,1045,1001,1027,1022,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 169, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1015,1007,958,964,1021,961,994,996,999,987],
[985,0,980,1004,926,997,970,999,944,1017,926],
[993,1020,0,972,1012,942,954,1048,949,974,921],
[1042,996,1028,0,1030,1017,1004,1049,1001,1037,989],
[1036,1074,988,970,0,1015,1007,1060,991,1012,981],
[979,1003,1058,983,985,0,938,1027,995,969,960],
[1039,1030,1046,996,993,1062,0,1091,950,1094,1018],
[1006,1001,952,951,940,973,909,0,935,957,950],
[1004,1056,1051,999,1009,1005,1050,1065,0,1090,997],
[1001,983,1026,963,988,1031,906,1043,910,0,969],
[1013,1074,1079,1011,1019,1040,982,1050,1003,1031,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 170, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1003,1060,983,948,980,979,1019,985,1029,1028],
[997,0,1017,1008,987,1003,984,1011,999,1016,1037],
[940,983,0,925,938,932,962,978,947,981,987],
[1017,992,1075,0,1003,985,1003,1014,992,1017,1019],
[1052,1013,1062,997,0,1002,984,999,1030,1048,1047],
[1020,997,1068,1015,998,0,994,998,984,993,1051],
[1021,1016,1038,997,1016,1006,0,1024,1023,1018,1036],
[981,989,1022,986,1001,1002,976,0,1024,1003,1018],
[1015,1001,1053,1008,970,1016,977,976,0,1030,1030],
[971,984,1019,983,952,1007,982,997,970,0,1012],
[972,963,1013,981,953,949,964,982,970,988,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 171, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1029,1023,1007,1040,1043,1030,1017,1017,1001,993],
[971,0,999,1013,1018,1002,986,987,981,1021,990],
[977,1001,0,1008,1010,1005,983,991,990,1004,999],
[993,987,992,0,1005,1001,957,990,961,987,976],
[960,982,990,995,0,1031,972,977,970,1008,995],
[957,998,995,999,969,0,999,982,970,1016,993],
[970,1014,1017,1043,1028,1001,0,994,992,1000,1001],
[983,1013,1009,1010,1023,1018,1006,0,1014,998,1010],
[983,1019,1010,1039,1030,1030,1008,986,0,1010,1011],
[999,979,996,1013,992,984,1000,1002,990,0,1003],
[1007,1010,1001,1024,1005,1007,999,990,989,997,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 172, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,895,1011,1033,980,986,1119,967,982,1063,1042],
[1105,0,1017,919,1025,1101,1089,921,923,1046,1115],
[989,983,0,1012,924,1090,994,1010,1085,1100,1184],
[967,1081,988,0,1086,993,1069,1109,1072,1089,1093],
[1020,975,1076,914,0,1084,1164,891,936,1211,1110],
[1014,899,910,1007,916,0,1158,980,1000,872,1080],
[881,911,1006,931,836,842,0,911,859,926,924],
[1033,1079,990,891,1109,1020,1089,0,1079,1188,1159],
[1018,1077,915,928,1064,1000,1141,921,0,1106,1098],
[937,954,900,911,789,1128,1074,812,894,0,981],
[958,885,816,907,890,920,1076,841,902,1019,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 173, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,998,1070,1107,1105,1011,1041,1005,998,1042,966],
[1002,0,999,1038,962,991,1084,915,1003,1059,976],
[930,1001,0,1024,1032,1058,1043,914,1004,1043,976],
[893,962,976,0,1022,998,998,947,966,1017,910],
[895,1038,968,978,0,976,1029,869,949,995,954],
[989,1009,942,1002,1024,0,1092,892,976,964,988],
[959,916,957,1002,971,908,0,873,970,936,831],
[995,1085,1086,1053,1131,1108,1127,0,1090,1094,1063],
[1002,997,996,1034,1051,1024,1030,910,0,995,941],
[958,941,957,983,1005,1036,1064,906,1005,0,945],
[1034,1024,1024,1090,1046,1012,1169,937,1059,1055,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 174, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,967,1072,1022,975,981,960,955,1012,964,973],
[1033,0,1136,994,1060,1033,1060,975,1027,1013,1058],
[928,864,0,905,917,927,893,905,980,937,860],
[978,1006,1095,0,1043,1031,971,918,1077,974,1031],
[1025,940,1083,957,0,1017,985,995,1004,995,974],
[1019,967,1073,969,983,0,1047,979,1053,977,999],
[1040,940,1107,1029,1015,953,0,946,1039,999,964],
[1045,1025,1095,1082,1005,1021,1054,0,1025,1024,978],
[988,973,1020,923,996,947,961,975,0,957,973],
[1036,987,1063,1026,1005,1023,1001,976,1043,0,987],
[1027,942,1140,969,1026,1001,1036,1022,1027,1013,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 175, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1022,1010,1002,999,966,1006,1001,1000,995,992],
[978,0,1053,999,996,1017,1007,1017,980,978,1027],
[990,947,0,963,1002,995,1012,1014,994,984,961],
[998,1001,1037,0,1030,981,1001,995,981,1012,1006],
[1001,1004,998,970,0,1008,1004,988,991,973,1000],
[1034,983,1005,1019,992,0,1019,1035,1013,1001,991],
[994,993,988,999,996,981,0,1000,998,974,990],
[999,983,986,1005,1012,965,1000,0,987,974,966],
[1000,1020,1006,1019,1009,987,1002,1013,0,1000,986],
[1005,1022,1016,988,1027,999,1026,1026,1000,0,971],
[1008,973,1039,994,1000,1009,1010,1034,1014,1029,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 176, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,890,894,960,1007,1089,984,920,852,945,1261],
[1110,0,889,1167,1049,849,1091,1155,983,1131,1299],
[1106,1111,0,1050,1067,1058,1128,1076,955,1215,1298],
[1040,833,950,0,986,1045,964,1081,909,1064,1106],
[993,951,933,1014,0,1009,981,766,1053,987,1084],
[911,1151,942,955,991,0,999,944,786,999,1158],
[1016,909,872,1036,1019,1001,0,794,904,1032,1039],
[1080,845,924,919,1234,1056,1206,0,820,1068,1055],
[1148,1017,1045,1091,947,1214,1096,1180,0,1111,1367],
[1055,869,785,936,1013,1001,968,932,889,0,1110],
[739,701,702,894,916,842,961,945,633,890,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 177, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1015,1010,1019,1000,1034,1008,1002,1047,1028,1020],
[985,0,1012,973,978,996,955,960,1023,995,1000],
[990,988,0,1014,1026,1028,1002,1014,1026,1019,1039],
[981,1027,986,0,997,1012,995,968,1025,963,1005],
[1000,1022,974,1003,0,1040,997,1001,1033,998,1032],
[966,1004,972,988,960,0,960,951,1023,996,983],
[992,1045,998,1005,1003,1040,0,985,1062,999,1031],
[998,1040,986,1032,999,1049,1015,0,1027,1016,1055],
[953,977,974,975,967,977,938,973,0,986,962],
[972,1005,981,1037,1002,1004,1001,984,1014,0,1010],
[980,1000,961,995,968,1017,969,945,1038,990,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 178, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,994,1054,1029,1029,1049,1038,1145,972,998,1077],
[1006,0,1024,1031,1065,1014,1006,1108,1044,985,1084],
[946,976,0,1030,1008,1005,1037,1067,1016,1000,1039],
[971,969,970,0,1036,987,1002,1097,998,976,1009],
[971,935,992,964,0,986,982,1044,989,970,981],
[951,986,995,1013,1014,0,1002,1064,989,999,1033],
[962,994,963,998,1018,998,0,1031,969,945,992],
[855,892,933,903,956,936,969,0,931,901,1006],
[1028,956,984,1002,1011,1011,1031,1069,0,937,1007],
[1002,1015,1000,1024,1030,1001,1055,1099,1063,0,1017],
[923,916,961,991,1019,967,1008,994,993,983,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 179, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1036,981,1003,1007,997,974,982,1014,998,974],
[964,0,992,1003,973,967,929,976,969,905,955],
[1019,1008,0,1003,1009,950,943,972,982,969,967],
[997,997,997,0,980,945,974,1015,1012,988,989],
[993,1027,991,1020,0,946,982,981,1004,985,1017],
[1003,1033,1050,1055,1054,0,1036,997,1043,975,1041],
[1026,1071,1057,1026,1018,964,0,982,1006,991,1007],
[1018,1024,1028,985,1019,1003,1018,0,1049,1022,1060],
[986,1031,1018,988,996,957,994,951,0,971,992],
[1002,1095,1031,1012,1015,1025,1009,978,1029,0,1040],
[1026,1045,1033,1011,983,959,993,940,1008,960,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 180, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1067,1069,1044,968,1007,1085,1058,992,1094,1057],
[933,0,1038,1001,1002,949,986,1019,958,1023,1005],
[931,962,0,914,929,949,927,996,943,992,1031],
[956,999,1086,0,955,1016,958,1024,930,1009,1034],
[1032,998,1071,1045,0,1047,995,1077,1055,1022,1084],
[993,1051,1051,984,953,0,1023,1052,987,1052,1064],
[915,1014,1073,1042,1005,977,0,1026,954,1012,1060],
[942,981,1004,976,923,948,974,0,949,1008,980],
[1008,1042,1057,1070,945,1013,1046,1051,0,1040,1068],
[906,977,1008,991,978,948,988,992,960,0,1027],
[943,995,969,966,916,936,940,1020,932,973,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 181, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1026,1019,1003,1007,978,1028,942,1066,942,1002],
[974,0,985,923,986,926,1013,961,1054,953,1003],
[981,1015,0,939,981,978,1030,964,1084,1013,958],
[997,1077,1061,0,989,1026,1041,1023,1035,974,995],
[993,1014,1019,1011,0,999,1044,993,1064,984,1035],
[1022,1074,1022,974,1001,0,1027,982,1097,1006,1027],
[972,987,970,959,956,973,0,968,1058,950,1013],
[1058,1039,1036,977,1007,1018,1032,0,1092,939,1036],
[934,946,916,965,936,903,942,908,0,864,975],
[1058,1047,987,1026,1016,994,1050,1061,1136,0,1021],
[998,997,1042,1005,965,973,987,964,1025,979,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 182, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,923,1043,1076,968,1051,929,1038,982,899,1056],
[1077,0,1058,999,1031,1044,1026,1111,974,998,977],
[957,942,0,983,971,1082,963,1056,972,926,1150],
[924,1001,1017,0,907,958,1023,1026,949,965,1060],
[1032,969,1029,1093,0,966,1047,1040,1076,953,1140],
[949,956,918,1042,1034,0,985,1021,960,973,998],
[1071,974,1037,977,953,1015,0,1103,1010,1083,994],
[962,889,944,974,960,979,897,0,810,938,1001],
[1018,1026,1028,1051,924,1040,990,1190,0,1015,1123],
[1101,1002,1074,1035,1047,1027,917,1062,985,0,1070],
[944,1023,850,940,860,1002,1006,999,877,930,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 183, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1059,1016,1033,1031,1053,1053,1022,1010,1044,1000],
[941,0,999,976,1003,999,1023,989,995,998,991],
[984,1001,0,1006,985,1024,1001,984,971,1007,974],
[967,1024,994,0,1027,988,1032,1022,1021,1015,973],
[969,997,1015,973,0,1013,988,1031,1011,1035,981],
[947,1001,976,1012,987,0,1015,982,982,997,959],
[947,977,999,968,1012,985,0,1004,978,1003,959],
[978,1011,1016,978,969,1018,996,0,1016,999,969],
[990,1005,1029,979,989,1018,1022,984,0,1023,977],
[956,1002,993,985,965,1003,997,1001,977,0,948],
[1000,1009,1026,1027,1019,1041,1041,1031,1023,1052,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 184, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,955,976,986,977,979,971,995,981,988,980],
[1045,0,1034,1007,1013,1006,1028,1022,995,1033,997],
[1024,966,0,1012,1004,1008,1004,1016,1017,1015,1030],
[1014,993,988,0,1040,975,1008,1017,984,994,1004],
[1023,987,996,960,0,1027,1008,1046,997,1023,1038],
[1021,994,992,1025,973,0,995,1031,1009,1027,1021],
[1029,972,996,992,992,1005,0,1017,1026,996,1015],
[1005,978,984,983,954,969,983,0,975,1015,986],
[1019,1005,983,1016,1003,991,974,1025,0,1006,1012],
[1012,967,985,1006,977,973,1004,985,994,0,992],
[1020,1003,970,996,962,979,985,1014,988,1008,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 185, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,978,929,981,979,1015,935,1059,993,915,1000],
[1022,0,957,982,1003,1053,1016,1059,1022,971,997],
[1071,1043,0,1006,984,1033,996,1129,1082,987,1053],
[1019,1018,994,0,982,994,965,1016,1043,957,979],
[1021,997,1016,1018,0,1040,1006,1013,1078,1012,1072],
[985,947,967,1006,960,0,960,1050,1017,948,991],
[1065,984,1004,1035,994,1040,0,1078,1033,1020,1040],
[941,941,871,984,987,950,922,0,977,900,964],
[1007,978,918,957,922,983,967,1023,0,924,1006],
[1085,1029,1013,1043,988,1052,980,1100,1076,0,1010],
[1000,1003,947,1021,928,1009,960,1036,994,990,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 186, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,975,950,996,957,1005,974,999,965,1015,1008],
[1025,0,970,1029,1000,1038,1028,1001,1011,1007,1029],
[1050,1030,0,1049,993,1048,1017,1035,1021,1052,1031],
[1004,971,951,0,946,972,976,994,955,1011,1014],
[1043,1000,1007,1054,0,1027,1019,1018,1017,1024,1022],
[995,962,952,1028,973,0,986,1000,989,1044,1041],
[1026,972,983,1024,981,1014,0,1003,992,1020,1029],
[1001,999,965,1006,982,1000,997,0,996,1023,1028],
[1035,989,979,1045,983,1011,1008,1004,0,1034,1046],
[985,993,948,989,976,956,980,977,966,0,1012],
[992,971,969,986,978,959,971,972,954,988,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 187, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1020,1045,1021,969,1052,982,997,1007,973,970],
[980,0,1058,1069,999,1022,1011,1014,1039,973,1042],
[955,942,0,1004,944,1038,1000,915,955,933,960],
[979,931,996,0,1002,984,963,974,982,992,990],
[1031,1001,1056,998,0,1053,1026,1026,1049,1021,989],
[948,978,962,1016,947,0,994,999,1006,933,992],
[1018,989,1000,1037,974,1006,0,1038,990,960,989],
[1003,986,1085,1026,974,1001,962,0,1006,1010,1013],
[993,961,1045,1018,951,994,1010,994,0,985,993],
[1027,1027,1067,1008,979,1067,1040,990,1015,0,1002],
[1030,958,1040,1010,1011,1008,1011,987,1007,998,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 188, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,969,991,946,993,995,965,976,985,973,1008],
[1031,0,1040,982,993,993,1004,1012,992,1001,1035],
[1009,960,0,942,956,979,981,1013,1005,979,977],
[1054,1018,1058,0,1017,1017,969,1032,1029,1041,1036],
[1007,1007,1044,983,0,998,990,1051,1019,1005,983],
[1005,1007,1021,983,1002,0,1008,1026,1038,1018,1011],
[1035,996,1019,1031,1010,992,0,1030,1019,1018,1049],
[1024,988,987,968,949,974,970,0,979,974,992],
[1015,1008,995,971,981,962,981,1021,0,988,1020],
[1027,999,1021,959,995,982,982,1026,1012,0,1041],
[992,965,1023,964,1017,989,951,1008,980,959,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 189, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,982,919,933,956,969,991,963,1010,970,974],
[1018,0,997,1035,1052,1015,1040,1032,1021,992,1028],
[1081,1003,0,987,1020,999,1058,1026,1039,990,1009],
[1067,965,1013,0,982,967,1037,995,1060,1011,1033],
[1044,948,980,1018,0,1001,1061,1030,1070,977,1035],
[1031,985,1001,1033,999,0,1038,972,1059,946,1032],
[1009,960,942,963,939,962,0,980,1010,927,1008],
[1037,968,974,1005,970,1028,1020,0,1087,971,1026],
[990,979,961,940,930,941,990,913,0,943,989],
[1030,1008,1010,989,1023,1054,1073,1029,1057,0,1027],
[1026,972,991,967,965,968,992,974,1011,973,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 190, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1182,974,1101,1353,986,1261,1196,1038,1097,1134],
[818,0,733,936,1418,944,995,766,1058,1091,1046],
[1026,1267,0,1219,1565,999,1256,939,1039,1212,1018],
[899,1064,781,0,1451,810,1062,743,611,733,853],
[647,582,435,549,0,582,589,419,532,433,567],
[1014,1056,1001,1190,1418,0,1130,1093,882,1068,1084],
[739,1005,744,938,1411,870,0,915,944,818,870],
[804,1234,1061,1257,1581,907,1085,0,830,1327,936],
[962,942,961,1389,1468,1118,1056,1170,0,1344,1110],
[903,909,788,1267,1567,932,1182,673,656,0,814],
[866,954,982,1147,1433,916,1130,1064,890,1186,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 191, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1032,1016,1032,1041,1025,995,1056,1013,1002,1020],
[968,0,1006,989,996,1011,984,999,1011,995,994],
[984,994,0,1002,1004,1018,974,1047,1003,1022,993],
[968,1011,998,0,1028,1000,972,1042,1007,1008,1004],
[959,1004,996,972,0,977,1004,1010,970,968,985],
[975,989,982,1000,1023,0,1019,1025,1006,1010,986],
[1005,1016,1026,1028,996,981,0,1061,995,1010,1016],
[944,1001,953,958,990,975,939,0,967,949,980],
[987,989,997,993,1030,994,1005,1033,0,982,995],
[998,1005,978,992,1032,990,990,1051,1018,0,994],
[980,1006,1007,996,1015,1014,984,1020,1005,1006,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 192, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,998,1029,1008,1018,1007,1009,1018,1006,1028,1032],
[1002,0,1011,1018,995,1015,982,1004,1003,1002,1007],
[971,989,0,1007,979,983,990,1005,995,1024,1020],
[992,982,993,0,979,975,990,983,983,1013,998],
[982,1005,1021,1021,0,997,999,1010,998,1015,1029],
[993,985,1017,1025,1003,0,993,1014,993,1002,1011],
[991,1018,1010,1010,1001,1007,0,1015,1004,1038,1009],
[982,996,995,1017,990,986,985,0,990,1004,1016],
[994,997,1005,1017,1002,1007,996,1010,0,1033,1013],
[972,998,976,987,985,998,962,996,967,0,993],
[968,993,980,1002,971,989,991,984,987,1007,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 193, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,960,994,979,959,984,962,1012,964,992,996],
[1040,0,1018,1031,1001,1055,1024,1029,982,1002,1029],
[1006,982,0,1040,979,998,1014,1034,997,1053,1042],
[1021,969,960,0,966,993,996,1003,971,979,984],
[1041,999,1021,1034,0,1025,978,1020,1006,1010,1013],
[1016,945,1002,1007,975,0,1004,992,1010,977,1026],
[1038,976,986,1004,1022,996,0,997,947,1002,1009],
[988,971,966,997,980,1008,1003,0,984,993,1013],
[1036,1018,1003,1029,994,990,1053,1016,0,1042,1043],
[1008,998,947,1021,990,1023,998,1007,958,0,1012],
[1004,971,958,1016,987,974,991,987,957,988,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 194, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1027,967,966,1029,995,1035,1017,978,983,993],
[973,0,926,949,978,950,961,969,940,952,961],
[1033,1074,0,1025,1047,994,1018,1013,988,1017,1022],
[1034,1051,975,0,1042,1015,1030,1020,1013,1006,1021],
[971,1022,953,958,0,955,1010,971,975,936,951],
[1005,1050,1006,985,1045,0,1041,1019,993,1016,1017],
[965,1039,982,970,990,959,0,1045,959,978,991],
[983,1031,987,980,1029,981,955,0,963,999,975],
[1022,1060,1012,987,1025,1007,1041,1037,0,1012,1014],
[1017,1048,983,994,1064,984,1022,1001,988,0,1035],
[1007,1039,978,979,1049,983,1009,1025,986,965,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 195, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1010,1017,1004,1017,1013,987,990,988,1006,986],
[990,0,1025,1026,1028,1036,990,1002,1014,1034,990],
[983,975,0,1001,1007,1003,997,1004,981,1005,968],
[996,974,999,0,992,1008,977,982,980,1005,979],
[983,972,993,1008,0,1003,980,973,971,1007,968],
[987,964,997,992,997,0,987,996,973,1009,957],
[1013,1010,1003,1023,1020,1013,0,1000,999,1012,1000],
[1010,998,996,1018,1027,1004,1000,0,1028,1024,991],
[1012,986,1019,1020,1029,1027,1001,972,0,1010,992],
[994,966,995,995,993,991,988,976,990,0,955],
[1014,1010,1032,1021,1032,1043,1000,1009,1008,1045,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 196, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,956,896,1066,964,1002,985,983,960,1008,1030],
[1044,0,962,1137,989,1029,1030,972,1010,996,1005],
[1104,1038,0,1073,1070,1059,987,992,1074,1036,1051],
[934,863,927,0,939,970,900,854,964,914,913],
[1036,1011,930,1061,0,1111,1030,954,1020,1066,991],
[998,971,941,1030,889,0,1004,918,1018,977,1000],
[1015,970,1013,1100,970,996,0,960,1028,1010,1018],
[1017,1028,1008,1146,1046,1082,1040,0,1070,1028,970],
[1040,990,926,1036,980,982,972,930,0,1004,1026],
[992,1004,964,1086,934,1023,990,972,996,0,991],
[970,995,949,1087,1009,1000,982,1030,974,1009,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 197, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,996,966,1021,1027,1006,949,943,950,958,994],
[1004,0,964,1027,1057,976,996,963,955,975,937],
[1034,1036,0,978,1037,1020,1017,956,978,982,1043],
[979,973,1022,0,1035,986,982,893,934,930,992],
[973,943,963,965,0,939,963,897,902,903,962],
[994,1024,980,1014,1061,0,1005,942,1025,971,1043],
[1051,1004,983,1018,1037,995,0,969,1021,995,1046],
[1057,1037,1044,1107,1103,1058,1031,0,1075,995,1083],
[1050,1045,1022,1066,1098,975,979,925,0,990,1012],
[1042,1025,1018,1070,1097,1029,1005,1005,1010,0,1000],
[1006,1063,957,1008,1038,957,954,917,988,1000,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 198, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,986,1011,1026,1010,991,1044,1012,1030,994,1033],
[1014,0,1000,1051,1018,977,1004,1007,1012,978,996],
[989,1000,0,1023,1030,976,1023,1030,1050,1002,1027],
[974,949,977,0,1005,953,980,989,989,943,958],
[990,982,970,995,0,959,975,996,998,979,1008],
[1009,1023,1024,1047,1041,0,1004,1001,1024,999,1044],
[956,996,977,1020,1025,996,0,986,1014,978,1000],
[988,993,970,1011,1004,999,1014,0,1030,982,1014],
[970,988,950,1011,1002,976,986,970,0,958,988],
[1006,1022,998,1057,1021,1001,1022,1018,1042,0,1036],
[967,1004,973,1042,992,956,1000,986,1012,964,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 199, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1005,956,967,998,919,986,966,948,914,983],
[995,0,938,1023,980,937,995,1026,976,969,995],
[1044,1062,0,1011,1005,1000,1047,994,1030,980,1019],
[1033,977,989,0,984,962,1042,963,1009,981,1017],
[1002,1020,995,1016,0,939,1033,988,1004,987,1015],
[1081,1063,1000,1038,1061,0,1072,1029,1018,1032,1059],
[1014,1005,953,958,967,928,0,970,951,927,1017],
[1034,974,1006,1037,1012,971,1030,0,996,972,1039],
[1052,1024,970,991,996,982,1049,1004,0,982,1025],
[1086,1031,1020,1019,1013,968,1073,1028,1018,0,1068],
[1017,1005,981,983,985,941,983,961,975,932,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2000, 200, "ME-PRCW", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/meprcw/meprcw_11_2000.csv", index=False, header=False)