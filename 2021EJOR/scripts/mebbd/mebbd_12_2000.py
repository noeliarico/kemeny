
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg
from kemeny import sc

rep = 1
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,1060,1077,984,1055,945,1026,1053,1002,1027,1000,1032],
[940,0,1055,952,963,972,986,1020,1000,922,970,983],
[923,945,0,895,914,916,952,951,890,924,907,954],
[1016,1048,1105,0,1045,992,1100,992,981,1003,990,1024],
[945,1037,1086,955,0,899,1004,1038,941,954,955,1024],
[1055,1028,1084,1008,1101,0,1046,1025,968,1046,1041,1073],
[974,1014,1048,900,996,954,0,982,980,993,912,942],
[947,980,1049,1008,962,975,1018,0,949,1013,953,996],
[998,1000,1110,1019,1059,1032,1020,1051,0,1052,989,1041],
[973,1078,1076,997,1046,954,1007,987,948,0,916,956],
[1000,1030,1093,1010,1045,959,1088,1047,1011,1084,0,1043],
[968,1017,1046,976,976,927,1058,1004,959,1044,957,0]])



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
result = np.append(np.array([12, 2000, 1, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,966,958,982,950,950,971,983,980,945,947,955],
[1034,0,996,995,1001,957,986,1016,1017,951,1015,991],
[1042,1004,0,997,1003,974,990,983,1020,992,993,989],
[1018,1005,1003,0,1014,988,981,1006,1004,989,980,992],
[1050,999,997,986,0,997,1038,1010,997,1005,1009,1004],
[1050,1043,1026,1012,1003,0,995,998,1006,991,1032,1008],
[1029,1014,1010,1019,962,1005,0,1006,1022,997,1000,1019],
[1017,984,1017,994,990,1002,994,0,982,948,993,963],
[1020,983,980,996,1003,994,978,1018,0,972,993,977],
[1055,1049,1008,1011,995,1009,1003,1052,1028,0,1034,1008],
[1053,985,1007,1020,991,968,1000,1007,1007,966,0,989],
[1045,1009,1011,1008,996,992,981,1037,1023,992,1011,0]])



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
result = np.append(np.array([12, 2000, 2, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,943,1284,1088,1043,1218,926,1219,1057,991,1207,878],
[1057,0,1061,1219,1012,866,848,988,1082,868,1400,1056],
[716,939,0,1041,923,766,730,1032,877,629,1220,812],
[912,781,959,0,919,817,746,925,1133,833,1086,784],
[957,988,1077,1081,0,849,876,1154,1202,660,1360,886],
[782,1134,1234,1183,1151,0,1032,1116,1250,1028,1337,800],
[1074,1152,1270,1254,1124,968,0,1409,1267,1246,1532,1321],
[781,1012,968,1075,846,884,591,0,890,952,1157,813],
[943,918,1123,867,798,750,733,1110,0,859,1242,687],
[1009,1132,1371,1167,1340,972,754,1048,1141,0,1337,926],
[793,600,780,914,640,663,468,843,758,663,0,735],
[1122,944,1188,1216,1114,1200,679,1187,1313,1074,1265,0]])



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
result = np.append(np.array([12, 2000, 3, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,849,823,1235,876,1232,782,921,775,885,1067,936],
[1151,0,923,1579,1111,1252,934,928,1285,1388,1016,1155],
[1177,1077,0,1138,1053,1265,1084,972,1300,1259,1125,900],
[765,421,862,0,506,729,507,681,745,922,790,675],
[1124,889,947,1494,0,1151,1017,1029,964,1058,847,1130],
[768,748,735,1271,849,0,950,662,1074,1024,803,1034],
[1218,1066,916,1493,983,1050,0,1090,922,1065,957,1171],
[1079,1072,1028,1319,971,1338,910,0,977,1100,1051,1134],
[1225,715,700,1255,1036,926,1078,1023,0,1124,1100,1073],
[1115,612,741,1078,942,976,935,900,876,0,1177,804],
[933,984,875,1210,1153,1197,1043,949,900,823,0,976],
[1064,845,1100,1325,870,966,829,866,927,1196,1024,0]])



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
result = np.append(np.array([12, 2000, 4, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,993,1001,964,1035,1023,1023,944,1011,968,1030,962],
[1007,0,995,1000,1006,1034,999,975,1016,1004,1010,982],
[999,1005,0,946,984,1007,1029,990,959,962,1012,954],
[1036,1000,1054,0,1002,1022,1016,1017,982,1011,1037,999],
[965,994,1016,998,0,982,993,972,961,925,1013,899],
[977,966,993,978,1018,0,969,929,962,971,961,978],
[977,1001,971,984,1007,1031,0,949,974,937,985,953],
[1056,1025,1010,983,1028,1071,1051,0,1058,1012,1040,1032],
[989,984,1041,1018,1039,1038,1026,942,0,987,1004,989],
[1032,996,1038,989,1075,1029,1063,988,1013,0,1023,986],
[970,990,988,963,987,1039,1015,960,996,977,0,941],
[1038,1018,1046,1001,1101,1022,1047,968,1011,1014,1059,0]])



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
result = np.append(np.array([12, 2000, 5, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,956,1053,925,905,859,945,999,884,1020,924,1009],
[1044,0,991,955,977,873,895,993,954,913,944,867],
[947,1009,0,945,1068,908,1031,978,824,880,883,961],
[1075,1045,1055,0,1039,988,1116,1030,893,926,973,1116],
[1095,1023,932,961,0,891,972,1040,857,937,956,980],
[1141,1127,1092,1012,1109,0,1168,1167,981,1069,1035,1021],
[1055,1105,969,884,1028,832,0,934,843,908,898,891],
[1001,1007,1022,970,960,833,1066,0,919,921,999,993],
[1116,1046,1176,1107,1143,1019,1157,1081,0,1127,987,1069],
[980,1087,1120,1074,1063,931,1092,1079,873,0,1055,1041],
[1076,1056,1117,1027,1044,965,1102,1001,1013,945,0,918],
[991,1133,1039,884,1020,979,1109,1007,931,959,1082,0]])



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
result = np.append(np.array([12, 2000, 6, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1029,1085,1108,1148,1122,959,1072,1105,1040,1096,1004],
[971,0,1055,1140,1054,1019,1004,1026,1052,1052,1022,1038],
[915,945,0,976,1002,1023,949,989,998,979,973,977],
[892,860,1024,0,1001,1004,958,994,957,1003,938,938],
[852,946,998,999,0,928,907,978,1011,998,1006,932],
[878,981,977,996,1072,0,968,1061,1006,981,1017,1036],
[1041,996,1051,1042,1093,1032,0,1013,1085,1029,1022,1038],
[928,974,1011,1006,1022,939,987,0,985,1007,1061,1011],
[895,948,1002,1043,989,994,915,1015,0,1022,985,954],
[960,948,1021,997,1002,1019,971,993,978,0,986,984],
[904,978,1027,1062,994,983,978,939,1015,1014,0,992],
[996,962,1023,1062,1068,964,962,989,1046,1016,1008,0]])



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
result = np.append(np.array([12, 2000, 7, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,965,998,1047,969,961,977,984,1026,1000,961,1069],
[1035,0,974,1038,992,1013,1022,1027,1061,1006,955,1085],
[1002,1026,0,1125,966,953,984,937,979,973,978,1026],
[953,962,875,0,929,890,962,929,944,967,918,1069],
[1031,1008,1034,1071,0,986,1016,980,992,1046,1070,1071],
[1039,987,1047,1110,1014,0,1029,1017,991,1007,1023,1041],
[1023,978,1016,1038,984,971,0,974,973,1010,953,1012],
[1016,973,1063,1071,1020,983,1026,0,1025,1039,967,1099],
[974,939,1021,1056,1008,1009,1027,975,0,994,935,1064],
[1000,994,1027,1033,954,993,990,961,1006,0,963,1056],
[1039,1045,1022,1082,930,977,1047,1033,1065,1037,0,1111],
[931,915,974,931,929,959,988,901,936,944,889,0]])



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
result = np.append(np.array([12, 2000, 8, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,993,1008,988,1032,1027,1044,995,976,954,990,1011],
[1007,0,936,1024,1025,971,1032,979,983,974,941,961],
[992,1064,0,962,1054,986,1062,962,1026,968,1004,957],
[1012,976,1038,0,992,1029,1046,980,1044,955,1040,983],
[968,975,946,1008,0,992,1009,975,1001,955,917,932],
[973,1029,1014,971,1008,0,1092,1045,1056,1030,1034,994],
[956,968,938,954,991,908,0,945,985,969,986,961],
[1005,1021,1038,1020,1025,955,1055,0,1039,1000,1011,945],
[1024,1017,974,956,999,944,1015,961,0,1018,980,948],
[1046,1026,1032,1045,1045,970,1031,1000,982,0,999,968],
[1010,1059,996,960,1083,966,1014,989,1020,1001,0,979],
[989,1039,1043,1017,1068,1006,1039,1055,1052,1032,1021,0]])



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
result = np.append(np.array([12, 2000, 9, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1014,1020,1013,1001,1052,1007,1005,1015,984,1018,1034],
[986,0,1008,1012,1006,1020,1029,979,1041,1000,1052,999],
[980,992,0,983,1023,1012,972,971,971,1015,1036,1027],
[987,988,1017,0,1046,1008,1045,999,1005,1010,1013,1029],
[999,994,977,954,0,994,992,1021,989,977,1033,1051],
[948,980,988,992,1006,0,997,974,1000,977,1023,1016],
[993,971,1028,955,1008,1003,0,984,982,1004,1009,995],
[995,1021,1029,1001,979,1026,1016,0,1017,984,1059,1036],
[985,959,1029,995,1011,1000,1018,983,0,960,1027,991],
[1016,1000,985,990,1023,1023,996,1016,1040,0,1057,1052],
[982,948,964,987,967,977,991,941,973,943,0,1005],
[966,1001,973,971,949,984,1005,964,1009,948,995,0]])



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
result = np.append(np.array([12, 2000, 10, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1050,1017,1036,1021,968,975,998,1021,1043,1025,1035],
[950,0,958,936,938,941,928,947,1030,1024,1038,998],
[983,1042,0,989,969,967,974,962,995,1040,995,1006],
[964,1064,1011,0,991,995,991,990,1042,1053,978,1013],
[979,1062,1031,1009,0,988,982,974,1013,1053,1013,992],
[1032,1059,1033,1005,1012,0,994,1001,998,1074,1034,1031],
[1025,1072,1026,1009,1018,1006,0,999,1049,1103,1040,1007],
[1002,1053,1038,1010,1026,999,1001,0,1060,1116,1059,1023],
[979,970,1005,958,987,1002,951,940,0,1021,1032,993],
[957,976,960,947,947,926,897,884,979,0,1000,938],
[975,962,1005,1022,987,966,960,941,968,1000,0,957],
[965,1002,994,987,1008,969,993,977,1007,1062,1043,0]])



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
result = np.append(np.array([12, 2000, 11, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,987,1034,1003,1022,1034,1027,1030,1089,986,1025,1006],
[1013,0,1031,1018,998,1018,1030,1028,1064,978,1020,1031],
[966,969,0,985,979,1001,997,1003,986,967,999,1001],
[997,982,1015,0,998,1003,1006,1032,1037,976,981,1020],
[978,1002,1021,1002,0,1024,1015,1030,1031,1003,1021,1012],
[966,982,999,997,976,0,1007,1026,1024,956,1003,989],
[973,970,1003,994,985,993,0,1007,1022,924,1011,973],
[970,972,997,968,970,974,993,0,1009,915,985,991],
[911,936,1014,963,969,976,978,991,0,921,971,968],
[1014,1022,1033,1024,997,1044,1076,1085,1079,0,1041,1045],
[975,980,1001,1019,979,997,989,1015,1029,959,0,999],
[994,969,999,980,988,1011,1027,1009,1032,955,1001,0]])



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
result = np.append(np.array([12, 2000, 12, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1006,998,1041,1003,1040,1042,1044,1013,1106,1031,1025],
[994,0,999,948,967,994,1015,998,963,1058,987,975],
[1002,1001,0,967,985,1001,1007,1009,966,1043,1012,1027],
[959,1052,1033,0,1027,1036,1032,1042,1012,1090,1048,1038],
[997,1033,1015,973,0,1011,1022,1022,990,1056,1009,1012],
[960,1006,999,964,989,0,1045,960,992,1056,1005,984],
[958,985,993,968,978,955,0,1000,967,1004,990,987],
[956,1002,991,958,978,1040,1000,0,993,1079,958,970],
[987,1037,1034,988,1010,1008,1033,1007,0,1051,994,1017],
[894,942,957,910,944,944,996,921,949,0,955,962],
[969,1013,988,952,991,995,1010,1042,1006,1045,0,998],
[975,1025,973,962,988,1016,1013,1030,983,1038,1002,0]])



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
result = np.append(np.array([12, 2000, 13, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,993,971,1017,974,1010,992,1013,978,990,1018,1025],
[1007,0,979,1041,980,1007,996,988,1020,998,1001,1028],
[1029,1021,0,1039,1025,1033,1034,997,1018,1026,1035,1043],
[983,959,961,0,954,975,1011,966,983,1019,996,984],
[1026,1020,975,1046,0,1022,1007,1016,998,1006,1025,1057],
[990,993,967,1025,978,0,991,1004,994,990,973,1015],
[1008,1004,966,989,993,1009,0,994,1001,1006,1013,1027],
[987,1012,1003,1034,984,996,1006,0,1028,1021,976,1031],
[1022,980,982,1017,1002,1006,999,972,0,1011,998,993],
[1010,1002,974,981,994,1010,994,979,989,0,990,1033],
[982,999,965,1004,975,1027,987,1024,1002,1010,0,1057],
[975,972,957,1016,943,985,973,969,1007,967,943,0]])



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
result = np.append(np.array([12, 2000, 14, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1033,1023,1031,995,1011,996,998,1019,1044,1037,1001],
[967,0,990,1009,990,1001,966,1001,964,994,971,961],
[977,1010,0,1017,1002,975,1001,1001,966,986,1013,994],
[969,991,983,0,944,993,958,980,935,962,969,988],
[1005,1010,998,1056,0,1017,976,981,1000,995,995,959],
[989,999,1025,1007,983,0,952,968,971,999,993,984],
[1004,1034,999,1042,1024,1048,0,1021,1016,1023,1029,999],
[1002,999,999,1020,1019,1032,979,0,985,991,972,997],
[981,1036,1034,1065,1000,1029,984,1015,0,1018,973,1007],
[956,1006,1014,1038,1005,1001,977,1009,982,0,1029,1013],
[963,1029,987,1031,1005,1007,971,1028,1027,971,0,1020],
[999,1039,1006,1012,1041,1016,1001,1003,993,987,980,0]])



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
result = np.append(np.array([12, 2000, 15, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1050,1035,1017,977,1011,999,1025,997,989,1022,1016],
[950,0,1015,1027,949,1004,982,1014,950,972,988,971],
[965,985,0,979,996,998,930,999,987,967,977,961],
[983,973,1021,0,934,971,918,1022,1005,938,985,989],
[1023,1051,1004,1066,0,1042,1010,1096,1007,965,1028,1014],
[989,996,1002,1029,958,0,966,1022,993,958,993,949],
[1001,1018,1070,1082,990,1034,0,1078,1001,969,1044,997],
[975,986,1001,978,904,978,922,0,959,911,956,926],
[1003,1050,1013,995,993,1007,999,1041,0,989,1018,1010],
[1011,1028,1033,1062,1035,1042,1031,1089,1011,0,1014,980],
[978,1012,1023,1015,972,1007,956,1044,982,986,0,994],
[984,1029,1039,1011,986,1051,1003,1074,990,1020,1006,0]])



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
result = np.append(np.array([12, 2000, 16, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,937,1041,1034,1045,1027,905,991,1020,983,1037,1020],
[1063,0,1023,1055,1047,1000,992,1090,1035,998,1027,994],
[959,977,0,986,985,955,895,951,1027,958,950,1011],
[966,945,1014,0,995,957,969,1027,1031,954,976,941],
[955,953,1015,1005,0,907,987,986,1018,948,985,953],
[973,1000,1045,1043,1093,0,1004,1037,1064,1011,1048,1019],
[1095,1008,1105,1031,1013,996,0,1065,1076,1008,1043,971],
[1009,910,1049,973,1014,963,935,0,1085,1005,995,968],
[980,965,973,969,982,936,924,915,0,924,930,920],
[1017,1002,1042,1046,1052,989,992,995,1076,0,1008,980],
[963,973,1050,1024,1015,952,957,1005,1070,992,0,978],
[980,1006,989,1059,1047,981,1029,1032,1080,1020,1022,0]])



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
result = np.append(np.array([12, 2000, 17, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1005,1014,1076,1050,985,1065,1009,1042,1012,1031,994],
[995,0,1002,1057,981,973,1057,1039,1023,992,1000,988],
[986,998,0,1035,1033,1019,1044,1011,1035,989,1021,1020],
[924,943,965,0,996,958,989,1001,1004,992,967,976],
[950,1019,967,1004,0,967,1019,984,1028,987,993,973],
[1015,1027,981,1042,1033,0,1060,1040,1035,1003,998,1022],
[935,943,956,1011,981,940,0,1008,1008,983,950,978],
[991,961,989,999,1016,960,992,0,988,994,991,980],
[958,977,965,996,972,965,992,1012,0,1001,1004,969],
[988,1008,1011,1008,1013,997,1017,1006,999,0,1008,992],
[969,1000,979,1033,1007,1002,1050,1009,996,992,0,981],
[1006,1012,980,1024,1027,978,1022,1020,1031,1008,1019,0]])



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
result = np.append(np.array([12, 2000, 18, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,979,1002,1044,965,1012,1003,998,1055,1001,1002,1055],
[1021,0,978,1019,984,1013,1009,1024,1038,977,1043,1004],
[998,1022,0,1012,993,1016,1022,976,1093,1007,1043,1031],
[956,981,988,0,985,1041,1011,982,1059,1004,1011,1007],
[1035,1016,1007,1015,0,1013,1038,971,1064,1006,1047,1028],
[988,987,984,959,987,0,994,995,1041,1019,995,1050],
[997,991,978,989,962,1006,0,938,1052,992,1011,1037],
[1002,976,1024,1018,1029,1005,1062,0,1071,1017,1049,1061],
[945,962,907,941,936,959,948,929,0,986,985,987],
[999,1023,993,996,994,981,1008,983,1014,0,1011,1033],
[998,957,957,989,953,1005,989,951,1015,989,0,976],
[945,996,969,993,972,950,963,939,1013,967,1024,0]])



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
result = np.append(np.array([12, 2000, 19, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1051,1074,1030,1030,992,1040,1016,1024,1043,1013,1026],
[949,0,957,979,900,906,958,897,1004,907,910,949],
[926,1043,0,1019,960,979,1055,970,1011,990,982,995],
[970,1021,981,0,990,964,1003,916,926,936,940,983],
[970,1100,1040,1010,0,995,1040,943,973,953,990,1037],
[1008,1094,1021,1036,1005,0,1070,966,1053,973,1043,991],
[960,1042,945,997,960,930,0,962,987,942,949,991],
[984,1103,1030,1084,1057,1034,1038,0,1018,1060,1026,1045],
[976,996,989,1074,1027,947,1013,982,0,956,1032,1013],
[957,1093,1010,1064,1047,1027,1058,940,1044,0,1020,1044],
[987,1090,1018,1060,1010,957,1051,974,968,980,0,1031],
[974,1051,1005,1017,963,1009,1009,955,987,956,969,0]])



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
result = np.append(np.array([12, 2000, 20, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,984,999,1022,987,960,1003,944,966,977,1008,1034],
[1016,0,993,1004,960,932,1037,929,1014,1013,949,1048],
[1001,1007,0,1044,1078,1067,1067,1032,987,1044,1022,1020],
[978,996,956,0,966,972,1012,948,951,994,965,1010],
[1013,1040,922,1034,0,928,1021,979,946,965,965,990],
[1040,1068,933,1028,1072,0,1018,983,987,1033,1037,1044],
[997,963,933,988,979,982,0,973,978,1003,947,965],
[1056,1071,968,1052,1021,1017,1027,0,960,1080,1036,1003],
[1034,986,1013,1049,1054,1013,1022,1040,0,997,1017,997],
[1023,987,956,1006,1035,967,997,920,1003,0,966,957],
[992,1051,978,1035,1035,963,1053,964,983,1034,0,1000],
[966,952,980,990,1010,956,1035,997,1003,1043,1000,0]])



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
result = np.append(np.array([12, 2000, 21, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1046,1070,992,1024,1055,1034,1031,1052,1037,1092,995],
[954,0,1044,982,958,975,992,966,1016,994,1068,987],
[930,956,0,932,975,958,956,955,986,986,953,932],
[1008,1018,1068,0,1046,1048,997,966,1042,1030,1036,1034],
[976,1042,1025,954,0,1011,957,1004,976,984,1032,975],
[945,1025,1042,952,989,0,1035,1003,1049,1040,1079,992],
[966,1008,1044,1003,1043,965,0,966,1049,1006,1106,1020],
[969,1034,1045,1034,996,997,1034,0,1038,994,1047,993],
[948,984,1014,958,1024,951,951,962,0,971,1019,963],
[963,1006,1014,970,1016,960,994,1006,1029,0,1039,979],
[908,932,1047,964,968,921,894,953,981,961,0,957],
[1005,1013,1068,966,1025,1008,980,1007,1037,1021,1043,0]])



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
result = np.append(np.array([12, 2000, 22, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1014,973,946,990,1007,875,947,969,990,980,975],
[986,0,906,920,975,986,915,934,1011,929,929,976],
[1027,1094,0,985,1020,1047,990,989,1022,1011,1011,1013],
[1054,1080,1015,0,1075,1045,1001,1039,1030,965,1020,1021],
[1010,1025,980,925,0,1047,963,976,999,1016,1013,1019],
[993,1014,953,955,953,0,970,977,959,1010,919,949],
[1125,1085,1010,999,1037,1030,0,1013,1023,1036,1077,999],
[1053,1066,1011,961,1024,1023,987,0,1007,1079,968,1091],
[1031,989,978,970,1001,1041,977,993,0,996,996,1005],
[1010,1071,989,1035,984,990,964,921,1004,0,989,1054],
[1020,1071,989,980,987,1081,923,1032,1004,1011,0,1055],
[1025,1024,987,979,981,1051,1001,909,995,946,945,0]])



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
result = np.append(np.array([12, 2000, 23, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1047,989,1032,953,1085,973,1010,1048,1024,1093,974],
[953,0,981,1027,968,1006,950,911,983,1029,1008,976],
[1011,1019,0,1109,1014,1075,1017,986,1014,1024,1043,1021],
[968,973,891,0,929,944,880,967,966,956,994,883],
[1047,1032,986,1071,0,1132,1048,984,1015,1062,1050,978],
[915,994,925,1056,868,0,959,920,976,940,1047,1008],
[1027,1050,983,1120,952,1041,0,941,1017,1046,1043,949],
[990,1089,1014,1033,1016,1080,1059,0,1026,1012,1115,1024],
[952,1017,986,1034,985,1024,983,974,0,976,1041,896],
[976,971,976,1044,938,1060,954,988,1024,0,1023,976],
[907,992,957,1006,950,953,957,885,959,977,0,856],
[1026,1024,979,1117,1022,992,1051,976,1104,1024,1144,0]])



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
result = np.append(np.array([12, 2000, 24, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1018,992,986,1030,1071,1095,984,1044,981,1043,1051],
[982,0,977,956,1024,1025,1001,970,1004,988,1001,1001],
[1008,1023,0,998,971,1078,1057,1027,1066,986,1022,1019],
[1014,1044,1002,0,1002,1075,1052,1034,987,997,1069,1021],
[970,976,1029,998,0,1101,1056,1003,1069,1000,990,992],
[929,975,922,925,899,0,993,936,987,885,969,943],
[905,999,943,948,944,1007,0,976,997,911,953,971],
[1016,1030,973,966,997,1064,1024,0,1031,1057,1017,987],
[956,996,934,1013,931,1013,1003,969,0,954,924,1017],
[1019,1012,1014,1003,1000,1115,1089,943,1046,0,1064,1017],
[957,999,978,931,1010,1031,1047,983,1076,936,0,953],
[949,999,981,979,1008,1057,1029,1013,983,983,1047,0]])



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
result = np.append(np.array([12, 2000, 25, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1072,939,1008,971,1094,993,1062,965,1153,1035,981],
[928,0,880,988,957,1009,963,972,1000,994,882,856],
[1061,1120,0,971,957,977,1017,1071,1127,1020,1016,976],
[992,1012,1029,0,986,985,1080,1136,1065,1061,1008,954],
[1029,1043,1043,1014,0,1007,1068,1037,1046,1153,941,1012],
[906,991,1023,1015,993,0,1017,1014,951,1029,924,909],
[1007,1037,983,920,932,983,0,1008,1026,1053,967,952],
[938,1028,929,864,963,986,992,0,1011,997,962,893],
[1035,1000,873,935,954,1049,974,989,0,1089,963,975],
[847,1006,980,939,847,971,947,1003,911,0,990,855],
[965,1118,984,992,1059,1076,1033,1038,1037,1010,0,976],
[1019,1144,1024,1046,988,1091,1048,1107,1025,1145,1024,0]])



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
result = np.append(np.array([12, 2000, 26, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,981,1007,978,969,1013,1018,970,978,1001,999,992],
[1019,0,1024,986,992,1032,1035,970,1003,1007,1012,1004],
[993,976,0,980,962,1045,980,953,1006,1004,1001,948],
[1022,1014,1020,0,984,1006,1024,1010,990,1005,1034,1026],
[1031,1008,1038,1016,0,1050,1017,1012,994,1004,1032,1013],
[987,968,955,994,950,0,1001,986,954,975,978,953],
[982,965,1020,976,983,999,0,1010,986,981,1007,1006],
[1030,1030,1047,990,988,1014,990,0,991,981,1018,1022],
[1022,997,994,1010,1006,1046,1014,1009,0,1016,997,995],
[999,993,996,995,996,1025,1019,1019,984,0,996,997],
[1001,988,999,966,968,1022,993,982,1003,1004,0,980],
[1008,996,1052,974,987,1047,994,978,1005,1003,1020,0]])



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
result = np.append(np.array([12, 2000, 27, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1072,987,969,953,993,1006,1034,955,1004,1002,943],
[928,0,925,928,903,936,965,963,937,917,948,918],
[1013,1075,0,1002,970,1016,972,1052,996,1013,1057,985],
[1031,1072,998,0,964,1033,1027,1001,982,997,1052,974],
[1047,1097,1030,1036,0,996,1042,1065,1011,1011,1035,972],
[1007,1064,984,967,1004,0,1041,990,952,957,1005,968],
[994,1035,1028,973,958,959,0,1033,950,1017,1002,949],
[966,1037,948,999,935,1010,967,0,943,932,984,961],
[1045,1063,1004,1018,989,1048,1050,1057,0,984,1097,996],
[996,1083,987,1003,989,1043,983,1068,1016,0,1031,1028],
[998,1052,943,948,965,995,998,1016,903,969,0,954],
[1057,1082,1015,1026,1028,1032,1051,1039,1004,972,1046,0]])



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
result = np.append(np.array([12, 2000, 28, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,998,979,1040,981,1001,993,984,1005,967,1016,998],
[1002,0,1026,1012,1033,1013,998,1046,1025,1018,932,1000],
[1021,974,0,986,970,1025,1016,1039,1008,916,950,1009],
[960,988,1014,0,967,973,943,1010,925,922,949,988],
[1019,967,1030,1033,0,987,986,1030,1051,962,1014,995],
[999,987,975,1027,1013,0,971,1005,992,943,977,980],
[1007,1002,984,1057,1014,1029,0,971,1026,988,976,1029],
[1016,954,961,990,970,995,1029,0,993,933,950,1011],
[995,975,992,1075,949,1008,974,1007,0,945,958,990],
[1033,982,1084,1078,1038,1057,1012,1067,1055,0,1054,1123],
[984,1068,1050,1051,986,1023,1024,1050,1042,946,0,1034],
[1002,1000,991,1012,1005,1020,971,989,1010,877,966,0]])



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
result = np.append(np.array([12, 2000, 29, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1005,992,1042,1000,990,962,964,1030,992,987,999],
[995,0,1008,991,1009,995,976,965,979,990,995,1001],
[1008,992,0,997,968,980,974,944,990,984,1010,977],
[958,1009,1003,0,964,975,970,932,998,954,966,973],
[1000,991,1032,1036,0,999,972,988,1032,1008,1005,1050],
[1010,1005,1020,1025,1001,0,968,992,1002,1010,986,969],
[1038,1024,1026,1030,1028,1032,0,974,1009,997,1015,1031],
[1036,1035,1056,1068,1012,1008,1026,0,1045,993,1001,1034],
[970,1021,1010,1002,968,998,991,955,0,988,982,1000],
[1008,1010,1016,1046,992,990,1003,1007,1012,0,983,1037],
[1013,1005,990,1034,995,1014,985,999,1018,1017,0,1001],
[1001,999,1023,1027,950,1031,969,966,1000,963,999,0]])



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
result = np.append(np.array([12, 2000, 30, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1013,972,1025,1041,1043,1015,1024,1028,1018,1021,1016],
[987,0,974,1001,1022,1015,967,998,1022,999,996,1031],
[1028,1026,0,993,1046,1028,974,1032,1009,1037,1014,1039],
[975,999,1007,0,1013,1004,976,1030,1010,1007,1022,1014],
[959,978,954,987,0,996,975,1008,964,992,996,979],
[957,985,972,996,1004,0,964,997,979,976,963,1014],
[985,1033,1026,1024,1025,1036,0,1053,1019,1017,1020,1039],
[976,1002,968,970,992,1003,947,0,998,974,982,982],
[972,978,991,990,1036,1021,981,1002,0,968,988,1002],
[982,1001,963,993,1008,1024,983,1026,1032,0,1000,996],
[979,1004,986,978,1004,1037,980,1018,1012,1000,0,1008],
[984,969,961,986,1021,986,961,1018,998,1004,992,0]])



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
result = np.append(np.array([12, 2000, 31, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,870,822,932,937,916,990,1057,965,884,926,898],
[1130,0,952,1005,1097,1039,1112,1171,1052,915,1036,1029],
[1178,1048,0,1087,1105,1019,1036,1122,1100,963,1007,972],
[1068,995,913,0,1066,1023,938,1158,1036,898,965,936],
[1063,903,895,934,0,980,946,1074,1017,888,942,903],
[1084,961,981,977,1020,0,1037,1101,980,983,968,955],
[1010,888,964,1062,1054,963,0,1170,1090,940,982,976],
[943,829,878,842,926,899,830,0,901,836,840,850],
[1035,948,900,964,983,1020,910,1099,0,922,902,939],
[1116,1085,1037,1102,1112,1017,1060,1164,1078,0,993,1017],
[1074,964,993,1035,1058,1032,1018,1160,1098,1007,0,1007],
[1102,971,1028,1064,1097,1045,1024,1150,1061,983,993,0]])



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
result = np.append(np.array([12, 2000, 32, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,985,1001,987,1012,1001,960,1006,955,1027,1002,1024],
[1015,0,986,1038,1019,1017,1021,1023,984,1014,1057,1010],
[999,1014,0,990,1032,981,1019,983,979,1043,1060,1007],
[1013,962,1010,0,1055,1043,1000,996,1014,1031,1027,1026],
[988,981,968,945,0,956,976,962,940,1002,1020,960],
[999,983,1019,957,1044,0,1015,1004,986,1051,1037,1022],
[1040,979,981,1000,1024,985,0,1032,957,1019,1044,1022],
[994,977,1017,1004,1038,996,968,0,970,994,987,993],
[1045,1016,1021,986,1060,1014,1043,1030,0,1068,1024,1031],
[973,986,957,969,998,949,981,1006,932,0,1015,928],
[998,943,940,973,980,963,956,1013,976,985,0,985],
[976,990,993,974,1040,978,978,1007,969,1072,1015,0]])



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
result = np.append(np.array([12, 2000, 33, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1014,978,1002,983,984,1018,941,996,1009,1012,999],
[986,0,1005,977,1007,964,976,937,937,1007,1059,963],
[1022,995,0,955,956,979,1011,977,983,950,1000,951],
[998,1023,1045,0,999,1046,977,1005,999,1001,1050,999],
[1017,993,1044,1001,0,1018,1047,987,1003,1054,1056,1028],
[1016,1036,1021,954,982,0,1003,1007,981,985,1025,956],
[982,1024,989,1023,953,997,0,935,1005,1014,1069,986],
[1059,1063,1023,995,1013,993,1065,0,974,1040,1059,1038],
[1004,1063,1017,1001,997,1019,995,1026,0,1021,1075,985],
[991,993,1050,999,946,1015,986,960,979,0,1032,956],
[988,941,1000,950,944,975,931,941,925,968,0,952],
[1001,1037,1049,1001,972,1044,1014,962,1015,1044,1048,0]])



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
result = np.append(np.array([12, 2000, 34, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,964,968,1010,983,979,1024,993,1004,986,1006,999],
[1036,0,998,1039,981,983,979,1029,1010,990,1010,1014],
[1032,1002,0,1019,979,999,1011,1031,1023,1012,1030,992],
[990,961,981,0,972,967,1008,1007,1036,995,1008,991],
[1017,1019,1021,1028,0,993,1010,1036,1017,996,1036,1004],
[1021,1017,1001,1033,1007,0,1000,1004,1034,999,1040,1020],
[976,1021,989,992,990,1000,0,1016,1004,1000,1014,1046],
[1007,971,969,993,964,996,984,0,983,1001,1018,1014],
[996,990,977,964,983,966,996,1017,0,965,1023,988],
[1014,1010,988,1005,1004,1001,1000,999,1035,0,1025,992],
[994,990,970,992,964,960,986,982,977,975,0,986],
[1001,986,1008,1009,996,980,954,986,1012,1008,1014,0]])



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
result = np.append(np.array([12, 2000, 35, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,979,1004,995,1013,956,958,957,999,1031,1004,1043],
[1021,0,1011,986,1008,1006,1009,1025,1005,998,982,1035],
[996,989,0,985,954,993,960,1003,954,1005,956,980],
[1005,1014,1015,0,1012,1070,982,1017,1013,1029,995,1047],
[987,992,1046,988,0,999,1001,973,962,975,960,1021],
[1044,994,1007,930,1001,0,993,997,1006,1011,964,1018],
[1042,991,1040,1018,999,1007,0,1024,1004,1032,965,1008],
[1043,975,997,983,1027,1003,976,0,950,994,1032,1019],
[1001,995,1046,987,1038,994,996,1050,0,1010,979,1041],
[969,1002,995,971,1025,989,968,1006,990,0,984,1015],
[996,1018,1044,1005,1040,1036,1035,968,1021,1016,0,1037],
[957,965,1020,953,979,982,992,981,959,985,963,0]])



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
result = np.append(np.array([12, 2000, 36, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1056,985,1007,1042,1026,971,1068,1084,1030,1026,1152],
[944,0,924,1003,1014,986,954,1033,1072,977,996,948],
[1015,1076,0,1032,1000,997,980,1045,1092,969,1051,1023],
[993,997,968,0,1053,1021,926,985,991,1043,942,1042],
[958,986,1000,947,0,966,983,1021,902,963,925,957],
[974,1014,1003,979,1034,0,988,1033,972,1019,1009,1006],
[1029,1046,1020,1074,1017,1012,0,1106,990,1063,1035,1088],
[932,967,955,1015,979,967,894,0,996,909,956,1030],
[916,928,908,1009,1098,1028,1010,1004,0,1046,976,954],
[970,1023,1031,957,1037,981,937,1091,954,0,989,978],
[974,1004,949,1058,1075,991,965,1044,1024,1011,0,927],
[848,1052,977,958,1043,994,912,970,1046,1022,1073,0]])



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
result = np.append(np.array([12, 2000, 37, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1087,1022,1008,999,1042,1041,1027,986,1110,1016,1005],
[913,0,938,977,968,985,972,1013,917,1027,993,927],
[978,1062,0,996,1049,1084,971,1047,987,1034,985,982],
[992,1023,1004,0,965,1024,992,1023,1013,1053,1007,977],
[1001,1032,951,1035,0,1056,952,1043,1035,1047,1020,1006],
[958,1015,916,976,944,0,964,988,939,959,973,981],
[959,1028,1029,1008,1048,1036,0,1025,960,1022,1019,985],
[973,987,953,977,957,1012,975,0,991,1004,961,995],
[1014,1083,1013,987,965,1061,1040,1009,0,1065,1012,986],
[890,973,966,947,953,1041,978,996,935,0,968,981],
[984,1007,1015,993,980,1027,981,1039,988,1032,0,1025],
[995,1073,1018,1023,994,1019,1015,1005,1014,1019,975,0]])



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
result = np.append(np.array([12, 2000, 38, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,952,988,1056,1026,979,962,1030,1081,1003,1017,1067],
[1048,0,1023,1063,1007,994,966,1018,1066,991,1064,1001],
[1012,977,0,1077,1031,1069,990,1026,1106,1043,1037,1040],
[944,937,923,0,992,960,879,953,1044,905,982,982],
[974,993,969,1008,0,1017,982,970,1129,1004,1075,1051],
[1021,1006,931,1040,983,0,1004,955,1031,1049,1019,945],
[1038,1034,1010,1121,1018,996,0,970,1110,984,1043,1064],
[970,982,974,1047,1030,1045,1030,0,1074,1070,1062,1052],
[919,934,894,956,871,969,890,926,0,885,936,928],
[997,1009,957,1095,996,951,1016,930,1115,0,950,994],
[983,936,963,1018,925,981,957,938,1064,1050,0,1036],
[933,999,960,1018,949,1055,936,948,1072,1006,964,0]])



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
result = np.append(np.array([12, 2000, 39, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,999,932,1004,992,1063,1006,880,950,1047,1007,1050],
[1001,0,1061,1054,1054,1056,1040,977,940,990,979,954],
[1068,939,0,915,978,1011,987,941,937,987,1056,998],
[996,946,1085,0,987,1136,1026,878,948,961,979,1008],
[1008,946,1022,1013,0,1021,1021,935,1058,1015,991,1113],
[937,944,989,864,979,0,954,937,906,937,964,975],
[994,960,1013,974,979,1046,0,889,1005,938,991,1042],
[1120,1023,1059,1122,1065,1063,1111,0,987,1093,1121,1095],
[1050,1060,1063,1052,942,1094,995,1013,0,997,1024,1090],
[953,1010,1013,1039,985,1063,1062,907,1003,0,959,1083],
[993,1021,944,1021,1009,1036,1009,879,976,1041,0,1012],
[950,1046,1002,992,887,1025,958,905,910,917,988,0]])



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
result = np.append(np.array([12, 2000, 40, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1159,952,882,903,1094,991,920,929,980,1060,965],
[841,0,760,835,773,810,691,780,858,864,851,887],
[1048,1240,0,1018,1033,940,1066,1011,1120,1067,996,1066],
[1118,1165,982,0,1084,1152,1148,986,1098,1123,1117,1143],
[1097,1227,967,916,0,1094,954,952,939,1075,1032,1030],
[906,1190,1060,848,906,0,926,928,877,999,1033,882],
[1009,1309,934,852,1046,1074,0,1031,1033,1128,954,1087],
[1080,1220,989,1014,1048,1072,969,0,1131,1066,945,1116],
[1071,1142,880,902,1061,1123,967,869,0,1112,1100,1070],
[1020,1136,933,877,925,1001,872,934,888,0,1037,1047],
[940,1149,1004,883,968,967,1046,1055,900,963,0,1003],
[1035,1113,934,857,970,1118,913,884,930,953,997,0]])



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
result = np.append(np.array([12, 2000, 41, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,994,1083,1006,1084,1023,1054,1118,1105,929,1024,1087],
[1006,0,893,1094,899,1029,1029,984,1030,881,1024,1051],
[917,1107,0,1062,991,974,971,1024,1097,1010,1033,988],
[994,906,938,0,1032,993,1060,1093,1031,916,964,1038],
[916,1101,1009,968,0,924,994,977,1015,880,983,1153],
[977,971,1026,1007,1076,0,1033,1018,999,935,1065,1095],
[946,971,1029,940,1006,967,0,1064,1075,969,950,1095],
[882,1016,976,907,1023,982,936,0,843,952,1023,1104],
[895,970,903,969,985,1001,925,1157,0,987,945,1032],
[1071,1119,990,1084,1120,1065,1031,1048,1013,0,1133,1098],
[976,976,967,1036,1017,935,1050,977,1055,867,0,980],
[913,949,1012,962,847,905,905,896,968,902,1020,0]])



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
result = np.append(np.array([12, 2000, 42, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,926,947,901,909,958,955,919,1013,909,894,1004],
[1074,0,976,1035,1094,959,1031,1099,1070,960,1080,1083],
[1053,1024,0,927,1062,1037,1070,1083,1070,1017,1023,1120],
[1099,965,1073,0,988,1023,1014,1055,1042,886,990,1101],
[1091,906,938,1012,0,955,996,1027,1035,940,962,939],
[1042,1041,963,977,1045,0,1077,1099,1075,1035,1015,1123],
[1045,969,930,986,1004,923,0,1057,1001,955,964,986],
[1081,901,917,945,973,901,943,0,1004,887,921,1012],
[987,930,930,958,965,925,999,996,0,840,949,1011],
[1091,1040,983,1114,1060,965,1045,1113,1160,0,1069,1142],
[1106,920,977,1010,1038,985,1036,1079,1051,931,0,1016],
[996,917,880,899,1061,877,1014,988,989,858,984,0]])



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
result = np.append(np.array([12, 2000, 43, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,918,1008,979,932,947,958,934,977,1040,995,956],
[1082,0,1025,1021,996,1051,1011,968,1049,1111,1021,1015],
[992,975,0,944,981,997,972,927,998,998,979,956],
[1021,979,1056,0,988,1027,981,1002,1017,1017,1023,962],
[1068,1004,1019,1012,0,991,986,988,1051,1016,1007,1032],
[1053,949,1003,973,1009,0,988,946,1016,1035,979,976],
[1042,989,1028,1019,1014,1012,0,984,1026,1072,1030,976],
[1066,1032,1073,998,1012,1054,1016,0,1061,1074,1058,1009],
[1023,951,1002,983,949,984,974,939,0,1035,988,957],
[960,889,1002,983,984,965,928,926,965,0,992,976],
[1005,979,1021,977,993,1021,970,942,1012,1008,0,1025],
[1044,985,1044,1038,968,1024,1024,991,1043,1024,975,0]])



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
result = np.append(np.array([12, 2000, 44, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1122,1031,970,1102,1068,978,1147,1035,1110,1199,939],
[878,0,818,816,816,851,1035,915,878,936,991,805],
[969,1182,0,968,1024,1057,1055,1068,991,1090,1023,980],
[1030,1184,1032,0,1077,978,1083,1066,977,1040,1142,986],
[898,1184,976,923,0,1025,1051,1197,1047,1045,1141,970],
[932,1149,943,1022,975,0,1040,1110,987,1002,1074,987],
[1022,965,945,917,949,960,0,973,1023,994,958,962],
[853,1085,932,934,803,890,1027,0,940,1007,963,932],
[965,1122,1009,1023,953,1013,977,1060,0,1082,1150,1010],
[890,1064,910,960,955,998,1006,993,918,0,1041,952],
[801,1009,977,858,859,926,1042,1037,850,959,0,869],
[1061,1195,1020,1014,1030,1013,1038,1068,990,1048,1131,0]])



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
result = np.append(np.array([12, 2000, 45, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,998,1095,1058,1060,1002,1009,1062,1041,1062,1159,1035],
[1002,0,968,922,972,873,981,1022,1044,954,1017,964],
[905,1032,0,962,985,952,988,1021,972,1003,1011,999],
[942,1078,1038,0,1066,952,964,1122,1060,1059,1031,1036],
[940,1028,1015,934,0,1004,958,1068,1020,1004,994,1010],
[998,1127,1048,1048,996,0,925,1079,1010,1034,1053,1037],
[991,1019,1012,1036,1042,1075,0,1104,1072,1061,1106,1064],
[938,978,979,878,932,921,896,0,962,1019,982,961],
[959,956,1028,940,980,990,928,1038,0,1014,1017,1060],
[938,1046,997,941,996,966,939,981,986,0,1009,959],
[841,983,989,969,1006,947,894,1018,983,991,0,1012],
[965,1036,1001,964,990,963,936,1039,940,1041,988,0]])



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
result = np.append(np.array([12, 2000, 46, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,974,983,925,958,940,980,1030,935,955,939,985],
[1026,0,1061,1011,1056,1042,980,1024,1002,1000,1074,1034],
[1017,939,0,941,978,1017,980,986,917,966,1010,939],
[1075,989,1059,0,993,996,934,1015,957,981,980,1000],
[1042,944,1022,1007,0,1039,1003,1027,946,983,1001,1013],
[1060,958,983,1004,961,0,970,1069,987,965,962,1001],
[1020,1020,1020,1066,997,1030,0,1025,1021,1020,1005,982],
[970,976,1014,985,973,931,975,0,990,991,974,980],
[1065,998,1083,1043,1054,1013,979,1010,0,1018,1070,1029],
[1045,1000,1034,1019,1017,1035,980,1009,982,0,1005,1001],
[1061,926,990,1020,999,1038,995,1026,930,995,0,987],
[1015,966,1061,1000,987,999,1018,1020,971,999,1013,0]])



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
result = np.append(np.array([12, 2000, 47, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,943,1007,956,917,984,929,1012,988,1006,1055,985],
[1057,0,1132,990,1072,1030,976,1119,1080,1085,1121,986],
[993,868,0,949,1004,941,917,1001,981,942,998,969],
[1044,1010,1051,0,1035,1049,971,1137,1081,1067,1049,1068],
[1083,928,996,965,0,980,942,1002,985,1039,1040,1028],
[1016,970,1059,951,1020,0,1001,1062,1025,1041,1039,983],
[1071,1024,1083,1029,1058,999,0,1078,1064,1096,1070,1048],
[988,881,999,863,998,938,922,0,986,936,1030,940],
[1012,920,1019,919,1015,975,936,1014,0,1002,1035,999],
[994,915,1058,933,961,959,904,1064,998,0,1027,918],
[945,879,1002,951,960,961,930,970,965,973,0,966],
[1015,1014,1031,932,972,1017,952,1060,1001,1082,1034,0]])



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
result = np.append(np.array([12, 2000, 48, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,933,982,990,966,983,960,965,967,949,991,964],
[1067,0,1069,1052,1070,1011,1011,1023,1025,998,1025,993],
[1018,931,0,1004,1006,976,1017,962,976,971,966,968],
[1010,948,996,0,990,957,1030,977,1012,970,957,946],
[1034,930,994,1010,0,999,1003,988,975,992,928,1026],
[1017,989,1024,1043,1001,0,948,1011,1017,993,1006,1004],
[1040,989,983,970,997,1052,0,984,1000,984,978,962],
[1035,977,1038,1023,1012,989,1016,0,981,994,1026,1002],
[1033,975,1024,988,1025,983,1000,1019,0,1032,1026,1035],
[1051,1002,1029,1030,1008,1007,1016,1006,968,0,1016,1009],
[1009,975,1034,1043,1072,994,1022,974,974,984,0,973],
[1036,1007,1032,1054,974,996,1038,998,965,991,1027,0]])



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
result = np.append(np.array([12, 2000, 49, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1005,1004,983,1019,1006,1049,989,983,1008,1020,1012],
[995,0,994,966,1035,987,1026,991,996,976,1016,1005],
[996,1006,0,970,1018,1020,1028,993,960,980,993,1021],
[1017,1034,1030,0,1030,988,1047,991,1012,1002,1030,1020],
[981,965,982,970,0,945,1011,972,978,940,991,972],
[994,1013,980,1012,1055,0,1042,1001,990,976,1027,1001],
[951,974,972,953,989,958,0,972,957,949,986,988],
[1011,1009,1007,1009,1028,999,1028,0,986,990,1035,1019],
[1017,1004,1040,988,1022,1010,1043,1014,0,1002,1026,1010],
[992,1024,1020,998,1060,1024,1051,1010,998,0,1050,1034],
[980,984,1007,970,1009,973,1014,965,974,950,0,1008],
[988,995,979,980,1028,999,1012,981,990,966,992,0]])



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
result = np.append(np.array([12, 2000, 50, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,999,1017,1016,1006,994,981,1025,1025,1008,1039,992],
[1001,0,1026,1037,1029,1017,984,1004,958,1027,1044,995],
[983,974,0,1017,1004,944,965,1012,965,998,1010,977],
[984,963,983,0,1002,963,1004,1003,988,1032,991,1017],
[994,971,996,998,0,986,976,1005,990,1020,1029,1017],
[1006,983,1056,1037,1014,0,1000,1013,1015,1018,1050,1016],
[1019,1016,1035,996,1024,1000,0,1037,999,1018,1050,1021],
[975,996,988,997,995,987,963,0,999,1024,1010,1026],
[975,1042,1035,1012,1010,985,1001,1001,0,1015,1025,1034],
[992,973,1002,968,980,982,982,976,985,0,1011,1000],
[961,956,990,1009,971,950,950,990,975,989,0,968],
[1008,1005,1023,983,983,984,979,974,966,1000,1032,0]])



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
result = np.append(np.array([12, 2000, 51, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,985,989,965,1014,996,984,1010,997,1005,984,987],
[1015,0,1016,1007,1032,1016,983,1048,1041,1016,1009,1027],
[1011,984,0,973,1001,980,970,1043,1006,996,979,1012],
[1035,993,1027,0,1016,1001,982,1047,1044,1007,1042,1036],
[986,968,999,984,0,980,1019,1008,997,1023,988,995],
[1004,984,1020,999,1020,0,979,1056,1014,1004,996,1008],
[1016,1017,1030,1018,981,1021,0,1019,1029,1007,1006,1028],
[990,952,957,953,992,944,981,0,985,960,958,999],
[1003,959,994,956,1003,986,971,1015,0,980,996,1003],
[995,984,1004,993,977,996,993,1040,1020,0,995,979],
[1016,991,1021,958,1012,1004,994,1042,1004,1005,0,1020],
[1013,973,988,964,1005,992,972,1001,997,1021,980,0]])



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
result = np.append(np.array([12, 2000, 52, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1053,867,1053,1050,1099,1015,824,1008,867,1044,1034],
[947,0,885,836,1002,862,875,1064,1032,835,919,980],
[1133,1115,0,996,921,991,1074,1047,970,989,985,1114],
[947,1164,1004,0,979,991,964,981,942,816,1104,989],
[950,998,1079,1021,0,1044,915,1056,991,972,1145,1126],
[901,1138,1009,1009,956,0,990,1016,969,880,932,1043],
[985,1125,926,1036,1085,1010,0,990,1084,1014,1142,983],
[1176,936,953,1019,944,984,1010,0,1093,1103,1068,948],
[992,968,1030,1058,1009,1031,916,907,0,875,1016,1093],
[1133,1165,1011,1184,1028,1120,986,897,1125,0,1176,1039],
[956,1081,1015,896,855,1068,858,932,984,824,0,914],
[966,1020,886,1011,874,957,1017,1052,907,961,1086,0]])



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
result = np.append(np.array([12, 2000, 53, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1025,945,992,1060,1032,1094,1036,1094,1018,1004,1016],
[975,0,945,967,1018,980,983,1017,1072,1002,987,959],
[1055,1055,0,1028,1084,1035,1028,1044,1077,1056,986,1060],
[1008,1033,972,0,1050,1019,983,1017,1087,1054,1022,1021],
[940,982,916,950,0,938,952,987,1043,988,969,902],
[968,1020,965,981,1062,0,959,1065,1087,968,949,1015],
[906,1017,972,1017,1048,1041,0,1005,1091,986,1005,978],
[964,983,956,983,1013,935,995,0,1007,1025,1013,1006],
[906,928,923,913,957,913,909,993,0,908,928,960],
[982,998,944,946,1012,1032,1014,975,1092,0,1037,1028],
[996,1013,1014,978,1031,1051,995,987,1072,963,0,1022],
[984,1041,940,979,1098,985,1022,994,1040,972,978,0]])



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
result = np.append(np.array([12, 2000, 54, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1009,1007,959,980,1038,1031,981,984,1011,1037,992],
[991,0,1006,987,1011,1042,1037,990,968,1001,1032,1023],
[993,994,0,970,970,1021,1026,1005,979,1017,1017,988],
[1041,1013,1030,0,988,1034,1074,1034,1017,1035,1051,1003],
[1020,989,1030,1012,0,1036,1034,1004,1039,1051,1054,1036],
[962,958,979,966,964,0,996,971,936,1008,992,969],
[969,963,974,926,966,1004,0,994,957,968,1019,977],
[1019,1010,995,966,996,1029,1006,0,966,1021,1054,978],
[1016,1032,1021,983,961,1064,1043,1034,0,1023,1044,998],
[989,999,983,965,949,992,1032,979,977,0,1008,993],
[963,968,983,949,946,1008,981,946,956,992,0,1019],
[1008,977,1012,997,964,1031,1023,1022,1002,1007,981,0]])



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
result = np.append(np.array([12, 2000, 55, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,972,943,718,874,1224,861,691,1059,1008,1001,912],
[1028,0,1039,1039,1025,1039,450,746,464,1276,946,1014],
[1057,961,0,1057,622,1053,782,422,782,1057,622,1180],
[1282,961,943,0,1007,1438,969,531,637,1463,1007,1240],
[1126,975,1378,993,0,845,1191,456,1124,1674,1344,1469],
[776,961,947,562,1155,0,980,11,899,1243,1293,1295],
[1139,1550,1218,1031,809,1020,0,1031,1137,1547,1426,1609],
[1309,1254,1578,1469,1544,1989,969,0,1414,1595,1815,1295],
[941,1536,1218,1363,876,1101,863,586,0,837,1147,1316],
[992,724,943,537,326,757,453,405,1163,0,1010,724],
[999,1054,1378,993,656,707,574,185,853,990,0,1388],
[1088,986,820,760,531,705,391,705,684,1276,612,0]])



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
result = np.append(np.array([12, 2000, 56, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,965,991,1004,992,1026,1019,1011,954,1006,973,1000],
[1035,0,1018,1016,1049,1011,1043,1033,1007,1014,978,1020],
[1009,982,0,1011,1025,1013,1023,1040,1008,1038,982,1022],
[996,984,989,0,1011,976,984,1052,974,1015,957,993],
[1008,951,975,989,0,990,1006,1015,934,984,967,985],
[974,989,987,1024,1010,0,1007,1016,977,981,965,1024],
[981,957,977,1016,994,993,0,997,990,1005,981,992],
[989,967,960,948,985,984,1003,0,954,976,978,971],
[1046,993,992,1026,1066,1023,1010,1046,0,1015,1005,1038],
[994,986,962,985,1016,1019,995,1024,985,0,983,990],
[1027,1022,1018,1043,1033,1035,1019,1022,995,1017,0,1022],
[1000,980,978,1007,1015,976,1008,1029,962,1010,978,0]])



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
result = np.append(np.array([12, 2000, 57, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,901,990,1069,1077,1026,1036,1100,1028,1066,996,978],
[1099,0,1073,1170,1045,1090,1087,1079,1062,1092,993,1059],
[1010,927,0,1058,1013,1007,978,1026,1012,974,1007,1025],
[931,830,942,0,999,895,954,1035,924,955,871,878],
[923,955,987,1001,0,982,934,956,1008,927,946,862],
[974,910,993,1105,1018,0,957,1025,1025,980,1014,984],
[964,913,1022,1046,1066,1043,0,1065,1096,1094,964,1073],
[900,921,974,965,1044,975,935,0,1027,947,954,972],
[972,938,988,1076,992,975,904,973,0,1047,930,999],
[934,908,1026,1045,1073,1020,906,1053,953,0,987,874],
[1004,1007,993,1129,1054,986,1036,1046,1070,1013,0,1047],
[1022,941,975,1122,1138,1016,927,1028,1001,1126,953,0]])



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
result = np.append(np.array([12, 2000, 58, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,997,1010,983,986,958,967,986,973,937,979,966],
[1003,0,1004,983,987,985,1003,1007,983,974,1007,976],
[990,996,0,975,989,966,970,982,972,964,977,996],
[1017,1017,1025,0,1024,975,981,988,1020,1003,1014,1011],
[1014,1013,1011,976,0,996,1002,1012,1006,955,1006,1023],
[1042,1015,1034,1025,1004,0,985,1000,996,969,1002,1005],
[1033,997,1030,1019,998,1015,0,1041,1017,980,1032,1017],
[1014,993,1018,1012,988,1000,959,0,983,946,990,986],
[1027,1017,1028,980,994,1004,983,1017,0,959,1010,982],
[1063,1026,1036,997,1045,1031,1020,1054,1041,0,1022,1030],
[1021,993,1023,986,994,998,968,1010,990,978,0,981],
[1034,1024,1004,989,977,995,983,1014,1018,970,1019,0]])



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
result = np.append(np.array([12, 2000, 59, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,989,954,1029,970,991,983,993,1004,1030,1055,999],
[1011,0,1018,1051,947,1011,1050,1013,1013,982,1041,995],
[1046,982,0,1063,993,1023,987,1068,967,980,1004,1004],
[971,949,937,0,929,939,970,1015,977,951,957,992],
[1030,1053,1007,1071,0,1035,985,1021,1010,973,1034,1085],
[1009,989,977,1061,965,0,1000,1045,1014,963,1044,998],
[1017,950,1013,1030,1015,1000,0,972,980,990,969,1040],
[1007,987,932,985,979,955,1028,0,930,947,1021,1017],
[996,987,1033,1023,990,986,1020,1070,0,987,1003,989],
[970,1018,1020,1049,1027,1037,1010,1053,1013,0,1016,1109],
[945,959,996,1043,966,956,1031,979,997,984,0,996],
[1001,1005,996,1008,915,1002,960,983,1011,891,1004,0]])



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
result = np.append(np.array([12, 2000, 60, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,990,1058,948,992,962,1041,968,920,962,1017,966],
[1010,0,1047,1042,982,942,1043,974,978,931,999,993],
[942,953,0,985,936,907,970,935,963,950,980,927],
[1052,958,1015,0,949,919,978,976,994,943,1035,944],
[1008,1018,1064,1051,0,946,1009,987,991,974,1018,1059],
[1038,1058,1093,1081,1054,0,1081,980,1016,1000,1066,1014],
[959,957,1030,1022,991,919,0,962,970,955,988,974],
[1032,1026,1065,1024,1013,1020,1038,0,984,948,1007,987],
[1080,1022,1037,1006,1009,984,1030,1016,0,968,1007,1003],
[1038,1069,1050,1057,1026,1000,1045,1052,1032,0,1071,1038],
[983,1001,1020,965,982,934,1012,993,993,929,0,950],
[1034,1007,1073,1056,941,986,1026,1013,997,962,1050,0]])



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
result = np.append(np.array([12, 2000, 61, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1012,1029,1036,998,1052,1016,988,998,1010,1031,1036],
[988,0,993,1026,1009,998,984,996,976,1011,1011,1020],
[971,1007,0,1038,1018,1024,1041,1011,994,1035,1022,1029],
[964,974,962,0,961,999,967,962,970,1001,1003,977],
[1002,991,982,1039,0,1021,1018,1006,998,1009,1016,1022],
[948,1002,976,1001,979,0,999,1004,998,1000,998,1016],
[984,1016,959,1033,982,1001,0,965,986,999,1020,999],
[1012,1004,989,1038,994,996,1035,0,1019,1014,1013,1019],
[1002,1024,1006,1030,1002,1002,1014,981,0,1017,1030,1033],
[990,989,965,999,991,1000,1001,986,983,0,985,1009],
[969,989,978,997,984,1002,980,987,970,1015,0,1006],
[964,980,971,1023,978,984,1001,981,967,991,994,0]])



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
result = np.append(np.array([12, 2000, 62, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,964,904,966,945,955,985,1023,977,987,1057,978],
[1036,0,961,991,1003,975,992,975,1029,1045,1102,967],
[1096,1039,0,1038,1023,1015,1039,1056,1024,993,1080,1021],
[1034,1009,962,0,1022,954,993,1018,1045,1072,1067,1014],
[1055,997,977,978,0,1004,989,1058,1028,962,1083,932],
[1045,1025,985,1046,996,0,985,1045,1004,1029,1098,1004],
[1015,1008,961,1007,1011,1015,0,1069,1001,1026,1121,968],
[977,1025,944,982,942,955,931,0,1007,954,1020,961],
[1023,971,976,955,972,996,999,993,0,977,1059,944],
[1013,955,1007,928,1038,971,974,1046,1023,0,1016,980],
[943,898,920,933,917,902,879,980,941,984,0,886],
[1022,1033,979,986,1068,996,1032,1039,1056,1020,1114,0]])



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
result = np.append(np.array([12, 2000, 63, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,948,1164,910,1139,1010,1058,1023,1152,1065,1084,1036],
[1052,0,1104,997,1162,1044,1085,992,1148,1169,978,1084],
[836,896,0,859,1050,889,932,904,1004,1030,996,982],
[1090,1003,1141,0,1155,997,1156,1048,1194,1209,1177,1158],
[861,838,950,845,0,868,971,745,969,984,911,970],
[990,956,1111,1003,1132,0,1050,1024,1117,1072,1053,1089],
[942,915,1068,844,1029,950,0,888,1043,999,962,1038],
[977,1008,1096,952,1255,976,1112,0,1221,1140,1088,1079],
[848,852,996,806,1031,883,957,779,0,1011,980,933],
[935,831,970,791,1016,928,1001,860,989,0,920,1006],
[916,1022,1004,823,1089,947,1038,912,1020,1080,0,1037],
[964,916,1018,842,1030,911,962,921,1067,994,963,0]])



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
result = np.append(np.array([12, 2000, 64, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1015,1017,1036,1015,988,960,1001,1045,979,1002,1028],
[985,0,1018,1020,1005,985,1007,1004,1025,1031,1019,1028],
[983,982,0,1015,984,973,966,1007,1009,950,969,1013],
[964,980,985,0,994,979,972,1004,999,961,1025,1025],
[985,995,1016,1006,0,1025,995,1023,1026,976,1026,1039],
[1012,1015,1027,1021,975,0,983,993,1022,973,1005,1041],
[1040,993,1034,1028,1005,1017,0,1011,1055,974,1026,1055],
[999,996,993,996,977,1007,989,0,999,975,1018,1014],
[955,975,991,1001,974,978,945,1001,0,947,1003,991],
[1021,969,1050,1039,1024,1027,1026,1025,1053,0,1022,1043],
[998,981,1031,975,974,995,974,982,997,978,0,1003],
[972,972,987,975,961,959,945,986,1009,957,997,0]])



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
result = np.append(np.array([12, 2000, 65, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1014,1017,1024,1047,1045,992,979,987,1049,1015,999],
[986,0,1013,989,986,985,1000,1009,938,1033,961,968],
[983,987,0,963,984,996,978,941,964,982,1007,974],
[976,1011,1037,0,994,999,1036,978,1006,1033,981,995],
[953,1014,1016,1006,0,1006,1045,1003,958,1041,1023,1019],
[955,1015,1004,1001,994,0,1016,976,956,1010,1013,1020],
[1008,1000,1022,964,955,984,0,955,954,1009,973,944],
[1021,991,1059,1022,997,1024,1045,0,963,1024,1018,960],
[1013,1062,1036,994,1042,1044,1046,1037,0,1029,989,1018],
[951,967,1018,967,959,990,991,976,971,0,974,1000],
[985,1039,993,1019,977,987,1027,982,1011,1026,0,978],
[1001,1032,1026,1005,981,980,1056,1040,982,1000,1022,0]])



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
result = np.append(np.array([12, 2000, 66, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1128,1089,1126,1019,1030,1125,1000,1007,1059,1204,876],
[872,0,1017,979,919,939,1055,910,894,1009,932,976],
[911,983,0,1026,929,955,996,1051,929,971,957,927],
[874,1021,974,0,882,863,1037,926,887,911,989,958],
[981,1081,1071,1118,0,1093,1085,1133,982,1051,1127,1023],
[970,1061,1045,1137,907,0,1098,1115,1104,1180,1067,949],
[875,945,1004,963,915,902,0,964,812,1016,896,896],
[1000,1090,949,1074,867,885,1036,0,940,1042,1201,998],
[993,1106,1071,1113,1018,896,1188,1060,0,1036,1130,1066],
[941,991,1029,1089,949,820,984,958,964,0,1065,941],
[796,1068,1043,1011,873,933,1104,799,870,935,0,996],
[1124,1024,1073,1042,977,1051,1104,1002,934,1059,1004,0]])



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
result = np.append(np.array([12, 2000, 67, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1012,995,1018,948,995,926,970,995,982,966,964],
[988,0,1010,1021,949,1000,954,973,1003,1000,1009,988],
[1005,990,0,980,965,998,970,963,992,983,976,986],
[982,979,1020,0,925,976,935,965,968,930,969,971],
[1052,1051,1035,1075,0,1017,995,1002,1018,996,1009,995],
[1005,1000,1002,1024,983,0,990,978,1015,963,1004,1006],
[1074,1046,1030,1065,1005,1010,0,1037,1020,1049,994,1022],
[1030,1027,1037,1035,998,1022,963,0,1020,1026,1004,1012],
[1005,997,1008,1032,982,985,980,980,0,982,1006,995],
[1018,1000,1017,1070,1004,1037,951,974,1018,0,1015,1015],
[1034,991,1024,1031,991,996,1006,996,994,985,0,1012],
[1036,1012,1014,1029,1005,994,978,988,1005,985,988,0]])



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
result = np.append(np.array([12, 2000, 68, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,957,947,981,936,986,949,981,998,991,977,960],
[1043,0,984,1032,1014,1020,991,979,1043,1011,1021,981],
[1053,1016,0,1030,1008,1038,1017,998,1063,1012,1032,1031],
[1019,968,970,0,983,990,994,1002,1023,1019,981,989],
[1064,986,992,1017,0,1022,1002,1023,1033,1012,1037,999],
[1014,980,962,1010,978,0,991,954,1004,987,991,972],
[1051,1009,983,1006,998,1009,0,984,1036,989,1010,1022],
[1019,1021,1002,998,977,1046,1016,0,1047,994,1029,1007],
[1002,957,937,977,967,996,964,953,0,950,968,982],
[1009,989,988,981,988,1013,1011,1006,1050,0,988,983],
[1023,979,968,1019,963,1009,990,971,1032,1012,0,1016],
[1040,1019,969,1011,1001,1028,978,993,1018,1017,984,0]])



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
result = np.append(np.array([12, 2000, 69, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1105,1032,1054,1041,1018,1041,1039,985,1053,1026,1030],
[895,0,947,996,958,944,1021,985,985,986,970,941],
[968,1053,0,1008,990,1024,998,991,999,1018,1002,976],
[946,1004,992,0,978,996,970,1028,962,956,958,977],
[959,1042,1010,1022,0,1002,993,1019,1017,986,968,985],
[982,1056,976,1004,998,0,1022,997,994,1015,968,1016],
[959,979,1002,1030,1007,978,0,1019,981,1017,963,945],
[961,1015,1009,972,981,1003,981,0,998,1006,1019,966],
[1015,1015,1001,1038,983,1006,1019,1002,0,1025,976,1006],
[947,1014,982,1044,1014,985,983,994,975,0,980,954],
[974,1030,998,1042,1032,1032,1037,981,1024,1020,0,997],
[970,1059,1024,1023,1015,984,1055,1034,994,1046,1003,0]])



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
result = np.append(np.array([12, 2000, 70, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1051,947,938,1006,1005,1047,979,940,1019,1003,968],
[949,0,955,902,985,956,1005,970,934,959,978,955],
[1053,1045,0,953,993,1016,1037,992,1010,1019,1037,1024],
[1062,1098,1047,0,1053,1041,1068,1065,995,1038,1066,1054],
[994,1015,1007,947,0,979,1011,996,984,973,976,953],
[995,1044,984,959,1021,0,1035,984,989,971,964,1005],
[953,995,963,932,989,965,0,927,921,950,997,972],
[1021,1030,1008,935,1004,1016,1073,0,1028,995,1018,996],
[1060,1066,990,1005,1016,1011,1079,972,0,1084,1048,1026],
[981,1041,981,962,1027,1029,1050,1005,916,0,1007,974],
[997,1022,963,934,1024,1036,1003,982,952,993,0,972],
[1032,1045,976,946,1047,995,1028,1004,974,1026,1028,0]])



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
result = np.append(np.array([12, 2000, 71, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1012,1001,1003,984,1017,985,994,992,1019,1007,1010],
[988,0,978,996,988,984,970,1000,994,1014,971,982],
[999,1022,0,998,986,957,970,988,985,1002,981,974],
[997,1004,1002,0,979,989,970,1000,981,1025,989,987],
[1016,1012,1014,1021,0,987,983,1016,998,1033,979,985],
[983,1016,1043,1011,1013,0,1015,1000,1006,1048,989,1006],
[1015,1030,1030,1030,1017,985,0,1032,1032,1040,996,997],
[1006,1000,1012,1000,984,1000,968,0,996,1014,973,1014],
[1008,1006,1015,1019,1002,994,968,1004,0,1012,993,1000],
[981,986,998,975,967,952,960,986,988,0,949,988],
[993,1029,1019,1011,1021,1011,1004,1027,1007,1051,0,995],
[990,1018,1026,1013,1015,994,1003,986,1000,1012,1005,0]])



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
result = np.append(np.array([12, 2000, 72, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,981,977,1029,999,990,990,995,991,998,1031,1003],
[1019,0,980,997,1022,985,1031,985,987,1009,1030,997],
[1023,1020,0,1035,1002,987,1015,1018,1002,1012,1034,998],
[971,1003,965,0,994,981,998,1002,979,970,999,990],
[1001,978,998,1006,0,1000,1022,1008,1018,1020,1018,1001],
[1010,1015,1013,1019,1000,0,1035,1006,996,1011,1002,1005],
[1010,969,985,1002,978,965,0,971,1000,966,1005,987],
[1005,1015,982,998,992,994,1029,0,992,996,1012,1024],
[1009,1013,998,1021,982,1004,1000,1008,0,984,1019,1002],
[1002,991,988,1030,980,989,1034,1004,1016,0,1008,1009],
[969,970,966,1001,982,998,995,988,981,992,0,972],
[997,1003,1002,1010,999,995,1013,976,998,991,1028,0]])



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
result = np.append(np.array([12, 2000, 73, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1029,1028,1006,1029,1098,997,1002,996,1025,992,995],
[971,0,1011,958,956,1022,958,958,976,1005,954,942],
[972,989,0,965,952,1002,983,998,973,968,1006,970],
[994,1042,1035,0,979,1071,1024,1053,1059,1038,1015,1014],
[971,1044,1048,1021,0,1096,1017,1063,988,1004,1003,1006],
[902,978,998,929,904,0,935,1001,972,1004,916,974],
[1003,1042,1017,976,983,1065,0,1079,1003,1031,1018,1030],
[998,1042,1002,947,937,999,921,0,959,1001,949,977],
[1004,1024,1027,941,1012,1028,997,1041,0,1047,998,1000],
[975,995,1032,962,996,996,969,999,953,0,995,1026],
[1008,1046,994,985,997,1084,982,1051,1002,1005,0,1016],
[1005,1058,1030,986,994,1026,970,1023,1000,974,984,0]])



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
result = np.append(np.array([12, 2000, 74, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1107,1023,1068,986,1013,1009,931,975,937,1008,954],
[893,0,971,852,969,977,975,856,942,916,972,1016],
[977,1029,0,950,1025,991,1027,945,918,973,946,968],
[932,1148,1050,0,954,911,1092,971,949,881,1050,1071],
[1014,1031,975,1046,0,942,1007,950,929,934,1024,1096],
[987,1023,1009,1089,1058,0,1071,958,929,862,996,1019],
[991,1025,973,908,993,929,0,926,854,960,970,901],
[1069,1144,1055,1029,1050,1042,1074,0,1100,965,956,1022],
[1025,1058,1082,1051,1071,1071,1146,900,0,1001,1068,1059],
[1063,1084,1027,1119,1066,1138,1040,1035,999,0,1019,982],
[992,1028,1054,950,976,1004,1030,1044,932,981,0,930],
[1046,984,1032,929,904,981,1099,978,941,1018,1070,0]])



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
result = np.append(np.array([12, 2000, 75, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1011,969,970,957,937,1015,969,966,995,967,1049],
[989,0,1004,922,947,997,1023,967,981,1012,940,1035],
[1031,996,0,967,973,993,998,965,1003,1007,973,1042],
[1030,1078,1033,0,1008,1018,998,1025,1014,1032,983,1052],
[1043,1053,1027,992,0,988,1041,948,1017,1037,959,1034],
[1063,1003,1007,982,1012,0,1097,954,984,1002,975,1033],
[985,977,1002,1002,959,903,0,961,940,1004,976,991],
[1031,1033,1035,975,1052,1046,1039,0,1004,1046,1026,1040],
[1034,1019,997,986,983,1016,1060,996,0,1051,982,1052],
[1005,988,993,968,963,998,996,954,949,0,960,1003],
[1033,1060,1027,1017,1041,1025,1024,974,1018,1040,0,1033],
[951,965,958,948,966,967,1009,960,948,997,967,0]])



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
result = np.append(np.array([12, 2000, 76, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,975,976,1012,949,944,1047,940,961,939,971,969],
[1025,0,986,1004,986,1014,1051,1013,1002,1002,988,1025],
[1024,1014,0,1032,1021,976,1064,1021,999,973,1010,992],
[988,996,968,0,924,971,1015,941,968,940,955,900],
[1051,1014,979,1076,0,996,1075,999,1003,1011,1023,1010],
[1056,986,1024,1029,1004,0,1043,979,1047,969,1004,982],
[953,949,936,985,925,957,0,945,958,964,981,930],
[1060,987,979,1059,1001,1021,1055,0,1014,1036,1024,1017],
[1039,998,1001,1032,997,953,1042,986,0,975,988,984],
[1061,998,1027,1060,989,1031,1036,964,1025,0,994,1007],
[1029,1012,990,1045,977,996,1019,976,1012,1006,0,980],
[1031,975,1008,1100,990,1018,1070,983,1016,993,1020,0]])



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
result = np.append(np.array([12, 2000, 77, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,984,998,1004,953,1040,980,1007,1027,993,1037,1039],
[1016,0,941,971,1006,1010,964,997,984,958,989,1016],
[1002,1059,0,953,987,1023,1004,1046,1017,1002,992,1005],
[996,1029,1047,0,976,1037,990,1068,1003,1015,1044,1060],
[1047,994,1013,1024,0,1059,1002,1055,1052,1012,1038,1070],
[960,990,977,963,941,0,957,992,996,982,952,1029],
[1020,1036,996,1010,998,1043,0,1051,1026,982,1028,1048],
[993,1003,954,932,945,1008,949,0,972,953,1006,1021],
[973,1016,983,997,948,1004,974,1028,0,945,982,1004],
[1007,1042,998,985,988,1018,1018,1047,1055,0,1038,1086],
[963,1011,1008,956,962,1048,972,994,1018,962,0,1023],
[961,984,995,940,930,971,952,979,996,914,977,0]])



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
result = np.append(np.array([12, 2000, 78, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1018,875,946,1040,1054,961,962,872,803,795,911],
[982,0,881,1008,1002,995,1181,1030,1052,1026,1022,937],
[1125,1119,0,915,991,1072,1096,904,1037,987,906,1064],
[1054,992,1085,0,1041,1030,956,988,957,1163,1079,1127],
[960,998,1009,959,0,981,1069,1051,1005,996,920,1098],
[946,1005,928,970,1019,0,969,1041,820,949,882,960],
[1039,819,904,1044,931,1031,0,860,811,812,862,1028],
[1038,970,1096,1012,949,959,1140,0,1099,1019,958,1057],
[1128,948,963,1043,995,1180,1189,901,0,1022,966,1047],
[1197,974,1013,837,1004,1051,1188,981,978,0,982,916],
[1205,978,1094,921,1080,1118,1138,1042,1034,1018,0,917],
[1089,1063,936,873,902,1040,972,943,953,1084,1083,0]])



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
result = np.append(np.array([12, 2000, 79, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1056,1032,1003,962,1043,953,1020,973,980,1068,1033],
[944,0,923,1007,1046,971,892,977,986,953,972,1019],
[968,1077,0,1083,1033,971,1021,1036,1032,1059,1039,1031],
[997,993,917,0,951,996,980,1005,983,1006,987,974],
[1038,954,967,1049,0,991,957,1010,1016,1027,1072,999],
[957,1029,1029,1004,1009,0,965,1024,954,984,1021,1006],
[1047,1108,979,1020,1043,1035,0,1029,1026,1051,1064,981],
[980,1023,964,995,990,976,971,0,997,963,980,1011],
[1027,1014,968,1017,984,1046,974,1003,0,1023,1016,1033],
[1020,1047,941,994,973,1016,949,1037,977,0,996,1004],
[932,1028,961,1013,928,979,936,1020,984,1004,0,940],
[967,981,969,1026,1001,994,1019,989,967,996,1060,0]])



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
result = np.append(np.array([12, 2000, 80, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1001,975,989,993,985,965,980,986,1029,1014,1017],
[999,0,1005,976,1017,995,987,1007,981,999,956,960],
[1025,995,0,1011,1035,961,1011,1022,1016,1004,1004,1021],
[1011,1024,989,0,1053,985,987,1001,961,1022,1020,987],
[1007,983,965,947,0,978,972,983,973,1031,981,1000],
[1015,1005,1039,1015,1022,0,993,1006,997,1052,1036,1016],
[1035,1013,989,1013,1028,1007,0,1026,1036,1053,1022,1011],
[1020,993,978,999,1017,994,974,0,1009,1021,1011,1025],
[1014,1019,984,1039,1027,1003,964,991,0,1015,995,1004],
[971,1001,996,978,969,948,947,979,985,0,965,982],
[986,1044,996,980,1019,964,978,989,1005,1035,0,994],
[983,1040,979,1013,1000,984,989,975,996,1018,1006,0]])



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
result = np.append(np.array([12, 2000, 81, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,995,1038,982,1008,1029,991,986,1018,981,1007,1001],
[1005,0,1019,1003,984,1010,982,999,992,972,1032,1035],
[962,981,0,954,981,983,988,1001,1013,961,990,960],
[1018,997,1046,0,985,1013,974,961,1009,972,1014,995],
[992,1016,1019,1015,0,1012,1012,1003,1033,951,1030,1026],
[971,990,1017,987,988,0,1027,1000,967,1001,998,991],
[1009,1018,1012,1026,988,973,0,975,1017,965,1024,1014],
[1014,1001,999,1039,997,1000,1025,0,1011,966,1025,1009],
[982,1008,987,991,967,1033,983,989,0,945,998,981],
[1019,1028,1039,1028,1049,999,1035,1034,1055,0,1006,1031],
[993,968,1010,986,970,1002,976,975,1002,994,0,993],
[999,965,1040,1005,974,1009,986,991,1019,969,1007,0]])



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
result = np.append(np.array([12, 2000, 82, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1029,991,1032,1023,1078,1015,1044,1052,1042,1050,1004],
[971,0,986,971,960,1010,997,977,967,956,1005,959],
[1009,1014,0,1040,981,1063,1043,1027,1000,1049,1024,1009],
[968,1029,960,0,963,1022,1004,1002,972,991,993,944],
[977,1040,1019,1037,0,1072,998,1059,995,1001,1038,984],
[922,990,937,978,928,0,981,974,973,968,988,956],
[985,1003,957,996,1002,1019,0,1014,992,977,1021,990],
[956,1023,973,998,941,1026,986,0,960,995,1000,964],
[948,1033,1000,1028,1005,1027,1008,1040,0,992,1042,988],
[958,1044,951,1009,999,1032,1023,1005,1008,0,1021,980],
[950,995,976,1007,962,1012,979,1000,958,979,0,973],
[996,1041,991,1056,1016,1044,1010,1036,1012,1020,1027,0]])



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
result = np.append(np.array([12, 2000, 83, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,993,1015,983,951,944,984,971,986,983,963,969],
[1007,0,1027,1000,1026,978,978,993,1015,1007,995,978],
[985,973,0,999,970,968,972,963,978,988,952,947],
[1017,1000,1001,0,991,934,959,1010,991,983,980,985],
[1049,974,1030,1009,0,960,980,988,999,1020,1018,981],
[1056,1022,1032,1066,1040,0,993,1029,1033,1051,1016,994],
[1016,1022,1028,1041,1020,1007,0,1022,1030,1023,996,1008],
[1029,1007,1037,990,1012,971,978,0,1001,1017,973,1001],
[1014,985,1022,1009,1001,967,970,999,0,1034,973,964],
[1017,993,1012,1017,980,949,977,983,966,0,995,969],
[1037,1005,1048,1020,982,984,1004,1027,1027,1005,0,975],
[1031,1022,1053,1015,1019,1006,992,999,1036,1031,1025,0]])



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
result = np.append(np.array([12, 2000, 84, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1007,1047,1020,969,1021,1043,998,1005,1065,1007,1034],
[993,0,1010,984,947,962,1015,972,978,1021,1010,991],
[953,990,0,998,979,938,996,980,937,1024,997,993],
[980,1016,1002,0,963,922,1050,977,969,971,1023,990],
[1031,1053,1021,1037,0,996,1010,992,1008,1033,1017,1016],
[979,1038,1062,1078,1004,0,1047,1006,1002,1024,1052,983],
[957,985,1004,950,990,953,0,941,974,1031,1032,985],
[1002,1028,1020,1023,1008,994,1059,0,1036,1028,1049,1006],
[995,1022,1063,1031,992,998,1026,964,0,1036,1034,1058],
[935,979,976,1029,967,976,969,972,964,0,983,981],
[993,990,1003,977,983,948,968,951,966,1017,0,950],
[966,1009,1007,1010,984,1017,1015,994,942,1019,1050,0]])



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
result = np.append(np.array([12, 2000, 85, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1015,988,987,942,986,946,1053,961,1006,907,923],
[985,0,1004,1012,983,1022,1007,999,968,969,987,975],
[1012,996,0,1007,957,985,989,999,916,956,934,939],
[1013,988,993,0,870,980,949,973,939,975,926,892],
[1058,1017,1043,1130,0,1040,1008,1010,1059,992,1031,1034],
[1014,978,1015,1020,960,0,995,1027,973,1003,892,1050],
[1054,993,1011,1051,992,1005,0,1021,974,954,910,945],
[947,1001,1001,1027,990,973,979,0,922,959,945,912],
[1039,1032,1084,1061,941,1027,1026,1078,0,1036,972,1039],
[994,1031,1044,1025,1008,997,1046,1041,964,0,945,922],
[1093,1013,1066,1074,969,1108,1090,1055,1028,1055,0,1070],
[1077,1025,1061,1108,966,950,1055,1088,961,1078,930,0]])



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
result = np.append(np.array([12, 2000, 86, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,998,1008,1025,989,983,971,992,988,994,1024,1006],
[1002,0,1002,981,1001,958,1010,982,1019,996,1003,985],
[992,998,0,1001,1057,963,969,995,982,983,1021,978],
[975,1019,999,0,1006,1005,953,989,1009,992,978,940],
[1011,999,943,994,0,934,963,983,980,1000,972,968],
[1017,1042,1037,995,1066,0,1014,1040,1017,1043,1052,1013],
[1029,990,1031,1047,1037,986,0,1019,970,1001,1016,974],
[1008,1018,1005,1011,1017,960,981,0,1013,1001,1025,959],
[1012,981,1018,991,1020,983,1030,987,0,1019,1016,979],
[1006,1004,1017,1008,1000,957,999,999,981,0,1023,978],
[976,997,979,1022,1028,948,984,975,984,977,0,956],
[994,1015,1022,1060,1032,987,1026,1041,1021,1022,1044,0]])



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
result = np.append(np.array([12, 2000, 87, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,936,966,973,887,930,909,921,1049,916,1110,889],
[1064,0,1086,1104,958,969,892,1097,1226,1059,1136,1087],
[1034,914,0,873,797,901,817,973,1006,970,988,1003],
[1027,896,1127,0,904,886,898,1080,1062,1055,1068,1053],
[1113,1042,1203,1096,0,922,1098,1091,1071,1052,1166,1150],
[1070,1031,1099,1114,1078,0,1064,1183,995,1075,1153,1006],
[1091,1108,1183,1102,902,936,0,1025,1072,1040,1019,1114],
[1079,903,1027,920,909,817,975,0,918,938,971,977],
[951,774,994,938,929,1005,928,1082,0,899,980,799],
[1084,941,1030,945,948,925,960,1062,1101,0,975,859],
[890,864,1012,932,834,847,981,1029,1020,1025,0,1125],
[1111,913,997,947,850,994,886,1023,1201,1141,875,0]])



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
result = np.append(np.array([12, 2000, 88, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1007,1070,933,1083,1054,1013,1014,1045,999,1004,1022],
[993,0,1140,853,956,948,896,1010,1015,979,1045,944],
[930,860,0,867,1004,965,948,953,964,975,964,874],
[1067,1147,1133,0,1053,1036,976,1091,1098,1106,980,961],
[917,1044,996,947,0,1017,909,956,1014,984,1050,917],
[946,1052,1035,964,983,0,932,956,1020,1016,1004,885],
[987,1104,1052,1024,1091,1068,0,1063,1051,1051,1027,1026],
[986,990,1047,909,1044,1044,937,0,1031,1024,987,952],
[955,985,1036,902,986,980,949,969,0,1064,977,977],
[1001,1021,1025,894,1016,984,949,976,936,0,916,926],
[996,955,1036,1020,950,996,973,1013,1023,1084,0,936],
[978,1056,1126,1039,1083,1115,974,1048,1023,1074,1064,0]])



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
result = np.append(np.array([12, 2000, 89, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,988,976,1016,1005,978,1000,987,1017,1006,986,925],
[1012,0,946,996,1018,1004,1028,1015,1041,1012,1002,951],
[1024,1054,0,1002,1014,1053,1047,1066,1036,1027,992,998],
[984,1004,998,0,1008,1019,1053,1029,972,1029,946,983],
[995,982,986,992,0,1000,988,1016,1013,1001,982,1008],
[1022,996,947,981,1000,0,1031,995,1007,989,1021,906],
[1000,972,953,947,1012,969,0,1023,1008,923,951,946],
[1013,985,934,971,984,1005,977,0,1050,997,998,980],
[983,959,964,1028,987,993,992,950,0,998,960,952],
[994,988,973,971,999,1011,1077,1003,1002,0,974,955],
[1014,998,1008,1054,1018,979,1049,1002,1040,1026,0,950],
[1075,1049,1002,1017,992,1094,1054,1020,1048,1045,1050,0]])



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
result = np.append(np.array([12, 2000, 90, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1015,1032,952,1203,1059,1107,1022,1068,1016,968,1118],
[985,0,971,962,1068,964,1063,994,1104,934,923,1112],
[968,1029,0,1033,1193,1002,1051,998,1039,995,995,1171],
[1048,1038,967,0,1141,1079,1081,942,1062,931,982,1263],
[797,932,807,859,0,872,970,901,931,715,778,1023],
[941,1036,998,921,1128,0,1114,953,1046,1011,953,999],
[893,937,949,919,1030,886,0,910,958,951,859,949],
[978,1006,1002,1058,1099,1047,1090,0,1093,969,1033,1084],
[932,896,961,938,1069,954,1042,907,0,920,950,1114],
[984,1066,1005,1069,1285,989,1049,1031,1080,0,914,1160],
[1032,1077,1005,1018,1222,1047,1141,967,1050,1086,0,1100],
[882,888,829,737,977,1001,1051,916,886,840,900,0]])



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
result = np.append(np.array([12, 2000, 91, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,969,1045,950,1015,1018,968,1032,1009,1022,1009,995],
[1031,0,1060,997,1035,1014,1025,1012,1020,1033,1032,987],
[955,940,0,941,992,993,1001,964,973,981,1002,963],
[1050,1003,1059,0,1031,1040,1010,1026,1002,1061,993,1028],
[985,965,1008,969,0,988,974,979,971,996,987,967],
[982,986,1007,960,1012,0,981,983,969,962,982,977],
[1032,975,999,990,1026,1019,0,1004,1025,1033,1026,995],
[968,988,1036,974,1021,1017,996,0,1010,1039,995,1008],
[991,980,1027,998,1029,1031,975,990,0,1009,1016,986],
[978,967,1019,939,1004,1038,967,961,991,0,997,996],
[991,968,998,1007,1013,1018,974,1005,984,1003,0,964],
[1005,1013,1037,972,1033,1023,1005,992,1014,1004,1036,0]])



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
result = np.append(np.array([12, 2000, 92, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1014,977,1044,1003,1030,1008,1016,1000,1029,1011,992],
[986,0,995,1033,994,1038,1026,999,1001,985,1017,1004],
[1023,1005,0,1013,1036,1042,1026,997,985,1006,974,1006],
[956,967,987,0,1000,1010,970,960,993,975,951,987],
[997,1006,964,1000,0,1024,1022,973,979,965,1014,973],
[970,962,958,990,976,0,1005,950,955,963,938,956],
[992,974,974,1030,978,995,0,972,988,984,953,977],
[984,1001,1003,1040,1027,1050,1028,0,1022,1010,987,1012],
[1000,999,1015,1007,1021,1045,1012,978,0,978,955,986],
[971,1015,994,1025,1035,1037,1016,990,1022,0,1005,992],
[989,983,1026,1049,986,1062,1047,1013,1045,995,0,1008],
[1008,996,994,1013,1027,1044,1023,988,1014,1008,992,0]])



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
result = np.append(np.array([12, 2000, 93, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1006,1038,1058,1013,991,982,1006,996,1007,1007,997],
[994,0,1018,1071,1046,1024,1003,1027,1042,1034,1039,994],
[962,982,0,1027,978,983,983,973,1003,1030,1022,981],
[942,929,973,0,966,952,971,957,1009,944,971,946],
[987,954,1022,1034,0,1000,1037,1003,1015,1010,990,1018],
[1009,976,1017,1048,1000,0,983,991,1034,1007,998,1004],
[1018,997,1017,1029,963,1017,0,1012,1037,1023,997,985],
[994,973,1027,1043,997,1009,988,0,1008,994,1006,970],
[1004,958,997,991,985,966,963,992,0,974,994,935],
[993,966,970,1056,990,993,977,1006,1026,0,1004,966],
[993,961,978,1029,1010,1002,1003,994,1006,996,0,985],
[1003,1006,1019,1054,982,996,1015,1030,1065,1034,1015,0]])



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
result = np.append(np.array([12, 2000, 94, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1087,841,1109,868,1082,919,977,962,1012,973,902],
[913,0,924,896,831,968,941,795,1010,996,909,890],
[1159,1076,0,983,1066,1003,965,1084,1198,969,1244,1068],
[891,1104,1017,0,769,896,943,834,915,914,1123,789],
[1132,1169,934,1231,0,987,1028,1026,1027,1128,1081,1003],
[918,1032,997,1104,1013,0,860,870,886,991,993,1018],
[1081,1059,1035,1057,972,1140,0,934,878,829,1196,1008],
[1023,1205,916,1166,974,1130,1066,0,1137,1022,918,1007],
[1038,990,802,1085,973,1114,1122,863,0,1052,963,990],
[988,1004,1031,1086,872,1009,1171,978,948,0,1068,997],
[1027,1091,756,877,919,1007,804,1082,1037,932,0,955],
[1098,1110,932,1211,997,982,992,993,1010,1003,1045,0]])



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
result = np.append(np.array([12, 2000, 95, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,980,1009,987,970,987,1013,997,972,1003,1013,991],
[1020,0,998,996,1032,1008,1030,1012,1036,1025,1044,1017],
[991,1002,0,991,1040,1008,1015,1029,981,1007,1050,1008],
[1013,1004,1009,0,1004,1005,1015,1004,985,1043,1012,1006],
[1030,968,960,996,0,953,1049,980,1027,1004,1050,983],
[1013,992,992,995,1047,0,1022,975,981,1004,1028,1008],
[987,970,985,985,951,978,0,961,988,1006,1026,1001],
[1003,988,971,996,1020,1025,1039,0,1018,1014,1045,1008],
[1028,964,1019,1015,973,1019,1012,982,0,1026,1008,1029],
[997,975,993,957,996,996,994,986,974,0,1033,1028],
[987,956,950,988,950,972,974,955,992,967,0,989],
[1009,983,992,994,1017,992,999,992,971,972,1011,0]])



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
result = np.append(np.array([12, 2000, 96, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,951,1025,990,968,1015,978,994,971,984,1023,993],
[1049,0,1013,1034,1020,998,1016,1039,1033,1021,1032,1006],
[975,987,0,979,972,964,990,1013,985,989,1000,969],
[1010,966,1021,0,968,975,992,1005,982,980,1007,977],
[1032,980,1028,1032,0,981,1021,1028,1017,1012,1022,1018],
[985,1002,1036,1025,1019,0,1050,1020,1038,1016,1016,996],
[1022,984,1010,1008,979,950,0,1006,1031,1007,1009,991],
[1006,961,987,995,972,980,994,0,995,991,997,975],
[1029,967,1015,1018,983,962,969,1005,0,1019,984,1002],
[1016,979,1011,1020,988,984,993,1009,981,0,1014,972],
[977,968,1000,993,978,984,991,1003,1016,986,0,968],
[1007,994,1031,1023,982,1004,1009,1025,998,1028,1032,0]])



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
result = np.append(np.array([12, 2000, 97, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1006,1031,1024,1005,1017,1010,1032,975,987,992,1000],
[994,0,1046,1027,994,1024,1011,1041,980,1014,999,993],
[969,954,0,1015,982,1022,985,1002,971,998,983,1001],
[976,973,985,0,1009,1001,989,1026,979,983,968,990],
[995,1006,1018,991,0,1034,1014,1023,968,988,990,1016],
[983,976,978,999,966,0,1019,999,964,983,992,967],
[990,989,1015,1011,986,981,0,1031,952,998,1000,956],
[968,959,998,974,977,1001,969,0,937,973,974,969],
[1025,1020,1029,1021,1032,1036,1048,1063,0,1016,1000,1013],
[1013,986,1002,1017,1012,1017,1002,1027,984,0,1005,995],
[1008,1001,1017,1032,1010,1008,1000,1026,1000,995,0,982],
[1000,1007,999,1010,984,1033,1044,1031,987,1005,1018,0]])



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
result = np.append(np.array([12, 2000, 98, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1035,1012,1012,1042,1037,1045,1007,982,986,1014,1000],
[965,0,933,947,968,981,988,968,968,975,945,995],
[988,1067,0,1014,1006,1054,1028,1011,1013,1025,1027,1073],
[988,1053,986,0,1019,1057,1029,976,996,985,986,1010],
[958,1032,994,981,0,1034,1016,1004,950,969,1007,998],
[963,1019,946,943,966,0,995,960,953,960,933,989],
[955,1012,972,971,984,1005,0,983,983,988,969,1014],
[993,1032,989,1024,996,1040,1017,0,988,967,974,1033],
[1018,1032,987,1004,1050,1047,1017,1012,0,1014,1022,1019],
[1014,1025,975,1015,1031,1040,1012,1033,986,0,988,1022],
[986,1055,973,1014,993,1067,1031,1026,978,1012,0,1018],
[1000,1005,927,990,1002,1011,986,967,981,978,982,0]])



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
result = np.append(np.array([12, 2000, 99, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,983,975,988,986,1004,977,973,976,1001,1013,1013],
[1017,0,1024,1009,1000,995,1021,971,991,1011,1022,1037],
[1025,976,0,977,970,1003,1012,979,980,999,1018,1007],
[1012,991,1023,0,992,979,1017,976,988,1008,1005,1010],
[1014,1000,1030,1008,0,1026,1001,983,991,1040,1035,1025],
[996,1005,997,1021,974,0,1022,986,1017,1014,1005,1007],
[1023,979,988,983,999,978,0,964,992,1007,1019,1011],
[1027,1029,1021,1024,1017,1014,1036,0,999,991,1042,1027],
[1024,1009,1020,1012,1009,983,1008,1001,0,1021,1015,1009],
[999,989,1001,992,960,986,993,1009,979,0,1010,994],
[987,978,982,995,965,995,981,958,985,990,0,995],
[987,963,993,990,975,993,989,973,991,1006,1005,0]])



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
result = np.append(np.array([12, 2000, 100, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1028,1022,1070,1024,1018,1013,1077,1004,975,1042,997],
[972,0,994,966,1007,1005,995,979,969,945,1001,989],
[978,1006,0,1009,975,1009,1013,1011,964,996,1024,994],
[930,1034,991,0,993,1014,985,1017,963,965,1012,993],
[976,993,1025,1007,0,1005,967,1009,966,964,987,966],
[982,995,991,986,995,0,1011,994,957,993,995,951],
[987,1005,987,1015,1033,989,0,1030,981,983,1006,970],
[923,1021,989,983,991,1006,970,0,975,975,992,961],
[996,1031,1036,1037,1034,1043,1019,1025,0,1000,1029,988],
[1025,1055,1004,1035,1036,1007,1017,1025,1000,0,1028,1041],
[958,999,976,988,1013,1005,994,1008,971,972,0,1004],
[1003,1011,1006,1007,1034,1049,1030,1039,1012,959,996,0]])



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
result = np.append(np.array([12, 2000, 101, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1019,989,1042,997,964,975,996,986,982,1038,995],
[981,0,1016,990,1000,1006,960,950,999,962,1028,1005],
[1011,984,0,973,1041,995,985,1019,1026,955,1010,980],
[958,1010,1027,0,994,959,961,999,1015,1002,996,959],
[1003,1000,959,1006,0,980,1037,1008,1009,988,1019,1008],
[1036,994,1005,1041,1020,0,1029,1017,1006,995,974,994],
[1025,1040,1015,1039,963,971,0,1032,1084,1016,1040,1004],
[1004,1050,981,1001,992,983,968,0,992,982,1027,1045],
[1014,1001,974,985,991,994,916,1008,0,933,967,967],
[1018,1038,1045,998,1012,1005,984,1018,1067,0,1050,1051],
[962,972,990,1004,981,1026,960,973,1033,950,0,978],
[1005,995,1020,1041,992,1006,996,955,1033,949,1022,0]])



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
result = np.append(np.array([12, 2000, 102, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,987,1020,995,966,971,997,1072,1065,979,999,1013],
[1013,0,986,1045,1002,940,967,1071,1036,995,1010,1041],
[980,1014,0,1060,1044,1041,1071,1050,1055,1002,1016,1047],
[1005,955,940,0,951,945,1004,1043,1044,977,1012,993],
[1034,998,956,1049,0,965,1044,1032,1052,973,1005,1000],
[1029,1060,959,1055,1035,0,1012,1071,1084,987,1058,1042],
[1003,1033,929,996,956,988,0,1028,1043,1013,997,1006],
[928,929,950,957,968,929,972,0,977,913,939,983],
[935,964,945,956,948,916,957,1023,0,968,967,976],
[1021,1005,998,1023,1027,1013,987,1087,1032,0,1035,1025],
[1001,990,984,988,995,942,1003,1061,1033,965,0,1046],
[987,959,953,1007,1000,958,994,1017,1024,975,954,0]])



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
result = np.append(np.array([12, 2000, 103, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1011,906,982,992,1028,1011,1022,1036,1013,1061,1045],
[989,0,929,1005,951,959,992,986,1029,1014,991,1044],
[1094,1071,0,1007,983,1013,1038,1033,1112,1036,1030,1057],
[1018,995,993,0,1003,992,1039,989,1033,1034,953,1066],
[1008,1049,1017,997,0,989,1035,1011,1045,1026,1052,1060],
[972,1041,987,1008,1011,0,1051,1019,1047,1024,1027,1054],
[989,1008,962,961,965,949,0,1000,987,985,996,1062],
[978,1014,967,1011,989,981,1000,0,1074,983,1019,1050],
[964,971,888,967,955,953,1013,926,0,989,1015,1022],
[987,986,964,966,974,976,1015,1017,1011,0,989,1062],
[939,1009,970,1047,948,973,1004,981,985,1011,0,1002],
[955,956,943,934,940,946,938,950,978,938,998,0]])



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
result = np.append(np.array([12, 2000, 104, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1001,987,1032,1002,1003,1005,1023,1030,1035,979,1004],
[999,0,1013,1001,1034,998,991,1018,1008,1006,979,964],
[1013,987,0,994,1023,1015,995,1013,1029,1037,986,962],
[968,999,1006,0,1026,1014,979,1017,1021,1031,999,1010],
[998,966,977,974,0,1011,1010,978,984,1022,989,977],
[997,1002,985,986,989,0,993,994,977,1019,1006,1011],
[995,1009,1005,1021,990,1007,0,1039,984,1052,975,1024],
[977,982,987,983,1022,1006,961,0,1019,1009,961,989],
[970,992,971,979,1016,1023,1016,981,0,1015,996,1021],
[965,994,963,969,978,981,948,991,985,0,973,954],
[1021,1021,1014,1001,1011,994,1025,1039,1004,1027,0,1025],
[996,1036,1038,990,1023,989,976,1011,979,1046,975,0]])



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
result = np.append(np.array([12, 2000, 105, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,977,964,949,974,1019,994,994,975,969,953,976],
[1023,0,987,953,1014,1004,1012,1001,1037,1006,1009,1000],
[1036,1013,0,1007,984,1048,1002,1006,1014,994,994,995],
[1051,1047,993,0,991,1029,1086,975,1038,1038,1030,1032],
[1026,986,1016,1009,0,1017,1032,1037,1012,1010,1011,977],
[981,996,952,971,983,0,989,958,958,1000,944,992],
[1006,988,998,914,968,1011,0,967,998,1031,1035,962],
[1006,999,994,1025,963,1042,1033,0,1046,983,1005,979],
[1025,963,986,962,988,1042,1002,954,0,977,965,933],
[1031,994,1006,962,990,1000,969,1017,1023,0,1005,1028],
[1047,991,1006,970,989,1056,965,995,1035,995,0,990],
[1024,1000,1005,968,1023,1008,1038,1021,1067,972,1010,0]])



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
result = np.append(np.array([12, 2000, 106, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1047,1014,1002,987,983,1000,1014,970,973,1051,971],
[953,0,987,971,1007,983,986,990,956,1007,1049,998],
[986,1013,0,1036,1036,1014,1008,992,976,1036,1043,1014],
[998,1029,964,0,985,1035,985,993,949,1013,1004,1001],
[1013,993,964,1015,0,1015,1000,1011,1007,1005,1023,1025],
[1017,1017,986,965,985,0,974,1021,984,996,1058,974],
[1000,1014,992,1015,1000,1026,0,1027,973,988,1028,1005],
[986,1010,1008,1007,989,979,973,0,965,974,1018,1007],
[1030,1044,1024,1051,993,1016,1027,1035,0,1039,1087,1035],
[1027,993,964,987,995,1004,1012,1026,961,0,1048,982],
[949,951,957,996,977,942,972,982,913,952,0,995],
[1029,1002,986,999,975,1026,995,993,965,1018,1005,0]])



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
result = np.append(np.array([12, 2000, 107, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1110,1107,947,1175,1117,973,1138,996,1017,988,1000],
[890,0,912,978,1023,980,989,1093,842,968,1016,870],
[893,1088,0,1098,1138,1169,1069,1042,1021,1115,1113,988],
[1053,1022,902,0,1049,1050,1063,1260,896,1065,1029,1031],
[825,977,862,951,0,1074,968,1019,933,922,984,917],
[883,1020,831,950,926,0,876,1033,824,969,938,956],
[1027,1011,931,937,1032,1124,0,1047,909,1053,1050,972],
[862,907,958,740,981,967,953,0,776,961,930,922],
[1004,1158,979,1104,1067,1176,1091,1224,0,1071,1067,975],
[983,1032,885,935,1078,1031,947,1039,929,0,1003,894],
[1012,984,887,971,1016,1062,950,1070,933,997,0,1059],
[1000,1130,1012,969,1083,1044,1028,1078,1025,1106,941,0]])



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
result = np.append(np.array([12, 2000, 108, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,972,951,976,942,964,974,954,916,931,926,981],
[1028,0,1014,1041,1043,1039,979,962,1001,941,994,1032],
[1049,986,0,958,951,985,1007,973,985,933,968,998],
[1024,959,1042,0,1017,1025,999,969,990,939,1045,959],
[1058,957,1049,983,0,1006,977,908,977,920,1013,971],
[1036,961,1015,975,994,0,970,944,934,972,973,1002],
[1026,1021,993,1001,1023,1030,0,937,940,955,972,952],
[1046,1038,1027,1031,1092,1056,1063,0,1064,1032,995,1018],
[1084,999,1015,1010,1023,1066,1060,936,0,946,948,1024],
[1069,1059,1067,1061,1080,1028,1045,968,1054,0,1026,990],
[1074,1006,1032,955,987,1027,1028,1005,1052,974,0,1017],
[1019,968,1002,1041,1029,998,1048,982,976,1010,983,0]])



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
result = np.append(np.array([12, 2000, 109, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,918,887,916,969,965,1003,965,963,918,975,921],
[1082,0,999,1024,1014,990,1061,1030,1069,993,1008,1051],
[1113,1001,0,1022,1011,1009,1062,1047,998,1021,990,1027],
[1084,976,978,0,1000,986,1010,1018,984,994,971,1023],
[1031,986,989,1000,0,1001,1022,1019,1060,996,967,985],
[1035,1010,991,1014,999,0,1003,1014,1053,997,976,1006],
[997,939,938,990,978,997,0,993,988,964,929,973],
[1035,970,953,982,981,986,1007,0,1005,940,995,1007],
[1037,931,1002,1016,940,947,1012,995,0,975,931,969],
[1082,1007,979,1006,1004,1003,1036,1060,1025,0,969,968],
[1025,992,1010,1029,1033,1024,1071,1005,1069,1031,0,945],
[1079,949,973,977,1015,994,1027,993,1031,1032,1055,0]])



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
result = np.append(np.array([12, 2000, 110, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1046,999,997,986,1036,1009,998,1040,1044,1035,1034],
[954,0,977,986,936,1011,967,962,957,975,960,968],
[1001,1023,0,1010,999,1078,998,1010,977,1021,985,1030],
[1003,1014,990,0,991,1050,975,973,994,1012,977,1011],
[1014,1064,1001,1009,0,1025,986,982,1043,1056,1017,1028],
[964,989,922,950,975,0,964,960,986,1020,1009,1016],
[991,1033,1002,1025,1014,1036,0,990,1024,1049,1023,1044],
[1002,1038,990,1027,1018,1040,1010,0,998,998,1067,1073],
[960,1043,1023,1006,957,1014,976,1002,0,945,1006,1023],
[956,1025,979,988,944,980,951,1002,1055,0,1016,1035],
[965,1040,1015,1023,983,991,977,933,994,984,0,1023],
[966,1032,970,989,972,984,956,927,977,965,977,0]])



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
result = np.append(np.array([12, 2000, 111, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1076,971,970,983,1000,1079,1039,1021,1000,1013,1018],
[924,0,923,915,960,938,985,930,969,959,928,963],
[1029,1077,0,1012,1059,1055,1082,1017,1026,1050,1062,1000],
[1030,1085,988,0,1049,1043,1070,1031,1009,1025,996,1048],
[1017,1040,941,951,0,948,1001,966,974,983,942,968],
[1000,1062,945,957,1052,0,1041,989,1028,985,983,992],
[921,1015,918,930,999,959,0,961,968,981,961,1003],
[961,1070,983,969,1034,1011,1039,0,1001,1028,995,1008],
[979,1031,974,991,1026,972,1032,999,0,985,1017,1002],
[1000,1041,950,975,1017,1015,1019,972,1015,0,951,981],
[987,1072,938,1004,1058,1017,1039,1005,983,1049,0,972],
[982,1037,1000,952,1032,1008,997,992,998,1019,1028,0]])



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
result = np.append(np.array([12, 2000, 112, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,867,1011,937,842,1027,918,854,963,873,905,954],
[1133,0,999,965,977,1029,1055,1018,987,1008,988,962],
[989,1001,0,997,919,943,1006,905,1036,940,952,983],
[1063,1035,1003,0,967,1045,1017,976,1016,958,1011,1037],
[1158,1023,1081,1033,0,1140,1007,942,1067,1037,1034,982],
[973,971,1057,955,860,0,957,939,937,1036,927,993],
[1082,945,994,983,993,1043,0,924,1015,998,938,925],
[1146,982,1095,1024,1058,1061,1076,0,1013,1105,1034,1016],
[1037,1013,964,984,933,1063,985,987,0,1010,987,1045],
[1127,992,1060,1042,963,964,1002,895,990,0,1019,987],
[1095,1012,1048,989,966,1073,1062,966,1013,981,0,1007],
[1046,1038,1017,963,1018,1007,1075,984,955,1013,993,0]])



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
result = np.append(np.array([12, 2000, 113, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1028,1046,995,1055,1018,970,1011,1024,1000,1004,1007],
[972,0,1046,1010,997,1023,950,1005,1010,981,1026,981],
[954,954,0,955,1005,983,928,977,955,921,979,984],
[1005,990,1045,0,963,983,969,1014,1008,960,1015,978],
[945,1003,995,1037,0,952,929,979,981,930,990,960],
[982,977,1017,1017,1048,0,965,955,1021,961,1028,1005],
[1030,1050,1072,1031,1071,1035,0,1016,1054,997,1048,1042],
[989,995,1023,986,1021,1045,984,0,1068,986,1032,1026],
[976,990,1045,992,1019,979,946,932,0,960,1027,981],
[1000,1019,1079,1040,1070,1039,1003,1014,1040,0,1080,1046],
[996,974,1021,985,1010,972,952,968,973,920,0,1008],
[993,1019,1016,1022,1040,995,958,974,1019,954,992,0]])



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
result = np.append(np.array([12, 2000, 114, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,956,972,976,978,982,1026,972,968,974,924,934],
[1044,0,975,1017,967,951,1015,962,965,1039,995,1009],
[1028,1025,0,1019,998,979,1018,988,993,1027,992,1010],
[1024,983,981,0,977,954,1031,1017,1018,1011,962,981],
[1022,1033,1002,1023,0,990,1060,974,1005,1015,959,996],
[1018,1049,1021,1046,1010,0,1030,1015,987,976,1028,992],
[974,985,982,969,940,970,0,956,971,992,928,958],
[1028,1038,1012,983,1026,985,1044,0,1024,1058,1005,980],
[1032,1035,1007,982,995,1013,1029,976,0,938,957,986],
[1026,961,973,989,985,1024,1008,942,1062,0,1006,954],
[1076,1005,1008,1038,1041,972,1072,995,1043,994,0,1058],
[1066,991,990,1019,1004,1008,1042,1020,1014,1046,942,0]])



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
result = np.append(np.array([12, 2000, 115, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,979,940,969,1004,1075,1086,939,1030,956,939,1049],
[1021,0,910,894,958,961,1025,939,988,958,930,998],
[1060,1090,0,1000,1066,1076,1144,994,1036,947,1028,1115],
[1031,1106,1000,0,1073,1080,1123,1022,1059,1011,1016,1065],
[996,1042,934,927,0,1013,1159,1036,1035,983,930,1056],
[925,1039,924,920,987,0,1053,857,932,956,921,1004],
[914,975,856,877,841,947,0,888,978,890,840,947],
[1061,1061,1006,978,964,1143,1112,0,1091,986,973,1090],
[970,1012,964,941,965,1068,1022,909,0,959,911,1059],
[1044,1042,1053,989,1017,1044,1110,1014,1041,0,1047,1144],
[1061,1070,972,984,1070,1079,1160,1027,1089,953,0,1028],
[951,1002,885,935,944,996,1053,910,941,856,972,0]])



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
result = np.append(np.array([12, 2000, 116, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1055,761,1014,715,722,1461,934,889,977,1347,937],
[945,0,799,787,687,665,1234,650,1072,799,1019,892],
[1239,1201,0,934,995,812,1523,923,801,879,1152,816],
[986,1213,1066,0,818,1049,1481,1153,1057,1043,1395,810],
[1285,1313,1005,1182,0,896,1380,820,1089,1053,1256,1251],
[1278,1335,1188,951,1104,0,1682,1316,969,1150,1465,784],
[539,766,477,519,620,318,0,581,423,465,792,467],
[1066,1350,1077,847,1180,684,1419,0,712,1092,1273,1253],
[1111,928,1199,943,911,1031,1577,1288,0,1020,1356,951],
[1023,1201,1121,957,947,850,1535,908,980,0,1219,845],
[653,981,848,605,744,535,1208,727,644,781,0,945],
[1063,1108,1184,1190,749,1216,1533,747,1049,1155,1055,0]])



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
result = np.append(np.array([12, 2000, 117, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,971,965,962,1038,971,964,970,965,1015,1016,964],
[1029,0,992,1012,1042,1008,1004,979,987,1019,999,994],
[1035,1008,0,990,1030,1021,985,1019,1021,993,1014,1030],
[1038,988,1010,0,1072,1060,1000,996,1042,1001,991,1006],
[962,958,970,928,0,925,935,991,961,937,893,929],
[1029,992,979,940,1075,0,972,977,994,964,992,984],
[1036,996,1015,1000,1065,1028,0,992,1034,1012,1006,1002],
[1030,1021,981,1004,1009,1023,1008,0,1008,982,966,983],
[1035,1013,979,958,1039,1006,966,992,0,1033,977,990],
[985,981,1007,999,1063,1036,988,1018,967,0,1002,1015],
[984,1001,986,1009,1107,1008,994,1034,1023,998,0,1010],
[1036,1006,970,994,1071,1016,998,1017,1010,985,990,0]])



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
result = np.append(np.array([12, 2000, 118, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,997,1015,960,994,1044,981,980,1005,974,1012,987],
[1003,0,980,992,986,1067,1012,989,1005,974,1031,996],
[985,1020,0,959,957,1045,989,997,977,989,1000,1012],
[1040,1008,1041,0,1020,1045,1028,1030,1010,991,1003,1041],
[1006,1014,1043,980,0,1062,1017,996,995,1000,1021,999],
[956,933,955,955,938,0,958,974,942,960,976,962],
[1019,988,1011,972,983,1042,0,1004,995,963,1019,987],
[1020,1011,1003,970,1004,1026,996,0,982,972,996,991],
[995,995,1023,990,1005,1058,1005,1018,0,1003,1006,1006],
[1026,1026,1011,1009,1000,1040,1037,1028,997,0,1016,1026],
[988,969,1000,997,979,1024,981,1004,994,984,0,1011],
[1013,1004,988,959,1001,1038,1013,1009,994,974,989,0]])



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
result = np.append(np.array([12, 2000, 119, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,994,1025,972,1028,1030,996,1002,986,1035,1007,1025],
[1006,0,1050,998,1020,1059,1002,1027,1023,1049,1059,1002],
[975,950,0,1005,1015,1027,999,974,994,986,1085,961],
[1028,1002,995,0,1012,1014,1027,1050,997,1034,1081,1002],
[972,980,985,988,0,971,1002,1005,996,1015,1015,965],
[970,941,973,986,1029,0,998,977,959,1017,1040,962],
[1004,998,1001,973,998,1002,0,1020,972,963,1064,995],
[998,973,1026,950,995,1023,980,0,974,1030,1049,969],
[1014,977,1006,1003,1004,1041,1028,1026,0,1014,1050,1012],
[965,951,1014,966,985,983,1037,970,986,0,1017,1026],
[993,941,915,919,985,960,936,951,950,983,0,952],
[975,998,1039,998,1035,1038,1005,1031,988,974,1048,0]])



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
result = np.append(np.array([12, 2000, 120, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1000,987,998,1010,1012,996,990,1028,1006,997,984],
[1000,0,970,993,997,994,989,967,1004,972,998,968],
[1013,1030,0,994,1014,998,977,975,1041,994,1033,997],
[1002,1007,1006,0,1005,999,989,1017,1041,1001,1014,995],
[990,1003,986,995,0,1028,992,968,1042,972,1026,997],
[988,1006,1002,1001,972,0,978,956,992,966,992,965],
[1004,1011,1023,1011,1008,1022,0,1001,1034,1013,1004,973],
[1010,1033,1025,983,1032,1044,999,0,1044,1030,1067,1026],
[972,996,959,959,958,1008,966,956,0,964,982,959],
[994,1028,1006,999,1028,1034,987,970,1036,0,1041,1008],
[1003,1002,967,986,974,1008,996,933,1018,959,0,969],
[1016,1032,1003,1005,1003,1035,1027,974,1041,992,1031,0]])



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
result = np.append(np.array([12, 2000, 121, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,987,927,1185,1040,981,1085,951,936,967,1044,930],
[1013,0,902,970,1124,858,1149,1017,915,1001,1143,1047],
[1073,1098,0,1236,1178,1134,1354,1103,1132,987,1190,1015],
[815,1030,764,0,1087,796,1103,1002,901,1035,1049,1001],
[960,876,822,913,0,863,989,883,863,999,1028,1067],
[1019,1142,866,1204,1137,0,1195,1076,1083,1131,1157,1131],
[915,851,646,897,1011,805,0,871,791,855,964,927],
[1049,983,897,998,1117,924,1129,0,946,1123,1134,945],
[1064,1085,868,1099,1137,917,1209,1054,0,1223,1087,1089],
[1033,999,1013,965,1001,869,1145,877,777,0,918,917],
[956,857,810,951,972,843,1036,866,913,1082,0,871],
[1070,953,985,999,933,869,1073,1055,911,1083,1129,0]])



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
result = np.append(np.array([12, 2000, 122, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,958,1189,967,1148,1120,934,1100,1078,1014,1007,1084],
[1042,0,1061,1074,1000,1051,1000,948,1136,966,1121,1022],
[811,939,0,967,860,976,1013,892,1083,925,935,830],
[1033,926,1033,0,840,974,940,1027,1092,827,1045,985],
[852,1000,1140,1160,0,1075,972,1023,1108,916,1066,950],
[880,949,1024,1026,925,0,1044,964,1023,911,1036,975],
[1066,1000,987,1060,1028,956,0,959,1007,834,1009,899],
[900,1052,1108,973,977,1036,1041,0,1079,1063,1058,942],
[922,864,917,908,892,977,993,921,0,933,1058,874],
[986,1034,1075,1173,1084,1089,1166,937,1067,0,978,1104],
[993,879,1065,955,934,964,991,942,942,1022,0,882],
[916,978,1170,1015,1050,1025,1101,1058,1126,896,1118,0]])



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
result = np.append(np.array([12, 2000, 123, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,935,1019,994,986,971,973,1002,1005,991,1023,1038],
[1065,0,1063,1007,974,1024,1001,1021,1071,1061,1064,1037],
[981,937,0,966,986,974,979,1006,986,1029,1002,995],
[1006,993,1034,0,992,964,956,996,1002,999,1000,956],
[1014,1026,1014,1008,0,1028,979,1021,1021,1007,1034,971],
[1029,976,1026,1036,972,0,967,986,962,992,1007,989],
[1027,999,1021,1044,1021,1033,0,1042,1111,1002,1056,990],
[998,979,994,1004,979,1014,958,0,992,1023,1019,1014],
[995,929,1014,998,979,1038,889,1008,0,1008,1004,988],
[1009,939,971,1001,993,1008,998,977,992,0,997,982],
[977,936,998,1000,966,993,944,981,996,1003,0,988],
[962,963,1005,1044,1029,1011,1010,986,1012,1018,1012,0]])



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
result = np.append(np.array([12, 2000, 124, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1022,928,1010,995,982,957,975,1006,1003,959,996],
[978,0,939,1001,1005,971,1022,982,985,1007,959,966],
[1072,1061,0,1008,992,1014,1031,1043,1028,1015,1017,1026],
[990,999,992,0,991,995,978,1001,974,1022,955,983],
[1005,995,1008,1009,0,949,978,1004,1007,979,985,989],
[1018,1029,986,1005,1051,0,1021,986,988,997,1021,999],
[1043,978,969,1022,1022,979,0,977,1010,1007,989,986],
[1025,1018,957,999,996,1014,1023,0,1032,1014,1005,996],
[994,1015,972,1026,993,1012,990,968,0,1006,957,988],
[997,993,985,978,1021,1003,993,986,994,0,961,996],
[1041,1041,983,1045,1015,979,1011,995,1043,1039,0,1001],
[1004,1034,974,1017,1011,1001,1014,1004,1012,1004,999,0]])



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
result = np.append(np.array([12, 2000, 125, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,997,985,1008,1010,1011,1031,997,1005,1001,1006,993],
[1003,0,1012,1009,1026,983,998,1026,996,1003,1009,1003],
[1015,988,0,997,1014,974,1003,989,1006,985,1024,989],
[992,991,1003,0,996,998,1006,967,981,968,1011,985],
[990,974,986,1004,0,1003,992,1004,1002,1006,996,985],
[989,1017,1026,1002,997,0,1041,1014,987,1009,1021,1014],
[969,1002,997,994,1008,959,0,984,1018,1007,1013,982],
[1003,974,1011,1033,996,986,1016,0,1006,1002,1016,980],
[995,1004,994,1019,998,1013,982,994,0,1030,999,1001],
[999,997,1015,1032,994,991,993,998,970,0,1004,983],
[994,991,976,989,1004,979,987,984,1001,996,0,992],
[1007,997,1011,1015,1015,986,1018,1020,999,1017,1008,0]])



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
result = np.append(np.array([12, 2000, 126, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,680,819,876,1001,1108,891,737,910,1234,644,872],
[1320,0,1352,1346,1332,1326,764,1126,1082,848,841,1492],
[1181,648,0,1053,766,1014,377,939,913,677,782,1252],
[1124,654,947,0,734,1179,295,886,1058,1093,886,1070],
[999,668,1234,1266,0,1009,678,934,1098,747,529,1294],
[892,674,986,821,991,0,1097,828,904,1151,629,1120],
[1109,1236,1623,1705,1322,903,0,1280,1331,1583,1280,1559],
[1263,874,1061,1114,1066,1172,720,0,1198,1005,878,1030],
[1090,918,1087,942,902,1096,669,802,0,1034,807,1103],
[766,1152,1323,907,1253,849,417,995,966,0,884,1109],
[1356,1159,1218,1114,1471,1371,720,1122,1193,1116,0,1483],
[1128,508,748,930,706,880,441,970,897,891,517,0]])



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
result = np.append(np.array([12, 2000, 127, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,956,989,1070,951,1010,994,955,984,1031,994,938],
[1044,0,1002,1071,997,1035,998,992,1009,950,993,949],
[1011,998,0,1049,1002,1015,1032,1013,1002,1056,1055,961],
[930,929,951,0,939,961,980,967,953,903,945,939],
[1049,1003,998,1061,0,967,982,1053,1034,982,994,975],
[990,965,985,1039,1033,0,1013,986,961,1011,972,940],
[1006,1002,968,1020,1018,987,0,1056,990,1056,1029,986],
[1045,1008,987,1033,947,1014,944,0,994,992,970,1006],
[1016,991,998,1047,966,1039,1010,1006,0,960,974,953],
[969,1050,944,1097,1018,989,944,1008,1040,0,1036,932],
[1006,1007,945,1055,1006,1028,971,1030,1026,964,0,944],
[1062,1051,1039,1061,1025,1060,1014,994,1047,1068,1056,0]])



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
result = np.append(np.array([12, 2000, 128, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,927,1125,918,1011,1103,972,939,962,957,1080,993],
[1073,0,1145,938,1075,1092,1035,1189,1004,1012,1039,1081],
[875,855,0,797,1039,1002,914,1023,757,952,932,867],
[1082,1062,1203,0,1169,1105,1069,1198,993,941,1156,1207],
[989,925,961,831,0,1057,893,953,967,946,969,932],
[897,908,998,895,943,0,967,963,843,811,898,946],
[1028,965,1086,931,1107,1033,0,1077,958,1054,995,943],
[1061,811,977,802,1047,1037,923,0,954,924,990,1001],
[1038,996,1243,1007,1033,1157,1042,1046,0,1013,1121,1072],
[1043,988,1048,1059,1054,1189,946,1076,987,0,1029,1019],
[920,961,1068,844,1031,1102,1005,1010,879,971,0,1013],
[1007,919,1133,793,1068,1054,1057,999,928,981,987,0]])



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
result = np.append(np.array([12, 2000, 129, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1013,995,1037,988,1011,1035,1014,1020,993,1010,1038],
[987,0,1009,1037,972,978,1010,981,987,972,972,1007],
[1005,991,0,1035,994,997,1036,1015,1006,1012,998,1034],
[963,963,965,0,973,948,963,961,972,950,961,977],
[1012,1028,1006,1027,0,1008,1039,1015,1013,995,1030,1014],
[989,1022,1003,1052,992,0,1024,1011,1022,987,993,1005],
[965,990,964,1037,961,976,0,995,972,991,1003,994],
[986,1019,985,1039,985,989,1005,0,1000,990,1015,1002],
[980,1013,994,1028,987,978,1028,1000,0,1004,994,1007],
[1007,1028,988,1050,1005,1013,1009,1010,996,0,1019,1019],
[990,1028,1002,1039,970,1007,997,985,1006,981,0,1015],
[962,993,966,1023,986,995,1006,998,993,981,985,0]])



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
result = np.append(np.array([12, 2000, 130, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,992,994,1019,1047,1020,983,960,1098,1021,1052,1036],
[1008,0,1021,1004,1027,965,973,1004,1082,1039,1010,1068],
[1006,979,0,983,1059,1017,1010,1008,1066,1064,1064,1028],
[981,996,1017,0,1052,994,989,1000,1077,1052,1101,1010],
[953,973,941,948,0,954,980,967,1058,994,1009,1005],
[980,1035,983,1006,1046,0,1043,1018,1075,1046,1051,1033],
[1017,1027,990,1011,1020,957,0,1005,1075,1013,1010,1035],
[1040,996,992,1000,1033,982,995,0,1070,1035,1023,993],
[902,918,934,923,942,925,925,930,0,975,984,933],
[979,961,936,948,1006,954,987,965,1025,0,1028,981],
[948,990,936,899,991,949,990,977,1016,972,0,950],
[964,932,972,990,995,967,965,1007,1067,1019,1050,0]])



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
result = np.append(np.array([12, 2000, 131, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,996,990,958,980,979,954,981,931,983,943,946],
[1004,0,994,917,966,938,952,1005,943,981,946,955],
[1010,1006,0,987,985,946,935,954,974,983,974,929],
[1042,1083,1013,0,1008,1031,995,1043,1002,1045,972,977],
[1020,1034,1015,992,0,978,965,1018,925,941,918,931],
[1021,1062,1054,969,1022,0,1078,1024,966,989,982,1026],
[1046,1048,1065,1005,1035,922,0,1006,1001,1046,1000,946],
[1019,995,1046,957,982,976,994,0,952,995,953,941],
[1069,1057,1026,998,1075,1034,999,1048,0,1021,1016,1010],
[1017,1019,1017,955,1059,1011,954,1005,979,0,988,987],
[1057,1054,1026,1028,1082,1018,1000,1047,984,1012,0,989],
[1054,1045,1071,1023,1069,974,1054,1059,990,1013,1011,0]])



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
result = np.append(np.array([12, 2000, 132, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,971,1029,967,945,979,1013,1078,977,1016,1025,1018],
[1029,0,1074,1035,975,1014,1024,1015,987,1054,1041,1087],
[971,926,0,1013,927,934,973,1016,1023,1013,954,1000],
[1033,965,987,0,938,1010,1020,1040,994,1016,1043,1013],
[1055,1025,1073,1062,0,994,1055,1057,1032,1028,1089,1063],
[1021,986,1066,990,1006,0,976,1048,1022,1060,1046,1063],
[987,976,1027,980,945,1024,0,1023,964,990,993,1023],
[922,985,984,960,943,952,977,0,994,985,1016,1007],
[1023,1013,977,1006,968,978,1036,1006,0,995,1072,1060],
[984,946,987,984,972,940,1010,1015,1005,0,973,990],
[975,959,1046,957,911,954,1007,984,928,1027,0,999],
[982,913,1000,987,937,937,977,993,940,1010,1001,0]])



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
result = np.append(np.array([12, 2000, 133, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1248,1096,1306,1079,1056,992,1213,1163,1131,1126,1173],
[752,0,750,793,865,903,830,988,938,811,762,748],
[904,1250,0,1151,983,1030,1032,1070,1126,1106,1078,895],
[694,1207,849,0,857,783,838,944,990,950,850,941],
[921,1135,1017,1143,0,853,1041,1202,1210,906,1105,1067],
[944,1097,970,1217,1147,0,1059,1228,1269,1096,883,1028],
[1008,1170,968,1162,959,941,0,1116,1092,1005,913,1072],
[787,1012,930,1056,798,772,884,0,1012,964,760,820],
[837,1062,874,1010,790,731,908,988,0,849,823,900],
[869,1189,894,1050,1094,904,995,1036,1151,0,862,949],
[874,1238,922,1150,895,1117,1087,1240,1177,1138,0,1072],
[827,1252,1105,1059,933,972,928,1180,1100,1051,928,0]])



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
result = np.append(np.array([12, 2000, 134, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1024,1021,1035,1019,1018,994,1036,1044,1012,1026,994],
[976,0,1021,1016,990,1012,979,1018,990,1010,1054,1012],
[979,979,0,1029,1001,1015,1012,1048,1020,1004,1024,997],
[965,984,971,0,1002,984,989,1039,1015,1002,990,947],
[981,1010,999,998,0,1026,963,1036,1030,1000,991,984],
[982,988,985,1016,974,0,980,1011,1021,978,1021,983],
[1006,1021,988,1011,1037,1020,0,1038,1019,989,1037,1001],
[964,982,952,961,964,989,962,0,971,978,968,938],
[956,1010,980,985,970,979,981,1029,0,1020,1040,1010],
[988,990,996,998,1000,1022,1011,1022,980,0,985,968],
[974,946,976,1010,1009,979,963,1032,960,1015,0,965],
[1006,988,1003,1053,1016,1017,999,1062,990,1032,1035,0]])



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
result = np.append(np.array([12, 2000, 135, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,831,808,760,775,771,859,469,908,795,862,757],
[1169,0,1269,857,933,857,1020,959,1090,989,1110,1231],
[1192,731,0,675,752,763,923,854,727,873,1070,1156],
[1240,1143,1325,0,951,1052,991,991,1002,1071,1235,1064],
[1225,1067,1248,1049,0,889,883,781,896,1182,1094,1154],
[1229,1143,1237,948,1111,0,1054,1034,953,1034,1287,1208],
[1141,980,1077,1009,1117,946,0,807,1025,1031,1023,1075],
[1531,1041,1146,1009,1219,966,1193,0,1171,1147,1171,1378],
[1092,910,1273,998,1104,1047,975,829,0,873,1092,1163],
[1205,1011,1127,929,818,966,969,853,1127,0,1002,971],
[1138,890,930,765,906,713,977,829,908,998,0,1196],
[1243,769,844,936,846,792,925,622,837,1029,804,0]])



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
result = np.append(np.array([12, 2000, 136, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1088,1012,987,1013,1015,1032,1013,1013,1100,1102,967],
[912,0,895,980,929,988,1006,956,942,1001,1028,952],
[988,1105,0,1007,999,1018,1027,970,993,1055,1053,972],
[1013,1020,993,0,987,1057,1006,961,978,1059,1075,969],
[987,1071,1001,1013,0,1059,1015,1044,967,1075,1084,988],
[985,1012,982,943,941,0,983,953,958,1054,1023,954],
[968,994,973,994,985,1017,0,984,986,1075,1035,954],
[987,1044,1030,1039,956,1047,1016,0,1037,1060,1077,1020],
[987,1058,1007,1022,1033,1042,1014,963,0,1065,1060,981],
[900,999,945,941,925,946,925,940,935,0,1039,917],
[898,972,947,925,916,977,965,923,940,961,0,926],
[1033,1048,1028,1031,1012,1046,1046,980,1019,1083,1074,0]])



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
result = np.append(np.array([12, 2000, 137, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,994,1028,955,972,1002,1008,997,974,995,1016,1010],
[1006,0,1052,1004,1005,1020,1032,1000,976,1009,1076,1032],
[972,948,0,977,951,975,993,953,971,942,1008,992],
[1045,996,1023,0,996,1001,1025,988,1000,1001,1052,1022],
[1028,995,1049,1004,0,1004,1015,994,986,996,1047,1005],
[998,980,1025,999,996,0,1019,1001,974,997,1056,1003],
[992,968,1007,975,985,981,0,941,957,985,1031,1017],
[1003,1000,1047,1012,1006,999,1059,0,992,1025,1071,1013],
[1026,1024,1029,1000,1014,1026,1043,1008,0,1027,1068,1021],
[1005,991,1058,999,1004,1003,1015,975,973,0,1004,1015],
[984,924,992,948,953,944,969,929,932,996,0,965],
[990,968,1008,978,995,997,983,987,979,985,1035,0]])



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
result = np.append(np.array([12, 2000, 138, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,985,1003,1039,1052,948,1018,1008,1008,1003,993,1029],
[1015,0,1040,1051,1005,1003,984,1102,1047,1042,994,1020],
[997,960,0,1037,930,965,968,1061,993,1045,990,1014],
[961,949,963,0,939,943,944,982,963,949,939,952],
[948,995,1070,1061,0,992,988,1068,1003,1005,999,1035],
[1052,997,1035,1057,1008,0,1059,1040,995,983,1027,1020],
[982,1016,1032,1056,1012,941,0,1069,1013,1019,961,1017],
[992,898,939,1018,932,960,931,0,920,943,902,973],
[992,953,1007,1037,997,1005,987,1080,0,974,982,1013],
[997,958,955,1051,995,1017,981,1057,1026,0,1004,972],
[1007,1006,1010,1061,1001,973,1039,1098,1018,996,0,1021],
[971,980,986,1048,965,980,983,1027,987,1028,979,0]])



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
result = np.append(np.array([12, 2000, 139, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,916,906,919,933,969,988,983,918,990,926,912],
[1084,0,976,972,1080,1033,1028,1019,981,1082,988,1027],
[1094,1024,0,1037,1041,975,1056,1073,1048,1057,1013,1043],
[1081,1028,963,0,1021,1041,1098,1073,1030,1093,1002,1060],
[1067,920,959,979,0,965,1041,997,947,1013,977,986],
[1031,967,1025,959,1035,0,1058,1041,932,1024,1067,1006],
[1012,972,944,902,959,942,0,991,968,982,966,988],
[1017,981,927,927,1003,959,1009,0,968,1018,932,988],
[1082,1019,952,970,1053,1068,1032,1032,0,1087,1036,1028],
[1010,918,943,907,987,976,1018,982,913,0,954,973],
[1074,1012,987,998,1023,933,1034,1068,964,1046,0,986],
[1088,973,957,940,1014,994,1012,1012,972,1027,1014,0]])



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
result = np.append(np.array([12, 2000, 140, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1013,1023,1051,1011,998,974,1011,1014,1021,1028,1017],
[987,0,981,1003,989,966,965,969,951,974,1006,967],
[977,1019,0,1020,1038,996,992,1023,985,1012,992,988],
[949,997,980,0,1006,970,965,967,950,1026,972,988],
[989,1011,962,994,0,945,990,968,992,980,1022,1012],
[1002,1034,1004,1030,1055,0,995,1005,962,1007,1021,1021],
[1026,1035,1008,1035,1010,1005,0,1010,992,1011,985,1032],
[989,1031,977,1033,1032,995,990,0,982,991,1011,1005],
[986,1049,1015,1050,1008,1038,1008,1018,0,998,1029,1029],
[979,1026,988,974,1020,993,989,1009,1002,0,1038,989],
[972,994,1008,1028,978,979,1015,989,971,962,0,968],
[983,1033,1012,1012,988,979,968,995,971,1011,1032,0]])



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
result = np.append(np.array([12, 2000, 141, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1004,994,1030,1016,973,967,1011,981,1025,981,987],
[996,0,1022,989,1016,998,979,1029,1004,1043,993,965],
[1006,978,0,991,977,976,987,994,958,1021,1005,961],
[970,1011,1009,0,1003,1006,962,1023,968,1048,1003,972],
[984,984,1023,997,0,976,1009,1012,983,1048,1016,960],
[1027,1002,1024,994,1024,0,986,1018,993,1055,999,973],
[1033,1021,1013,1038,991,1014,0,1053,1014,1086,1003,1003],
[989,971,1006,977,988,982,947,0,984,1016,996,977],
[1019,996,1042,1032,1017,1007,986,1016,0,1066,1018,1005],
[975,957,979,952,952,945,914,984,934,0,949,940],
[1019,1007,995,997,984,1001,997,1004,982,1051,0,982],
[1013,1035,1039,1028,1040,1027,997,1023,995,1060,1018,0]])



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
result = np.append(np.array([12, 2000, 142, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,955,984,1027,985,1032,1013,1001,1022,1017,1014,1006],
[1045,0,991,1039,1012,1015,1003,1016,1004,1008,1024,1021],
[1016,1009,0,1037,1009,1016,981,1020,1010,1018,981,1000],
[973,961,963,0,956,991,954,950,995,969,971,974],
[1015,988,991,1044,0,1025,994,968,1038,1023,999,1028],
[968,985,984,1009,975,0,974,996,1012,983,980,986],
[987,997,1019,1046,1006,1026,0,995,1032,1000,1027,1030],
[999,984,980,1050,1032,1004,1005,0,998,1007,998,1003],
[978,996,990,1005,962,988,968,1002,0,999,975,999],
[983,992,982,1031,977,1017,1000,993,1001,0,984,1022],
[986,976,1019,1029,1001,1020,973,1002,1025,1016,0,1025],
[994,979,1000,1026,972,1014,970,997,1001,978,975,0]])



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
result = np.append(np.array([12, 2000, 143, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1037,1010,1042,972,1055,1042,1026,1043,1044,1011,996],
[963,0,971,988,966,1015,1006,1000,1028,994,994,966],
[990,1029,0,1000,989,1011,995,1035,1018,959,1025,981],
[958,1012,1000,0,960,981,1039,1030,1004,1001,976,967],
[1028,1034,1011,1040,0,1010,1009,1028,1008,1047,991,998],
[945,985,989,1019,990,0,964,991,988,982,980,968],
[958,994,1005,961,991,1036,0,1015,1003,981,989,1007],
[974,1000,965,970,972,1009,985,0,1015,980,990,972],
[957,972,982,996,992,1012,997,985,0,989,988,969],
[956,1006,1041,999,953,1018,1019,1020,1011,0,990,973],
[989,1006,975,1024,1009,1020,1011,1010,1012,1010,0,969],
[1004,1034,1019,1033,1002,1032,993,1028,1031,1027,1031,0]])



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
result = np.append(np.array([12, 2000, 144, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1002,1110,1127,1067,1078,1019,978,1073,1058,1127,1084],
[998,0,1082,1061,1018,1020,1006,1064,1023,1004,1078,1069],
[890,918,0,955,951,949,974,941,1001,970,1040,1012],
[873,939,1045,0,977,932,942,975,874,913,960,984],
[933,982,1049,1023,0,966,940,986,979,969,1056,1041],
[922,980,1051,1068,1034,0,951,1028,1018,1002,1079,1125],
[981,994,1026,1058,1060,1049,0,1074,1012,978,1088,1082],
[1022,936,1059,1025,1014,972,926,0,1000,980,957,1017],
[927,977,999,1126,1021,982,988,1000,0,1032,1043,1055],
[942,996,1030,1087,1031,998,1022,1020,968,0,1092,1090],
[873,922,960,1040,944,921,912,1043,957,908,0,1008],
[916,931,988,1016,959,875,918,983,945,910,992,0]])



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
result = np.append(np.array([12, 2000, 145, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,963,996,969,974,1014,1008,970,954,991,958,992],
[1037,0,1043,989,994,1041,1005,1010,1007,996,979,1025],
[1004,957,0,1008,1000,1048,1026,1007,972,1019,977,1015],
[1031,1011,992,0,999,1018,1032,1034,1005,1002,1003,1001],
[1026,1006,1000,1001,0,1012,1019,1004,992,1017,973,990],
[986,959,952,982,988,0,984,983,993,987,961,1016],
[992,995,974,968,981,1016,0,989,950,987,958,977],
[1030,990,993,966,996,1017,1011,0,991,997,970,996],
[1046,993,1028,995,1008,1007,1050,1009,0,1016,991,1015],
[1009,1004,981,998,983,1013,1013,1003,984,0,996,989],
[1042,1021,1023,997,1027,1039,1042,1030,1009,1004,0,1048],
[1008,975,985,999,1010,984,1023,1004,985,1011,952,0]])



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
result = np.append(np.array([12, 2000, 146, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,990,981,1024,980,1021,1046,1012,1045,980,962,1041],
[1010,0,973,1021,960,985,1044,1033,1005,969,1008,988],
[1019,1027,0,1069,993,1038,1027,1070,1085,1008,996,1041],
[976,979,931,0,950,983,1027,1030,1011,903,1018,994],
[1020,1040,1007,1050,0,1055,1032,1021,1063,1023,996,1031],
[979,1015,962,1017,945,0,1037,1029,1040,988,1002,1006],
[954,956,973,973,968,963,0,971,1011,947,941,938],
[988,967,930,970,979,971,1029,0,1010,983,912,997],
[955,995,915,989,937,960,989,990,0,938,933,976],
[1020,1031,992,1097,977,1012,1053,1017,1062,0,980,971],
[1038,992,1004,982,1004,998,1059,1088,1067,1020,0,1026],
[959,1012,959,1006,969,994,1062,1003,1024,1029,974,0]])



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
result = np.append(np.array([12, 2000, 147, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,998,948,1016,1008,1045,993,1002,1056,1040,1030,993],
[1002,0,1038,1000,1033,1048,1041,1004,1051,1065,1057,1041],
[1052,962,0,952,1006,1078,1023,993,1033,1062,1070,990],
[984,1000,1048,0,1033,1077,1036,1025,1040,1022,1015,1033],
[992,967,994,967,0,1063,983,976,985,1043,988,986],
[955,952,922,923,937,0,914,920,985,953,962,988],
[1007,959,977,964,1017,1086,0,960,1019,1034,991,1067],
[998,996,1007,975,1024,1080,1040,0,1073,1042,987,1031],
[944,949,967,960,1015,1015,981,927,0,1011,946,1008],
[960,935,938,978,957,1047,966,958,989,0,958,995],
[970,943,930,985,1012,1038,1009,1013,1054,1042,0,1025],
[1007,959,1010,967,1014,1012,933,969,992,1005,975,0]])



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
result = np.append(np.array([12, 2000, 148, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,928,995,989,999,997,933,980,999,908,989,1051],
[1072,0,1035,1050,1074,1014,974,1036,1026,1004,1027,1046],
[1005,965,0,987,1030,1013,958,1001,999,1002,966,1033],
[1011,950,1013,0,1039,999,936,984,1026,981,972,1001],
[1001,926,970,961,0,926,926,932,976,947,950,951],
[1003,986,987,1001,1074,0,938,951,1044,983,999,990],
[1067,1026,1042,1064,1074,1062,0,1019,1076,982,1028,1080],
[1020,964,999,1016,1068,1049,981,0,1055,991,988,1065],
[1001,974,1001,974,1024,956,924,945,0,958,942,1033],
[1092,996,998,1019,1053,1017,1018,1009,1042,0,1044,1020],
[1011,973,1034,1028,1050,1001,972,1012,1058,956,0,1046],
[949,954,967,999,1049,1010,920,935,967,980,954,0]])



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
result = np.append(np.array([12, 2000, 149, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,953,948,1023,1001,1048,994,1031,977,998,999,1006],
[1047,0,1008,992,1003,1028,1019,1040,1010,1025,986,984],
[1052,992,0,1005,994,1020,1014,1011,1002,1038,1002,987],
[977,1008,995,0,999,1022,999,1038,992,993,1010,983],
[999,997,1006,1001,0,1076,1006,1040,1065,989,1005,997],
[952,972,980,978,924,0,956,992,1000,951,973,971],
[1006,981,986,1001,994,1044,0,1013,975,1014,1018,963],
[969,960,989,962,960,1008,987,0,982,1007,989,960],
[1023,990,998,1008,935,1000,1025,1018,0,1027,1011,985],
[1002,975,962,1007,1011,1049,986,993,973,0,1016,1001],
[1001,1014,998,990,995,1027,982,1011,989,984,0,972],
[994,1016,1013,1017,1003,1029,1037,1040,1015,999,1028,0]])



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
result = np.append(np.array([12, 2000, 150, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,985,998,1000,1004,1017,1025,978,1043,976,1015,998],
[1015,0,1025,1022,1005,1022,1012,991,1037,1004,1017,1006],
[1002,975,0,1005,995,1021,998,987,1013,959,1003,991],
[1000,978,995,0,991,1034,1006,995,1014,941,1028,975],
[996,995,1005,1009,0,993,1036,1013,1059,956,1020,998],
[983,978,979,966,1007,0,996,978,1010,968,1030,978],
[975,988,1002,994,964,1004,0,959,989,933,990,997],
[1022,1009,1013,1005,987,1022,1041,0,1022,968,1031,1025],
[957,963,987,986,941,990,1011,978,0,944,975,983],
[1024,996,1041,1059,1044,1032,1067,1032,1056,0,1037,1028],
[985,983,997,972,980,970,1010,969,1025,963,0,988],
[1002,994,1009,1025,1002,1022,1003,975,1017,972,1012,0]])



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
result = np.append(np.array([12, 2000, 151, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1003,1002,1023,1031,1009,996,1007,1020,1016,998,1002],
[997,0,978,1022,1013,1021,985,1015,996,1006,1016,1027],
[998,1022,0,1053,1029,992,992,1002,1012,1027,1038,1019],
[977,978,947,0,998,959,950,986,972,995,968,973],
[969,987,971,1002,0,989,941,970,985,1026,1006,1000],
[991,979,1008,1041,1011,0,972,1013,979,1006,972,1003],
[1004,1015,1008,1050,1059,1028,0,1002,997,1004,1007,1017],
[993,985,998,1014,1030,987,998,0,975,998,994,1008],
[980,1004,988,1028,1015,1021,1003,1025,0,1011,989,1016],
[984,994,973,1005,974,994,996,1002,989,0,996,988],
[1002,984,962,1032,994,1028,993,1006,1011,1004,0,996],
[998,973,981,1027,1000,997,983,992,984,1012,1004,0]])



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
result = np.append(np.array([12, 2000, 152, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,992,979,952,994,971,1035,996,1003,963,1033,991],
[1008,0,1019,1055,1136,958,1070,988,1041,1008,1061,1003],
[1021,981,0,962,1055,968,1100,1009,1029,1067,994,968],
[1048,945,1038,0,1042,1008,974,978,930,1048,1043,1007],
[1006,864,945,958,0,985,999,1033,1000,983,984,943],
[1029,1042,1032,992,1015,0,1083,1047,1024,1021,1044,953],
[965,930,900,1026,1001,917,0,892,921,985,967,919],
[1004,1012,991,1022,967,953,1108,0,1012,1006,1031,995],
[997,959,971,1070,1000,976,1079,988,0,1071,1032,974],
[1037,992,933,952,1017,979,1015,994,929,0,994,953],
[967,939,1006,957,1016,956,1033,969,968,1006,0,939],
[1009,997,1032,993,1057,1047,1081,1005,1026,1047,1061,0]])



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
result = np.append(np.array([12, 2000, 153, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,972,991,978,969,987,963,1006,995,982,955,929],
[1028,0,953,943,1022,974,925,966,1033,984,959,1012],
[1009,1047,0,988,1042,1013,986,1034,1019,1007,1017,1034],
[1022,1057,1012,0,1016,981,966,1010,1019,1015,994,979],
[1031,978,958,984,0,969,1000,981,1013,1003,948,978],
[1013,1026,987,1019,1031,0,1010,1017,1094,1061,973,1012],
[1037,1075,1014,1034,1000,990,0,1002,1022,1036,968,988],
[994,1034,966,990,1019,983,998,0,1008,947,975,963],
[1005,967,981,981,987,906,978,992,0,968,963,1022],
[1018,1016,993,985,997,939,964,1053,1032,0,1000,965],
[1045,1041,983,1006,1052,1027,1032,1025,1037,1000,0,1002],
[1071,988,966,1021,1022,988,1012,1037,978,1035,998,0]])



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
result = np.append(np.array([12, 2000, 154, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1048,990,1002,972,1033,995,1037,1086,1091,996,963],
[952,0,984,1056,949,976,931,986,1042,949,977,905],
[1010,1016,0,999,943,990,1049,1055,1026,1018,910,1014],
[998,944,1001,0,950,949,975,942,1063,992,961,920],
[1028,1051,1057,1050,0,1004,1049,1057,1050,1000,1050,1015],
[967,1024,1010,1051,996,0,1082,1052,1053,1038,1031,938],
[1005,1069,951,1025,951,918,0,959,1005,984,964,990],
[963,1014,945,1058,943,948,1041,0,970,952,944,985],
[914,958,974,937,950,947,995,1030,0,903,918,971],
[909,1051,982,1008,1000,962,1016,1048,1097,0,938,1008],
[1004,1023,1090,1039,950,969,1036,1056,1082,1062,0,1029],
[1037,1095,986,1080,985,1062,1010,1015,1029,992,971,0]])



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
result = np.append(np.array([12, 2000, 155, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,984,1022,1017,968,1017,938,964,1009,980,983,1003],
[1016,0,1043,1000,962,1012,1005,960,990,1002,999,997],
[978,957,0,979,945,1002,951,967,979,988,940,957],
[983,1000,1021,0,987,1018,952,971,1001,984,972,1013],
[1032,1038,1055,1013,0,1039,945,997,1035,998,987,1028],
[983,988,998,982,961,0,922,963,963,963,939,953],
[1062,995,1049,1048,1055,1078,0,1016,1050,1034,1035,1035],
[1036,1040,1033,1029,1003,1037,984,0,1042,1005,964,1023],
[991,1010,1021,999,965,1037,950,958,0,972,999,994],
[1020,998,1012,1016,1002,1037,966,995,1028,0,953,1019],
[1017,1001,1060,1028,1013,1061,965,1036,1001,1047,0,1026],
[997,1003,1043,987,972,1047,965,977,1006,981,974,0]])



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
result = np.append(np.array([12, 2000, 156, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1012,1046,1034,1039,1050,992,1029,1025,1021,1018,1045],
[988,0,1008,990,1014,1026,1048,1007,999,986,999,1005],
[954,992,0,984,1004,1000,993,1016,986,950,993,1002],
[966,1010,1016,0,1005,1033,1011,1044,1007,1016,1007,1034],
[961,986,996,995,0,1011,983,995,990,996,974,986],
[950,974,1000,967,989,0,977,974,967,974,986,960],
[1008,952,1007,989,1017,1023,0,1032,1001,993,977,995],
[971,993,984,956,1005,1026,968,0,997,993,994,1019],
[975,1001,1014,993,1010,1033,999,1003,0,988,994,1026],
[979,1014,1050,984,1004,1026,1007,1007,1012,0,1031,1021],
[982,1001,1007,993,1026,1014,1023,1006,1006,969,0,1019],
[955,995,998,966,1014,1040,1005,981,974,979,981,0]])



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
result = np.append(np.array([12, 2000, 157, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1086,1410,1158,1060,1056,1261,1176,1049,1065,969,1073],
[914,0,1118,1193,981,989,976,1275,993,1041,877,903],
[590,882,0,850,824,956,882,1012,890,888,920,750],
[842,807,1150,0,987,851,951,926,886,902,963,842],
[940,1019,1176,1013,0,1097,966,1262,1210,1191,1165,930],
[944,1011,1044,1149,903,0,919,1085,1023,959,897,847],
[739,1024,1118,1049,1034,1081,0,1072,905,1181,1120,978],
[824,725,988,1074,738,915,928,0,827,813,739,881],
[951,1007,1110,1114,790,977,1095,1173,0,1000,920,1001],
[935,959,1112,1098,809,1041,819,1187,1000,0,895,890],
[1031,1123,1080,1037,835,1103,880,1261,1080,1105,0,946],
[927,1097,1250,1158,1070,1153,1022,1119,999,1110,1054,0]])



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
result = np.append(np.array([12, 2000, 158, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,941,978,992,1005,1024,941,959,994,1040,1034,925],
[1059,0,1002,997,989,1038,1038,1034,1038,1078,1071,996],
[1022,998,0,983,1013,1005,1019,1012,1038,1102,1018,1019],
[1008,1003,1017,0,1011,1051,998,992,992,1047,1039,1008],
[995,1011,987,989,0,1041,979,1022,985,1051,1029,1020],
[976,962,995,949,959,0,981,992,1001,1002,1010,951],
[1059,962,981,1002,1021,1019,0,1022,1048,1098,1054,1000],
[1041,966,988,1008,978,1008,978,0,995,1047,1015,968],
[1006,962,962,1008,1015,999,952,1005,0,1024,951,965],
[960,922,898,953,949,998,902,953,976,0,1002,947],
[966,929,982,961,971,990,946,985,1049,998,0,962],
[1075,1004,981,992,980,1049,1000,1032,1035,1053,1038,0]])



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
result = np.append(np.array([12, 2000, 159, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1038,998,1032,1025,1049,941,996,1054,975,975,1088],
[962,0,975,963,999,1002,923,964,993,924,931,1074],
[1002,1025,0,1017,1077,1041,964,1060,1090,943,1028,1051],
[968,1037,983,0,1012,1052,932,972,1078,952,952,1066],
[975,1001,923,988,0,1014,952,1014,1052,988,905,1041],
[951,998,959,948,986,0,843,934,1058,967,868,1002],
[1059,1077,1036,1068,1048,1157,0,1023,1092,1152,988,1134],
[1004,1036,940,1028,986,1066,977,0,1036,1034,933,1069],
[946,1007,910,922,948,942,908,964,0,904,929,1021],
[1025,1076,1057,1048,1012,1033,848,966,1096,0,940,1097],
[1025,1069,972,1048,1095,1132,1012,1067,1071,1060,0,1166],
[912,926,949,934,959,998,866,931,979,903,834,0]])



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
result = np.append(np.array([12, 2000, 160, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,905,1034,982,927,997,962,945,937,979,958,1022],
[1095,0,1032,975,972,1040,988,995,1012,1011,1019,1008],
[966,968,0,928,897,952,921,892,930,974,937,999],
[1018,1025,1072,0,940,1051,960,1037,967,1015,969,1063],
[1073,1028,1103,1060,0,1040,1063,1055,1037,1077,1000,1075],
[1003,960,1048,949,960,0,973,972,936,976,979,1047],
[1038,1012,1079,1040,937,1027,0,987,975,1029,1031,1041],
[1055,1005,1108,963,945,1028,1013,0,989,1015,992,1075],
[1063,988,1070,1033,963,1064,1025,1011,0,1016,1006,1092],
[1021,989,1026,985,923,1024,971,985,984,0,1004,1023],
[1042,981,1063,1031,1000,1021,969,1008,994,996,0,1040],
[978,992,1001,937,925,953,959,925,908,977,960,0]])



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
result = np.append(np.array([12, 2000, 161, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1045,1014,860,1009,986,1058,1121,1021,988,1006,1002],
[955,0,990,889,1010,927,1057,1104,1073,878,902,876],
[986,1010,0,910,963,975,1015,1068,994,1023,973,995],
[1140,1111,1090,0,1110,1070,1116,1113,1069,996,1035,1000],
[991,990,1037,890,0,997,1022,998,1022,967,1041,1014],
[1014,1073,1025,930,1003,0,1097,1055,1036,1063,1028,1031],
[942,943,985,884,978,903,0,985,1006,882,977,871],
[879,896,932,887,1002,945,1015,0,825,932,970,859],
[979,927,1006,931,978,964,994,1175,0,1039,1024,928],
[1012,1122,977,1004,1033,937,1118,1068,961,0,982,950],
[994,1098,1027,965,959,972,1023,1030,976,1018,0,994],
[998,1124,1005,1000,986,969,1129,1141,1072,1050,1006,0]])



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
result = np.append(np.array([12, 2000, 162, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,971,994,996,1016,995,972,1011,1007,1035,1049,1016],
[1029,0,1012,1003,1002,996,996,1014,1029,1043,1041,1028],
[1006,988,0,1009,1011,988,1001,1026,1027,1016,1043,1023],
[1004,997,991,0,1015,1002,1012,1039,1042,1022,1053,992],
[984,998,989,985,0,994,974,1001,1032,1020,1023,991],
[1005,1004,1012,998,1006,0,998,986,1010,1050,1061,987],
[1028,1004,999,988,1026,1002,0,1043,1038,1048,1068,1037],
[989,986,974,961,999,1014,957,0,1019,1026,1029,968],
[993,971,973,958,968,990,962,981,0,981,1013,991],
[965,957,984,978,980,950,952,974,1019,0,1027,991],
[951,959,957,947,977,939,932,971,987,973,0,931],
[984,972,977,1008,1009,1013,963,1032,1009,1009,1069,0]])



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
result = np.append(np.array([12, 2000, 163, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1007,999,979,981,1024,987,1002,1037,998,986,986],
[993,0,1058,990,1009,993,1018,956,996,1013,988,1014],
[1001,942,0,982,968,938,965,952,1023,979,972,950],
[1021,1010,1018,0,995,979,968,965,1029,984,989,1000],
[1019,991,1032,1005,0,982,980,984,1055,986,965,977],
[976,1007,1062,1021,1018,0,983,1003,1036,1014,996,997],
[1013,982,1035,1032,1020,1017,0,984,1028,1025,988,1013],
[998,1044,1048,1035,1016,997,1016,0,1014,1034,1036,1007],
[963,1004,977,971,945,964,972,986,0,1014,993,953],
[1002,987,1021,1016,1014,986,975,966,986,0,1009,1000],
[1014,1012,1028,1011,1035,1004,1012,964,1007,991,0,998],
[1014,986,1050,1000,1023,1003,987,993,1047,1000,1002,0]])



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
result = np.append(np.array([12, 2000, 164, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1031,1014,1026,1026,965,973,989,1002,1018,1025,991],
[969,0,1034,1006,999,997,984,1001,991,1030,1031,1000],
[986,966,0,992,1007,978,975,995,975,1015,1015,962],
[974,994,1008,0,994,959,973,990,998,985,996,973],
[974,1001,993,1006,0,959,932,975,1006,1005,1016,973],
[1035,1003,1022,1041,1041,0,1011,1006,1012,1022,1033,991],
[1027,1016,1025,1027,1068,989,0,1031,1014,1009,1009,989],
[1011,999,1005,1010,1025,994,969,0,1003,1017,1018,994],
[998,1009,1025,1002,994,988,986,997,0,991,1001,983],
[982,970,985,1015,995,978,991,983,1009,0,997,988],
[975,969,985,1004,984,967,991,982,999,1003,0,977],
[1009,1000,1038,1027,1027,1009,1011,1006,1017,1012,1023,0]])



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
result = np.append(np.array([12, 2000, 165, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,988,996,972,991,1016,981,1004,1016,981,1041,988],
[1012,0,999,1037,1028,1028,989,1017,1022,1009,1030,1005],
[1004,1001,0,989,1018,1016,1014,966,987,968,1016,986],
[1028,963,1011,0,1000,992,993,991,1008,1025,1017,1018],
[1009,972,982,1000,0,988,958,975,1022,965,999,991],
[984,972,984,1008,1012,0,990,982,1007,1011,1032,1018],
[1019,1011,986,1007,1042,1010,0,1012,1020,987,1062,1004],
[996,983,1034,1009,1025,1018,988,0,1012,1017,1011,989],
[984,978,1013,992,978,993,980,988,0,1006,1005,973],
[1019,991,1032,975,1035,989,1013,983,994,0,1007,1012],
[959,970,984,983,1001,968,938,989,995,993,0,978],
[1012,995,1014,982,1009,982,996,1011,1027,988,1022,0]])



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
result = np.append(np.array([12, 2000, 166, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,884,1063,973,996,1068,1024,908,973,987,914,914],
[1116,0,1137,1100,992,1197,963,980,1025,1072,990,1072],
[937,863,0,924,909,1092,931,931,821,860,951,840],
[1027,900,1076,0,967,1127,908,906,868,979,915,925],
[1004,1008,1091,1033,0,1242,1065,1032,989,1020,996,1028],
[932,803,908,873,758,0,799,877,823,927,878,849],
[976,1037,1069,1092,935,1201,0,1048,997,972,899,958],
[1092,1020,1069,1094,968,1123,952,0,1041,942,971,873],
[1027,975,1179,1132,1011,1177,1003,959,0,970,934,919],
[1013,928,1140,1021,980,1073,1028,1058,1030,0,957,933],
[1086,1010,1049,1085,1004,1122,1101,1029,1066,1043,0,946],
[1086,928,1160,1075,972,1151,1042,1127,1081,1067,1054,0]])



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
result = np.append(np.array([12, 2000, 167, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,884,984,993,1039,958,916,1005,1022,860,935,1028],
[1116,0,1060,988,1128,1015,1002,1110,1064,1033,1032,1085],
[1016,940,0,1038,1085,958,937,1051,962,1022,993,1046],
[1007,1012,962,0,1056,882,912,1010,955,969,969,1005],
[961,872,915,944,0,891,941,997,930,879,927,1029],
[1042,985,1042,1118,1109,0,1005,1065,995,919,1058,1082],
[1084,998,1063,1088,1059,995,0,1003,1086,1018,1034,1132],
[995,890,949,990,1003,935,997,0,986,944,935,1001],
[978,936,1038,1045,1070,1005,914,1014,0,1014,989,1103],
[1140,967,978,1031,1121,1081,982,1056,986,0,968,1068],
[1065,968,1007,1031,1073,942,966,1065,1011,1032,0,1078],
[972,915,954,995,971,918,868,999,897,932,922,0]])



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
result = np.append(np.array([12, 2000, 168, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1019,1064,1074,1022,1046,1045,1002,995,1029,1095,1028],
[981,0,1050,1056,993,1023,1052,1000,1022,1013,1004,986],
[936,950,0,989,955,989,1024,946,954,973,981,933],
[926,944,1011,0,975,980,973,941,939,958,979,933],
[978,1007,1045,1025,0,1021,989,992,998,1017,1009,952],
[954,977,1011,1020,979,0,1021,951,1027,989,1006,955],
[955,948,976,1027,1011,979,0,932,977,989,957,922],
[998,1000,1054,1059,1008,1049,1068,0,1013,1019,1060,1010],
[1005,978,1046,1061,1002,973,1023,987,0,1028,1017,1001],
[971,987,1027,1042,983,1011,1011,981,972,0,1008,961],
[905,996,1019,1021,991,994,1043,940,983,992,0,948],
[972,1014,1067,1067,1048,1045,1078,990,999,1039,1052,0]])



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
result = np.append(np.array([12, 2000, 169, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1042,1030,1032,1032,1055,1022,1007,942,979,1027,1046],
[958,0,997,1024,1040,1029,1033,1004,1000,1002,980,968],
[970,1003,0,981,974,1055,1003,1018,962,993,994,1045],
[968,976,1019,0,1018,1040,986,972,948,1007,1053,984],
[968,960,1026,982,0,1003,973,993,915,937,953,997],
[945,971,945,960,997,0,982,979,947,1023,995,956],
[978,967,997,1014,1027,1018,0,974,967,995,1000,969],
[993,996,982,1028,1007,1021,1026,0,997,973,999,1032],
[1058,1000,1038,1052,1085,1053,1033,1003,0,1024,999,1050],
[1021,998,1007,993,1063,977,1005,1027,976,0,1017,988],
[973,1020,1006,947,1047,1005,1000,1001,1001,983,0,995],
[954,1032,955,1016,1003,1044,1031,968,950,1012,1005,0]])



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
result = np.append(np.array([12, 2000, 170, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,982,969,970,1018,1018,935,1016,1018,1064,956,1036],
[1018,0,1031,1009,1010,1010,975,1077,998,1041,996,1033],
[1031,969,0,990,1033,1041,971,1027,1009,1053,995,1071],
[1030,991,1010,0,1053,1050,1006,1068,1032,1075,1061,1026],
[982,990,967,947,0,1024,929,985,968,1063,969,1047],
[982,990,959,950,976,0,963,957,928,1039,955,1021],
[1065,1025,1029,994,1071,1037,0,1068,1003,1107,1015,1032],
[984,923,973,932,1015,1043,932,0,989,1027,937,1016],
[982,1002,991,968,1032,1072,997,1011,0,1071,993,1043],
[936,959,947,925,937,961,893,973,929,0,944,974],
[1044,1004,1005,939,1031,1045,985,1063,1007,1056,0,1073],
[964,967,929,974,953,979,968,984,957,1026,927,0]])



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
result = np.append(np.array([12, 2000, 171, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,977,1004,1034,943,975,1007,975,1008,971,1006,983],
[1023,0,971,1014,999,949,985,962,936,983,1017,929],
[996,1029,0,1021,1008,965,962,964,926,984,997,977],
[966,986,979,0,992,940,948,1016,1004,968,1028,968],
[1057,1001,992,1008,0,964,986,963,1026,939,1036,975],
[1025,1051,1035,1060,1036,0,1003,972,1025,1015,1068,980],
[993,1015,1038,1052,1014,997,0,961,1014,997,1015,989],
[1025,1038,1036,984,1037,1028,1039,0,1024,990,1064,984],
[992,1064,1074,996,974,975,986,976,0,965,1017,1029],
[1029,1017,1016,1032,1061,985,1003,1010,1035,0,1033,997],
[994,983,1003,972,964,932,985,936,983,967,0,955],
[1017,1071,1023,1032,1025,1020,1011,1016,971,1003,1045,0]])



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
result = np.append(np.array([12, 2000, 172, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1034,1016,993,1014,1025,1008,1045,953,978,1008,976],
[966,0,918,1019,987,979,931,957,948,942,987,972],
[984,1082,0,1064,1012,1027,1041,1031,988,1017,1011,987],
[1007,981,936,0,967,960,978,949,957,965,945,936],
[986,1013,988,1033,0,1019,984,979,955,986,986,973],
[975,1021,973,1040,981,0,986,995,976,947,1019,985],
[992,1069,959,1022,1016,1014,0,981,1007,981,1030,1015],
[955,1043,969,1051,1021,1005,1019,0,1002,973,965,976],
[1047,1052,1012,1043,1045,1024,993,998,0,991,1012,1007],
[1022,1058,983,1035,1014,1053,1019,1027,1009,0,1027,977],
[992,1013,989,1055,1014,981,970,1035,988,973,0,1007],
[1024,1028,1013,1064,1027,1015,985,1024,993,1023,993,0]])



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
result = np.append(np.array([12, 2000, 173, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1003,1020,998,961,989,968,993,982,976,992,998],
[997,0,962,1019,932,962,940,993,971,998,1008,1013],
[980,1038,0,987,1024,1046,1016,965,1006,1019,1046,1019],
[1002,981,1013,0,977,978,997,977,994,955,1015,985],
[1039,1068,976,1023,0,1010,1023,999,992,1030,1045,1026],
[1011,1038,954,1022,990,0,987,1001,1011,965,1003,1058],
[1032,1060,984,1003,977,1013,0,963,1003,972,1024,1002],
[1007,1007,1035,1023,1001,999,1037,0,1001,1000,1042,1019],
[1018,1029,994,1006,1008,989,997,999,0,975,1001,1002],
[1024,1002,981,1045,970,1035,1028,1000,1025,0,995,1006],
[1008,992,954,985,955,997,976,958,999,1005,0,1023],
[1002,987,981,1015,974,942,998,981,998,994,977,0]])



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
result = np.append(np.array([12, 2000, 174, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,980,1011,990,992,1003,990,980,982,992,999,1047],
[1020,0,1027,1013,1021,1004,973,1011,994,1040,1031,1045],
[989,973,0,1010,995,1017,989,994,972,1015,990,1017],
[1010,987,990,0,986,1026,1005,1047,1013,991,1038,1049],
[1008,979,1005,1014,0,1044,985,1035,990,1030,1056,1044],
[997,996,983,974,956,0,964,1024,990,997,1047,1055],
[1010,1027,1011,995,1015,1036,0,1057,1042,1041,1036,1038],
[1020,989,1006,953,965,976,943,0,982,999,1016,1016],
[1018,1006,1028,987,1010,1010,958,1018,0,979,1026,1047],
[1008,960,985,1009,970,1003,959,1001,1021,0,1014,1046],
[1001,969,1010,962,944,953,964,984,974,986,0,1021],
[953,955,983,951,956,945,962,984,953,954,979,0]])



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
result = np.append(np.array([12, 2000, 175, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1009,953,968,926,988,952,1033,1016,1009,953,1054],
[991,0,943,976,961,988,927,1007,987,1019,934,963],
[1047,1057,0,990,1017,1050,944,1020,997,1023,974,1024],
[1032,1024,1010,0,1005,1051,974,1063,1022,1017,1015,1029],
[1074,1039,983,995,0,1006,1008,1080,1067,1028,985,991],
[1012,1012,950,949,994,0,965,1038,991,992,967,915],
[1048,1073,1056,1026,992,1035,0,1101,1076,1060,1026,1028],
[967,993,980,937,920,962,899,0,996,968,946,946],
[984,1013,1003,978,933,1009,924,1004,0,962,969,978],
[991,981,977,983,972,1008,940,1032,1038,0,946,998],
[1047,1066,1026,985,1015,1033,974,1054,1031,1054,0,1016],
[946,1037,976,971,1009,1085,972,1054,1022,1002,984,0]])



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
result = np.append(np.array([12, 2000, 176, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1020,1022,1027,977,983,1013,1031,998,1045,1019,993],
[980,0,995,989,980,974,986,988,977,1008,979,1020],
[978,1005,0,1014,986,965,991,1008,974,1028,1010,1013],
[973,1011,986,0,973,964,1013,994,995,990,982,980],
[1023,1020,1014,1027,0,985,1007,1043,1025,1052,1003,1013],
[1017,1026,1035,1036,1015,0,1004,1037,999,1026,1017,1034],
[987,1014,1009,987,993,996,0,1030,1011,1034,1010,1033],
[969,1012,992,1006,957,963,970,0,995,986,981,979],
[1002,1023,1026,1005,975,1001,989,1005,0,1023,1000,1011],
[955,992,972,1010,948,974,966,1014,977,0,962,995],
[981,1021,990,1018,997,983,990,1019,1000,1038,0,995],
[1007,980,987,1020,987,966,967,1021,989,1005,1005,0]])



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
result = np.append(np.array([12, 2000, 177, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,982,999,953,998,990,965,1011,1015,973,986,981],
[1018,0,996,1012,1037,1006,953,1022,1005,1009,996,1012],
[1001,1004,0,976,983,1013,976,1059,1046,1002,1001,1003],
[1047,988,1024,0,1007,993,978,1048,1045,1023,1019,975],
[1002,963,1017,993,0,998,1017,1019,1024,1020,974,960],
[1010,994,987,1007,1002,0,991,1040,1023,1009,989,980],
[1035,1047,1024,1022,983,1009,0,1053,1030,987,1012,1023],
[989,978,941,952,981,960,947,0,970,956,974,951],
[985,995,954,955,976,977,970,1030,0,994,979,974],
[1027,991,998,977,980,991,1013,1044,1006,0,994,962],
[1014,1004,999,981,1026,1011,988,1026,1021,1006,0,976],
[1019,988,997,1025,1040,1020,977,1049,1026,1038,1024,0]])



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
result = np.append(np.array([12, 2000, 178, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,993,997,991,1014,1039,991,980,985,1024,977,994],
[1007,0,990,984,972,1058,958,974,974,1016,1022,1011],
[1003,1010,0,1027,1009,1046,1000,1018,983,1023,1020,1041],
[1009,1016,973,0,984,1005,959,1003,962,1012,1003,997],
[986,1028,991,1016,0,1008,956,997,968,1008,1021,1010],
[961,942,954,995,992,0,969,980,948,998,996,964],
[1009,1042,1000,1041,1044,1031,0,1059,1023,1040,1005,1021],
[1020,1026,982,997,1003,1020,941,0,959,990,1005,997],
[1015,1026,1017,1038,1032,1052,977,1041,0,1054,1015,1057],
[976,984,977,988,992,1002,960,1010,946,0,974,1003],
[1023,978,980,997,979,1004,995,995,985,1026,0,1003],
[1006,989,959,1003,990,1036,979,1003,943,997,997,0]])



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
result = np.append(np.array([12, 2000, 179, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1017,995,1041,1031,1022,1033,1003,1020,1007,1022,1011],
[983,0,997,1013,1023,1027,1000,1007,1006,959,993,980],
[1005,1003,0,1036,1045,1017,1040,1008,997,976,1031,1025],
[959,987,964,0,1025,1000,1043,965,986,945,1003,971],
[969,977,955,975,0,979,1018,974,965,950,989,971],
[978,973,983,1000,1021,0,1016,989,995,969,1007,1002],
[967,1000,960,957,982,984,0,955,972,948,985,974],
[997,993,992,1035,1026,1011,1045,0,993,988,1010,1002],
[980,994,1003,1014,1035,1005,1028,1007,0,998,1030,1010],
[993,1041,1024,1055,1050,1031,1052,1012,1002,0,1044,1046],
[978,1007,969,997,1011,993,1015,990,970,956,0,987],
[989,1020,975,1029,1029,998,1026,998,990,954,1013,0]])



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
result = np.append(np.array([12, 2000, 180, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1005,986,1016,1024,1003,1018,1030,997,985,999,1010],
[995,0,1005,1013,998,1026,1019,1053,1028,982,1021,1017],
[1014,995,0,1030,1018,1032,1004,1022,1011,1001,1037,1014],
[984,987,970,0,996,993,1016,998,984,992,1014,986],
[976,1002,982,1004,0,996,1008,1033,1007,998,993,986],
[997,974,968,1007,1004,0,988,1028,986,979,1000,992],
[982,981,996,984,992,1012,0,1006,1007,1001,1013,984],
[970,947,978,1002,967,972,994,0,967,973,998,1006],
[1003,972,989,1016,993,1014,993,1033,0,990,1017,986],
[1015,1018,999,1008,1002,1021,999,1027,1010,0,1025,1023],
[1001,979,963,986,1007,1000,987,1002,983,975,0,997],
[990,983,986,1014,1014,1008,1016,994,1014,977,1003,0]])



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
result = np.append(np.array([12, 2000, 181, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1049,1018,1015,1047,991,1057,1021,1005,1017,1035,1006],
[951,0,1014,1003,984,960,1001,1012,1002,955,1016,958],
[982,986,0,1025,1017,977,1009,1010,1006,979,1024,988],
[985,997,975,0,981,977,979,1002,990,948,1003,975],
[953,1016,983,1019,0,977,988,1001,963,978,1005,960],
[1009,1040,1023,1023,1023,0,1026,1028,993,991,1009,1021],
[943,999,991,1021,1012,974,0,995,987,958,991,969],
[979,988,990,998,999,972,1005,0,940,940,989,982],
[995,998,994,1010,1037,1007,1013,1060,0,964,1007,982],
[983,1045,1021,1052,1022,1009,1042,1060,1036,0,1025,1015],
[965,984,976,997,995,991,1009,1011,993,975,0,960],
[994,1042,1012,1025,1040,979,1031,1018,1018,985,1040,0]])



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
result = np.append(np.array([12, 2000, 182, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,974,1003,960,994,992,962,984,961,992,946,952],
[1026,0,1018,1008,1035,1010,1021,1031,1021,1050,998,1018],
[997,982,0,970,1056,1000,1038,990,971,1021,1024,978],
[1040,992,1030,0,1084,1006,1039,1026,998,1008,1016,1027],
[1006,965,944,916,0,955,950,993,967,954,947,916],
[1008,990,1000,994,1045,0,990,1018,997,1007,985,988],
[1038,979,962,961,1050,1010,0,1030,981,990,1005,992],
[1016,969,1010,974,1007,982,970,0,997,974,973,977],
[1039,979,1029,1002,1033,1003,1019,1003,0,1047,984,1022],
[1008,950,979,992,1046,993,1010,1026,953,0,982,995],
[1054,1002,976,984,1053,1015,995,1027,1016,1018,0,1005],
[1048,982,1022,973,1084,1012,1008,1023,978,1005,995,0]])



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
result = np.append(np.array([12, 2000, 183, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1010,1071,978,1049,1052,998,1063,1111,1060,1008,1018],
[990,0,988,1005,1046,1028,976,998,1040,951,928,952],
[929,1012,0,926,1029,919,987,987,980,968,990,961],
[1022,995,1074,0,1084,985,1000,1042,1028,1050,1007,1021],
[951,954,971,916,0,912,950,986,1024,1013,979,990],
[948,972,1081,1015,1088,0,994,1037,1040,1040,972,1049],
[1002,1024,1013,1000,1050,1006,0,1015,1078,1022,1027,1039],
[937,1002,1013,958,1014,963,985,0,1014,980,1003,956],
[889,960,1020,972,976,960,922,986,0,982,1041,981],
[940,1049,1032,950,987,960,978,1020,1018,0,1035,980],
[992,1072,1010,993,1021,1028,973,997,959,965,0,1029],
[982,1048,1039,979,1010,951,961,1044,1019,1020,971,0]])



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
result = np.append(np.array([12, 2000, 184, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1002,1008,989,1015,1010,993,1019,1025,995,984,1013],
[998,0,1018,1009,1029,1016,1012,1003,1046,1000,1014,997],
[992,982,0,969,983,990,1011,1014,1005,980,989,961],
[1011,991,1031,0,1009,1022,1003,1030,1058,980,1031,1007],
[985,971,1017,991,0,990,994,1009,1031,995,959,970],
[990,984,1010,978,1010,0,1014,981,1034,982,991,987],
[1007,988,989,997,1006,986,0,1011,1011,975,1001,974],
[981,997,986,970,991,1019,989,0,1023,972,958,988],
[975,954,995,942,969,966,989,977,0,948,953,971],
[1005,1000,1020,1020,1005,1018,1025,1028,1052,0,998,1002],
[1016,986,1011,969,1041,1009,999,1042,1047,1002,0,997],
[987,1003,1039,993,1030,1013,1026,1012,1029,998,1003,0]])



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
result = np.append(np.array([12, 2000, 185, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,941,971,953,994,958,923,957,985,1016,980,983],
[1059,0,1052,1003,1059,1074,1020,1000,1089,1087,1060,1093],
[1029,948,0,955,1002,1038,977,974,1022,1028,1025,1037],
[1047,997,1045,0,1031,1023,1068,1008,1068,1073,1032,1080],
[1006,941,998,969,0,1010,958,962,1046,1021,997,973],
[1042,926,962,977,990,0,990,978,1025,1038,991,1005],
[1077,980,1023,932,1042,1010,0,1011,1048,1021,1023,1021],
[1043,1000,1026,992,1038,1022,989,0,1064,1059,989,1026],
[1015,911,978,932,954,975,952,936,0,1028,987,1001],
[984,913,972,927,979,962,979,941,972,0,955,1021],
[1020,940,975,968,1003,1009,977,1011,1013,1045,0,990],
[1017,907,963,920,1027,995,979,974,999,979,1010,0]])



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
result = np.append(np.array([12, 2000, 186, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,989,970,979,1017,985,996,986,979,1022,1009,1002],
[1011,0,1004,963,1006,991,1000,1032,1004,1030,1019,1009],
[1030,996,0,1000,1039,964,1012,993,1010,1023,1062,1014],
[1021,1037,1000,0,1065,1020,1050,1023,1034,1059,1039,1039],
[983,994,961,935,0,942,976,999,966,1009,1012,999],
[1015,1009,1036,980,1058,0,998,981,1016,1004,1035,998],
[1004,1000,988,950,1024,1002,0,996,975,1004,998,965],
[1014,968,1007,977,1001,1019,1004,0,978,1005,997,989],
[1021,996,990,966,1034,984,1025,1022,0,994,1013,1021],
[978,970,977,941,991,996,996,995,1006,0,975,985],
[991,981,938,961,988,965,1002,1003,987,1025,0,990],
[998,991,986,961,1001,1002,1035,1011,979,1015,1010,0]])



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
result = np.append(np.array([12, 2000, 187, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1019,996,1032,1002,968,959,1006,1007,972,1023,985],
[981,0,998,994,964,986,987,989,994,973,1014,989],
[1004,1002,0,995,969,984,984,1041,1019,973,1018,1010],
[968,1006,1005,0,969,974,949,997,968,963,1001,984],
[998,1036,1031,1031,0,987,1000,1013,1052,1004,1042,1009],
[1032,1014,1016,1026,1013,0,1012,1040,1020,1014,1038,986],
[1041,1013,1016,1051,1000,988,0,1023,1026,1005,1023,1021],
[994,1011,959,1003,987,960,977,0,968,970,1010,979],
[993,1006,981,1032,948,980,974,1032,0,962,986,981],
[1028,1027,1027,1037,996,986,995,1030,1038,0,1047,1018],
[977,986,982,999,958,962,977,990,1014,953,0,948],
[1015,1011,990,1016,991,1014,979,1021,1019,982,1052,0]])



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
result = np.append(np.array([12, 2000, 188, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1002,986,1019,989,1031,1008,1010,1027,1008,1008,1049],
[998,0,977,998,964,982,986,1044,998,981,993,1016],
[1014,1023,0,986,991,1002,1046,986,1096,995,1006,1021],
[981,1002,1014,0,983,961,992,1005,971,972,958,1009],
[1011,1036,1009,1017,0,1009,1052,1048,1018,1037,978,1040],
[969,1018,998,1039,991,0,984,1023,1029,1000,1010,1054],
[992,1014,954,1008,948,1016,0,1035,1031,995,975,1010],
[990,956,1014,995,952,977,965,0,943,982,969,966],
[973,1002,904,1029,982,971,969,1057,0,989,976,1012],
[992,1019,1005,1028,963,1000,1005,1018,1011,0,991,1032],
[992,1007,994,1042,1022,990,1025,1031,1024,1009,0,1049],
[951,984,979,991,960,946,990,1034,988,968,951,0]])



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
result = np.append(np.array([12, 2000, 189, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1007,992,1055,1024,1050,1073,1086,1040,1025,1009,1002],
[993,0,1032,1074,1023,1012,1034,1054,1028,1042,999,1019],
[1008,968,0,977,1012,1004,1012,1018,1003,932,1013,966],
[945,926,1023,0,983,988,1003,991,1010,949,987,986],
[976,977,988,1017,0,1011,1042,1006,1033,997,988,1002],
[950,988,996,1012,989,0,1020,963,1033,978,1011,968],
[927,966,988,997,958,980,0,968,967,977,996,972],
[914,946,982,1009,994,1037,1032,0,999,998,1016,963],
[960,972,997,990,967,967,1033,1001,0,992,973,941],
[975,958,1068,1051,1003,1022,1023,1002,1008,0,1066,982],
[991,1001,987,1013,1012,989,1004,984,1027,934,0,951],
[998,981,1034,1014,998,1032,1028,1037,1059,1018,1049,0]])



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
result = np.append(np.array([12, 2000, 190, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1043,1058,1067,1009,982,977,1008,1013,1012,1000,1023],
[957,0,1015,991,996,966,941,1011,1030,986,998,999],
[942,985,0,997,1010,1001,960,969,1018,965,993,1008],
[933,1009,1003,0,1004,951,990,998,1020,1000,1017,1020],
[991,1004,990,996,0,949,954,988,1041,955,985,1000],
[1018,1034,999,1049,1051,0,1005,997,1037,1024,1025,1042],
[1023,1059,1040,1010,1046,995,0,1044,1063,1016,999,1017],
[992,989,1031,1002,1012,1003,956,0,1017,973,983,990],
[987,970,982,980,959,963,937,983,0,977,1015,989],
[988,1014,1035,1000,1045,976,984,1027,1023,0,996,1017],
[1000,1002,1007,983,1015,975,1001,1017,985,1004,0,1003],
[977,1001,992,980,1000,958,983,1010,1011,983,997,0]])



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
result = np.append(np.array([12, 2000, 191, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1045,1031,1001,1035,997,1003,1017,1031,973,1011,1022],
[955,0,975,962,992,970,970,992,980,948,968,972],
[969,1025,0,996,985,957,994,985,996,965,989,976],
[999,1038,1004,0,1003,981,1005,989,1000,978,996,992],
[965,1008,1015,997,0,970,979,1003,995,961,983,964],
[1003,1030,1043,1019,1030,0,991,992,988,1001,994,1012],
[997,1030,1006,995,1021,1009,0,1003,1006,994,982,1010],
[983,1008,1015,1011,997,1008,997,0,1001,983,1014,1025],
[969,1020,1004,1000,1005,1012,994,999,0,977,985,981],
[1027,1052,1035,1022,1039,999,1006,1017,1023,0,1016,1014],
[989,1032,1011,1004,1017,1006,1018,986,1015,984,0,990],
[978,1028,1024,1008,1036,988,990,975,1019,986,1010,0]])



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
result = np.append(np.array([12, 2000, 192, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1035,1051,1055,979,1064,1000,1066,1028,996,1077,1091],
[965,0,1018,1022,1029,992,996,1014,980,1088,1029,1007],
[949,982,0,1032,934,985,959,1001,992,964,1028,1041],
[945,978,968,0,933,982,948,1051,963,1006,908,963],
[1021,971,1066,1067,0,1111,1011,1083,1035,1047,1043,1084],
[936,1008,1015,1018,889,0,922,1004,1039,978,919,1006],
[1000,1004,1041,1052,989,1078,0,1006,1071,1026,962,1015],
[934,986,999,949,917,996,994,0,977,991,921,991],
[972,1020,1008,1037,965,961,929,1023,0,1030,974,1026],
[1004,912,1036,994,953,1022,974,1009,970,0,982,937],
[923,971,972,1092,957,1081,1038,1079,1026,1018,0,1025],
[909,993,959,1037,916,994,985,1009,974,1063,975,0]])



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
result = np.append(np.array([12, 2000, 193, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1026,1056,1026,1000,1035,1042,1073,1030,1045,1020,1048],
[974,0,988,1000,951,1009,972,997,981,1005,970,978],
[944,1012,0,992,998,1001,947,1028,960,960,962,1022],
[974,1000,1008,0,948,990,966,987,988,986,974,993],
[1000,1049,1002,1052,0,995,1017,1008,1014,1076,995,1052],
[965,991,999,1010,1005,0,1007,1040,990,985,993,1011],
[958,1028,1053,1034,983,993,0,1017,993,1033,1008,1045],
[927,1003,972,1013,992,960,983,0,1010,1001,991,986],
[970,1019,1040,1012,986,1010,1007,990,0,1001,963,980],
[955,995,1040,1014,924,1015,967,999,999,0,982,1007],
[980,1030,1038,1026,1005,1007,992,1009,1037,1018,0,1020],
[952,1022,978,1007,948,989,955,1014,1020,993,980,0]])



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
result = np.append(np.array([12, 2000, 194, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1010,1020,1007,968,956,970,1042,943,1016,1059,959],
[990,0,1012,1044,1017,1034,1011,1038,1026,1039,1020,1005],
[980,988,0,995,1036,999,1011,1021,1040,1064,1087,1006],
[993,956,1005,0,969,976,949,998,1032,1010,1059,953],
[1032,983,964,1031,0,980,982,1029,1003,1016,1038,971],
[1044,966,1001,1024,1020,0,1005,1054,1072,1045,1045,995],
[1030,989,989,1051,1018,995,0,1071,1000,1074,1072,983],
[958,962,979,1002,971,946,929,0,1003,998,972,920],
[1057,974,960,968,997,928,1000,997,0,1033,1019,1018],
[984,961,936,990,984,955,926,1002,967,0,955,946],
[941,980,913,941,962,955,928,1028,981,1045,0,963],
[1041,995,994,1047,1029,1005,1017,1080,982,1054,1037,0]])



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
result = np.append(np.array([12, 2000, 195, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,992,979,1004,1040,1011,983,1029,994,982,1001,1003],
[1008,0,903,1019,1015,1017,1032,1037,999,936,972,1001],
[1021,1097,0,1070,1051,992,1036,1058,1015,1043,1052,1041],
[996,981,930,0,977,980,1003,1019,966,947,971,985],
[960,985,949,1023,0,1011,1010,1036,989,973,979,1014],
[989,983,1008,1020,989,0,1042,1032,977,930,989,988],
[1017,968,964,997,990,958,0,976,949,969,1008,977],
[971,963,942,981,964,968,1024,0,967,939,954,985],
[1006,1001,985,1034,1011,1023,1051,1033,0,999,1012,1023],
[1018,1064,957,1053,1027,1070,1031,1061,1001,0,1012,1015],
[999,1028,948,1029,1021,1011,992,1046,988,988,0,981],
[997,999,959,1015,986,1012,1023,1015,977,985,1019,0]])



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
result = np.append(np.array([12, 2000, 196, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,985,988,1000,1040,1040,1003,998,982,1013,1051,1043],
[1015,0,972,1014,1011,1025,1015,996,945,990,1015,997],
[1012,1028,0,1018,1023,990,1049,1014,1004,989,1019,1031],
[1000,986,982,0,996,1022,1020,990,970,997,1046,1040],
[960,989,977,1004,0,992,1012,999,992,976,1052,1037],
[960,975,1010,978,1008,0,1009,964,967,976,1043,992],
[997,985,951,980,988,991,0,955,944,1016,1001,1001],
[1002,1004,986,1010,1001,1036,1045,0,992,1006,984,1032],
[1018,1055,996,1030,1008,1033,1056,1008,0,1000,1035,1046],
[987,1010,1011,1003,1024,1024,984,994,1000,0,995,1017],
[949,985,981,954,948,957,999,1016,965,1005,0,966],
[957,1003,969,960,963,1008,999,968,954,983,1034,0]])



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
result = np.append(np.array([12, 2000, 197, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1031,1025,1018,1006,1019,1038,971,1016,1024,978,1015],
[969,0,989,981,999,1003,977,949,989,958,952,973],
[975,1011,0,994,1010,1000,998,1007,1013,1004,981,975],
[982,1019,1006,0,1005,1019,1023,993,1008,999,963,994],
[994,1001,990,995,0,991,1005,979,1030,1010,979,950],
[981,997,1000,981,1009,0,1029,987,1008,967,967,989],
[962,1023,1002,977,995,971,0,951,999,981,973,957],
[1029,1051,993,1007,1021,1013,1049,0,1046,1039,1025,995],
[984,1011,987,992,970,992,1001,954,0,985,983,969],
[976,1042,996,1001,990,1033,1019,961,1015,0,993,953],
[1022,1048,1019,1037,1021,1033,1027,975,1017,1007,0,991],
[985,1027,1025,1006,1050,1011,1043,1005,1031,1047,1009,0]])



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
result = np.append(np.array([12, 2000, 198, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1018,984,985,978,1041,1014,959,971,988,1019,992],
[982,0,977,1002,1006,1015,1019,993,1026,986,1016,987],
[1016,1023,0,975,1035,1022,1010,983,999,1004,1033,1024],
[1015,998,1025,0,1026,1027,986,1005,1042,1026,1025,973],
[1022,994,965,974,0,991,965,974,978,970,987,969],
[959,985,978,973,1009,0,960,948,980,998,983,952],
[986,981,990,1014,1035,1040,0,993,1019,1056,992,971],
[1041,1007,1017,995,1026,1052,1007,0,1026,1070,1052,1014],
[1029,974,1001,958,1022,1020,981,974,0,1030,982,967],
[1012,1014,996,974,1030,1002,944,930,970,0,987,967],
[981,984,967,975,1013,1017,1008,948,1018,1013,0,959],
[1008,1013,976,1027,1031,1048,1029,986,1033,1033,1041,0]])



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
result = np.append(np.array([12, 2000, 199, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,996,892,903,944,850,915,979,971,869,882,932],
[1004,0,803,818,899,974,839,1009,899,918,869,936],
[1108,1197,0,975,978,1221,1137,1108,1071,1124,1079,1116],
[1097,1182,1025,0,1176,1081,1074,1201,1025,981,1065,1189],
[1056,1101,1022,824,0,985,1046,968,890,921,978,1018],
[1150,1026,779,919,1015,0,1021,1047,955,996,899,1104],
[1085,1161,863,926,954,979,0,1056,921,921,938,1018],
[1021,991,892,799,1032,953,944,0,1002,846,934,928],
[1029,1101,929,975,1110,1045,1079,998,0,967,982,1103],
[1131,1082,876,1019,1079,1004,1079,1154,1033,0,1062,1074],
[1118,1131,921,935,1022,1101,1062,1066,1018,938,0,1077],
[1068,1064,884,811,982,896,982,1072,897,926,923,0]])



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
result = np.append(np.array([12, 2000, 200, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/mebbd/mebbd_12_2000.csv", index=False, header=False)