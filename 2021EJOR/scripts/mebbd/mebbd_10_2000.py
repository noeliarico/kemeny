
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg
from kemeny import sc

rep = 3
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,1025,1050,1043,1005,955,1000,1017,1082,1004],
[975,0,1025,943,931,974,967,1047,1036,1012],
[950,975,0,922,1011,931,856,935,1029,987],
[957,1057,1078,0,965,1000,995,1027,1090,963],
[995,1069,989,1035,0,999,1047,1027,1095,1017],
[1045,1026,1069,1000,1001,0,974,1030,1020,984],
[1000,1033,1144,1005,953,1026,0,973,982,1044],
[983,953,1065,973,973,970,1027,0,1023,1039],
[918,964,971,910,905,980,1018,977,0,920],
[996,988,1013,1037,983,1016,956,961,1080,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 1, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,967,923,1000,996,942,946,946,958,971],
[1033,0,987,1025,996,1006,964,1018,1024,989],
[1077,1013,0,1085,1058,975,975,1053,1064,1033],
[1000,975,915,0,1051,1029,976,1015,979,1003],
[1004,1004,942,949,0,990,983,1024,992,998],
[1058,994,1025,971,1010,0,1003,1027,1037,1003],
[1054,1036,1025,1024,1017,997,0,1053,1102,1027],
[1054,982,947,985,976,973,947,0,1001,994],
[1042,976,936,1021,1008,963,898,999,0,981],
[1029,1011,967,997,1002,997,973,1006,1019,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 2, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,927,939,935,946,1018,963,925,963,980],
[1073,0,1003,1046,988,1015,1042,1009,1043,1026],
[1061,997,0,1015,1018,1031,1001,997,1032,982],
[1065,954,985,0,928,1027,1044,993,957,994],
[1054,1012,982,1072,0,1042,1055,1023,992,1035],
[982,985,969,973,958,0,991,925,1024,1016],
[1037,958,999,956,945,1009,0,986,960,999],
[1075,991,1003,1007,977,1075,1014,0,979,992],
[1037,957,968,1043,1008,976,1040,1021,0,1029],
[1020,974,1018,1006,965,984,1001,1008,971,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 3, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,851,1047,978,1015,909,1105,905,1011,1041],
[1149,0,1070,1134,882,1031,1121,1181,960,1048],
[953,930,0,1068,1047,966,1152,1042,968,923],
[1022,866,932,0,950,760,1070,982,992,1060],
[985,1118,953,1050,0,1101,1172,1058,1096,887],
[1091,969,1034,1240,899,0,1162,1069,1222,1079],
[895,879,848,930,828,838,0,893,928,923],
[1095,819,958,1018,942,931,1107,0,1110,953],
[989,1040,1032,1008,904,778,1072,890,0,948],
[959,952,1077,940,1113,921,1077,1047,1052,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 4, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1002,947,1012,983,1014,990,983,1007,996],
[998,0,1034,992,1005,1022,992,991,1023,1005],
[1053,966,0,1002,1038,1043,1002,1019,1073,1057],
[988,1008,998,0,1025,1045,1020,1009,1045,1043],
[1017,995,962,975,0,1026,990,1009,1017,1010],
[986,978,957,955,974,0,975,971,992,983],
[1010,1008,998,980,1010,1025,0,1005,1006,993],
[1017,1009,981,991,991,1029,995,0,1055,1026],
[993,977,927,955,983,1008,994,945,0,1021],
[1004,995,943,957,990,1017,1007,974,979,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 5, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,980,1025,1004,1002,984,1015,1006,972,1002],
[1020,0,990,1053,985,989,1009,1024,1008,1013],
[975,1010,0,988,983,976,988,988,1004,1007],
[996,947,1012,0,960,971,1007,972,982,1002],
[998,1015,1017,1040,0,1016,1015,1003,1016,1000],
[1016,1011,1024,1029,984,0,994,1022,1017,1019],
[985,991,1012,993,985,1006,0,1000,977,984],
[994,976,1012,1028,997,978,1000,0,989,1000],
[1028,992,996,1018,984,983,1023,1011,0,1011],
[998,987,993,998,1000,981,1016,1000,989,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 6, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,946,1053,1038,1030,1038,1045,1027,1045,983],
[1054,0,1028,1077,984,1104,1127,1022,1040,1038],
[947,972,0,1048,1004,1056,1003,988,1012,1007],
[962,923,952,0,923,989,961,953,949,953],
[970,1016,996,1077,0,1013,1013,1038,1026,975],
[962,896,944,1011,987,0,979,945,924,975],
[955,873,997,1039,987,1021,0,906,988,1023],
[973,978,1012,1047,962,1055,1094,0,990,961],
[955,960,988,1051,974,1076,1012,1010,0,982],
[1017,962,993,1047,1025,1025,977,1039,1018,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 7, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1005,1011,1017,971,1014,987,998,991,958],
[995,0,1010,1032,1000,999,1002,1025,1007,957],
[989,990,0,998,983,996,986,979,975,971],
[983,968,1002,0,991,979,967,976,933,938],
[1029,1000,1017,1009,0,1000,962,986,1024,1003],
[986,1001,1004,1021,1000,0,986,995,1006,967],
[1013,998,1014,1033,1038,1014,0,1013,1019,1003],
[1002,975,1021,1024,1014,1005,987,0,1030,973],
[1009,993,1025,1067,976,994,981,970,0,982],
[1042,1043,1029,1062,997,1033,997,1027,1018,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 8, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,994,973,990,1004,1010,979,965,950,1007],
[1006,0,975,956,969,966,998,953,967,976],
[1027,1025,0,1018,1007,995,991,1025,1005,1043],
[1010,1044,982,0,1011,975,1014,1006,984,1026],
[996,1031,993,989,0,996,972,986,1004,1030],
[990,1034,1005,1025,1004,0,1038,1015,977,1004],
[1021,1002,1009,986,1028,962,0,1013,974,1005],
[1035,1047,975,994,1014,985,987,0,995,1044],
[1050,1033,995,1016,996,1023,1026,1005,0,1039],
[993,1024,957,974,970,996,995,956,961,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 9, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,911,220,604,1425,1462,1701,1246,1063,1432],
[1089,0,1145,1197,1305,1043,1099,1342,999,1305],
[1780,855,0,1133,1645,1574,1701,1944,1545,1212],
[1396,803,867,0,1134,1350,1466,1410,1306,1626],
[575,695,355,866,0,669,1295,903,515,945],
[538,957,426,650,1331,0,944,739,370,646],
[299,901,299,534,705,1056,0,708,615,515],
[754,658,56,590,1097,1261,1292,0,1161,1094],
[937,1001,455,694,1485,1630,1385,839,0,1493],
[568,695,788,374,1055,1354,1485,906,507,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 10, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1040,993,1053,955,1020,966,999,1025,1017],
[960,0,1009,1045,1061,984,934,1009,1024,975],
[1007,991,0,985,973,1026,983,949,988,1003],
[947,955,1015,0,999,1008,1013,1031,1003,994],
[1045,939,1027,1001,0,1075,977,977,1046,973],
[980,1016,974,992,925,0,980,922,1029,938],
[1034,1066,1017,987,1023,1020,0,993,1036,1071],
[1001,991,1051,969,1023,1078,1007,0,1033,954],
[975,976,1012,997,954,971,964,967,0,987],
[983,1025,997,1006,1027,1062,929,1046,1013,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 11, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,979,988,947,999,940,975,987,1045,935],
[1021,0,984,1005,1047,1053,1026,1072,1015,1002],
[1012,1016,0,1012,1033,1027,1016,1039,1015,965],
[1053,995,988,0,1033,1021,1035,1097,1034,1020],
[1001,953,967,967,0,994,986,956,984,899],
[1060,947,973,979,1006,0,1012,1018,1036,943],
[1025,974,984,965,1014,988,0,1045,999,941],
[1013,928,961,903,1044,982,955,0,989,931],
[955,985,985,966,1016,964,1001,1011,0,922],
[1065,998,1035,980,1101,1057,1059,1069,1078,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 12, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1015,1077,850,998,1002,1001,1090,1068,990],
[985,0,1024,909,1029,960,996,981,1014,975],
[923,976,0,873,919,858,887,867,930,954],
[1150,1091,1127,0,1138,986,1039,1131,999,1021],
[1002,971,1081,862,0,876,939,933,994,1038],
[998,1040,1142,1014,1124,0,1157,1015,1068,1096],
[999,1004,1113,961,1061,843,0,978,1048,972],
[910,1019,1133,869,1067,985,1022,0,955,967],
[932,986,1070,1001,1006,932,952,1045,0,1004],
[1010,1025,1046,979,962,904,1028,1033,996,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 13, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,955,996,1030,1039,991,982,939,968,958],
[1045,0,1037,1041,1119,995,994,983,1017,1005],
[1004,963,0,1004,1034,979,932,986,990,950],
[970,959,996,0,1027,988,962,1006,991,968],
[961,881,966,973,0,926,905,989,954,899],
[1009,1005,1021,1012,1074,0,958,999,1043,924],
[1018,1006,1068,1038,1095,1042,0,1002,1022,990],
[1061,1017,1014,994,1011,1001,998,0,1019,969],
[1032,983,1010,1009,1046,957,978,981,0,966],
[1042,995,1050,1032,1101,1076,1010,1031,1034,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 14, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,921,992,941,950,949,984,923,1056,1011],
[1079,0,987,997,1064,1058,1043,1055,1086,1011],
[1008,1013,0,1023,981,995,1026,1004,1042,955],
[1059,1003,977,0,975,1040,1015,943,1123,1020],
[1050,936,1019,1025,0,976,976,975,1057,943],
[1051,942,1005,960,1024,0,965,1015,1081,1021],
[1016,957,974,985,1024,1035,0,1027,1043,967],
[1077,945,996,1057,1025,985,973,0,1086,1040],
[944,914,958,877,943,919,957,914,0,945],
[989,989,1045,980,1057,979,1033,960,1055,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 15, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,992,967,1030,765,897,828,1210,761,990],
[1008,0,783,1099,785,729,882,1029,658,904],
[1033,1217,0,1166,739,1097,970,1268,865,933],
[970,901,834,0,696,680,916,873,511,703],
[1235,1215,1261,1304,0,886,1069,1191,1039,1196],
[1103,1271,903,1320,1114,0,910,1022,799,914],
[1172,1118,1030,1084,931,1090,0,1329,1030,1168],
[790,971,732,1127,809,978,671,0,595,688],
[1239,1342,1135,1489,961,1201,970,1405,0,957],
[1010,1096,1067,1297,804,1086,832,1312,1043,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 16, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1001,1014,989,991,1011,998,1011,1057,1016],
[999,0,952,970,1014,999,968,999,1040,1018],
[986,1048,0,1021,1018,1028,1017,1000,1045,1041],
[1011,1030,979,0,995,995,991,998,1033,1001],
[1009,986,982,1005,0,1011,979,1034,1044,1012],
[989,1001,972,1005,989,0,986,1012,1033,1024],
[1002,1032,983,1009,1021,1014,0,998,1012,1034],
[989,1001,1000,1002,966,988,1002,0,1028,1018],
[943,960,955,967,956,967,988,972,0,950],
[984,982,959,999,988,976,966,982,1050,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 17, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,999,1030,1021,999,1039,997,1006,1040,1070],
[1001,0,1026,998,982,1021,975,974,1036,1030],
[970,974,0,987,994,1013,973,981,1032,1035],
[979,1002,1013,0,977,1011,959,994,995,1035],
[1001,1018,1006,1023,0,1044,1003,984,1075,1055],
[961,979,987,989,956,0,951,964,1006,975],
[1003,1025,1027,1041,997,1049,0,1028,1044,1048],
[994,1026,1019,1006,1016,1036,972,0,1042,1043],
[960,964,968,1005,925,994,956,958,0,981],
[930,970,965,965,945,1025,952,957,1019,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 18, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1029,1010,1003,995,1045,1003,1034,994,1003],
[971,0,987,972,975,1020,1017,969,967,981],
[990,1013,0,980,987,1031,1008,1015,1005,1009],
[997,1028,1020,0,998,1013,1016,1000,1029,1016],
[1005,1025,1013,1002,0,1071,1040,1036,1042,1000],
[955,980,969,987,929,0,996,992,1018,1006],
[997,983,992,984,960,1004,0,1011,987,968],
[966,1031,985,1000,964,1008,989,0,1020,992],
[1006,1033,995,971,958,982,1013,980,0,1001],
[997,1019,991,984,1000,994,1032,1008,999,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 19, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1043,1032,1025,991,1040,1019,1031,1029,1007],
[957,0,974,972,967,996,1033,973,961,987],
[968,1026,0,978,975,1039,999,981,982,1008],
[975,1028,1022,0,1015,1031,1043,1047,1010,1025],
[1009,1033,1025,985,0,1032,1027,1024,1012,985],
[960,1004,961,969,968,0,1015,999,1010,991],
[981,967,1001,957,973,985,0,988,992,980],
[969,1027,1019,953,976,1001,1012,0,978,1010],
[971,1039,1018,990,988,990,1008,1022,0,957],
[993,1013,992,975,1015,1009,1020,990,1043,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 20, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,962,1011,961,986,943,1007,890,1003,952],
[1038,0,1069,978,1055,1001,1017,978,1018,956],
[989,931,0,969,1038,969,1016,969,1002,963],
[1039,1022,1031,0,993,1036,1041,989,1030,990],
[1014,945,962,1007,0,923,970,951,950,959],
[1057,999,1031,964,1077,0,1049,984,1041,1028],
[993,983,984,959,1030,951,0,926,1002,935],
[1110,1022,1031,1011,1049,1016,1074,0,1011,993],
[997,982,998,970,1050,959,998,989,0,988],
[1048,1044,1037,1010,1041,972,1065,1007,1012,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 21, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,995,1050,1048,1058,999,1095,989,994,1052],
[1005,0,1040,1030,983,991,1084,1031,996,1055],
[950,960,0,1006,1021,961,1049,976,1031,1051],
[952,970,994,0,954,972,1053,959,954,986],
[942,1017,979,1046,0,996,1044,991,967,1036],
[1001,1009,1039,1028,1004,0,1030,984,939,1032],
[905,916,951,947,956,970,0,1003,899,1004],
[1011,969,1024,1041,1009,1016,997,0,977,1000],
[1006,1004,969,1046,1033,1061,1101,1023,0,1043],
[948,945,949,1014,964,968,996,1000,957,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 22, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1028,997,1204,1108,1121,1185,1100,1109,1181],
[972,0,1035,1117,1069,1074,1068,961,1005,1148],
[1003,965,0,1129,1085,1039,1124,1008,984,1108],
[796,883,871,0,1042,934,931,891,945,1012],
[892,931,915,958,0,948,1007,969,980,1070],
[879,926,961,1066,1052,0,950,883,987,1038],
[815,932,876,1069,993,1050,0,1005,1022,1057],
[900,1039,992,1109,1031,1117,995,0,1091,1022],
[891,995,1016,1055,1020,1013,978,909,0,1064],
[819,852,892,988,930,962,943,978,936,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 23, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1000,1009,986,995,1005,1015,991,990,1014],
[1000,0,997,974,1004,966,997,997,989,988],
[991,1003,0,1002,998,999,997,972,990,987],
[1014,1026,998,0,1035,1006,1029,1016,989,1003],
[1005,996,1002,965,0,994,1011,1007,992,1018],
[995,1034,1001,994,1006,0,1019,979,984,987],
[985,1003,1003,971,989,981,0,1004,1024,993],
[1009,1003,1028,984,993,1021,996,0,1002,1008],
[1010,1011,1010,1011,1008,1016,976,998,0,1001],
[986,1012,1013,997,982,1013,1007,992,999,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 24, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1039,1013,1009,993,1010,1012,1032,1063,1055],
[961,0,999,1022,974,971,996,1014,1007,1025],
[987,1001,0,989,999,958,963,1020,1023,1004],
[991,978,1011,0,989,957,969,1017,1030,1009],
[1007,1026,1001,1011,0,1029,999,1013,1059,1023],
[990,1029,1042,1043,971,0,983,1049,1044,1039],
[988,1004,1037,1031,1001,1017,0,1035,1001,1046],
[968,986,980,983,987,951,965,0,1028,995],
[937,993,977,970,941,956,999,972,0,990],
[945,975,996,991,977,961,954,1005,1010,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 25, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,947,974,1014,1014,956,988,935,946,1006],
[1053,0,1064,1024,1052,1087,983,1026,988,1072],
[1026,936,0,995,994,1006,975,952,923,1080],
[986,976,1005,0,984,1009,1000,1013,984,1043],
[986,948,1006,1016,0,1023,972,1018,1003,1027],
[1044,913,994,991,977,0,948,1003,958,1033],
[1012,1017,1025,1000,1028,1052,0,989,1046,1101],
[1065,974,1048,987,982,997,1011,0,1018,1057],
[1054,1012,1077,1016,997,1042,954,982,0,1043],
[994,928,920,957,973,967,899,943,957,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 26, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1042,1020,1091,1029,969,1083,922,982,995],
[958,0,990,1134,1122,940,1058,908,890,990],
[980,1010,0,1031,999,898,840,905,947,905],
[909,866,969,0,1079,969,1037,906,828,894],
[971,878,1001,921,0,862,983,892,924,899],
[1031,1060,1102,1031,1138,0,984,892,964,997],
[917,942,1160,963,1017,1016,0,942,928,923],
[1078,1092,1095,1094,1108,1108,1058,0,1017,964],
[1018,1110,1053,1172,1076,1036,1072,983,0,1000],
[1005,1010,1095,1106,1101,1003,1077,1036,1000,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 27, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1014,967,1009,968,1043,944,975,1004,1035],
[986,0,987,930,973,996,931,994,983,996],
[1033,1013,0,971,1028,922,982,988,1002,1036],
[991,1070,1029,0,1009,1035,1013,1065,1037,1017],
[1032,1027,972,991,0,982,915,983,988,1017],
[957,1004,1078,965,1018,0,926,998,1026,983],
[1056,1069,1018,987,1085,1074,0,1043,1059,1051],
[1025,1006,1012,935,1017,1002,957,0,1027,994],
[996,1017,998,963,1012,974,941,973,0,978],
[965,1004,964,983,983,1017,949,1006,1022,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 28, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,997,979,1028,1065,955,997,1029,1013,983],
[1003,0,1012,1012,1019,999,1019,1011,996,1011],
[1021,988,0,1026,1036,1016,1032,1034,1048,1004],
[972,988,974,0,1052,1028,984,1023,1022,968],
[935,981,964,948,0,932,941,963,985,957],
[1045,1001,984,972,1068,0,995,984,992,996],
[1003,981,968,1016,1059,1005,0,1029,1025,999],
[971,989,966,977,1037,1016,971,0,982,1002],
[987,1004,952,978,1015,1008,975,1018,0,1003],
[1017,989,996,1032,1043,1004,1001,998,997,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 29, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,991,999,1014,1006,992,996,967,1009,985],
[1009,0,1032,995,1021,969,1024,1021,1022,966],
[1001,968,0,984,1034,992,984,994,995,988],
[986,1005,1016,0,1004,1009,1023,988,1010,986],
[994,979,966,996,0,960,986,990,975,1000],
[1008,1031,1008,991,1040,0,1002,986,1017,1018],
[1004,976,1016,977,1014,998,0,998,1011,1003],
[1033,979,1006,1012,1010,1014,1002,0,1000,1000],
[991,978,1005,990,1025,983,989,1000,0,985],
[1015,1034,1012,1014,1000,982,997,1000,1015,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 30, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,955,885,953,922,947,885,999,932,898],
[1045,0,988,1041,1008,1008,904,965,988,1045],
[1115,1012,0,1093,1039,1082,1064,1019,994,1093],
[1047,959,907,0,978,1035,986,1017,945,956],
[1078,992,961,1022,0,1034,1019,993,1019,901],
[1053,992,918,965,966,0,969,938,956,975],
[1115,1096,936,1014,981,1031,0,1042,1016,1010],
[1001,1035,981,983,1007,1062,958,0,1046,1002],
[1068,1012,1006,1055,981,1044,984,954,0,993],
[1102,955,907,1044,1099,1025,990,998,1007,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 31, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1013,984,1008,972,947,968,986,979,956],
[987,0,975,1018,974,944,937,986,963,937],
[1016,1025,0,1024,972,972,993,1013,973,974],
[992,982,976,0,972,948,939,959,949,935],
[1028,1026,1028,1028,0,975,984,989,992,942],
[1053,1056,1028,1052,1025,0,1024,1022,1016,986],
[1032,1063,1007,1061,1016,976,0,1015,1047,1005],
[1014,1014,987,1041,1011,978,985,0,1023,991],
[1021,1037,1027,1051,1008,984,953,977,0,968],
[1044,1063,1026,1065,1058,1014,995,1009,1032,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 32, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1125,1062,1006,888,1059,1134,1121,1041,1050],
[875,0,979,874,920,1007,1036,994,1001,989],
[938,1021,0,881,936,933,1028,978,995,1012],
[994,1126,1119,0,1068,1008,1109,995,1138,1071],
[1112,1080,1064,932,0,1050,1032,1066,1012,1023],
[941,993,1067,992,950,0,1019,1024,986,1068],
[866,964,972,891,968,981,0,1029,931,968],
[879,1006,1022,1005,934,976,971,0,1052,1065],
[959,999,1005,862,988,1014,1069,948,0,992],
[950,1011,988,929,977,932,1032,935,1008,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 33, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1097,985,1002,1018,998,984,1031,1016,1057],
[903,0,921,907,975,925,942,946,928,944],
[1015,1079,0,991,1020,971,1011,1057,1002,1012],
[998,1093,1009,0,1018,956,1019,1001,986,985],
[982,1025,980,982,0,957,999,1011,976,1011],
[1002,1075,1029,1044,1043,0,995,1046,990,1017],
[1016,1058,989,981,1001,1005,0,1012,980,982],
[969,1054,943,999,989,954,988,0,965,995],
[984,1072,998,1014,1024,1010,1020,1035,0,1023],
[943,1056,988,1015,989,983,1018,1005,977,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 34, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1003,1011,1072,1017,1070,1004,1064,1066,980],
[997,0,936,999,967,996,960,955,999,895],
[989,1064,0,1017,938,1026,839,1002,960,940],
[928,1001,983,0,869,897,987,1014,1011,876],
[983,1033,1062,1131,0,965,1055,1077,1157,1050],
[930,1004,974,1103,1035,0,968,1003,993,1006],
[996,1040,1161,1013,945,1032,0,1074,1069,964],
[936,1045,998,986,923,997,926,0,952,908],
[934,1001,1040,989,843,1007,931,1048,0,864],
[1020,1105,1060,1124,950,994,1036,1092,1136,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 35, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,937,1070,961,982,1012,941,966,1025,1009],
[1063,0,1105,968,1055,1067,1003,995,1066,1005],
[930,895,0,890,988,952,936,937,939,926],
[1039,1032,1110,0,1045,1024,965,1005,1032,1025],
[1018,945,1012,955,0,1039,941,948,1017,1023],
[988,933,1048,976,961,0,984,942,989,991],
[1059,997,1064,1035,1059,1016,0,1015,1024,1021],
[1034,1005,1063,995,1052,1058,985,0,1041,1070],
[975,934,1061,968,983,1011,976,959,0,990],
[991,995,1074,975,977,1009,979,930,1010,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 36, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1010,1005,1014,970,1056,991,1020,957,1006],
[990,0,1017,1082,1022,1038,1014,1029,1008,999],
[995,983,0,1020,988,973,1010,983,968,965],
[986,918,980,0,959,967,1017,1006,935,975],
[1030,978,1012,1041,0,1035,1054,1047,1024,996],
[944,962,1027,1033,965,0,1021,998,957,953],
[1009,986,990,983,946,979,0,1002,984,990],
[980,971,1017,994,953,1002,998,0,973,993],
[1043,992,1032,1065,976,1043,1016,1027,0,980],
[994,1001,1035,1025,1004,1047,1010,1007,1020,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 37, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,957,1019,954,951,967,993,953,962,922],
[1043,0,1022,1002,1032,974,1021,1018,980,983],
[981,978,0,1014,1019,1004,1032,1031,1010,1042],
[1046,998,986,0,1039,991,1054,1013,1032,1002],
[1049,968,981,961,0,980,1011,994,994,962],
[1033,1026,996,1009,1020,0,1047,1049,1042,1010],
[1007,979,968,946,989,953,0,980,998,982],
[1047,982,969,987,1006,951,1020,0,1029,1024],
[1038,1020,990,968,1006,958,1002,971,0,969],
[1078,1017,958,998,1038,990,1018,976,1031,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 38, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,905,1102,1024,1063,1017,1029,1066,1015,1071],
[1095,0,1044,1006,1079,920,1061,1114,969,1023],
[898,956,0,993,1027,933,1015,1008,947,1020],
[976,994,1007,0,1060,939,1028,1024,965,974],
[937,921,973,940,0,1036,1027,975,978,917],
[983,1080,1067,1061,964,0,1082,1009,917,1008],
[971,939,985,972,973,918,0,1037,879,982],
[934,886,992,976,1025,991,963,0,1016,1023],
[985,1031,1053,1035,1022,1083,1121,984,0,1094],
[929,977,980,1026,1083,992,1018,977,906,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 39, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,991,928,950,964,986,1005,959,994,1026],
[1009,0,975,1010,975,990,987,991,1009,1053],
[1072,1025,0,1000,1015,1059,1057,1033,1047,1034],
[1050,990,1000,0,1000,993,993,1021,1013,1044],
[1036,1025,985,1000,0,996,1051,1013,991,1069],
[1014,1010,941,1007,1004,0,1023,1036,993,1066],
[995,1013,943,1007,949,977,0,1024,990,1082],
[1041,1009,967,979,987,964,976,0,961,1040],
[1006,991,953,987,1009,1007,1010,1039,0,1040],
[974,947,966,956,931,934,918,960,960,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 40, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,973,963,970,984,959,979,1012,980,982],
[1027,0,983,969,983,945,1010,1010,1019,950],
[1037,1017,0,979,1008,947,1026,1017,1001,980],
[1030,1031,1021,0,1005,988,981,1035,1028,993],
[1016,1017,992,995,0,1015,1025,1056,1032,988],
[1041,1055,1053,1012,985,0,1018,1039,1045,1014],
[1021,990,974,1019,975,982,0,1011,995,1006],
[988,990,983,965,944,961,989,0,1001,999],
[1020,981,999,972,968,955,1005,999,0,976],
[1018,1050,1020,1007,1012,986,994,1001,1024,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 41, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,961,951,1002,964,951,992,974,966,979],
[1039,0,988,1040,998,1000,1025,975,1010,1010],
[1049,1012,0,1034,969,1006,1046,1025,1019,1048],
[998,960,966,0,930,977,988,972,968,1002],
[1036,1002,1031,1070,0,995,1024,990,988,1035],
[1049,1000,994,1023,1005,0,1001,1014,1017,995],
[1008,975,954,1012,976,999,0,965,992,1011],
[1026,1025,975,1028,1010,986,1035,0,1015,1033],
[1034,990,981,1032,1012,983,1008,985,0,1050],
[1021,990,952,998,965,1005,989,967,950,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 42, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1076,1040,958,1030,966,976,973,992,1018],
[924,0,980,917,1004,948,992,967,948,975],
[960,1020,0,945,993,964,969,991,984,1014],
[1042,1083,1055,0,1048,1044,1040,990,984,1022],
[970,996,1007,952,0,955,978,980,969,956],
[1034,1052,1036,956,1045,0,1042,1003,974,1013],
[1024,1008,1031,960,1022,958,0,982,982,1018],
[1027,1033,1009,1010,1020,997,1018,0,965,988],
[1008,1052,1016,1016,1031,1026,1018,1035,0,990],
[982,1025,986,978,1044,987,982,1012,1010,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 43, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,918,1205,948,1114,1025,945,1116,1016,901],
[1082,0,1139,1071,1076,976,1009,1185,1090,924],
[795,861,0,981,1165,881,948,976,1044,990],
[1052,929,1019,0,1007,949,949,996,876,879],
[886,924,835,993,0,814,856,927,945,755],
[975,1024,1119,1051,1186,0,1000,1232,1000,1050],
[1055,991,1052,1051,1144,1000,0,1061,959,836],
[884,815,1024,1004,1073,768,939,0,984,982],
[984,910,956,1124,1055,1000,1041,1016,0,825],
[1099,1076,1010,1121,1245,950,1164,1018,1175,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 44, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1002,1042,1043,997,1044,1018,1009,1002,1007],
[998,0,1036,1027,1016,1007,1036,1020,970,972],
[958,964,0,1024,965,1008,993,970,1001,952],
[957,973,976,0,975,996,1021,998,1000,977],
[1003,984,1035,1025,0,1010,1024,997,967,990],
[956,993,992,1004,990,0,976,975,985,995],
[982,964,1007,979,976,1024,0,1000,971,976],
[991,980,1030,1002,1003,1025,1000,0,999,986],
[998,1030,999,1000,1033,1015,1029,1001,0,1034],
[993,1028,1048,1023,1010,1005,1024,1014,966,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 45, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,944,1004,994,1010,996,1029,1000,1031,989],
[1056,0,1031,1027,1010,1025,1029,972,1029,990],
[996,969,0,1015,1004,995,1033,969,1022,1037],
[1006,973,985,0,1038,1015,1039,981,1015,977],
[990,990,996,962,0,978,996,968,997,955],
[1004,975,1005,985,1022,0,1000,997,1009,972],
[971,971,967,961,1004,1000,0,975,1001,959],
[1000,1028,1031,1019,1032,1003,1025,0,1028,1017],
[969,971,978,985,1003,991,999,972,0,962],
[1011,1010,963,1023,1045,1028,1041,983,1038,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 46, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1012,1016,989,1043,1006,1014,999,1006,1004],
[988,0,1030,990,1045,1052,1017,1013,1018,987],
[984,970,0,997,1065,1049,975,1015,1035,965],
[1011,1010,1003,0,1047,1055,1021,1017,993,996],
[957,955,935,953,0,1021,1000,935,969,965],
[994,948,951,945,979,0,978,976,963,957],
[986,983,1025,979,1000,1022,0,1038,990,1027],
[1001,987,985,983,1065,1024,962,0,1002,965],
[994,982,965,1007,1031,1037,1010,998,0,1003],
[996,1013,1035,1004,1035,1043,973,1035,997,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 47, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,925,964,982,973,988,965,995,965,981],
[1075,0,1013,1055,1017,1030,1041,1027,999,985],
[1036,987,0,1026,986,1053,1007,1040,984,971],
[1018,945,974,0,975,1017,1010,998,950,1009],
[1027,983,1014,1025,0,1020,988,1031,958,981],
[1012,970,947,983,980,0,984,993,983,951],
[1035,959,993,990,1012,1016,0,1012,1002,962],
[1005,973,960,1002,969,1007,988,0,953,945],
[1035,1001,1016,1050,1042,1017,998,1047,0,999],
[1019,1015,1029,991,1019,1049,1038,1055,1001,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 48, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1029,1015,1022,1010,983,978,1031,976,1012],
[971,0,972,992,973,983,963,963,981,968],
[985,1028,0,998,1030,1005,985,988,963,998],
[978,1008,1002,0,1010,1007,985,990,962,983],
[990,1027,970,990,0,963,958,1019,1014,976],
[1017,1017,995,993,1037,0,989,1013,985,990],
[1022,1037,1015,1015,1042,1011,0,1032,986,1000],
[969,1037,1012,1010,981,987,968,0,978,999],
[1024,1019,1037,1038,986,1015,1014,1022,0,1008],
[988,1032,1002,1017,1024,1010,1000,1001,992,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 49, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1058,989,1008,1087,1017,1045,1055,981,1129],
[942,0,981,989,1030,998,988,1059,981,1062],
[1011,1019,0,997,1072,1023,1010,1020,949,1037],
[992,1011,1003,0,1063,1049,1012,1035,1004,1076],
[913,970,928,937,0,923,984,968,929,1027],
[983,1002,977,951,1077,0,1023,1066,1020,1050],
[955,1012,990,988,1016,977,0,1029,1000,1079],
[945,941,980,965,1032,934,971,0,921,1008],
[1019,1019,1051,996,1071,980,1000,1079,0,1102],
[871,938,963,924,973,950,921,992,898,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 50, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1009,987,993,1012,992,979,1004,986,1031],
[991,0,954,987,1045,1000,942,1023,989,1016],
[1013,1046,0,1003,1045,993,998,1015,1024,1043],
[1007,1013,997,0,1060,992,979,1010,989,1032],
[988,955,955,940,0,980,949,967,953,978],
[1008,1000,1007,1008,1020,0,1003,981,987,1018],
[1021,1058,1002,1021,1051,997,0,1017,1001,1022],
[996,977,985,990,1033,1019,983,0,984,1011],
[1014,1011,976,1011,1047,1013,999,1016,0,1033],
[969,984,957,968,1022,982,978,989,967,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 51, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,960,1076,969,1102,1023,1085,1029,1057,912],
[1040,0,1005,1026,1002,967,1054,1018,1049,954],
[924,995,0,908,1026,998,1094,1038,1052,1015],
[1031,974,1092,0,1055,1033,1100,1046,1017,963],
[898,998,974,945,0,972,1014,951,1017,955],
[977,1033,1002,967,1028,0,1154,966,1020,999],
[915,946,906,900,986,846,0,884,1008,957],
[971,982,962,954,1049,1034,1116,0,1012,969],
[943,951,948,983,983,980,992,988,0,975],
[1088,1046,985,1037,1045,1001,1043,1031,1025,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 52, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1013,1076,1041,1087,1082,851,1012,984,1041],
[987,0,1032,1085,1018,1062,984,1007,1051,1007],
[924,968,0,1024,942,1033,902,915,908,1057],
[959,915,976,0,947,951,913,920,928,941],
[913,982,1058,1053,0,1006,972,1003,924,1073],
[918,938,967,1049,994,0,864,972,1002,948],
[1149,1016,1098,1087,1028,1136,0,956,1027,1156],
[988,993,1085,1080,997,1028,1044,0,970,1102],
[1016,949,1092,1072,1076,998,973,1030,0,1062],
[959,993,943,1059,927,1052,844,898,938,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 53, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,979,926,1020,995,938,938,959,988,986],
[1021,0,968,1049,990,993,961,1034,936,983],
[1074,1032,0,996,1025,1029,1027,995,1004,1018],
[980,951,1004,0,1032,977,956,979,943,1035],
[1005,1010,975,968,0,980,1004,945,993,1026],
[1062,1007,971,1023,1020,0,980,1009,1004,1032],
[1062,1039,973,1044,996,1020,0,1008,1012,1048],
[1041,966,1005,1021,1055,991,992,0,1017,1017],
[1012,1064,996,1057,1007,996,988,983,0,1015],
[1014,1017,982,965,974,968,952,983,985,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 54, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,986,1038,1002,965,992,972,985,995,960],
[1014,0,1027,1059,975,994,1016,1030,1020,991],
[962,973,0,1003,964,967,972,988,1031,957],
[998,941,997,0,990,951,961,960,994,952],
[1035,1025,1036,1010,0,1029,996,1009,1018,1023],
[1008,1006,1033,1049,971,0,1017,1030,1015,986],
[1028,984,1028,1039,1004,983,0,1002,998,998],
[1015,970,1012,1040,991,970,998,0,1014,997],
[1005,980,969,1006,982,985,1002,986,0,967],
[1040,1009,1043,1048,977,1014,1002,1003,1033,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 55, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,946,948,1001,896,1015,992,948,1022,956],
[1054,0,1030,922,890,989,996,971,886,904],
[1052,970,0,921,928,951,1002,973,927,985],
[999,1078,1079,0,950,1011,1107,1029,946,1008],
[1104,1110,1072,1050,0,1037,1035,982,1064,1085],
[985,1011,1049,989,963,0,1060,998,977,1062],
[1008,1004,998,893,965,940,0,957,914,1013],
[1052,1029,1027,971,1018,1002,1043,0,950,980],
[978,1114,1073,1054,936,1023,1086,1050,0,963],
[1044,1096,1015,992,915,938,987,1020,1037,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 56, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1002,989,990,987,974,987,1026,963,961],
[998,0,979,1021,1020,1007,1013,1014,1012,999],
[1011,1021,0,1051,1013,1002,1008,1049,1008,979],
[1010,979,949,0,1003,1015,1003,1004,981,971],
[1013,980,987,997,0,934,976,1018,961,981],
[1026,993,998,985,1066,0,1036,1072,983,1005],
[1013,987,992,997,1024,964,0,1006,944,948],
[974,986,951,996,982,928,994,0,920,921],
[1037,988,992,1019,1039,1017,1056,1080,0,963],
[1039,1001,1021,1029,1019,995,1052,1079,1037,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 57, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,932,962,1014,1042,932,976,956,943,1003],
[1068,0,986,991,1030,1052,1024,1035,1009,947],
[1038,1014,0,971,1059,974,1089,1008,997,971],
[986,1009,1029,0,1087,976,1005,1005,925,1024],
[958,970,941,913,0,962,1022,973,982,976],
[1068,948,1026,1024,1038,0,988,1076,953,985],
[1024,976,911,995,978,1012,0,1009,900,937],
[1044,965,992,995,1027,924,991,0,935,1045],
[1057,991,1003,1075,1018,1047,1100,1065,0,1032],
[997,1053,1029,976,1024,1015,1063,955,968,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 58, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,962,1002,958,996,935,975,1014,968,1011],
[1038,0,1015,992,1008,1007,1050,1038,1019,1059],
[998,985,0,968,964,928,995,1021,955,1031],
[1042,1008,1032,0,969,970,990,1030,993,1055],
[1004,992,1036,1031,0,931,1005,1026,1002,1056],
[1065,993,1072,1030,1069,0,1057,1057,1046,1101],
[1025,950,1005,1010,995,943,0,1010,992,1036],
[986,962,979,970,974,943,990,0,1049,1019],
[1032,981,1045,1007,998,954,1008,951,0,1005],
[989,941,969,945,944,899,964,981,995,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 59, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1048,997,1016,1012,1043,1050,1007,1014,1001],
[952,0,962,992,975,999,984,951,999,967],
[1003,1038,0,991,1034,1061,1060,1025,1015,1030],
[984,1008,1009,0,1011,1027,1007,1025,1022,1008],
[988,1025,966,989,0,1037,1002,974,997,950],
[957,1001,939,973,963,0,999,956,965,994],
[950,1016,940,993,998,1001,0,1003,999,960],
[993,1049,975,975,1026,1044,997,0,1038,979],
[986,1001,985,978,1003,1035,1001,962,0,981],
[999,1033,970,992,1050,1006,1040,1021,1019,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 60, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,990,982,1039,1032,1052,1021,1007,1025,1055],
[1010,0,1052,1059,1009,1020,1060,1006,980,1007],
[1018,948,0,996,978,973,1078,1040,966,1062],
[961,941,1004,0,1017,962,958,979,1039,1056],
[968,991,1022,983,0,1031,946,995,980,1036],
[948,980,1027,1038,969,0,987,969,1010,1043],
[979,940,922,1042,1054,1013,0,979,1033,1031],
[993,994,960,1021,1005,1031,1021,0,962,1096],
[975,1020,1034,961,1020,990,967,1038,0,1024],
[945,993,938,944,964,957,969,904,976,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 61, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,946,993,990,995,989,1039,1018,997,1055],
[1054,0,1000,1034,1039,1027,1020,1053,1073,1036],
[1007,1000,0,995,987,1007,984,1038,1020,1011],
[1010,966,1005,0,1028,1009,1042,1008,980,970],
[1005,961,1013,972,0,982,1010,1001,992,944],
[1011,973,993,991,1018,0,999,1009,993,980],
[961,980,1016,958,990,1001,0,999,993,935],
[982,947,962,992,999,991,1001,0,980,1005],
[1003,927,980,1020,1008,1007,1007,1020,0,993],
[945,964,989,1030,1056,1020,1065,995,1007,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 62, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,855,1194,991,909,1142,1054,1043,895,1181],
[1145,0,1062,1077,1075,1076,937,1083,1116,1107],
[806,938,0,938,862,917,653,966,895,837],
[1009,923,1062,0,952,1095,908,1104,1075,1045],
[1091,925,1138,1048,0,1208,883,1109,992,1163],
[858,924,1083,905,792,0,762,1064,799,939],
[946,1063,1347,1092,1117,1238,0,1171,810,1191],
[957,917,1034,896,891,936,829,0,878,934],
[1105,884,1105,925,1008,1201,1190,1122,0,1056],
[819,893,1163,955,837,1061,809,1066,944,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 63, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1466,1276,1319,1310,1256,1057,762,1299,1241],
[534,0,239,1332,845,845,330,945,925,514],
[724,1761,0,1762,1366,1346,541,945,1411,1140],
[681,668,238,0,703,625,477,350,443,645],
[690,1155,634,1297,0,925,451,945,890,1276],
[744,1155,654,1375,1075,0,746,762,988,929],
[943,1670,1459,1523,1549,1254,0,1332,1503,1048],
[1238,1055,1055,1650,1055,1238,668,0,1367,976],
[701,1075,589,1557,1110,1012,497,633,0,976],
[759,1486,860,1355,724,1071,952,1024,1024,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 64, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,985,879,1008,993,1009,906,948,909,954],
[1015,0,980,1059,954,1074,1006,1008,940,1031],
[1121,1020,0,1117,1025,1063,964,1012,1023,1040],
[992,941,883,0,937,1079,962,936,923,977],
[1007,1046,975,1063,0,1049,1052,969,960,1108],
[991,926,937,921,951,0,904,932,872,1025],
[1094,994,1036,1038,948,1096,0,1029,1002,1025],
[1052,992,988,1064,1031,1068,971,0,925,1026],
[1091,1060,977,1077,1040,1128,998,1075,0,1141],
[1046,969,960,1023,892,975,975,974,859,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 65, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,981,1038,953,1036,995,1043,967,973,980],
[1019,0,1028,1041,1004,1009,1031,982,1010,1012],
[962,972,0,950,962,964,1033,1005,916,991],
[1047,959,1050,0,1029,1027,1061,1013,968,1043],
[964,996,1038,971,0,985,999,938,974,991],
[1005,991,1036,973,1015,0,1047,962,978,1008],
[957,969,967,939,1001,953,0,945,948,938],
[1033,1018,995,987,1062,1038,1055,0,967,1034],
[1027,990,1084,1032,1026,1022,1052,1033,0,1057],
[1020,988,1009,957,1009,992,1062,966,943,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 66, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1015,994,1009,1007,996,980,1022,1000,1003],
[985,0,985,988,990,1017,978,994,979,962],
[1006,1015,0,1018,1014,1004,1019,1037,1000,1008],
[991,1012,982,0,994,996,983,1020,1017,970],
[993,1010,986,1006,0,1002,1020,1013,976,977],
[1004,983,996,1004,998,0,950,998,988,986],
[1020,1022,981,1017,980,1050,0,1035,996,1006],
[978,1006,963,980,987,1002,965,0,970,1004],
[1000,1021,1000,983,1024,1012,1004,1030,0,998],
[997,1038,992,1030,1023,1014,994,996,1002,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 67, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1040,998,974,1031,978,996,1005,1003,1024],
[960,0,992,988,1005,988,991,991,1001,993],
[1002,1008,0,996,987,976,968,978,969,1012],
[1026,1012,1004,0,1006,1011,987,1018,983,1006],
[969,995,1013,994,0,992,979,1000,1006,1013],
[1022,1012,1024,989,1008,0,997,991,1004,1046],
[1004,1009,1032,1013,1021,1003,0,1042,1030,996],
[995,1009,1022,982,1000,1009,958,0,986,1008],
[997,999,1031,1017,994,996,970,1014,0,1004],
[976,1007,988,994,987,954,1004,992,996,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 68, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1299,1087,920,1086,1053,1228,1108,1222,1358],
[701,0,925,930,1144,913,1015,876,956,1002],
[913,1075,0,862,985,1007,1030,824,872,985],
[1080,1070,1138,0,1201,1087,1226,912,996,1136],
[914,856,1015,799,0,1038,1172,833,959,1139],
[947,1087,993,913,962,0,1174,1005,1080,1119],
[772,985,970,774,828,826,0,772,765,880],
[892,1124,1176,1088,1167,995,1228,0,1061,988],
[778,1044,1128,1004,1041,920,1235,939,0,1212],
[642,998,1015,864,861,881,1120,1012,788,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 69, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,998,1013,996,982,945,952,1055,995,957],
[1002,0,972,976,978,967,964,1040,978,1005],
[987,1028,0,991,1032,967,998,1061,984,966],
[1004,1024,1009,0,969,967,960,1011,992,979],
[1018,1022,968,1031,0,979,962,1042,978,982],
[1055,1033,1033,1033,1021,0,1036,1087,990,1013],
[1048,1036,1002,1040,1038,964,0,1058,1029,986],
[945,960,939,989,958,913,942,0,946,945],
[1005,1022,1016,1008,1022,1010,971,1054,0,998],
[1043,995,1034,1021,1018,987,1014,1055,1002,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 70, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,932,1085,1037,991,983,1013,992,968,1037],
[1068,0,1124,1102,999,1120,1022,1074,1067,1026],
[915,876,0,1013,899,917,954,978,886,1049],
[963,898,987,0,939,882,1000,1006,980,952],
[1009,1001,1101,1061,0,959,1006,1004,1072,1034],
[1017,880,1083,1118,1041,0,1012,1120,1027,1021],
[987,978,1046,1000,994,988,0,1125,1055,1106],
[1008,926,1022,994,996,880,875,0,931,981],
[1032,933,1114,1020,928,973,945,1069,0,992],
[963,974,951,1048,966,979,894,1019,1008,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 71, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1025,1022,1018,1018,998,1011,1029,1021,976],
[975,0,994,1024,1032,978,985,989,1009,1009],
[978,1006,0,1027,1035,972,991,976,997,970],
[982,976,973,0,1005,971,966,974,992,989],
[982,968,965,995,0,975,974,986,988,951],
[1002,1022,1028,1029,1025,0,937,991,1015,1008],
[989,1015,1009,1034,1026,1063,0,1013,1016,1033],
[971,1011,1024,1026,1014,1009,987,0,1034,1009],
[979,991,1003,1008,1012,985,984,966,0,979],
[1024,991,1030,1011,1049,992,967,991,1021,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 72, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1028,1063,1054,984,1038,1090,1039,1027,1111],
[972,0,995,1000,973,1029,1057,1046,960,1015],
[937,1005,0,949,957,994,1024,1026,975,1078],
[946,1000,1051,0,909,942,1038,1012,922,1051],
[1016,1027,1043,1091,0,1076,1115,1051,987,1037],
[962,971,1006,1058,924,0,1004,927,1023,973],
[910,943,976,962,885,996,0,902,914,984],
[961,954,974,988,949,1073,1098,0,1013,1088],
[973,1040,1025,1078,1013,977,1086,987,0,1072],
[889,985,922,949,963,1027,1016,912,928,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 73, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,979,962,983,933,1022,978,992,1021,1010],
[1021,0,988,1011,1034,1050,1032,982,1052,1011],
[1038,1012,0,1055,992,1065,1025,1031,1088,1024],
[1017,989,945,0,991,1014,990,983,1017,1038],
[1067,966,1008,1009,0,1041,997,985,1059,1027],
[978,950,935,986,959,0,986,897,995,985],
[1022,968,975,1010,1003,1014,0,951,1003,1026],
[1008,1018,969,1017,1015,1103,1049,0,1052,1052],
[979,948,912,983,941,1005,997,948,0,997],
[990,989,976,962,973,1015,974,948,1003,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 74, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,957,969,969,982,987,949,991,944,969],
[1043,0,1005,1034,993,1038,1015,1043,1003,998],
[1031,995,0,1027,1012,1022,1019,1033,999,992],
[1031,966,973,0,981,1010,978,1031,984,999],
[1018,1007,988,1019,0,1006,988,1038,985,990],
[1013,962,978,990,994,0,978,1019,1013,979],
[1051,985,981,1022,1012,1022,0,1023,999,1018],
[1009,957,967,969,962,981,977,0,937,981],
[1056,997,1001,1016,1015,987,1001,1063,0,1009],
[1031,1002,1008,1001,1010,1021,982,1019,991,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 75, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,998,1011,1028,1036,1037,956,923,876,1041],
[1002,0,932,988,1039,1029,843,994,881,976],
[989,1068,0,1068,944,1079,912,995,880,995],
[972,1012,932,0,961,963,832,912,898,893],
[964,961,1056,1039,0,910,919,985,936,1027],
[963,971,921,1037,1090,0,794,862,921,844],
[1044,1157,1088,1168,1081,1206,0,1162,990,1060],
[1077,1006,1005,1088,1015,1138,838,0,890,1011],
[1124,1119,1120,1102,1064,1079,1010,1110,0,988],
[959,1024,1005,1107,973,1156,940,989,1012,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 76, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,985,978,944,1003,975,1036,1070,981,1012],
[1015,0,938,1004,971,1009,1012,995,906,1022],
[1022,1062,0,931,1012,1031,1044,1039,989,977],
[1056,996,1069,0,998,1041,1035,1054,1025,1066],
[997,1029,988,1002,0,1041,1053,996,962,1078],
[1025,991,969,959,959,0,1012,997,910,1058],
[964,988,956,965,947,988,0,991,982,1062],
[930,1005,961,946,1004,1003,1009,0,912,998],
[1019,1094,1011,975,1038,1090,1018,1088,0,1092],
[988,978,1023,934,922,942,938,1002,908,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 77, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,965,1004,992,993,966,953,981,992,992],
[1035,0,1025,1011,1015,1015,1004,1000,1010,1008],
[996,975,0,994,972,990,977,979,987,992],
[1008,989,1006,0,987,1021,1022,995,1000,1013],
[1007,985,1028,1013,0,1027,985,978,1020,1003],
[1034,985,1010,979,973,0,993,1014,967,1032],
[1047,996,1023,978,1015,1007,0,996,1019,1027],
[1019,1000,1021,1005,1022,986,1004,0,998,998],
[1008,990,1013,1000,980,1033,981,1002,0,1025],
[1008,992,1008,987,997,968,973,1002,975,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 78, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,934,951,919,903,928,954,951,977,915],
[1066,0,986,989,937,992,966,1010,996,947],
[1049,1014,0,978,980,955,1033,1024,1030,944],
[1081,1011,1022,0,995,987,1067,1033,1063,949],
[1097,1063,1020,1005,0,1011,1039,1046,1020,952],
[1072,1008,1045,1013,989,0,1071,1063,1040,1030],
[1046,1034,967,933,961,929,0,1012,960,916],
[1049,990,976,967,954,937,988,0,999,931],
[1023,1004,970,937,980,960,1040,1001,0,993],
[1085,1053,1056,1051,1048,970,1084,1069,1007,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 79, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1030,993,1021,985,1013,989,1022,1014,1036],
[970,0,987,1005,956,977,979,973,968,988],
[1007,1013,0,982,971,986,983,1011,1007,1007],
[979,995,1018,0,960,984,964,1007,1022,1014],
[1015,1044,1029,1040,0,1023,1004,1004,996,1010],
[987,1023,1014,1016,977,0,1002,996,983,980],
[1011,1021,1017,1036,996,998,0,1035,1013,1009],
[978,1027,989,993,996,1004,965,0,988,1004],
[986,1032,993,978,1004,1017,987,1012,0,1017],
[964,1012,993,986,990,1020,991,996,983,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 80, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1040,1007,1040,1021,1009,969,977,1051,1026],
[960,0,989,1033,998,1049,1026,1008,1058,1011],
[993,1011,0,1051,1023,1037,1001,995,1025,1006],
[960,967,949,0,1014,987,992,957,988,959],
[979,1002,977,986,0,1011,993,992,1035,1016],
[991,951,963,1013,989,0,998,988,997,1012],
[1031,974,999,1008,1007,1002,0,969,1029,995],
[1023,992,1005,1043,1008,1012,1031,0,1027,1007],
[949,942,975,1012,965,1003,971,973,0,1009],
[974,989,994,1041,984,988,1005,993,991,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 81, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,923,992,961,902,1011,966,894,977,933],
[1077,0,1008,966,979,1069,1057,985,1001,1059],
[1008,992,0,900,947,1030,1013,927,928,975],
[1039,1034,1100,0,1012,1123,1096,982,1063,1096],
[1098,1021,1053,988,0,1103,1061,1035,994,1102],
[989,931,970,877,897,0,1013,922,918,987],
[1034,943,987,904,939,987,0,960,994,1015],
[1106,1015,1073,1018,965,1078,1040,0,1022,1024],
[1023,999,1072,937,1006,1082,1006,978,0,993],
[1067,941,1025,904,898,1013,985,976,1007,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 82, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1020,1046,1026,1040,996,1025,1026,1027,1043],
[980,0,984,974,970,913,998,1006,1022,1020],
[954,1016,0,1018,989,974,1054,1048,953,1067],
[974,1026,982,0,971,937,962,974,985,1035],
[960,1030,1011,1029,0,996,977,1009,1003,1014],
[1004,1087,1026,1063,1004,0,1036,1018,991,1025],
[975,1002,946,1038,1023,964,0,972,963,1049],
[974,994,952,1026,991,982,1028,0,1055,1041],
[973,978,1047,1015,997,1009,1037,945,0,989],
[957,980,933,965,986,975,951,959,1011,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 83, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1037,1066,1012,1003,1032,984,1069,999,1028],
[963,0,1056,967,1022,978,1013,988,1004,1034],
[934,944,0,947,983,988,907,989,999,1004],
[988,1033,1053,0,967,1019,1020,1039,1000,1071],
[997,978,1017,1033,0,1018,1022,1056,1067,993],
[968,1022,1012,981,982,0,988,1042,990,1042],
[1016,987,1093,980,978,1012,0,1020,995,999],
[931,1012,1011,961,944,958,980,0,977,998],
[1001,996,1001,1000,933,1010,1005,1023,0,995],
[972,966,996,929,1007,958,1001,1002,1005,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 84, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1036,1019,1047,973,1013,912,930,1031,1054],
[964,0,1104,911,983,1038,982,957,1153,1038],
[981,896,0,938,966,1057,958,859,1084,1038],
[953,1089,1062,0,1025,1031,982,922,1062,1066],
[1027,1017,1034,975,0,1017,1019,936,1098,1041],
[987,962,943,969,983,0,960,946,1059,911],
[1088,1018,1042,1018,981,1040,0,977,1108,964],
[1070,1043,1141,1078,1064,1054,1023,0,1255,938],
[969,847,916,938,902,941,892,745,0,859],
[946,962,962,934,959,1089,1036,1062,1141,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 85, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1009,970,1010,995,984,1010,1036,1016,996],
[991,0,934,996,982,1006,1003,1006,976,995],
[1030,1066,0,1054,1039,999,1013,1078,1002,992],
[990,1004,946,0,989,944,940,993,930,1016],
[1005,1018,961,1011,0,1015,982,1026,1012,975],
[1016,994,1001,1056,985,0,983,1023,986,1004],
[990,997,987,1060,1018,1017,0,1026,971,1022],
[964,994,922,1007,974,977,974,0,958,956],
[984,1024,998,1070,988,1014,1029,1042,0,998],
[1004,1005,1008,984,1025,996,978,1044,1002,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 86, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1019,1030,1033,1034,1054,1048,1052,1056,987],
[981,0,1004,1063,982,988,1027,999,1046,989],
[970,996,0,1021,994,994,1055,995,1036,996],
[967,937,979,0,947,980,988,961,1006,904],
[966,1018,1006,1053,0,990,1016,996,1034,1009],
[946,1012,1006,1020,1010,0,1012,983,1080,1030],
[952,973,945,1012,984,988,0,1015,1019,991],
[948,1001,1005,1039,1004,1017,985,0,1017,980],
[944,954,964,994,966,920,981,983,0,971],
[1013,1011,1004,1096,991,970,1009,1020,1029,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 87, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1025,1004,976,974,998,1056,994,1006,995],
[975,0,1033,967,962,975,1024,981,977,980],
[996,967,0,985,983,964,1019,977,952,955],
[1024,1033,1015,0,1001,969,1048,1016,982,1012],
[1026,1038,1017,999,0,971,1045,1007,983,1021],
[1002,1025,1036,1031,1029,0,1078,1017,994,1027],
[944,976,981,952,955,922,0,951,964,964],
[1006,1019,1023,984,993,983,1049,0,971,1005],
[994,1023,1048,1018,1017,1006,1036,1029,0,1000],
[1005,1020,1045,988,979,973,1036,995,1000,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 88, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1006,1120,1029,969,931,996,941,936,952],
[994,0,1086,1035,936,1076,1040,785,950,952],
[880,914,0,888,824,899,1002,865,942,952],
[971,965,1112,0,856,904,1046,892,986,996],
[1031,1064,1176,1144,0,1089,1141,1057,1078,979],
[1069,924,1101,1096,911,0,1093,932,893,971],
[1004,960,998,954,859,907,0,961,868,1030],
[1059,1215,1135,1108,943,1068,1039,0,1054,1014],
[1064,1050,1058,1014,922,1107,1132,946,0,1055],
[1048,1048,1048,1004,1021,1029,970,986,945,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 89, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,960,1010,972,991,980,974,985,964,978],
[1040,0,1028,979,963,962,960,937,993,993],
[990,972,0,919,1014,995,1006,939,981,964],
[1028,1021,1081,0,1084,1040,984,1042,1010,997],
[1009,1037,986,916,0,958,990,973,982,968],
[1020,1038,1005,960,1042,0,1010,984,989,972],
[1026,1040,994,1016,1010,990,0,950,981,987],
[1015,1063,1061,958,1027,1016,1050,0,1028,986],
[1036,1007,1019,990,1018,1011,1019,972,0,1009],
[1022,1007,1036,1003,1032,1028,1013,1014,991,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 90, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,999,994,970,1007,997,1011,1012,973,975],
[1001,0,1005,986,999,1012,983,1026,1021,993],
[1006,995,0,1013,1031,1025,1007,1023,1032,1019],
[1030,1014,987,0,1038,1020,1000,1032,984,1002],
[993,1001,969,962,0,978,992,981,972,969],
[1003,988,975,980,1022,0,963,976,988,966],
[989,1017,993,1000,1008,1037,0,998,1025,1001],
[988,974,977,968,1019,1024,1002,0,985,969],
[1027,979,968,1016,1028,1012,975,1015,0,990],
[1025,1007,981,998,1031,1034,999,1031,1010,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 91, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,983,988,860,1013,929,907,714,794,862],
[1017,0,1039,886,1038,997,952,904,824,763],
[1012,961,0,929,983,1120,969,825,849,816],
[1140,1114,1071,0,1093,1061,937,1062,1076,887],
[987,962,1017,907,0,910,1012,964,797,943],
[1071,1003,880,939,1090,0,1066,849,874,856],
[1093,1048,1031,1063,988,934,0,1064,960,955],
[1286,1096,1175,938,1036,1151,936,0,861,1082],
[1206,1176,1151,924,1203,1126,1040,1139,0,982],
[1138,1237,1184,1113,1057,1144,1045,918,1018,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 92, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,981,1064,1015,1024,1045,1064,1067,1064,1003],
[1019,0,1038,1019,1001,1038,1038,1033,1014,988],
[936,962,0,967,1012,1046,1028,1018,991,1001],
[985,981,1033,0,1029,1017,1018,1037,1030,999],
[976,999,988,971,0,995,972,1011,958,982],
[955,962,954,983,1005,0,1015,996,1019,1024],
[936,962,972,982,1028,985,0,984,977,966],
[933,967,982,963,989,1004,1016,0,985,989],
[936,986,1009,970,1042,981,1023,1015,0,964],
[997,1012,999,1001,1018,976,1034,1011,1036,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 93, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,959,991,976,1070,989,1027,1022,1078,1094],
[1041,0,1004,1034,995,1041,1030,1095,1102,1073],
[1009,996,0,1069,997,1026,1000,962,1048,1041],
[1024,966,931,0,993,940,979,959,1063,1070],
[930,1005,1003,1007,0,910,970,981,1007,1021],
[1011,959,974,1060,1090,0,1062,1069,1095,1136],
[973,970,1000,1021,1030,938,0,1020,1027,1075],
[978,905,1038,1041,1019,931,980,0,1021,1029],
[922,898,952,937,993,905,973,979,0,1016],
[906,927,959,930,979,864,925,971,984,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 94, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,983,995,1041,985,1005,989,1001,969,1000],
[1017,0,1008,1044,977,1027,975,1034,1004,987],
[1005,992,0,1040,944,1002,1030,997,969,998],
[959,956,960,0,958,981,964,980,960,997],
[1015,1023,1056,1042,0,1028,1024,1001,981,1017],
[995,973,998,1019,972,0,1011,1023,988,1027],
[1011,1025,970,1036,976,989,0,1014,996,1011],
[999,966,1003,1020,999,977,986,0,976,1004],
[1031,996,1031,1040,1019,1012,1004,1024,0,987],
[1000,1013,1002,1003,983,973,989,996,1013,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 95, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1032,1000,978,1003,1015,1011,1010,957,990],
[968,0,946,985,1008,959,945,1007,941,1004],
[1000,1054,0,1011,1009,1040,1033,1023,1016,1030],
[1022,1015,989,0,1008,1019,970,1035,966,1007],
[997,992,991,992,0,1017,1024,1018,1016,1009],
[985,1041,960,981,983,0,1004,1021,986,990],
[989,1055,967,1030,976,996,0,1026,1008,1063],
[990,993,977,965,982,979,974,0,998,987],
[1043,1059,984,1034,984,1014,992,1002,0,1024],
[1010,996,970,993,991,1010,937,1013,976,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 96, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1010,952,1013,1007,965,963,1012,978,1028],
[990,0,1024,988,960,962,985,977,976,980],
[1048,976,0,992,1004,1023,1012,1014,1004,1034],
[987,1012,1008,0,995,981,983,949,1013,1023],
[993,1040,996,1005,0,1001,959,982,1024,1000],
[1035,1038,977,1019,999,0,997,1030,1031,1042],
[1037,1015,988,1017,1041,1003,0,1004,990,1064],
[988,1023,986,1051,1018,970,996,0,971,1025],
[1022,1024,996,987,976,969,1010,1029,0,1028],
[972,1020,966,977,1000,958,936,975,972,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 97, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1140,880,886,730,901,953,925,1089,966],
[860,0,821,688,889,906,997,1000,1008,1006],
[1120,1179,0,914,758,1044,1029,953,1164,883],
[1114,1312,1086,0,1009,988,1039,1033,1156,998],
[1270,1111,1242,991,0,1030,1129,942,1014,1006],
[1099,1094,956,1012,970,0,1095,1011,1192,1219],
[1047,1003,971,961,871,905,0,1027,973,886],
[1075,1000,1047,967,1058,989,973,0,941,1118],
[911,992,836,844,986,808,1027,1059,0,968],
[1034,994,1117,1002,994,781,1114,882,1032,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 98, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,999,1050,1029,998,1004,1063,960,996,962],
[1001,0,1061,990,944,976,1143,958,982,978],
[950,939,0,978,982,1067,976,946,988,956],
[971,1010,1022,0,1016,1022,1033,1005,970,937],
[1002,1056,1018,984,0,1018,1072,977,975,1021],
[996,1024,933,978,982,0,1081,1003,1007,967],
[937,857,1024,967,928,919,0,947,947,893],
[1040,1042,1054,995,1023,997,1053,0,993,967],
[1004,1018,1012,1030,1025,993,1053,1007,0,968],
[1038,1022,1044,1063,979,1033,1107,1033,1032,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 99, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1003,984,988,1002,1037,992,997,973,965],
[997,0,1001,961,998,1046,985,1008,1000,1013],
[1016,999,0,980,1017,1043,1009,1011,1015,997],
[1012,1039,1020,0,1013,1047,1016,1019,1016,998],
[998,1002,983,987,0,1033,1024,998,987,989],
[963,954,957,953,967,0,950,974,951,962],
[1008,1015,991,984,976,1050,0,993,1016,1026],
[1003,992,989,981,1002,1026,1007,0,1017,978],
[1027,1000,985,984,1013,1049,984,983,0,980],
[1035,987,1003,1002,1011,1038,974,1022,1020,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 100, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,975,999,982,978,986,975,1002,994,1005],
[1025,0,999,979,976,998,971,1018,995,1009],
[1001,1001,0,989,996,994,974,1014,979,1037],
[1018,1021,1011,0,1009,1024,995,1002,984,1025],
[1022,1024,1004,991,0,1036,988,1004,998,1015],
[1014,1002,1006,976,964,0,974,1009,1003,1017],
[1025,1029,1026,1005,1012,1026,0,1013,988,1005],
[998,982,986,998,996,991,987,0,991,1021],
[1006,1005,1021,1016,1002,997,1012,1009,0,1001],
[995,991,963,975,985,983,995,979,999,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 101, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1045,996,1029,1000,1060,1043,1012,995,1022],
[955,0,980,940,911,978,1016,1020,1000,1004],
[1004,1020,0,1010,990,1055,1047,1056,1021,981],
[971,1060,990,0,981,1029,1050,1008,992,1019],
[1000,1089,1010,1019,0,1070,1033,1018,1087,1038],
[940,1022,945,971,930,0,990,962,973,985],
[957,984,953,950,967,1010,0,939,1001,984],
[988,980,944,992,982,1038,1061,0,1031,1011],
[1005,1000,979,1008,913,1027,999,969,0,989],
[978,996,1019,981,962,1015,1016,989,1011,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 102, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,990,939,928,815,932,946,904,979,933],
[1010,0,964,1022,950,1059,1034,961,1129,1014],
[1061,1036,0,1063,984,1055,1031,1007,1102,1037],
[1072,978,937,0,951,1002,1033,1011,1086,1009],
[1185,1050,1016,1049,0,1077,1071,980,1057,1084],
[1068,941,945,998,923,0,976,993,1059,958],
[1054,966,969,967,929,1024,0,977,1040,978],
[1096,1039,993,989,1020,1007,1023,0,1052,1049],
[1021,871,898,914,943,941,960,948,0,1013],
[1067,986,963,991,916,1042,1022,951,987,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 103, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,984,1017,975,998,972,989,993,979,1023],
[1016,0,995,993,999,968,960,958,976,960],
[983,1005,0,955,999,975,953,967,947,977],
[1025,1007,1045,0,1031,1026,976,1028,1008,1049],
[1002,1001,1001,969,0,990,957,971,974,954],
[1028,1032,1025,974,1010,0,999,1023,972,1007],
[1011,1040,1047,1024,1043,1001,0,983,1003,1043],
[1007,1042,1033,972,1029,977,1017,0,1013,1011],
[1021,1024,1053,992,1026,1028,997,987,0,1002],
[977,1040,1023,951,1046,993,957,989,998,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 104, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,979,970,964,920,986,1033,987,990,972],
[1021,0,1051,1037,1022,978,1002,1001,999,1008],
[1030,949,0,1004,1000,934,995,955,925,1000],
[1036,963,996,0,922,967,1001,979,953,972],
[1080,978,1000,1078,0,966,1067,1029,1015,1017],
[1014,1022,1066,1033,1034,0,1052,1034,990,1035],
[967,998,1005,999,933,948,0,965,952,970],
[1013,999,1045,1021,971,966,1035,0,996,1002],
[1010,1001,1075,1047,985,1010,1048,1004,0,991],
[1028,992,1000,1028,983,965,1030,998,1009,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 105, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1028,1026,1018,1005,1027,1020,1025,1043,982],
[972,0,1011,1012,1011,1008,1020,1064,1040,1007],
[974,989,0,1001,1004,1003,1011,1018,1007,1032],
[982,988,999,0,1010,1006,1003,1022,991,990],
[995,989,996,990,0,976,1015,1043,1020,1005],
[973,992,997,994,1024,0,1006,1028,1006,1005],
[980,980,989,997,985,994,0,1030,988,996],
[975,936,982,978,957,972,970,0,985,946],
[957,960,993,1009,980,994,1012,1015,0,975],
[1018,993,968,1010,995,995,1004,1054,1025,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 106, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1227,1081,1042,1001,1050,1108,913,1083,1033],
[773,0,1045,1031,932,906,1077,881,764,1018],
[919,955,0,945,973,1044,896,862,930,928],
[958,969,1055,0,1069,971,866,900,915,962],
[999,1068,1027,931,0,934,1054,977,959,1161],
[950,1094,956,1029,1066,0,1032,1050,995,1103],
[892,923,1104,1134,946,968,0,837,848,901],
[1087,1119,1138,1100,1023,950,1163,0,964,969],
[917,1236,1070,1085,1041,1005,1152,1036,0,974],
[967,982,1072,1038,839,897,1099,1031,1026,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 107, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1068,1040,1000,1034,1051,1024,1069,1053,1051],
[932,0,978,975,1007,983,1001,1003,1008,997],
[960,1022,0,992,990,1041,1025,1030,1003,1041],
[1000,1025,1008,0,1025,1037,1039,1042,1031,1053],
[966,993,1010,975,0,1019,983,1003,987,1003],
[949,1017,959,963,981,0,978,1031,983,995],
[976,999,975,961,1017,1022,0,1011,990,1061],
[931,997,970,958,997,969,989,0,994,1016],
[947,992,997,969,1013,1017,1010,1006,0,1026],
[949,1003,959,947,997,1005,939,984,974,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 108, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,982,993,1013,956,990,987,990,983,974],
[1018,0,987,993,972,987,1017,973,988,1004],
[1007,1013,0,978,983,1023,1017,997,1003,974],
[987,1007,1022,0,1004,998,1033,969,978,1002],
[1044,1028,1017,996,0,1008,1017,1033,1008,1022],
[1010,1013,977,1002,992,0,1007,1013,1017,1020],
[1013,983,983,967,983,993,0,1023,968,985],
[1010,1027,1003,1031,967,987,977,0,1024,1009],
[1017,1012,997,1022,992,983,1032,976,0,993],
[1026,996,1026,998,978,980,1015,991,1007,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 109, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1017,1089,1000,937,1044,1014,1058,952,1091],
[983,0,1006,987,965,1007,1048,1003,993,989],
[911,994,0,918,1032,964,998,1089,902,1000],
[1000,1013,1082,0,991,1007,1100,1024,977,1027],
[1063,1035,968,1009,0,1048,966,1038,934,1000],
[956,993,1036,993,952,0,995,1031,896,973],
[986,952,1002,900,1034,1005,0,952,995,957],
[942,997,911,976,962,969,1048,0,935,970],
[1048,1007,1098,1023,1066,1104,1005,1065,0,970],
[909,1011,1000,973,1000,1027,1043,1030,1030,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 110, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1019,984,997,1013,1024,1025,1018,1021,968],
[981,0,1013,983,969,971,984,969,1031,991],
[1016,987,0,983,1009,978,1031,996,1053,1003],
[1003,1017,1017,0,1009,998,1017,978,1008,988],
[987,1031,991,991,0,1009,1023,988,997,996],
[976,1029,1022,1002,991,0,1029,983,1000,967],
[975,1016,969,983,977,971,0,962,1013,969],
[982,1031,1004,1022,1012,1017,1038,0,1027,1002],
[979,969,947,992,1003,1000,987,973,0,980],
[1032,1009,997,1012,1004,1033,1031,998,1020,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 111, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1024,996,1069,1017,1023,999,1008,1026,998],
[976,0,979,1011,994,983,981,1019,958,993],
[1004,1021,0,1011,992,1014,996,1052,1004,1013],
[931,989,989,0,971,1028,958,995,1003,972],
[983,1006,1008,1029,0,1010,994,1017,1003,993],
[977,1017,986,972,990,0,1010,993,988,1002],
[1001,1019,1004,1042,1006,990,0,1020,988,1019],
[992,981,948,1005,983,1007,980,0,986,989],
[974,1042,996,997,997,1012,1012,1014,0,1016],
[1002,1007,987,1028,1007,998,981,1011,984,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 112, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1025,1043,1000,1039,1062,1025,1009,1010,1010],
[975,0,1032,976,1009,1015,997,988,1003,989],
[957,968,0,962,979,965,971,951,965,937],
[1000,1024,1038,0,998,1010,1017,999,1010,1017],
[961,991,1021,1002,0,1033,999,993,973,1004],
[938,985,1035,990,967,0,991,973,1003,990],
[975,1003,1029,983,1001,1009,0,965,976,1000],
[991,1012,1049,1001,1007,1027,1035,0,1016,977],
[990,997,1035,990,1027,997,1024,984,0,987],
[990,1011,1063,983,996,1010,1000,1023,1013,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 113, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,966,1002,965,1008,1012,981,998,995,1013],
[1034,0,1034,973,973,1038,1013,1007,993,1025],
[998,966,0,937,991,961,961,992,980,970],
[1035,1027,1063,0,1049,1030,1027,1008,1017,1000],
[992,1027,1009,951,0,1025,998,1041,1014,983],
[988,962,1039,970,975,0,961,985,992,958],
[1019,987,1039,973,1002,1039,0,995,1011,954],
[1002,993,1008,992,959,1015,1005,0,1018,988],
[1005,1007,1020,983,986,1008,989,982,0,962],
[987,975,1030,1000,1017,1042,1046,1012,1038,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 114, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1006,981,989,981,988,958,1022,1000,992],
[994,0,1008,1010,1047,995,1021,1036,1013,1002],
[1019,992,0,1002,1024,978,1008,1003,998,1026],
[1011,990,998,0,1031,983,1004,1020,1011,997],
[1019,953,976,969,0,962,960,1023,1000,987],
[1012,1005,1022,1017,1038,0,999,1031,1027,1018],
[1042,979,992,996,1040,1001,0,1059,1011,1000],
[978,964,997,980,977,969,941,0,975,962],
[1000,987,1002,989,1000,973,989,1025,0,987],
[1008,998,974,1003,1013,982,1000,1038,1013,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 115, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1006,1140,982,1142,1012,1156,1036,1016,1013],
[994,0,1061,911,1095,996,1048,967,1019,994],
[860,939,0,989,1096,1017,993,972,1043,909],
[1018,1089,1011,0,1054,1018,1017,941,1072,947],
[858,905,904,946,0,987,910,876,1013,897],
[988,1004,983,982,1013,0,939,930,1076,885],
[844,952,1007,983,1090,1061,0,1068,1099,943],
[964,1033,1028,1059,1124,1070,932,0,991,1021],
[984,981,957,928,987,924,901,1009,0,939],
[987,1006,1091,1053,1103,1115,1057,979,1061,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 116, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,982,983,989,956,990,972,995,987,930],
[1018,0,1011,992,1000,978,995,1012,1005,1000],
[1017,989,0,967,989,962,952,979,991,999],
[1011,1008,1033,0,1009,1007,966,1025,986,961],
[1044,1000,1011,991,0,993,966,996,1010,989],
[1010,1022,1038,993,1007,0,981,1025,1012,986],
[1028,1005,1048,1034,1034,1019,0,1046,1038,998],
[1005,988,1021,975,1004,975,954,0,1020,987],
[1013,995,1009,1014,990,988,962,980,0,979],
[1070,1000,1001,1039,1011,1014,1002,1013,1021,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 117, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1037,1041,999,1002,977,1001,964,1016,986],
[963,0,1024,972,1007,953,973,940,957,954],
[959,976,0,967,970,947,911,925,959,949],
[1001,1028,1033,0,1001,999,971,1005,1025,984],
[998,993,1030,999,0,1005,963,998,970,966],
[1023,1047,1053,1001,995,0,975,1033,1022,982],
[999,1027,1089,1029,1037,1025,0,1029,1030,1022],
[1036,1060,1075,995,1002,967,971,0,1018,981],
[984,1043,1041,975,1030,978,970,982,0,934],
[1014,1046,1051,1016,1034,1018,978,1019,1066,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 118, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,993,961,939,949,975,963,951,986,948],
[1007,0,1012,1008,991,966,969,944,1004,939],
[1039,988,0,975,952,908,973,955,1008,954],
[1061,992,1025,0,1022,987,958,1013,1018,984],
[1051,1009,1048,978,0,988,1008,998,1003,986],
[1025,1034,1092,1013,1012,0,992,1003,1006,957],
[1037,1031,1027,1042,992,1008,0,945,993,1007],
[1049,1056,1045,987,1002,997,1055,0,1000,1062],
[1014,996,992,982,997,994,1007,1000,0,1002],
[1052,1061,1046,1016,1014,1043,993,938,998,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 119, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,976,971,981,982,959,1007,971,956,960],
[1024,0,956,1006,986,966,1045,1022,989,1051],
[1029,1044,0,1021,974,1008,1021,1011,960,989],
[1019,994,979,0,968,1006,1038,1011,1008,981],
[1018,1014,1026,1032,0,1013,1020,1013,996,1011],
[1041,1034,992,994,987,0,1031,1036,1012,982],
[993,955,979,962,980,969,0,976,975,943],
[1029,978,989,989,987,964,1024,0,991,963],
[1044,1011,1040,992,1004,988,1025,1009,0,1034],
[1040,949,1011,1019,989,1018,1057,1037,966,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 120, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1011,1049,1011,998,1010,1037,1056,1056,959],
[989,0,976,945,949,965,992,1038,1008,977],
[951,1024,0,1006,972,1045,992,989,1044,1016],
[989,1055,994,0,957,1006,1030,988,1015,999],
[1002,1051,1028,1043,0,996,1005,1050,1060,1065],
[990,1035,955,994,1004,0,987,990,979,977],
[963,1008,1008,970,995,1013,0,993,1006,991],
[944,962,1011,1012,950,1010,1007,0,1002,1003],
[944,992,956,985,940,1021,994,998,0,995],
[1041,1023,984,1001,935,1023,1009,997,1005,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 121, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1036,1067,1021,1004,986,1033,1008,1001,1000],
[964,0,1033,964,989,993,986,978,1004,979],
[933,967,0,973,984,1003,972,969,957,966],
[979,1036,1027,0,1023,974,1011,1004,997,990],
[996,1011,1016,977,0,945,987,986,957,943],
[1014,1007,997,1026,1055,0,1003,1010,990,1012],
[967,1014,1028,989,1013,997,0,965,961,983],
[992,1022,1031,996,1014,990,1035,0,1010,1023],
[999,996,1043,1003,1043,1010,1039,990,0,1024],
[1000,1021,1034,1010,1057,988,1017,977,976,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 122, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1055,1005,1031,995,1011,1048,1005,1009,1046],
[945,0,975,1000,1036,985,1009,987,1018,989],
[995,1025,0,1039,1015,1018,1048,1037,1043,1009],
[969,1000,961,0,981,951,992,1031,992,976],
[1005,964,985,1019,0,996,1051,1016,986,1003],
[989,1015,982,1049,1004,0,1025,1019,1017,985],
[952,991,952,1008,949,975,0,987,1010,997],
[995,1013,963,969,984,981,1013,0,989,991],
[991,982,957,1008,1014,983,990,1011,0,972],
[954,1011,991,1024,997,1015,1003,1009,1028,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 123, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1037,919,964,929,986,977,970,989,1027],
[963,0,979,962,969,967,1014,1030,981,989],
[1081,1021,0,989,968,1000,1045,1020,987,989],
[1036,1038,1011,0,1070,1008,995,1038,1002,1041],
[1071,1031,1032,930,0,1019,1041,1024,1016,1009],
[1014,1033,1000,992,981,0,1015,1026,1002,1021],
[1023,986,955,1005,959,985,0,983,986,1000],
[1030,970,980,962,976,974,1017,0,990,1005],
[1011,1019,1013,998,984,998,1014,1010,0,997],
[973,1011,1011,959,991,979,1000,995,1003,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 124, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1011,994,983,993,998,1002,1022,988,1016],
[989,0,997,1010,956,995,978,1012,982,996],
[1006,1003,0,1026,960,992,986,1037,976,990],
[1017,990,974,0,928,989,980,1013,952,967],
[1007,1044,1040,1072,0,1028,999,1071,1008,1038],
[1002,1005,1008,1011,972,0,991,1006,956,995],
[998,1022,1014,1020,1001,1009,0,1026,959,969],
[978,988,963,987,929,994,974,0,959,979],
[1012,1018,1024,1048,992,1044,1041,1041,0,1008],
[984,1004,1010,1033,962,1005,1031,1021,992,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 125, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,902,1035,1097,1145,1169,1046,919,1043,1067],
[1098,0,1220,1046,1162,1168,1027,947,1238,1197],
[965,780,0,1009,1172,1016,1077,996,987,1001],
[903,954,991,0,924,824,889,955,990,947],
[855,838,828,1076,0,1022,780,1029,931,869],
[831,832,984,1176,978,0,860,916,925,886],
[954,973,923,1111,1220,1140,0,1105,1130,1121],
[1081,1053,1004,1045,971,1084,895,0,1312,1186],
[957,762,1013,1010,1069,1075,870,688,0,965],
[933,803,999,1053,1131,1114,879,814,1035,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 126, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1007,983,981,1070,1028,920,988,984,1033],
[993,0,1013,1027,994,952,1006,1018,978,1010],
[1017,987,0,993,1051,997,965,968,1044,1072],
[1019,973,1007,0,1085,1050,1006,993,1001,1050],
[930,1006,949,915,0,1011,927,1010,941,984],
[972,1048,1003,950,989,0,1012,953,979,1040],
[1080,994,1035,994,1073,988,0,976,1018,1041],
[1012,982,1032,1007,990,1047,1024,0,1017,1029],
[1016,1022,956,999,1059,1021,982,983,0,1010],
[967,990,928,950,1016,960,959,971,990,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 127, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,984,973,1034,1000,1066,961,997,1059,952],
[1016,0,978,996,1017,1010,978,1014,1028,975],
[1027,1022,0,1145,1003,1073,1073,977,1127,1070],
[966,1004,855,0,938,1014,955,997,986,972],
[1000,983,997,1062,0,1033,998,1027,1129,1010],
[934,990,927,986,967,0,933,988,1017,944],
[1039,1022,927,1045,1002,1067,0,992,1049,1007],
[1003,986,1023,1003,973,1012,1008,0,1069,967],
[941,972,873,1014,871,983,951,931,0,984],
[1048,1025,930,1028,990,1056,993,1033,1016,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 128, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,975,956,999,1003,964,957,976,996,973],
[1025,0,1004,1025,1027,998,1025,1042,991,1001],
[1044,996,0,1060,1049,1046,1040,1046,1024,1040],
[1001,975,940,0,974,986,964,1006,985,1011],
[997,973,951,1026,0,973,989,973,963,974],
[1036,1002,954,1014,1027,0,986,1009,1016,1007],
[1043,975,960,1036,1011,1014,0,987,995,983],
[1024,958,954,994,1027,991,1013,0,1011,993],
[1004,1009,976,1015,1037,984,1005,989,0,969],
[1027,999,960,989,1026,993,1017,1007,1031,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 129, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,966,996,992,982,962,992,1000,1001,1009],
[1034,0,1015,1017,1002,988,994,1009,1019,1023],
[1004,985,0,995,988,1019,1011,987,1013,1006],
[1008,983,1005,0,1007,1007,985,1038,998,1013],
[1018,998,1012,993,0,998,1047,1020,1006,1021],
[1038,1012,981,993,1002,0,1008,1022,1012,1018],
[1008,1006,989,1015,953,992,0,1028,970,1027],
[1000,991,1013,962,980,978,972,0,976,1004],
[999,981,987,1002,994,988,1030,1024,0,1001],
[991,977,994,987,979,982,973,996,999,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 130, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,978,1272,1032,1188,1055,1058,961,1025,1002],
[1022,0,1179,997,1102,1132,941,1057,1051,879],
[728,821,0,994,993,1105,644,777,1039,864],
[968,1003,1006,0,957,981,940,1057,965,854],
[812,898,1007,1043,0,992,780,881,893,858],
[945,868,895,1019,1008,0,892,898,880,852],
[942,1059,1356,1060,1220,1108,0,1036,1134,1160],
[1039,943,1223,943,1119,1102,964,0,1039,989],
[975,949,961,1035,1107,1120,866,961,0,1100],
[998,1121,1136,1146,1142,1148,840,1011,900,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 131, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1126,1169,888,1278,782,893,1275,1000,1025],
[874,0,1093,886,1151,774,954,1019,1027,830],
[831,907,0,971,1367,949,1009,1191,1063,936],
[1112,1114,1029,0,1192,858,938,1229,1222,977],
[722,849,633,808,0,770,634,842,1023,696],
[1218,1226,1051,1142,1230,0,953,1334,1022,959],
[1107,1046,991,1062,1366,1047,0,1217,1057,1038],
[725,981,809,771,1158,666,783,0,898,587],
[1000,973,937,778,977,978,943,1102,0,807],
[975,1170,1064,1023,1304,1041,962,1413,1193,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 132, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1025,1016,1009,1016,989,1001,999,1014,979],
[975,0,1006,968,994,947,1000,985,963,972],
[984,994,0,982,1011,968,1023,990,1004,977],
[991,1032,1018,0,1000,1000,1002,1011,1003,1007],
[984,1006,989,1000,0,952,989,991,972,980],
[1011,1053,1032,1000,1048,0,1048,1044,1018,994],
[999,1000,977,998,1011,952,0,1020,984,990],
[1001,1015,1010,989,1009,956,980,0,981,967],
[986,1037,996,997,1028,982,1016,1019,0,968],
[1021,1028,1023,993,1020,1006,1010,1033,1032,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 133, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1131,1077,947,1011,1082,1036,1122,1041,1049],
[869,0,924,880,1044,953,990,954,955,972],
[923,1076,0,975,1046,997,999,1049,921,1014],
[1053,1120,1025,0,1108,1043,990,1056,1046,1042],
[989,956,954,892,0,945,934,1042,900,961],
[918,1047,1003,957,1055,0,982,1005,974,1000],
[964,1010,1001,1010,1066,1018,0,1005,953,968],
[878,1046,951,944,958,995,995,0,961,997],
[959,1045,1079,954,1100,1026,1047,1039,0,1066],
[951,1028,986,958,1039,1000,1032,1003,934,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 134, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,993,1002,986,998,1028,1018,998,1070,1014],
[1007,0,943,991,1030,1009,1026,1024,1064,1025],
[998,1057,0,1001,1053,1015,1041,1019,1043,1032],
[1014,1009,999,0,1050,1023,1012,989,1034,1024],
[1002,970,947,950,0,987,988,1029,1038,990],
[972,991,985,977,1013,0,1040,980,1024,1021],
[982,974,959,988,1012,960,0,971,1025,1024],
[1002,976,981,1011,971,1020,1029,0,1023,999],
[930,936,957,966,962,976,975,977,0,970],
[986,975,968,976,1010,979,976,1001,1030,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 135, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1041,1039,992,1043,1013,1062,1008,1040,994],
[959,0,1045,958,1002,1003,1001,973,980,1012],
[961,955,0,996,976,956,986,957,958,960],
[1008,1042,1004,0,1018,1059,1083,971,1060,1008],
[957,998,1024,982,0,983,1059,968,1023,996],
[987,997,1044,941,1017,0,1026,979,931,974],
[938,999,1014,917,941,974,0,986,945,962],
[992,1027,1043,1029,1032,1021,1014,0,978,1000],
[960,1020,1042,940,977,1069,1055,1022,0,1014],
[1006,988,1040,992,1004,1026,1038,1000,986,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 136, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1024,982,977,1034,967,1026,960,999,1002],
[976,0,947,955,989,934,977,949,969,931],
[1018,1053,0,1000,1077,1016,1037,1035,990,992],
[1023,1045,1000,0,1074,1030,980,999,1008,1015],
[966,1011,923,926,0,946,979,936,971,999],
[1033,1066,984,970,1054,0,1010,994,977,1029],
[974,1023,963,1020,1021,990,0,988,985,1010],
[1040,1051,965,1001,1064,1006,1012,0,1019,1051],
[1001,1031,1010,992,1029,1023,1015,981,0,991],
[998,1069,1008,985,1001,971,990,949,1009,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 137, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1004,971,1023,943,1006,1004,949,1001,1002],
[996,0,964,1008,1004,988,981,980,992,1007],
[1029,1036,0,1025,970,1043,946,987,1011,1001],
[977,992,975,0,985,1019,960,946,969,979],
[1057,996,1030,1015,0,1036,1034,1014,1019,1035],
[994,1012,957,981,964,0,934,942,973,1010],
[996,1019,1054,1040,966,1066,0,1022,1018,1036],
[1051,1020,1013,1054,986,1058,978,0,1010,1027],
[999,1008,989,1031,981,1027,982,990,0,1004],
[998,993,999,1021,965,990,964,973,996,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 138, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,990,992,1011,985,1022,968,985,1020,967],
[1010,0,993,963,1027,1012,986,973,980,953],
[1008,1007,0,1009,963,1069,988,921,987,972],
[989,1037,991,0,990,983,988,939,962,982],
[1015,973,1037,1010,0,1072,979,1002,948,1030],
[978,988,931,1017,928,0,998,946,958,970],
[1032,1014,1012,1012,1021,1002,0,992,1010,979],
[1015,1027,1079,1061,998,1054,1008,0,1024,1026],
[980,1020,1013,1038,1052,1042,990,976,0,1031],
[1033,1047,1028,1018,970,1030,1021,974,969,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 139, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1013,980,1017,1010,1021,1049,1020,1025,1006],
[987,0,973,1036,1022,989,1022,969,1027,1029],
[1020,1027,0,996,1025,1027,1043,1024,1018,985],
[983,964,1004,0,1017,1034,993,973,1036,1009],
[990,978,975,983,0,990,991,958,1018,990],
[979,1011,973,966,1010,0,988,1007,1003,985],
[951,978,957,1007,1009,1012,0,971,1000,962],
[980,1031,976,1027,1042,993,1029,0,1049,1019],
[975,973,982,964,982,997,1000,951,0,982],
[994,971,1015,991,1010,1015,1038,981,1018,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 140, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1025,998,976,997,949,1053,954,1031,963],
[975,0,995,946,993,981,977,985,1060,940],
[1002,1005,0,983,979,975,1015,1050,1073,968],
[1024,1054,1017,0,1014,1032,1020,1067,1103,993],
[1003,1007,1021,986,0,1005,957,1043,1024,954],
[1051,1019,1025,968,995,0,981,994,1053,989],
[947,1023,985,980,1043,1019,0,992,1090,1005],
[1046,1015,950,933,957,1006,1008,0,1038,954],
[969,940,927,897,976,947,910,962,0,934],
[1037,1060,1032,1007,1046,1011,995,1046,1066,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 141, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,647,771,862,795,992,960,701,840,789],
[1353,0,1261,1239,986,1237,1309,1028,1224,1141],
[1229,739,0,1032,955,1013,1043,1083,1034,898],
[1138,761,968,0,945,1098,1095,898,1019,976],
[1205,1014,1045,1055,0,1104,1007,912,1007,984],
[1008,763,987,902,896,0,954,815,1057,795],
[1040,691,957,905,993,1046,0,852,939,810],
[1299,972,917,1102,1088,1185,1148,0,1115,958],
[1160,776,966,981,993,943,1061,885,0,936],
[1211,859,1102,1024,1016,1205,1190,1042,1064,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 142, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1019,1011,999,1049,1013,1033,1029,991,996],
[981,0,995,986,1006,1011,968,1008,986,951],
[989,1005,0,993,1009,992,998,1006,972,988],
[1001,1014,1007,0,1024,998,995,1030,981,1008],
[951,994,991,976,0,966,977,1017,953,963],
[987,989,1008,1002,1034,0,983,1015,979,988],
[967,1032,1002,1005,1023,1017,0,1015,991,990],
[971,992,994,970,983,985,985,0,941,994],
[1009,1014,1028,1019,1047,1021,1009,1059,0,964],
[1004,1049,1012,992,1037,1012,1010,1006,1036,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 143, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1002,973,972,947,1065,1009,1001,973,978],
[998,0,1024,940,1054,1043,1014,1021,1010,1009],
[1027,976,0,955,1005,1061,1003,1013,967,974],
[1028,1060,1045,0,1042,1092,1078,969,1010,1049],
[1053,946,995,958,0,991,1010,974,964,990],
[935,957,939,908,1009,0,937,994,912,966],
[991,986,997,922,990,1063,0,1004,980,1019],
[999,979,987,1031,1026,1006,996,0,936,1009],
[1027,990,1033,990,1036,1088,1020,1064,0,1022],
[1022,991,1026,951,1010,1034,981,991,978,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 144, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1116,1029,1085,998,1048,1005,1032,1077,1009],
[884,0,984,1040,975,1001,927,931,1014,957],
[971,1016,0,1071,1039,1043,1022,1077,1088,1078],
[915,960,929,0,948,985,936,998,970,992],
[1002,1025,961,1052,0,1044,980,992,1012,1014],
[952,999,957,1015,956,0,929,984,1003,959],
[995,1073,978,1064,1020,1071,0,1018,1030,1040],
[968,1069,923,1002,1008,1016,982,0,1010,1005],
[923,986,912,1030,988,997,970,990,0,983],
[991,1043,922,1008,986,1041,960,995,1017,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 145, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1013,995,1028,1013,986,1043,980,1010,1054],
[987,0,978,997,982,987,1036,978,984,1018],
[1005,1022,0,1022,990,1004,1008,965,959,1054],
[972,1003,978,0,980,1001,1007,984,991,988],
[987,1018,1010,1020,0,1015,1003,1000,1029,1041],
[1014,1013,996,999,985,0,1008,969,1049,1015],
[957,964,992,993,997,992,0,970,995,998],
[1020,1022,1035,1016,1000,1031,1030,0,999,1063],
[990,1016,1041,1009,971,951,1005,1001,0,1051],
[946,982,946,1012,959,985,1002,937,949,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 146, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1011,1082,1050,1043,1078,981,1062,1028,1038],
[989,0,1097,1088,1061,1089,1046,1023,1044,1041],
[918,903,0,955,962,985,898,939,924,932],
[950,912,1045,0,984,1029,953,980,970,1026],
[957,939,1038,1016,0,1051,973,989,1001,983],
[922,911,1015,971,949,0,920,947,947,925],
[1019,954,1102,1047,1027,1080,0,1001,1025,1043],
[938,977,1061,1020,1011,1053,999,0,1000,971],
[972,956,1076,1030,999,1053,975,1000,0,1062],
[962,959,1068,974,1017,1075,957,1029,938,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 147, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,944,991,1022,1020,1025,1024,1007,1001,1021],
[1056,0,1008,982,1036,1023,1071,1062,1042,1020],
[1009,992,0,971,1010,1043,1039,989,995,1015],
[978,1018,1029,0,1066,1047,1086,1041,1072,1043],
[980,964,990,934,0,979,1011,1014,988,996],
[975,977,957,953,1021,0,1038,965,1002,997],
[976,929,961,914,989,962,0,940,962,907],
[993,938,1011,959,986,1035,1060,0,1025,950],
[999,958,1005,928,1012,998,1038,975,0,973],
[979,980,985,957,1004,1003,1093,1050,1027,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 148, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1007,971,1015,1011,1013,1019,1027,1028,1048],
[993,0,947,952,998,1004,1020,1026,997,1038],
[1029,1053,0,1000,1050,1029,1044,1055,1044,1043],
[985,1048,1000,0,1010,1016,1044,1041,1047,1026],
[989,1002,950,990,0,981,990,1002,1012,1004],
[987,996,971,984,1019,0,1007,1034,1026,1039],
[981,980,956,956,1010,993,0,980,1029,990],
[973,974,945,959,998,966,1020,0,1005,1008],
[972,1003,956,953,988,974,971,995,0,1021],
[952,962,957,974,996,961,1010,992,979,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 149, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,952,1027,984,967,1016,920,972,1016,1019],
[1048,0,1027,1035,1013,1036,1044,988,1022,1024],
[973,973,0,951,984,1018,930,1007,1021,992],
[1016,965,1049,0,997,973,1006,1050,1064,1037],
[1033,987,1016,1003,0,1014,1026,1011,1002,1085],
[984,964,982,1027,986,0,973,1005,965,1024],
[1080,956,1070,994,974,1027,0,1076,1064,1018],
[1028,1012,993,950,989,995,924,0,1033,1031],
[984,978,979,936,998,1035,936,967,0,1028],
[981,976,1008,963,915,976,982,969,972,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 150, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1004,996,995,996,1025,1000,998,1007,970],
[996,0,985,1009,1003,1042,1010,972,1040,969],
[1004,1015,0,986,988,1034,1025,967,1009,1007],
[1005,991,1014,0,999,1048,1012,991,1027,1010],
[1004,997,1012,1001,0,1042,1011,968,1030,991],
[975,958,966,952,958,0,985,943,977,975],
[1000,990,975,988,989,1015,0,977,1000,991],
[1002,1028,1033,1009,1032,1057,1023,0,1025,973],
[993,960,991,973,970,1023,1000,975,0,983],
[1030,1031,993,990,1009,1025,1009,1027,1017,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 151, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1000,1009,1049,1018,997,1073,1043,1032,1059],
[1000,0,1010,1027,1034,985,1061,1017,1027,1017],
[991,990,0,997,1044,1052,1026,1046,1014,1041],
[951,973,1003,0,987,973,995,943,941,991],
[982,966,956,1013,0,983,1000,993,987,1011],
[1003,1015,948,1027,1017,0,1067,1012,993,1042],
[927,939,974,1005,1000,933,0,976,942,1007],
[957,983,954,1057,1007,988,1024,0,1040,1010],
[968,973,986,1059,1013,1007,1058,960,0,1024],
[941,983,959,1009,989,958,993,990,976,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 152, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1003,1010,1109,944,989,1037,1010,929,1056],
[997,0,1004,1073,1090,956,1084,977,1007,977],
[990,996,0,1017,1049,1067,1104,951,927,927],
[891,927,983,0,1094,959,1038,965,986,982],
[1056,910,951,906,0,1019,1165,926,1000,986],
[1011,1044,933,1041,981,0,1080,1073,1038,1021],
[963,916,896,962,835,920,0,964,935,879],
[990,1023,1049,1035,1074,927,1036,0,972,1003],
[1071,993,1073,1014,1000,962,1065,1028,0,1034],
[944,1023,1073,1018,1014,979,1121,997,966,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 153, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1002,953,990,972,1037,973,1002,993,1003],
[998,0,964,980,990,993,974,968,1002,981],
[1047,1036,0,1022,1004,1024,987,997,999,974],
[1010,1020,978,0,983,1009,968,982,1025,968],
[1028,1010,996,1017,0,1006,973,1011,1003,1010],
[963,1007,976,991,994,0,974,997,967,972],
[1027,1026,1013,1032,1027,1026,0,995,1036,1021],
[998,1032,1003,1018,989,1003,1005,0,975,1004],
[1007,998,1001,975,997,1033,964,1025,0,1002],
[997,1019,1026,1032,990,1028,979,996,998,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 154, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,982,991,1010,1009,970,1013,1021,964,1025],
[1018,0,1002,1062,1026,992,989,1007,1012,1029],
[1009,998,0,1028,953,983,983,1015,982,1031],
[990,938,972,0,1005,947,989,1003,969,999],
[991,974,1047,995,0,970,986,964,978,982],
[1030,1008,1017,1053,1030,0,1031,995,991,1018],
[987,1011,1017,1011,1014,969,0,982,975,1000],
[979,993,985,997,1036,1005,1018,0,969,997],
[1036,988,1018,1031,1022,1009,1025,1031,0,1013],
[975,971,969,1001,1018,982,1000,1003,987,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 155, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1134,1013,1155,990,1138,1025,838,1080,921],
[866,0,1082,1011,843,968,986,669,952,871],
[987,918,0,993,1038,936,886,729,996,868],
[845,989,1007,0,985,973,927,770,952,828],
[1010,1157,962,1015,0,1037,991,786,973,1072],
[862,1032,1064,1027,963,0,961,858,932,902],
[975,1014,1114,1073,1009,1039,0,825,1110,923],
[1162,1331,1271,1230,1214,1142,1175,0,1109,995],
[920,1048,1004,1048,1027,1068,890,891,0,1071],
[1079,1129,1132,1172,928,1098,1077,1005,929,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 156, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,964,974,954,1041,993,954,1068,964,1108],
[1036,0,1008,1019,1055,1035,931,1135,997,1155],
[1026,992,0,1051,1076,1028,977,1097,1010,1107],
[1046,981,949,0,1087,1031,1019,1069,976,1110],
[959,945,924,913,0,914,933,978,915,1025],
[1007,965,972,969,1086,0,959,1045,962,1030],
[1046,1069,1023,981,1067,1041,0,1071,1010,1162],
[932,865,903,931,1022,955,929,0,961,1023],
[1036,1003,990,1024,1085,1038,990,1039,0,1161],
[892,845,893,890,975,970,838,977,839,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 157, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1012,976,1019,994,957,1022,983,1015,1011],
[988,0,972,983,976,956,987,995,999,996],
[1024,1028,0,1019,1013,980,989,1010,1011,1011],
[981,1017,981,0,1018,977,985,963,984,996],
[1006,1024,987,982,0,1005,1011,1003,996,1042],
[1043,1044,1020,1023,995,0,1031,1015,1012,1029],
[978,1013,1011,1015,989,969,0,957,981,1031],
[1017,1005,990,1037,997,985,1043,0,1037,1041],
[985,1001,989,1016,1004,988,1019,963,0,998],
[989,1004,989,1004,958,971,969,959,1002,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 158, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1018,1049,981,1020,982,1023,1005,1004,971],
[982,0,976,1020,975,928,1015,1009,990,976],
[951,1024,0,1012,981,979,1038,1008,1013,978],
[1019,980,988,0,995,955,1050,1000,1016,987],
[980,1025,1019,1005,0,973,1024,1005,1021,974],
[1018,1072,1021,1045,1027,0,1048,1030,1054,1000],
[977,985,962,950,976,952,0,989,955,971],
[995,991,992,1000,995,970,1011,0,983,987],
[996,1010,987,984,979,946,1045,1017,0,979],
[1029,1024,1022,1013,1026,1000,1029,1013,1021,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 159, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1001,997,962,1013,970,1026,1015,984,990],
[999,0,1025,989,1006,990,1016,1004,985,1003],
[1003,975,0,993,1001,971,1031,1004,998,1029],
[1038,1011,1007,0,1030,988,1045,974,1000,1035],
[987,994,999,970,0,968,967,981,968,1006],
[1030,1010,1029,1012,1032,0,1038,995,985,1031],
[974,984,969,955,1033,962,0,973,950,989],
[985,996,996,1026,1019,1005,1027,0,981,1020],
[1016,1015,1002,1000,1032,1015,1050,1019,0,1026],
[1010,997,971,965,994,969,1011,980,974,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 160, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,992,1011,1017,977,980,991,1011,1002,970],
[1008,0,1002,1022,962,1011,1099,1050,1043,1046],
[989,998,0,1006,942,933,1039,1017,958,983],
[983,978,994,0,957,944,1042,1055,1001,984],
[1023,1038,1058,1043,0,990,1069,1062,1017,1040],
[1020,989,1067,1056,1010,0,1048,1040,1004,1022],
[1009,901,961,958,931,952,0,996,977,1003],
[989,950,983,945,938,960,1004,0,940,995],
[998,957,1042,999,983,996,1023,1060,0,1027],
[1030,954,1017,1016,960,978,997,1005,973,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 161, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1024,984,994,986,1001,1023,1024,967,999],
[976,0,988,980,989,1007,995,1023,998,991],
[1016,1012,0,987,995,1002,1018,1012,997,994],
[1006,1020,1013,0,1038,999,1007,1013,1018,1012],
[1014,1011,1005,962,0,994,1022,1020,1022,986],
[999,993,998,1001,1006,0,1019,1026,1000,997],
[977,1005,982,993,978,981,0,1001,1010,975],
[976,977,988,987,980,974,999,0,978,983],
[1033,1002,1003,982,978,1000,990,1022,0,988],
[1001,1009,1006,988,1014,1003,1025,1017,1012,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 162, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,990,1028,1009,1052,973,1047,1088,1049,1020],
[1010,0,996,1049,1026,1031,1100,1021,1039,1016],
[972,1004,0,1011,930,1065,1055,1050,970,1001],
[991,951,989,0,967,1000,1014,989,999,958],
[948,974,1070,1033,0,962,1016,962,962,921],
[1027,969,935,1000,1038,0,979,1098,996,947],
[953,900,945,986,984,1021,0,932,952,1030],
[912,979,950,1011,1038,902,1068,0,1019,986],
[951,961,1030,1001,1038,1004,1048,981,0,983],
[980,984,999,1042,1079,1053,970,1014,1017,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 163, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,841,1041,949,1084,929,1006,859,995,1095],
[1159,0,1146,997,959,936,1051,851,1085,1193],
[959,854,0,786,819,845,815,912,804,959],
[1051,1003,1214,0,1002,905,956,1026,1062,1162],
[916,1041,1181,998,0,826,1058,829,1009,1058],
[1071,1064,1155,1095,1174,0,1109,927,1158,1169],
[994,949,1185,1044,942,891,0,916,920,998],
[1141,1149,1088,974,1171,1073,1084,0,970,1158],
[1005,915,1196,938,991,842,1080,1030,0,1118],
[905,807,1041,838,942,831,1002,842,882,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 164, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,952,976,988,1011,991,982,971,911,1049],
[1048,0,955,967,1046,1036,1014,1001,920,1016],
[1024,1045,0,971,1080,992,1015,972,946,1035],
[1012,1033,1029,0,976,997,917,956,930,1069],
[989,954,920,1024,0,1012,943,981,862,1040],
[1009,964,1008,1003,988,0,981,958,890,1077],
[1018,986,985,1083,1057,1019,0,958,943,1119],
[1029,999,1028,1044,1019,1042,1042,0,1021,1004],
[1089,1080,1054,1070,1138,1110,1057,979,0,1046],
[951,984,965,931,960,923,881,996,954,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 165, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1023,1022,1054,986,999,995,996,981,1004],
[977,0,1020,1037,1011,987,979,1016,1008,977],
[978,980,0,1005,981,973,980,959,1008,973],
[946,963,995,0,960,965,980,945,946,969],
[1014,989,1019,1040,0,1017,988,983,1036,991],
[1001,1013,1027,1035,983,0,1003,1007,1025,992],
[1005,1021,1020,1020,1012,997,0,998,986,1002],
[1004,984,1041,1055,1017,993,1002,0,989,988],
[1019,992,992,1054,964,975,1014,1011,0,974],
[996,1023,1027,1031,1009,1008,998,1012,1026,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 166, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,991,1021,1048,1069,1066,1001,1023,1026,993],
[1009,0,981,1014,1004,1040,983,989,993,976],
[979,1019,0,976,1038,1053,1009,990,992,970],
[952,986,1024,0,984,1022,947,971,1026,979],
[931,996,962,1016,0,1004,982,1041,995,982],
[934,960,947,978,996,0,929,938,914,956],
[999,1017,991,1053,1018,1071,0,973,1011,978],
[977,1011,1010,1029,959,1062,1027,0,1026,1008],
[974,1007,1008,974,1005,1086,989,974,0,957],
[1007,1024,1030,1021,1018,1044,1022,992,1043,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 167, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,961,1013,1061,941,1061,968,1029,983,996],
[1039,0,1042,1101,1012,1022,1012,1037,1040,993],
[987,958,0,1047,978,1018,952,994,999,942],
[939,899,953,0,913,983,889,974,970,912],
[1059,988,1022,1087,0,1062,1025,1027,1049,946],
[939,978,982,1017,938,0,927,991,952,932],
[1032,988,1048,1111,975,1073,0,1048,995,1019],
[971,963,1006,1026,973,1009,952,0,947,966],
[1017,960,1001,1030,951,1048,1005,1053,0,975],
[1004,1007,1058,1088,1054,1068,981,1034,1025,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 168, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1022,1031,996,1049,1042,1050,1026,988,1037],
[978,0,1023,1013,986,1018,999,985,973,959],
[969,977,0,1014,995,981,984,995,949,996],
[1004,987,986,0,999,1058,997,1000,1008,1016],
[951,1014,1005,1001,0,1026,974,978,986,1038],
[958,982,1019,942,974,0,995,1007,992,1040],
[950,1001,1016,1003,1026,1005,0,976,1011,1001],
[974,1015,1005,1000,1022,993,1024,0,1000,989],
[1012,1027,1051,992,1014,1008,989,1000,0,1015],
[963,1041,1004,984,962,960,999,1011,985,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 169, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,981,977,956,931,967,967,936,972,977],
[1019,0,1003,965,980,959,943,957,983,992],
[1023,997,0,944,988,975,970,959,966,976],
[1044,1035,1056,0,1013,1038,1012,999,1006,1025],
[1069,1020,1012,987,0,1030,991,989,1010,1002],
[1033,1041,1025,962,970,0,1015,981,987,1007],
[1033,1057,1030,988,1009,985,0,1015,1009,983],
[1064,1043,1041,1001,1011,1019,985,0,965,1000],
[1028,1017,1034,994,990,1013,991,1035,0,985],
[1023,1008,1024,975,998,993,1017,1000,1015,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 170, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,988,1012,1023,1011,1001,1012,999,1006,990],
[1012,0,1000,957,995,959,1058,976,1009,1001],
[988,1000,0,980,991,959,982,1009,990,968],
[977,1043,1020,0,938,982,1016,964,1014,915],
[989,1005,1009,1062,0,1019,1040,1037,1058,987],
[999,1041,1041,1018,981,0,1019,1050,1037,1027],
[988,942,1018,984,960,981,0,979,1000,934],
[1001,1024,991,1036,963,950,1021,0,1015,1006],
[994,991,1010,986,942,963,1000,985,0,957],
[1010,999,1032,1085,1013,973,1066,994,1043,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 171, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1067,1059,1036,964,1001,993,998,1030,1037],
[933,0,1014,995,945,1018,1011,966,1029,1016],
[941,986,0,1037,984,992,996,919,1007,1018],
[964,1005,963,0,1008,958,974,916,964,1010],
[1036,1055,1016,992,0,1015,997,948,1023,1048],
[999,982,1008,1042,985,0,991,983,1004,1010],
[1007,989,1004,1026,1003,1009,0,1020,1021,1030],
[1002,1034,1081,1084,1052,1017,980,0,1017,1091],
[970,971,993,1036,977,996,979,983,0,983],
[963,984,982,990,952,990,970,909,1017,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 172, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1002,1018,981,1007,1027,963,1008,1000,960],
[998,0,999,988,1044,990,1019,1006,997,970],
[982,1001,0,977,981,996,946,1011,967,942],
[1019,1012,1023,0,1007,1010,979,1037,1025,1026],
[993,956,1019,993,0,1020,963,1015,989,977],
[973,1010,1004,990,980,0,990,1013,977,998],
[1037,981,1054,1021,1037,1010,0,990,996,993],
[992,994,989,963,985,987,1010,0,996,986],
[1000,1003,1033,975,1011,1023,1004,1004,0,972],
[1040,1030,1058,974,1023,1002,1007,1014,1028,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 173, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,983,991,1020,986,973,963,1020,960,1038],
[1017,0,1016,1011,984,984,981,1012,983,1012],
[1009,984,0,1013,969,967,971,1002,988,1041],
[980,989,987,0,976,953,976,985,996,1025],
[1014,1016,1031,1024,0,1029,1002,1031,991,1053],
[1027,1016,1033,1047,971,0,1005,1044,1026,1064],
[1037,1019,1029,1024,998,995,0,1027,982,1046],
[980,988,998,1015,969,956,973,0,965,994],
[1040,1017,1012,1004,1009,974,1018,1035,0,1035],
[962,988,959,975,947,936,954,1006,965,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 174, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,933,974,950,987,978,1011,948,1031,1016],
[1067,0,934,991,1027,954,1041,938,993,1012],
[1026,1066,0,1016,1000,1053,1087,985,1047,980],
[1050,1009,984,0,999,974,997,990,1068,975],
[1013,973,1000,1001,0,1032,1017,1067,1042,973],
[1022,1046,947,1026,968,0,1045,1015,1055,994],
[989,959,913,1003,983,955,0,954,1013,935],
[1052,1062,1015,1010,933,985,1046,0,1044,1004],
[969,1007,953,932,958,945,987,956,0,943],
[984,988,1020,1025,1027,1006,1065,996,1057,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 175, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,933,963,982,918,1013,952,1019,980,993],
[1067,0,972,1009,977,1024,982,949,985,1016],
[1037,1028,0,1010,1017,1026,987,957,969,1048],
[1018,991,990,0,967,1007,977,969,1007,1066],
[1082,1023,983,1033,0,1082,1001,1014,1001,1073],
[987,976,974,993,918,0,985,938,994,978],
[1048,1018,1013,1023,999,1015,0,1023,996,1070],
[981,1051,1043,1031,986,1062,977,0,995,1055],
[1020,1015,1031,993,999,1006,1004,1005,0,1068],
[1007,984,952,934,927,1022,930,945,932,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 176, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,951,988,1049,986,1002,974,994,1002,992],
[1049,0,1054,1051,990,1037,1021,1019,1012,1023],
[1012,946,0,1029,976,1020,990,1001,1013,1000],
[951,949,971,0,987,971,953,954,976,961],
[1014,1010,1024,1013,0,1021,1020,1019,1046,989],
[998,963,980,1029,979,0,1013,963,987,968],
[1026,979,1010,1047,980,987,0,1016,1010,1026],
[1006,981,999,1046,981,1037,984,0,1004,1016],
[998,988,987,1024,954,1013,990,996,0,982],
[1008,977,1000,1039,1011,1032,974,984,1018,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 177, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,903,973,966,918,938,974,955,1070,1003],
[1097,0,988,1005,1044,1034,1044,1012,1092,1021],
[1027,1012,0,1009,1034,1008,997,983,976,1024],
[1034,995,991,0,1045,1043,1006,989,1038,1086],
[1082,956,966,955,0,979,1005,1020,1021,1032],
[1062,966,992,957,1021,0,1023,1008,1021,1017],
[1026,956,1003,994,995,977,0,1037,992,1052],
[1045,988,1017,1011,980,992,963,0,1007,1066],
[930,908,1024,962,979,979,1008,993,0,1061],
[997,979,976,914,968,983,948,934,939,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 178, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,932,924,1006,975,960,1028,1002,966,996],
[1068,0,984,1023,1027,987,1034,980,1064,1014],
[1076,1016,0,1012,1024,989,987,991,1022,961],
[994,977,988,0,1010,979,1005,988,1019,971],
[1025,973,976,990,0,961,1031,996,1004,990],
[1040,1013,1011,1021,1039,0,1041,1026,1000,990],
[972,966,1013,995,969,959,0,947,972,962],
[998,1020,1009,1012,1004,974,1053,0,1047,1010],
[1034,936,978,981,996,1000,1028,953,0,977],
[1004,986,1039,1029,1010,1010,1038,990,1023,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 179, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1011,1027,1027,984,1010,1031,992,1016,1007],
[989,0,1010,1009,986,1006,1018,984,1044,997],
[973,990,0,1010,957,999,1004,982,1000,974],
[973,991,990,0,967,994,1003,968,993,974],
[1016,1014,1043,1033,0,1000,1028,1010,1047,1030],
[990,994,1001,1006,1000,0,1014,999,1014,997],
[969,982,996,997,972,986,0,980,1022,970],
[1008,1016,1018,1032,990,1001,1020,0,1011,1010],
[984,956,1000,1007,953,986,978,989,0,976],
[993,1003,1026,1026,970,1003,1030,990,1024,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 180, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,962,987,979,990,999,989,958,966,1015],
[1038,0,1005,995,1054,1036,1006,1013,1035,1016],
[1013,995,0,1007,1006,1027,989,1017,1001,995],
[1021,1005,993,0,1011,1011,1045,1042,1008,1052],
[1010,946,994,989,0,992,944,999,987,992],
[1001,964,973,989,1008,0,964,969,1010,993],
[1011,994,1011,955,1056,1036,0,992,1005,991],
[1042,987,983,958,1001,1031,1008,0,1032,998],
[1034,965,999,992,1013,990,995,968,0,995],
[985,984,1005,948,1008,1007,1009,1002,1005,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 181, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1205,1144,983,1154,1190,1129,1107,938,1208],
[795,0,1118,892,1085,998,1003,930,940,784],
[856,882,0,929,874,990,953,961,777,909],
[1017,1108,1071,0,1022,1136,1090,1029,938,1021],
[846,915,1126,978,0,907,952,1011,662,886],
[810,1002,1010,864,1093,0,1060,993,1038,974],
[871,997,1047,910,1048,940,0,1118,920,794],
[893,1070,1039,971,989,1007,882,0,913,1023],
[1062,1060,1223,1062,1338,962,1080,1087,0,970],
[792,1216,1091,979,1114,1026,1206,977,1030,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 182, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1035,989,1008,1023,1082,1075,1024,1027,1007],
[965,0,994,982,1009,1009,1019,974,965,950],
[1011,1006,0,1025,1099,1021,1053,970,994,1046],
[992,1018,975,0,1024,1010,1033,990,987,965],
[977,991,901,976,0,1031,1060,971,943,975],
[918,991,979,990,969,0,992,970,908,935],
[925,981,947,967,940,1008,0,920,961,975],
[976,1026,1030,1010,1029,1030,1080,0,1002,993],
[973,1035,1006,1013,1057,1092,1039,998,0,998],
[993,1050,954,1035,1025,1065,1025,1007,1002,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 183, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,949,973,957,965,944,932,942,978,989],
[1051,0,1019,1018,1045,956,1015,1031,1070,1018],
[1027,981,0,967,1002,997,987,1009,1024,1027],
[1043,982,1033,0,1023,997,991,1058,1041,1066],
[1035,955,998,977,0,1032,989,988,1042,980],
[1056,1044,1003,1003,968,0,1006,1004,1041,1012],
[1068,985,1013,1009,1011,994,0,1007,1026,1033],
[1058,969,991,942,1012,996,993,0,1018,1023],
[1022,930,976,959,958,959,974,982,0,979],
[1011,982,973,934,1020,988,967,977,1021,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 184, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1026,1036,971,968,1006,998,985,1028,1019],
[974,0,984,944,967,1014,996,947,988,923],
[964,1016,0,962,1009,977,955,977,977,921],
[1029,1056,1038,0,1028,1039,1005,1003,1035,975],
[1032,1033,991,972,0,1030,1028,967,991,959],
[994,986,1023,961,970,0,963,957,1005,958],
[1002,1004,1045,995,972,1037,0,983,1033,984],
[1015,1053,1023,997,1033,1043,1017,0,1010,1013],
[972,1012,1023,965,1009,995,967,990,0,969],
[981,1077,1079,1025,1041,1042,1016,987,1031,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 185, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,990,1028,973,1014,983,973,1021,1010,996],
[1010,0,1045,1020,1013,997,972,1028,1068,994],
[972,955,0,981,1008,947,945,1024,1052,988],
[1027,980,1019,0,996,999,1041,1040,1076,977],
[986,987,992,1004,0,978,949,984,1007,980],
[1017,1003,1053,1001,1022,0,958,1052,1022,990],
[1027,1028,1055,959,1051,1042,0,1071,1032,1040],
[979,972,976,960,1016,948,929,0,1013,959],
[990,932,948,924,993,978,968,987,0,924],
[1004,1006,1012,1023,1020,1010,960,1041,1076,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 186, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1003,955,1020,992,993,984,996,1007,1007],
[997,0,981,990,973,1013,972,1013,958,1007],
[1045,1019,0,1022,991,1002,1009,1013,1012,1011],
[980,1010,978,0,1003,996,979,998,997,983],
[1008,1027,1009,997,0,1017,965,1041,976,996],
[1007,987,998,1004,983,0,1021,1021,983,1014],
[1016,1028,991,1021,1035,979,0,1039,1015,1012],
[1004,987,987,1002,959,979,961,0,976,998],
[993,1042,988,1003,1024,1017,985,1024,0,1023],
[993,993,989,1017,1004,986,988,1002,977,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 187, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1038,1049,1084,1033,1046,1015,1035,998,1011],
[962,0,994,1018,995,1006,1015,994,985,986],
[951,1006,0,1027,983,1020,981,973,968,986],
[916,982,973,0,970,1008,940,1007,968,975],
[967,1005,1017,1030,0,1003,968,995,1002,1013],
[954,994,980,992,997,0,994,1000,972,1000],
[985,985,1019,1060,1032,1006,0,1011,983,1002],
[965,1006,1027,993,1005,1000,989,0,950,955],
[1002,1015,1032,1032,998,1028,1017,1050,0,1015],
[989,1014,1014,1025,987,1000,998,1045,985,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 188, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,981,999,963,955,1026,1022,1047,1032,1021],
[1019,0,1003,996,1037,988,1009,1016,1037,1011],
[1001,997,0,989,1005,997,1001,1020,1025,1002],
[1037,1004,1011,0,998,1004,994,1019,1013,998],
[1045,963,995,1002,0,988,1012,1050,980,1023],
[974,1012,1003,996,1012,0,987,1029,1011,1020],
[978,991,999,1006,988,1013,0,1032,1027,1015],
[953,984,980,981,950,971,968,0,1017,959],
[968,963,975,987,1020,989,973,983,0,975],
[979,989,998,1002,977,980,985,1041,1025,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 189, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1040,1037,965,1036,984,973,1001,992,1046],
[960,0,996,952,1017,993,967,983,1005,999],
[963,1004,0,998,1033,982,1024,996,976,1001],
[1035,1048,1002,0,1018,1011,987,990,1021,1045],
[964,983,967,982,0,960,936,1029,991,1010],
[1016,1007,1018,989,1040,0,995,1033,983,1041],
[1027,1033,976,1013,1064,1005,0,1009,981,1048],
[999,1017,1004,1010,971,967,991,0,980,1082],
[1008,995,1024,979,1009,1017,1019,1020,0,1014],
[954,1001,999,955,990,959,952,918,986,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 190, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1002,1073,1040,1041,1042,1015,1018,943,1043],
[998,0,1081,1030,1056,998,1017,944,904,984],
[927,919,0,977,941,1021,1011,990,1015,951],
[960,970,1023,0,913,998,1000,896,917,919],
[959,944,1059,1087,0,1083,1037,1036,1098,1050],
[958,1002,979,1002,917,0,971,942,914,904],
[985,983,989,1000,963,1029,0,956,1017,987],
[982,1056,1010,1104,964,1058,1044,0,1005,1088],
[1057,1096,985,1083,902,1086,983,995,0,1024],
[957,1016,1049,1081,950,1096,1013,912,976,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 191, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,971,987,947,1008,961,960,963,968,964],
[1029,0,962,998,1035,1017,999,1035,1017,955],
[1013,1038,0,990,1061,1039,996,1028,1059,995],
[1053,1002,1010,0,1019,1031,992,1005,1019,1034],
[992,965,939,981,0,1031,998,960,985,910],
[1039,983,961,969,969,0,907,999,990,979],
[1040,1001,1004,1008,1002,1093,0,973,1048,1015],
[1037,965,972,995,1040,1001,1027,0,991,991],
[1032,983,941,981,1015,1010,952,1009,0,1013],
[1036,1045,1005,966,1090,1021,985,1009,987,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 192, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,984,988,993,1020,1010,957,970,986,982],
[1016,0,1008,1005,1010,1019,984,999,1023,1007],
[1012,992,0,990,1027,1045,989,986,1032,1002],
[1007,995,1010,0,1027,1038,989,1021,1012,1001],
[980,990,973,973,0,1052,957,1000,1007,998],
[990,981,955,962,948,0,963,971,995,1008],
[1043,1016,1011,1011,1043,1037,0,954,1037,989],
[1030,1001,1014,979,1000,1029,1046,0,1027,993],
[1014,977,968,988,993,1005,963,973,0,968],
[1018,993,998,999,1002,992,1011,1007,1032,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 193, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,964,983,976,1005,1035,1015,1010,1009,1012],
[1036,0,1007,999,985,1043,1042,1065,1011,991],
[1017,993,0,1016,1007,1053,1029,1043,1041,1009],
[1024,1001,984,0,1004,1042,1027,1014,990,976],
[995,1015,993,996,0,1047,1057,1053,1030,1033],
[965,957,947,958,953,0,1007,987,989,953],
[985,958,971,973,943,993,0,987,975,983],
[990,935,957,986,947,1013,1013,0,1000,969],
[991,989,959,1010,970,1011,1025,1000,0,978],
[988,1009,991,1024,967,1047,1017,1031,1022,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 194, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1021,973,1022,996,1013,946,982,976,973],
[979,0,979,1025,984,961,986,978,954,995],
[1027,1021,0,1055,1028,1023,993,972,989,1033],
[978,975,945,0,953,960,974,947,938,952],
[1004,1016,972,1047,0,1007,998,1000,979,1018],
[987,1039,977,1040,993,0,973,988,979,1037],
[1054,1014,1007,1026,1002,1027,0,988,998,1014],
[1018,1022,1028,1053,1000,1012,1012,0,1011,998],
[1024,1046,1011,1062,1021,1021,1002,989,0,1037],
[1027,1005,967,1048,982,963,986,1002,963,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 195, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,917,944,937,1005,953,910,990,940,1027],
[1083,0,994,981,1055,995,970,1053,1002,989],
[1056,1006,0,1009,1028,1061,1054,1089,989,990],
[1063,1019,991,0,1054,1070,936,973,925,997],
[995,945,972,946,0,983,946,1011,934,928],
[1047,1005,939,930,1017,0,966,981,1000,992],
[1090,1030,946,1064,1054,1034,0,1094,995,1027],
[1010,947,911,1027,989,1019,906,0,975,889],
[1060,998,1011,1075,1066,1000,1005,1025,0,969],
[973,1011,1010,1003,1072,1008,973,1111,1031,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 196, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1013,974,993,982,1003,998,977,1001,998],
[987,0,964,1003,993,1062,987,986,1026,981],
[1026,1036,0,984,1005,1026,1048,1003,1014,984],
[1007,997,1016,0,1003,1030,1018,982,1004,996],
[1018,1007,995,997,0,1006,1026,1014,990,973],
[997,938,974,970,994,0,1006,1004,998,972],
[1002,1013,952,982,974,994,0,986,1004,957],
[1023,1014,997,1018,986,996,1014,0,1039,1012],
[999,974,986,996,1010,1002,996,961,0,987],
[1002,1019,1016,1004,1027,1028,1043,988,1013,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 197, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1011,1036,993,1014,1006,1006,1015,977,991],
[989,0,1027,1019,1045,998,1035,992,978,966],
[964,973,0,949,1022,1010,960,999,980,968],
[1007,981,1051,0,990,1005,1018,1036,1028,1018],
[986,955,978,1010,0,971,952,1009,1000,973],
[994,1002,990,995,1029,0,986,988,983,1003],
[994,965,1040,982,1048,1014,0,1035,1032,981],
[985,1008,1001,964,991,1012,965,0,987,983],
[1023,1022,1020,972,1000,1017,968,1013,0,1009],
[1009,1034,1032,982,1027,997,1019,1017,991,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 198, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1015,996,1030,997,1006,986,974,984,984],
[985,0,1004,1014,991,988,971,987,1007,991],
[1004,996,0,1030,1031,1001,1002,1022,1004,999],
[970,986,970,0,996,976,986,987,971,979],
[1003,1009,969,1004,0,996,1005,985,967,984],
[994,1012,999,1024,1004,0,994,1001,1004,1006],
[1014,1029,998,1014,995,1006,0,1003,1026,992],
[1026,1013,978,1013,1015,999,997,0,1002,1008],
[1016,993,996,1029,1033,996,974,998,0,1011],
[1016,1009,1001,1021,1016,994,1008,992,989,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 199, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1016,1010,1044,1033,999,992,1005,980,1020],
[984,0,1002,1021,1037,1003,994,994,1009,1044],
[990,998,0,1016,1020,999,990,1011,987,1008],
[956,979,984,0,1017,987,988,965,978,1001],
[967,963,980,983,0,994,981,980,987,1014],
[1001,997,1001,1013,1006,0,1014,968,1017,1014],
[1008,1006,1010,1012,1019,986,0,1015,1016,1039],
[995,1006,989,1035,1020,1032,985,0,993,1039],
[1020,991,1013,1022,1013,983,984,1007,0,1042],
[980,956,992,999,986,986,961,961,958,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2000, 200, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/mebbd/mebbd_10_2000.csv", index=False, header=False)