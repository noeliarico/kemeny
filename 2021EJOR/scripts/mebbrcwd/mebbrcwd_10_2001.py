
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg
from kemeny import sc

rep = 3
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,1026,1050,1044,1005,955,1001,1018,1083,1004],
[975,0,1025,943,931,974,968,1047,1037,1012],
[951,976,0,923,1011,931,857,936,1030,987],
[957,1058,1078,0,965,1000,996,1028,1091,963],
[996,1070,990,1036,0,1000,1048,1028,1096,1017],
[1046,1027,1070,1001,1001,0,975,1031,1021,984],
[1000,1033,1144,1005,953,1026,0,973,982,1044],
[983,954,1065,973,973,970,1028,0,1024,1039],
[918,964,971,910,905,980,1019,977,0,920],
[997,989,1014,1038,984,1017,957,962,1081,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 1, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,953,980,973,1004,989,975,954,978,988],
[1048,0,986,1006,1015,1011,1033,1020,1019,1035],
[1021,1015,0,977,1012,994,993,970,979,1007],
[1028,995,1024,0,1003,1028,1000,992,1014,1019],
[997,986,989,998,0,969,984,973,966,993],
[1012,990,1007,973,1032,0,1007,976,1001,1022],
[1026,968,1008,1001,1017,994,0,1013,991,1018],
[1047,981,1031,1009,1028,1025,988,0,969,998],
[1023,982,1022,987,1035,1000,1010,1032,0,1014],
[1013,966,994,982,1008,979,983,1003,987,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 2, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,825,1048,1196,1118,1016,1136,1037,719,1229],
[1176,0,728,1268,1076,1314,997,1102,1014,1390],
[953,1273,0,1083,1160,1261,1231,792,1193,1348],
[805,733,918,0,1015,807,1118,929,962,1132],
[883,925,841,986,0,1034,1266,1153,892,1248],
[985,687,740,1194,967,0,936,1025,1195,996],
[865,1004,770,883,735,1065,0,1070,819,1219],
[964,899,1209,1072,848,976,931,0,1117,1218],
[1282,987,808,1039,1109,806,1182,884,0,885],
[772,611,653,869,753,1005,782,783,1116,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 3, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1015,1027,1000,984,1011,1025,1007,1015,990],
[986,0,1013,1026,1024,998,1015,1031,1008,1002],
[974,988,0,1020,1005,987,1001,1022,1018,974],
[1001,975,981,0,1016,982,998,1025,993,997],
[1017,977,996,985,0,962,1024,993,997,998],
[990,1003,1014,1019,1039,0,1013,1048,1013,1009],
[976,986,1000,1003,977,988,0,1011,962,978],
[994,970,979,976,1008,953,990,0,1003,957],
[986,993,983,1008,1004,988,1039,998,0,1010],
[1011,999,1027,1004,1003,992,1023,1044,991,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 4, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1014,1032,1039,1013,995,1006,1003,954,1033],
[987,0,1042,1010,985,978,1008,1012,990,1014],
[969,959,0,988,964,948,1001,898,974,965],
[962,991,1013,0,957,982,1001,1007,943,1001],
[988,1016,1037,1044,0,1024,1013,955,979,1054],
[1006,1023,1053,1019,977,0,1078,985,979,1012],
[995,993,1000,1000,988,923,0,985,999,985],
[998,989,1103,994,1046,1016,1016,0,1001,1058],
[1047,1011,1027,1058,1022,1022,1002,1000,0,1028],
[968,987,1036,1000,947,989,1016,943,973,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 5, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,957,1008,1021,1065,1011,1022,1039,1045,982],
[1044,0,1014,1006,1045,1045,1029,1059,1034,997],
[993,987,0,1015,1054,1046,988,999,1014,1003],
[980,995,986,0,1010,977,1031,1034,999,1058],
[936,956,947,991,0,962,1024,1007,1024,982],
[990,956,955,1024,1039,0,984,1004,993,979],
[979,972,1013,970,977,1017,0,1012,992,1006],
[962,942,1002,967,994,997,989,0,1006,1012],
[956,967,987,1002,977,1008,1009,995,0,1028],
[1019,1004,998,943,1019,1022,995,989,973,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 6, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1015,985,987,1013,948,942,989,984,946],
[986,0,964,988,1016,1000,993,1047,963,971],
[1016,1037,0,997,1037,1021,984,1053,960,954],
[1014,1013,1004,0,1020,993,1012,1071,980,997],
[988,985,964,981,0,984,1001,1015,950,973],
[1053,1001,980,1008,1017,0,1002,1047,973,982],
[1059,1008,1017,989,1000,999,0,1044,971,1018],
[1012,954,948,930,986,954,957,0,939,971],
[1017,1038,1041,1021,1051,1028,1030,1062,0,978],
[1055,1030,1047,1004,1028,1019,983,1030,1023,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 7, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,987,1068,1046,992,1011,1019,1008,1023,1039],
[1014,0,1037,1016,975,975,1005,1021,1012,1034],
[933,964,0,967,947,969,950,991,994,993],
[955,985,1034,0,994,994,1005,1022,1001,1027],
[1009,1026,1054,1007,0,996,1012,1064,1075,1036],
[990,1026,1032,1007,1005,0,1017,1004,1034,1041],
[982,996,1051,996,989,984,0,1008,995,1034],
[993,980,1010,979,937,997,993,0,1031,1005],
[978,989,1007,1000,926,967,1006,970,0,993],
[962,967,1008,974,965,960,967,996,1008,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 8, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,987,983,972,1000,994,989,984,1060,1023],
[1014,0,961,991,1007,1007,979,1028,1053,1004],
[1018,1040,0,1053,1021,988,1034,1027,1067,1035],
[1029,1010,948,0,1002,989,999,1008,1034,971],
[1001,994,980,999,0,997,936,1028,1031,966],
[1007,994,1013,1012,1004,0,991,1056,1033,1033],
[1012,1022,967,1002,1065,1010,0,1038,1038,985],
[1017,973,974,993,973,945,963,0,1037,1000],
[941,948,934,967,970,968,963,964,0,938],
[978,997,966,1030,1035,968,1016,1001,1063,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 9, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1033,993,1023,973,1040,1063,1010,1084,1019],
[968,0,962,961,947,991,987,961,1016,969],
[1008,1039,0,1043,1003,1046,1087,983,1078,1066],
[978,1040,958,0,978,1009,1018,975,1030,1000],
[1028,1054,998,1023,0,1016,1048,1037,1073,1051],
[961,1010,955,992,985,0,1028,987,1027,1004],
[938,1014,914,983,953,973,0,940,991,968],
[991,1040,1018,1026,964,1014,1061,0,1048,1032],
[917,985,923,971,928,974,1010,953,0,925],
[982,1032,935,1001,950,997,1033,969,1076,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 10, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,890,930,937,864,1055,1031,986,968,893],
[1111,0,1201,1111,923,1079,1090,1108,1024,976],
[1071,800,0,1038,921,973,1005,920,892,918],
[1064,890,963,0,873,977,1103,1051,965,914],
[1137,1078,1080,1128,0,1050,1149,1118,1072,982],
[946,922,1028,1024,951,0,1079,1032,992,1004],
[970,911,996,898,852,922,0,978,930,877],
[1015,893,1081,950,883,969,1023,0,942,922],
[1033,977,1109,1036,929,1009,1071,1059,0,909],
[1108,1025,1083,1087,1019,997,1124,1079,1092,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 11, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,914,908,1041,890,944,911,866,947,939],
[1087,0,1043,1059,1012,972,1107,1010,1065,1223],
[1093,958,0,960,1021,1041,1140,832,1088,1117],
[960,942,1041,0,1004,978,1037,844,930,1000],
[1111,989,980,997,0,969,1091,952,1109,1126],
[1057,1029,960,1023,1032,0,1086,973,940,1144],
[1090,894,861,964,910,915,0,900,961,905],
[1135,991,1169,1157,1049,1028,1101,0,1114,1110],
[1054,936,913,1071,892,1061,1040,887,0,1159],
[1062,778,884,1001,875,857,1096,891,842,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 12, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1000,1016,1129,1064,1032,1034,1131,1027,1057],
[1001,0,929,999,1006,988,1032,1115,951,1063],
[985,1072,0,1069,1057,1088,1069,1139,1020,1116],
[872,1002,932,0,1122,982,1021,1046,945,1022],
[937,995,944,879,0,919,931,1045,904,996],
[969,1013,913,1019,1082,0,1017,1027,994,1028],
[967,969,932,980,1070,984,0,1048,945,1022],
[870,886,862,955,956,974,953,0,851,1015],
[974,1050,981,1056,1097,1007,1056,1150,0,1014],
[944,938,885,979,1005,973,979,986,987,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 13, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1093,997,1162,1155,980,1351,1176,1116,1276],
[908,0,916,931,1004,820,1193,866,995,989],
[1004,1085,0,1033,1087,1084,1318,872,1105,1069],
[839,1070,968,0,1166,1067,1225,1013,1171,1245],
[846,997,914,835,0,920,1176,998,1295,1086],
[1021,1181,917,934,1081,0,1325,865,1009,1085],
[650,808,683,776,825,676,0,607,911,811],
[825,1135,1129,988,1003,1136,1394,0,1015,1208],
[885,1006,896,830,706,992,1090,986,0,1020],
[725,1012,932,756,915,916,1190,793,981,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 14, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1040,1019,989,1009,1031,1021,1040,1039,1003],
[961,0,986,959,1004,987,986,990,970,953],
[982,1015,0,974,1004,1022,1010,1026,988,991],
[1012,1042,1027,0,1020,1008,1031,1046,1030,999],
[992,997,997,981,0,989,1005,1012,990,953],
[970,1014,979,993,1012,0,1015,1034,997,969],
[980,1015,991,970,996,986,0,1006,969,984],
[961,1011,975,955,989,967,995,0,973,974],
[962,1031,1013,971,1011,1004,1032,1028,0,970],
[998,1048,1010,1002,1048,1032,1017,1027,1031,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 15, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1009,1014,967,1069,961,972,927,947,960],
[992,0,1040,1044,1040,1033,992,1034,1012,1046],
[987,961,0,976,1034,990,1002,994,915,960],
[1034,957,1025,0,1020,982,942,938,991,982],
[932,961,967,981,0,978,938,938,939,952],
[1040,968,1011,1019,1023,0,931,996,999,969],
[1029,1009,999,1059,1063,1070,0,1012,1024,1039],
[1074,967,1007,1063,1063,1005,989,0,997,984],
[1054,989,1086,1010,1062,1002,977,1004,0,973],
[1041,955,1041,1019,1049,1032,962,1017,1028,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 16, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,984,1050,968,1015,947,1001,1079,974,973],
[1017,0,993,940,996,967,988,1005,991,993],
[951,1008,0,956,1010,969,1045,1044,1002,998],
[1033,1061,1045,0,1059,1032,1069,1072,1002,999],
[986,1005,991,942,0,940,1001,1026,966,975],
[1054,1034,1032,969,1061,0,1033,1067,1016,1005],
[1000,1013,956,932,1000,968,0,1068,980,1014],
[922,996,957,929,975,934,933,0,908,985],
[1027,1010,999,999,1035,985,1021,1093,0,1049],
[1028,1008,1003,1002,1026,996,987,1016,952,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 17, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1013,1036,1038,1033,1006,1079,1018,995,1054],
[988,0,1062,999,1006,1002,1063,1024,981,1048],
[965,939,0,1012,1007,965,1060,999,1016,1002],
[963,1002,989,0,1027,1003,1036,1001,1003,1046],
[968,995,994,974,0,991,1015,1002,960,1036],
[995,999,1036,998,1010,0,1022,976,954,1053],
[922,938,941,965,986,979,0,1027,993,1020],
[983,977,1002,1000,999,1025,974,0,997,1006],
[1006,1020,985,998,1041,1047,1008,1004,0,1045],
[947,953,999,955,965,948,981,995,956,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 18, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,970,1016,982,990,990,980,937,965,1010],
[1031,0,998,1009,1024,964,996,972,1024,1017],
[985,1003,0,1006,1022,946,980,952,986,990],
[1019,992,995,0,991,998,986,973,948,1001],
[1011,977,979,1010,0,976,990,1003,1028,1012],
[1011,1037,1055,1003,1025,0,1009,968,1009,994],
[1021,1005,1021,1015,1011,992,0,990,1037,1011],
[1064,1029,1049,1028,998,1033,1011,0,1014,1022],
[1036,977,1015,1053,973,992,964,987,0,983],
[991,984,1011,1000,989,1007,990,979,1018,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 19, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,988,1041,1027,1011,1015,1025,1085,1019,996],
[1013,0,1023,983,1019,964,1003,1037,1020,964],
[960,978,0,997,1004,989,1002,995,1006,1023],
[974,1018,1004,0,967,970,1023,1038,1072,1027],
[990,982,997,1034,0,985,1040,989,1002,1017],
[986,1037,1012,1031,1016,0,1017,1002,1057,1001],
[976,998,999,978,961,984,0,1027,986,997],
[916,964,1006,963,1012,999,974,0,986,1017],
[982,981,995,929,999,944,1015,1015,0,979],
[1005,1037,978,974,984,1000,1004,984,1022,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 20, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,999,975,1036,962,939,1040,1049,1097,1019],
[1002,0,976,1089,954,1024,1077,1094,1100,1044],
[1026,1025,0,1077,1051,935,1041,1072,1049,1043],
[965,912,924,0,985,933,894,1008,991,961],
[1039,1047,950,1016,0,1051,988,1039,1135,1084],
[1062,977,1066,1068,950,0,961,1064,1124,1108],
[961,924,960,1107,1013,1040,0,1040,1011,1033],
[952,907,929,993,962,937,961,0,1056,1018],
[904,901,952,1010,866,877,990,945,0,955],
[982,957,958,1040,917,893,968,983,1046,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 21, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1015,986,1033,972,1019,981,997,976,987],
[986,0,1029,978,1005,1019,969,998,950,1000],
[1015,972,0,981,994,1011,961,995,968,1027],
[968,1023,1020,0,971,1033,1003,1051,975,974],
[1029,996,1007,1030,0,1040,969,1007,998,1017],
[982,982,990,968,961,0,946,953,950,961],
[1020,1032,1040,998,1032,1055,0,1044,1037,1027],
[1004,1003,1006,950,994,1048,957,0,985,988],
[1025,1051,1033,1026,1003,1051,964,1016,0,995],
[1014,1001,974,1027,984,1040,974,1013,1006,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 22, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1011,956,1026,1012,1009,954,988,1026,1000],
[990,0,997,1022,985,1029,970,984,1008,1019],
[1045,1004,0,1023,1016,1022,1020,996,1045,1027],
[975,979,978,0,1026,1031,969,988,1025,991],
[989,1016,985,975,0,1001,954,940,1022,1001],
[992,972,979,970,1000,0,935,953,996,1005],
[1047,1031,981,1032,1047,1066,0,1006,1046,1035],
[1013,1017,1005,1013,1061,1048,995,0,1021,1011],
[975,993,956,976,979,1005,955,980,0,1019],
[1001,982,974,1010,1000,996,966,990,982,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 23, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,979,999,983,1039,994,1015,1033,1011,1036],
[1022,0,1039,965,1018,985,1032,1027,1046,1072],
[1002,962,0,970,983,993,993,1038,1010,1027],
[1018,1036,1031,0,982,1060,1021,1035,1018,1029],
[962,983,1018,1019,0,960,969,1018,1026,1050],
[1007,1016,1008,941,1041,0,1031,996,977,1018],
[986,969,1008,980,1032,970,0,1018,999,1055],
[968,974,963,966,983,1005,983,0,970,1055],
[990,955,991,983,975,1024,1002,1031,0,1053],
[965,929,974,972,951,983,946,946,948,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 24, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,977,1003,1028,995,966,992,955,1029,989],
[1024,0,1030,1049,1036,993,1040,998,1082,1000],
[998,971,0,1005,1039,1004,967,997,1010,1021],
[973,952,996,0,1009,976,1003,983,1062,998],
[1006,965,962,992,0,952,985,966,1003,991],
[1035,1008,997,1025,1049,0,998,990,1082,1052],
[1009,961,1034,998,1016,1003,0,972,1072,1014],
[1046,1003,1004,1018,1035,1011,1029,0,1067,1000],
[972,919,991,939,998,919,929,934,0,947],
[1012,1001,980,1003,1010,949,987,1001,1054,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 25, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,979,951,1000,934,971,925,974,1018,957],
[1022,0,1024,1066,1015,1054,971,985,1022,1017],
[1050,977,0,1068,1036,1047,1055,1027,1049,1046],
[1001,935,933,0,960,1048,977,996,982,951],
[1067,986,965,1041,0,1053,1020,1013,1046,919],
[1030,947,954,953,948,0,945,970,1011,971],
[1076,1030,946,1024,981,1056,0,1018,1044,978],
[1027,1016,974,1005,988,1031,983,0,1071,991],
[983,979,952,1019,955,990,957,930,0,957],
[1044,984,955,1050,1082,1030,1023,1010,1044,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 26, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1015,860,903,1019,924,991,924,980,903],
[986,0,989,974,997,1050,1035,955,977,921],
[1141,1012,0,1019,1099,1131,1021,1038,994,1017],
[1098,1027,982,0,1004,1057,1068,1015,1028,1004],
[982,1004,902,997,0,983,1037,935,983,952],
[1077,951,870,944,1018,0,1116,1025,945,910],
[1010,966,980,933,964,885,0,967,949,945],
[1077,1046,963,986,1066,976,1034,0,1019,929],
[1021,1024,1007,973,1018,1056,1052,982,0,870],
[1098,1080,984,997,1049,1091,1056,1072,1131,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 27, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1000,1007,982,1015,1027,1031,1002,971,1001],
[1001,0,1020,937,969,965,1023,1025,952,981],
[994,981,0,947,965,1000,1018,976,953,1014],
[1019,1064,1054,0,1051,1061,1032,1017,1011,991],
[986,1032,1036,950,0,976,1034,978,979,1009],
[974,1036,1001,940,1025,0,1002,988,952,987],
[970,978,983,969,967,999,0,989,950,993],
[999,976,1025,984,1023,1013,1012,0,998,1007],
[1030,1049,1048,990,1022,1049,1051,1003,0,1044],
[1000,1020,987,1010,992,1014,1008,994,957,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 28, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,997,979,991,990,963,966,987,966,965],
[1004,0,1002,1001,998,973,930,992,965,950],
[1022,999,0,1008,1007,975,980,1005,968,975],
[1010,1000,993,0,1001,955,946,979,972,965],
[1011,1003,994,1000,0,951,957,986,976,939],
[1038,1028,1026,1046,1050,0,1024,1020,1013,988],
[1035,1071,1021,1055,1044,977,0,1016,1044,1021],
[1014,1009,996,1022,1015,981,985,0,1025,980],
[1035,1036,1033,1029,1025,988,957,976,0,985],
[1036,1051,1026,1036,1062,1013,980,1021,1016,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 29, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,995,917,960,1018,984,966,972,999,975],
[1006,0,921,960,919,922,991,943,968,941],
[1084,1080,0,1058,1017,1051,1010,994,1031,1059],
[1041,1041,943,0,975,1018,974,985,990,957],
[983,1082,984,1026,0,982,1001,1000,1066,1040],
[1017,1079,950,983,1019,0,980,960,1003,1021],
[1035,1010,991,1027,1000,1021,0,1010,985,1044],
[1029,1058,1007,1016,1001,1041,991,0,982,1006],
[1002,1033,970,1011,935,998,1016,1019,0,992],
[1026,1060,942,1044,961,980,957,995,1009,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 30, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,988,975,959,957,986,959,967,994,986],
[1013,0,1001,972,990,990,985,982,1016,986],
[1026,1000,0,963,959,979,977,1003,1005,984],
[1042,1029,1038,0,1011,1012,1027,1031,1033,1000],
[1044,1011,1042,990,0,1035,1029,1045,1005,1003],
[1015,1011,1022,989,966,0,958,1000,1020,1005],
[1042,1016,1024,974,972,1043,0,1009,1028,1032],
[1034,1019,998,970,956,1001,992,0,1022,1005],
[1007,985,996,968,996,981,973,979,0,995],
[1015,1015,1017,1001,998,996,969,996,1006,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 31, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,978,934,978,944,954,965,978,958,969],
[1023,0,989,984,983,984,1010,989,998,983],
[1067,1012,0,1018,989,1018,1051,1028,1021,1050],
[1023,1017,983,0,960,997,1012,1014,986,1013],
[1057,1018,1012,1041,0,1015,1025,995,998,1028],
[1047,1017,983,1004,986,0,1016,1011,1011,978],
[1036,991,950,989,976,985,0,1014,991,1033],
[1023,1012,973,987,1006,990,987,0,1013,1028],
[1043,1003,980,1015,1003,990,1010,988,0,1017],
[1032,1018,951,988,973,1023,968,973,984,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 32, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1078,1055,1106,997,1023,1093,1073,943,1031],
[923,0,932,1039,1009,890,1084,1006,943,986],
[946,1069,0,1025,1043,974,1086,1070,1031,1099],
[895,962,976,0,947,1022,1048,1039,922,969],
[1004,992,958,1054,0,1011,1037,1136,991,980],
[978,1111,1027,979,990,0,1084,1114,976,1012],
[908,917,915,953,964,917,0,1040,903,999],
[928,995,931,962,865,887,961,0,857,931],
[1058,1058,970,1079,1010,1025,1098,1144,0,989],
[970,1015,902,1032,1021,989,1002,1070,1012,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 33, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1039,982,1005,1029,974,1004,972,992,987],
[962,0,967,993,971,929,962,968,976,985],
[1019,1034,0,995,1000,985,992,963,970,977],
[996,1008,1006,0,990,985,962,964,1001,979],
[972,1030,1001,1011,0,954,995,970,997,1012],
[1027,1072,1016,1016,1047,0,1033,985,998,1005],
[997,1039,1009,1039,1006,968,0,992,1003,1020],
[1029,1033,1038,1037,1031,1016,1009,0,990,1018],
[1009,1025,1031,1000,1004,1003,998,1011,0,999],
[1014,1016,1024,1022,989,996,981,983,1002,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 34, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,967,1084,996,1116,944,1091,921,1030,979],
[1034,0,1105,1046,1026,964,1113,955,986,974],
[917,896,0,851,1021,935,1016,905,929,887],
[1005,955,1150,0,1065,1010,1063,1035,1040,988],
[885,975,980,936,0,880,1038,855,1007,905],
[1057,1037,1066,991,1121,0,1081,946,1079,1091],
[910,888,985,938,963,920,0,859,956,933],
[1080,1046,1096,966,1146,1055,1142,0,1024,1003],
[971,1015,1072,961,994,922,1045,977,0,1000],
[1022,1027,1114,1013,1096,910,1068,998,1001,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 35, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,988,995,980,989,1054,1012,990,981,963],
[1013,0,1007,963,975,1017,1020,1012,987,1011],
[1006,994,0,988,1005,1028,1007,1013,997,1003],
[1021,1038,1013,0,974,1050,1052,1031,1034,1025],
[1012,1026,996,1027,0,1044,1035,1023,1025,990],
[947,984,973,951,957,0,966,993,971,948],
[989,981,994,949,966,1035,0,993,990,977],
[1011,989,988,970,978,1008,1008,0,996,1027],
[1020,1014,1004,967,976,1030,1011,1005,0,1001],
[1038,990,998,976,1011,1053,1024,974,1000,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 36, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1008,1005,972,1028,1008,996,1016,997,1037],
[993,0,996,984,1011,1050,1017,1010,1048,1026],
[996,1005,0,995,1027,1045,1002,1020,1027,1010],
[1029,1017,1006,0,998,1039,1027,1018,1000,1004],
[973,990,974,1003,0,1015,973,996,1002,989],
[993,951,956,962,986,0,958,1014,935,1003],
[1005,984,999,974,1028,1043,0,1047,981,1011],
[985,991,981,983,1005,987,954,0,984,990],
[1004,953,974,1001,999,1066,1020,1017,0,1018],
[964,975,991,997,1012,998,990,1011,983,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 37, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,979,1026,981,975,1025,1003,1037,1015,1026],
[1022,0,1024,1017,1002,1025,1034,1033,1021,982],
[975,977,0,977,955,1031,989,1024,987,967],
[1020,984,1024,0,985,1043,1029,1029,1004,1006],
[1026,999,1046,1016,0,1043,1016,1022,1011,1001],
[976,976,970,958,958,0,986,1023,976,951],
[998,967,1012,972,985,1015,0,1018,1011,962],
[964,968,977,972,979,978,983,0,990,964],
[986,980,1014,997,990,1025,990,1011,0,969],
[975,1019,1034,995,1000,1050,1039,1037,1032,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 38, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1085,988,987,981,1020,1013,972,984,1052],
[916,0,852,873,877,899,888,962,971,910],
[1013,1149,0,966,1003,952,943,1004,971,977],
[1014,1128,1035,0,1022,1042,980,1001,1022,1007],
[1020,1124,998,979,0,998,1035,1002,1021,953],
[981,1102,1049,959,1003,0,934,944,955,993],
[988,1113,1058,1021,966,1067,0,988,1025,1030],
[1029,1039,997,1000,999,1057,1013,0,997,1054],
[1017,1030,1030,979,980,1046,976,1004,0,1044],
[949,1091,1024,994,1048,1008,971,947,957,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 39, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,967,957,985,995,988,956,987,990,978],
[1034,0,993,955,1007,977,985,1004,1006,1026],
[1044,1008,0,987,1029,1016,1004,1010,1009,985],
[1016,1046,1014,0,1045,1014,991,1003,1055,1020],
[1006,994,972,956,0,988,984,1002,973,953],
[1013,1024,985,987,1013,0,983,1026,998,1013],
[1045,1016,997,1010,1017,1018,0,1025,991,1037],
[1014,997,991,998,999,975,976,0,1007,992],
[1011,995,992,946,1028,1003,1010,994,0,994],
[1023,975,1016,981,1048,988,964,1009,1007,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 40, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1062,1044,1032,975,988,1053,1018,981,1108],
[939,0,970,1015,990,956,1017,1007,963,1042],
[957,1031,0,1055,981,965,1038,919,954,1029],
[969,986,946,0,1007,1028,1078,969,1013,1051],
[1026,1011,1020,994,0,1033,1077,1008,1002,1026],
[1013,1045,1036,973,968,0,1053,1046,1003,1058],
[948,984,963,923,924,948,0,961,953,966],
[983,994,1082,1032,993,955,1040,0,1044,1066],
[1020,1038,1047,988,999,998,1048,957,0,1016],
[893,959,972,950,975,943,1035,935,985,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 41, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1020,1033,948,1042,1061,1017,1010,1042,961],
[981,0,993,971,1114,1117,965,1023,1098,1082],
[968,1008,0,928,934,992,989,976,937,920],
[1053,1030,1073,0,1069,1134,1128,1140,1091,992],
[959,887,1067,932,0,1083,1045,1141,1010,964],
[940,884,1009,867,918,0,928,976,941,956],
[984,1036,1012,873,956,1073,0,1021,1011,870],
[991,978,1025,861,860,1025,980,0,940,945],
[959,903,1064,910,991,1060,990,1061,0,1037],
[1040,919,1081,1009,1037,1045,1131,1056,964,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 42, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1014,1007,1009,991,1016,1007,991,1002,994],
[987,0,992,969,971,983,994,1000,1006,974],
[994,1009,0,1009,968,985,1025,1022,1023,982],
[992,1032,992,0,986,975,1035,1009,1014,996],
[1010,1030,1033,1015,0,1000,1022,1039,1025,1006],
[985,1018,1016,1026,1001,0,1006,1017,1025,980],
[994,1007,976,966,979,995,0,984,987,993],
[1010,1001,979,992,962,984,1017,0,1001,971],
[999,995,978,987,976,976,1014,1000,0,983],
[1007,1027,1019,1005,995,1021,1008,1030,1018,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 43, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1047,1007,1014,1046,986,1011,1040,1062,1034],
[954,0,985,1002,1032,964,977,996,1029,998],
[994,1016,0,1010,1017,995,1025,1009,1032,998],
[987,999,991,0,1026,1015,1012,1011,1054,993],
[955,969,984,975,0,1002,973,998,988,982],
[1015,1037,1006,986,999,0,1004,994,1006,993],
[990,1024,976,989,1028,997,0,1023,1016,1007],
[961,1005,992,990,1003,1007,978,0,1062,1000],
[939,972,969,947,1013,995,985,939,0,986],
[967,1003,1003,1008,1019,1008,994,1001,1015,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 44, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,998,980,1025,1028,1016,946,1017,1058,1001],
[1003,0,990,994,1001,1037,937,1052,949,971],
[1021,1011,0,973,971,1046,1020,998,1019,972],
[976,1007,1028,0,1018,1045,967,1017,1019,1031],
[973,1000,1030,983,0,1031,1019,1029,1030,1014],
[985,964,955,956,970,0,943,993,1016,945],
[1055,1064,981,1034,982,1058,0,1014,1049,1015],
[984,949,1003,984,972,1008,987,0,1015,964],
[943,1052,982,982,971,985,952,986,0,963],
[1000,1030,1029,970,987,1056,986,1037,1038,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 45, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,992,1018,990,989,1007,960,1003,988,984],
[1009,0,1016,1035,979,997,1003,1038,989,968],
[983,985,0,1015,977,1004,973,1010,1023,946],
[1011,966,986,0,974,984,960,978,1009,953],
[1012,1022,1024,1027,0,1032,981,1032,999,1002],
[994,1004,997,1017,969,0,996,1026,1002,969],
[1041,998,1028,1041,1020,1005,0,1026,1018,997],
[998,963,991,1023,969,975,975,0,998,990],
[1013,1012,978,992,1002,999,983,1003,0,975],
[1017,1033,1055,1048,999,1032,1004,1011,1026,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 46, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1017,991,1000,966,991,963,988,982,929],
[984,0,1012,963,975,977,976,1008,994,979],
[1010,989,0,979,995,953,950,992,982,965],
[1001,1038,1022,0,1014,1034,988,1017,1007,1017],
[1035,1026,1006,987,0,1015,987,1056,1016,1005],
[1010,1024,1048,967,986,0,972,1009,971,955],
[1038,1025,1051,1013,1014,1029,0,1024,1026,994],
[1013,993,1009,984,945,992,977,0,996,995],
[1019,1007,1019,994,985,1030,975,1005,0,976],
[1072,1022,1036,984,996,1046,1007,1006,1025,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 47, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1052,911,958,948,1110,859,1079,941,934],
[949,0,1000,937,971,1044,936,1057,914,930],
[1090,1001,0,874,972,946,1045,1113,995,945],
[1043,1064,1127,0,1014,1147,966,1062,959,951],
[1053,1030,1029,987,0,1091,1066,1199,1073,1052],
[891,957,1055,854,910,0,894,1047,1015,976],
[1142,1065,956,1035,935,1107,0,1057,1014,985],
[922,944,888,939,802,954,944,0,899,855],
[1060,1087,1006,1042,928,986,987,1102,0,1030],
[1067,1071,1056,1050,949,1025,1016,1146,971,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 48, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,955,1138,1167,1136,1182,1247,1046,1023,1167],
[1046,0,1219,1192,1148,1080,1099,998,1051,1011],
[863,782,0,1034,1009,1023,966,923,786,971],
[834,809,967,0,1066,983,883,828,852,927],
[865,853,992,935,0,962,920,847,981,869],
[819,921,978,1018,1039,0,924,853,962,1078],
[754,902,1035,1118,1081,1077,0,836,842,1024],
[955,1003,1078,1173,1154,1148,1165,0,1045,1156],
[978,950,1215,1149,1020,1039,1159,956,0,1094],
[834,990,1030,1074,1132,923,977,845,907,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 49, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,982,1004,1013,962,975,966,1010,948,1004],
[1019,0,1070,990,979,973,1059,967,996,978],
[997,931,0,925,982,956,969,1027,953,1024],
[988,1011,1076,0,1017,989,1054,1012,1017,1056],
[1039,1022,1019,984,0,974,1061,1024,1006,1022],
[1026,1028,1045,1012,1027,0,1022,1072,955,955],
[1035,942,1032,947,940,979,0,1038,994,982],
[991,1034,974,989,977,929,963,0,934,964],
[1053,1005,1048,984,995,1046,1007,1067,0,927],
[997,1023,977,945,979,1046,1019,1037,1074,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 50, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1010,1034,976,1078,1062,1020,1017,998,1024],
[991,0,911,924,980,929,999,978,906,968],
[967,1090,0,1013,996,1059,1065,999,961,988],
[1025,1077,988,0,1034,1081,1034,947,1020,982],
[923,1021,1005,967,0,1016,1026,895,972,950],
[939,1072,942,920,985,0,962,915,894,912],
[981,1002,936,967,975,1039,0,932,1036,981],
[984,1023,1002,1054,1106,1086,1069,0,1011,1004],
[1003,1095,1040,981,1029,1107,965,990,0,977],
[977,1033,1013,1019,1051,1089,1020,997,1024,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 51, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,992,986,946,984,981,1001,980,996,960],
[1009,0,979,986,995,1027,1019,1001,984,1011],
[1015,1022,0,999,998,1014,990,1010,994,1007],
[1055,1015,1002,0,1053,1024,1007,962,1017,1010],
[1017,1006,1003,948,0,1005,1020,982,1005,979],
[1020,974,987,977,996,0,1008,970,1013,978],
[1000,982,1011,994,981,993,0,989,1007,987],
[1021,1000,991,1039,1019,1031,1012,0,1012,997],
[1005,1017,1007,984,996,988,994,989,0,985],
[1041,990,994,991,1022,1023,1014,1004,1016,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 52, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,960,1013,962,1028,1024,1017,981,978,1006],
[1041,0,1021,1046,1016,1052,996,1010,1042,1043],
[988,980,0,975,985,1008,964,968,953,995],
[1039,955,1026,0,1012,1058,1024,989,1011,1051],
[973,985,1016,989,0,1008,981,948,988,1001],
[977,949,993,943,993,0,975,971,965,1000],
[984,1005,1037,977,1020,1026,0,1013,996,1008],
[1020,991,1033,1012,1053,1030,988,0,973,1031],
[1023,959,1048,990,1013,1036,1005,1028,0,1041],
[995,958,1006,950,1000,1001,993,970,960,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 53, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1003,952,1004,1068,1013,982,981,1044,989],
[998,0,972,1007,1039,1038,1021,962,1047,973],
[1049,1029,0,967,1032,1023,966,964,1040,1019],
[997,994,1034,0,1068,1051,1028,987,1060,971],
[933,962,969,933,0,1007,970,968,1026,1006],
[988,963,978,950,994,0,967,939,994,993],
[1019,980,1035,973,1031,1034,0,1016,1101,998],
[1020,1039,1037,1014,1033,1062,985,0,1003,1042],
[957,954,961,941,975,1007,900,998,0,979],
[1012,1028,982,1030,995,1008,1003,959,1022,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 54, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1042,1005,1009,1027,1016,1000,993,995,1036],
[959,0,1009,1006,1012,994,994,996,983,993],
[996,992,0,1005,987,1001,975,987,955,989],
[992,995,996,0,979,1003,978,991,977,994],
[974,989,1014,1022,0,979,981,990,983,1011],
[985,1007,1000,998,1022,0,1010,991,986,1020],
[1001,1007,1026,1023,1020,991,0,1030,1012,1008],
[1008,1005,1014,1010,1011,1010,971,0,957,1010],
[1006,1018,1046,1024,1018,1015,989,1044,0,1019],
[965,1008,1012,1007,990,981,993,991,982,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 55, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1002,1023,1024,985,963,961,1045,1010,956],
[999,0,1009,1009,977,978,1005,1025,1021,1009],
[978,992,0,965,992,948,973,1014,997,938],
[977,992,1036,0,1001,977,987,995,977,981],
[1016,1024,1009,1000,0,1010,984,1062,1013,975],
[1038,1023,1053,1024,991,0,1054,1051,995,1001],
[1040,996,1028,1014,1017,947,0,1061,1016,952],
[956,976,987,1006,939,950,940,0,959,957],
[991,980,1004,1024,988,1006,985,1042,0,976],
[1045,992,1063,1020,1026,1000,1049,1044,1025,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 56, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1021,1028,1012,991,1004,1009,1033,1044,952],
[980,0,1004,1005,1022,994,980,1007,1015,994],
[973,997,0,995,1023,936,994,985,1010,968],
[989,996,1006,0,996,953,976,989,997,973],
[1010,979,978,1005,0,994,1001,997,1036,958],
[997,1007,1065,1048,1007,0,989,1020,1046,974],
[992,1021,1007,1025,1000,1012,0,1040,1034,1013],
[968,994,1016,1012,1004,981,961,0,1028,985],
[957,986,991,1004,965,955,967,973,0,951],
[1049,1007,1033,1028,1043,1027,988,1016,1050,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 57, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1013,990,978,1038,1059,1000,1021,993,915],
[988,0,961,1023,1012,1018,976,998,940,947],
[1011,1040,0,1056,1067,1109,1032,1084,1013,952],
[1023,978,945,0,1014,1053,995,1021,1045,1033],
[963,989,934,987,0,999,962,990,972,936],
[942,983,892,948,1002,0,908,984,935,981],
[1001,1025,969,1006,1039,1093,0,1039,993,985],
[980,1003,917,980,1011,1017,962,0,1023,990],
[1008,1061,988,956,1029,1066,1008,978,0,1033],
[1086,1054,1049,968,1065,1020,1016,1011,968,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 58, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,985,1023,1010,997,974,971,959,1006,994],
[1016,0,996,993,977,984,980,934,983,981],
[978,1005,0,1018,983,991,971,970,990,1019],
[991,1008,983,0,1003,1018,1002,981,1013,1015],
[1004,1024,1018,998,0,1034,971,959,1024,996],
[1027,1017,1010,983,967,0,996,1002,983,1002],
[1030,1021,1030,999,1030,1005,0,1001,1021,1017],
[1042,1067,1031,1020,1042,999,1000,0,1010,1009],
[995,1018,1011,988,977,1018,980,991,0,1009],
[1007,1020,982,986,1005,999,984,992,992,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 59, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,913,986,1003,1016,871,984,994,965,908],
[1088,0,1100,1034,968,992,1032,996,1005,990],
[1015,901,0,1008,1009,940,1007,1023,947,980],
[998,967,993,0,927,951,985,1046,977,951],
[985,1033,992,1074,0,949,992,1022,952,1013],
[1130,1009,1061,1050,1052,0,955,1079,1020,1028],
[1017,969,994,1016,1009,1046,0,966,978,914],
[1007,1005,978,955,979,922,1035,0,1000,932],
[1036,996,1054,1024,1049,981,1023,1001,0,1089],
[1093,1011,1021,1050,988,973,1087,1069,912,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 60, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,989,998,988,966,996,974,995,995,1003],
[1012,0,991,964,954,965,985,1017,1009,966],
[1003,1010,0,965,962,973,953,985,981,993],
[1013,1037,1036,0,965,1016,1030,1028,998,1011],
[1035,1047,1039,1036,0,1026,1021,1040,1010,995],
[1005,1036,1028,985,975,0,1000,1015,990,1006],
[1027,1016,1048,971,980,1001,0,1012,969,993],
[1006,984,1016,973,961,986,989,0,966,970],
[1006,992,1020,1003,991,1011,1032,1035,0,992],
[998,1035,1008,990,1006,995,1008,1031,1009,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 61, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,964,1006,978,971,1020,966,952,1000,983],
[1037,0,965,1056,992,1031,1007,1026,1007,1067],
[995,1036,0,1067,1007,1003,1000,1001,1042,1040],
[1023,945,934,0,975,1021,962,1002,967,1006],
[1030,1009,994,1026,0,1007,994,980,1025,1047],
[981,970,998,980,994,0,1001,1019,1013,1047],
[1035,994,1001,1039,1007,1000,0,1010,1040,1088],
[1049,975,1000,999,1021,982,991,0,1033,998],
[1001,994,959,1034,976,988,961,968,0,1007],
[1018,934,961,995,954,954,913,1003,994,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 62, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,956,962,955,985,982,972,964,1024,1018],
[1045,0,1024,995,1024,1035,1048,1026,1030,1063],
[1039,977,0,987,994,997,1030,996,997,1044],
[1046,1006,1014,0,1000,1021,1032,976,1047,1049],
[1016,977,1007,1001,0,1000,1024,994,992,1056],
[1019,966,1004,980,1001,0,1010,975,1004,1020],
[1029,953,971,969,977,991,0,995,1012,1019],
[1037,975,1005,1025,1007,1026,1006,0,1035,1033],
[977,971,1004,954,1009,997,989,966,0,976],
[983,938,957,952,945,981,982,968,1025,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 63, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1026,1050,979,1033,1031,971,1017,1007,991],
[975,0,1017,958,1035,1007,990,977,1001,1030],
[951,984,0,969,1018,995,965,953,986,987],
[1022,1043,1032,0,1040,1014,985,1000,995,998],
[968,966,983,961,0,980,990,971,985,985],
[970,994,1006,987,1021,0,983,992,987,977],
[1030,1011,1036,1016,1011,1018,0,978,989,988],
[984,1024,1048,1001,1030,1009,1023,0,1031,991],
[994,1000,1015,1006,1016,1014,1012,970,0,983],
[1010,971,1014,1003,1016,1024,1013,1010,1018,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 64, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,995,1042,1060,1004,1029,1036,1025,1014,1089],
[1006,0,1059,982,1026,1049,1036,988,1040,1065],
[959,942,0,966,998,1009,990,922,1011,981],
[941,1019,1035,0,1017,1040,1057,986,1041,1017],
[997,975,1003,984,0,974,1046,961,975,1059],
[972,952,992,961,1027,0,1040,955,978,1054],
[965,965,1011,944,955,961,0,962,965,1014],
[976,1013,1079,1015,1040,1046,1039,0,1010,1052],
[987,961,990,960,1026,1023,1036,991,0,1058],
[912,936,1020,984,942,947,987,949,943,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 65, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1033,1001,997,995,1041,961,1009,988,979],
[968,0,955,983,975,997,977,995,955,978],
[1000,1046,0,1008,1013,1025,996,1042,985,997],
[1004,1018,993,0,1008,1051,977,994,1002,1008],
[1006,1026,988,993,0,1069,997,1040,1001,1009],
[960,1004,976,950,932,0,953,992,947,978],
[1040,1024,1005,1024,1004,1048,0,1029,977,1004],
[992,1006,959,1007,961,1009,972,0,971,998],
[1013,1046,1016,999,1000,1054,1024,1030,0,1011],
[1022,1023,1004,993,992,1023,997,1003,990,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 66, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1016,1048,1037,1050,1017,990,1015,1034,975],
[985,0,995,1037,956,1020,1002,973,974,997],
[953,1006,0,1016,990,997,948,988,1000,989],
[964,964,985,0,989,976,965,957,924,971],
[951,1045,1011,1012,0,1000,1022,989,1018,1026],
[984,981,1004,1025,1001,0,1010,978,1018,961],
[1011,999,1053,1036,979,991,0,1026,983,1003],
[986,1028,1013,1044,1012,1023,975,0,1038,1002],
[967,1027,1001,1077,983,983,1018,963,0,980],
[1026,1004,1012,1030,975,1040,998,999,1021,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 67, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1014,1015,1024,1040,1003,1003,1034,958,1015],
[987,0,961,961,986,982,976,1013,957,968],
[986,1040,0,1030,1025,985,1014,1027,1018,1016],
[977,1040,971,0,1041,977,993,1027,965,983],
[961,1015,976,960,0,973,991,1007,957,953],
[998,1019,1016,1024,1028,0,1010,1000,1027,992],
[998,1025,987,1008,1010,991,0,994,988,978],
[967,988,974,974,994,1001,1007,0,985,958],
[1043,1044,983,1036,1044,974,1013,1016,0,978],
[986,1033,985,1018,1048,1009,1023,1043,1023,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 68, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,936,908,969,1070,990,968,1091,1041,1033],
[1065,0,963,1020,1109,1013,1008,1076,998,1065],
[1093,1038,0,967,1090,990,1016,1082,1046,1110],
[1032,981,1034,0,1117,1000,1102,1127,1092,1102],
[931,892,911,884,0,896,924,1027,922,936],
[1011,988,1011,1001,1105,0,999,1023,1078,1055],
[1033,993,985,899,1077,1002,0,1027,1010,1031],
[910,925,919,874,974,978,974,0,946,969],
[960,1003,955,909,1079,923,991,1055,0,990],
[968,936,891,899,1065,946,970,1032,1011,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 69, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,968,1051,1014,1016,1043,1018,1067,1087,991],
[1033,0,1041,1016,955,1022,1056,1086,1062,1004],
[950,960,0,1002,995,1042,1030,1054,1072,1025],
[987,985,999,0,993,1019,994,1020,1059,982],
[985,1046,1006,1008,0,1029,1020,1056,1042,1008],
[958,979,959,982,972,0,1001,1021,1035,1011],
[983,945,971,1007,981,1000,0,1038,1049,1004],
[934,915,947,981,945,980,963,0,999,948],
[914,939,929,942,959,966,952,1002,0,924],
[1010,997,976,1019,993,990,997,1053,1077,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 70, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,985,1005,945,1041,997,951,991,1012,967],
[1016,0,965,964,984,977,947,983,1010,992],
[996,1036,0,989,998,944,1000,998,984,984],
[1056,1037,1012,0,1067,984,938,1001,990,966],
[960,1017,1003,934,0,968,954,958,992,910],
[1004,1024,1057,1017,1033,0,983,998,985,1012],
[1050,1054,1001,1063,1047,1018,0,985,1055,1016],
[1010,1018,1003,1000,1043,1003,1016,0,1100,1013],
[989,991,1017,1011,1009,1016,946,901,0,975],
[1034,1009,1017,1035,1091,989,985,988,1026,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 71, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1050,1012,1030,1087,950,1040,1029,1113,1069],
[951,0,948,957,947,930,975,993,1053,1010],
[989,1053,0,1047,1022,1015,1039,1023,1066,1046],
[971,1044,954,0,985,939,1002,960,1051,1027],
[914,1054,979,1016,0,905,1003,1007,1019,990],
[1051,1071,986,1062,1096,0,1073,1067,1129,1124],
[961,1026,962,999,998,928,0,969,1013,1020],
[972,1008,978,1041,994,934,1032,0,1026,1041],
[888,948,935,950,982,872,988,975,0,980],
[932,991,955,974,1011,877,981,960,1021,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 72, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,874,987,873,926,939,869,1013,998,1049],
[1127,0,1151,978,964,1070,1068,1055,1059,1135],
[1014,850,0,905,937,938,927,883,960,972],
[1128,1023,1096,0,1038,1061,995,996,1177,1101],
[1075,1037,1064,963,0,1082,1042,1017,1175,1134],
[1062,931,1063,940,919,0,976,988,993,1126],
[1132,933,1074,1006,959,1025,0,1038,1018,1118],
[988,946,1118,1005,984,1013,963,0,1054,1048],
[1003,942,1041,824,826,1008,983,947,0,1043],
[952,866,1029,900,867,875,883,953,958,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 73, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1011,1032,1013,1021,972,1027,983,994,989],
[990,0,1006,1022,980,969,1013,977,1027,1026],
[969,995,0,1009,1026,980,990,979,1026,1022],
[988,979,992,0,995,1008,981,996,1021,995],
[980,1021,975,1006,0,979,978,971,988,1006],
[1029,1032,1021,993,1022,0,1016,1035,1036,1023],
[974,988,1011,1020,1023,985,0,995,994,987],
[1018,1024,1022,1005,1030,966,1006,0,1026,1032],
[1007,974,975,980,1013,965,1007,975,0,1006],
[1012,975,979,1006,995,978,1014,969,995,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 74, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1034,976,1020,974,1012,1001,954,965,914],
[967,0,897,971,979,989,972,958,940,953],
[1025,1104,0,1050,1040,1033,1046,984,987,1008],
[981,1030,951,0,997,1020,1022,979,968,930],
[1027,1022,961,1004,0,1014,1019,992,997,917],
[989,1012,968,981,987,0,1001,1001,969,976],
[1000,1029,955,979,982,1000,0,971,996,1007],
[1047,1043,1017,1022,1009,1000,1030,0,978,982],
[1036,1061,1014,1033,1004,1032,1005,1023,0,984],
[1087,1048,993,1071,1084,1025,994,1019,1017,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 75, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,986,1015,990,1010,1011,967,1018,997,988],
[1015,0,989,998,986,1006,956,1010,976,1005],
[986,1012,0,981,1000,1016,962,997,943,1014],
[1011,1003,1020,0,997,1028,945,994,988,1005],
[991,1015,1001,1004,0,1029,981,1005,1000,1005],
[990,995,985,973,972,0,962,984,993,999],
[1034,1045,1039,1056,1020,1039,0,1048,1005,994],
[983,991,1004,1007,996,1017,953,0,995,997],
[1004,1025,1058,1013,1001,1008,996,1006,0,1006],
[1013,996,987,996,996,1002,1007,1004,995,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 76, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1018,1000,1048,971,1050,997,1003,980,995],
[983,0,1016,1014,986,1031,995,1024,1003,1002],
[1001,985,0,1019,1035,1022,1022,985,1010,991],
[953,987,982,0,947,1004,956,985,1003,979],
[1030,1015,966,1054,0,1025,988,1007,1011,988],
[951,970,979,997,976,0,966,1019,973,993],
[1004,1006,979,1045,1013,1035,0,1008,1024,1002],
[998,977,1016,1016,994,982,993,0,1007,975],
[1021,998,991,998,990,1028,977,994,0,1010],
[1006,999,1010,1022,1013,1008,999,1026,991,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 77, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1091,998,1042,1157,1117,1012,1111,1006,1059],
[910,0,916,979,981,935,935,933,876,999],
[1003,1085,0,1000,1035,996,954,1084,984,1019],
[959,1022,1001,0,1112,985,972,956,962,1033],
[844,1020,966,889,0,1025,943,952,888,1037],
[884,1066,1005,1016,976,0,986,1026,976,953],
[989,1066,1047,1029,1058,1015,0,994,920,1020],
[890,1068,917,1045,1049,975,1007,0,936,1034],
[995,1125,1017,1039,1113,1025,1081,1065,0,995],
[942,1002,982,968,964,1048,981,967,1006,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 78, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1083,1003,1050,1009,986,1010,1024,952,1047],
[918,0,947,918,899,922,987,958,976,982],
[998,1054,0,1004,965,1034,1000,1064,1022,960],
[951,1083,997,0,982,968,1025,999,986,1009],
[992,1102,1036,1019,0,1024,1016,995,1074,1059],
[1015,1079,967,1033,977,0,1028,1015,1005,1047],
[991,1014,1001,976,985,973,0,995,1034,957],
[977,1043,937,1002,1006,986,1006,0,982,946],
[1049,1025,979,1015,927,996,967,1019,0,911],
[954,1019,1041,992,942,954,1044,1055,1090,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 79, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,986,1050,1097,968,1006,953,994,971,1019],
[1015,0,1035,976,989,1067,963,1028,1039,972],
[951,966,0,1027,946,985,969,955,977,946],
[904,1025,974,0,873,962,984,977,914,935],
[1033,1012,1055,1128,0,1049,993,1046,937,1016],
[995,934,1016,1039,952,0,951,1003,988,966],
[1048,1038,1032,1017,1008,1050,0,1014,988,1021],
[1007,973,1046,1024,955,998,987,0,1000,1026],
[1030,962,1024,1087,1064,1013,1013,1001,0,1062],
[982,1029,1055,1066,985,1035,980,975,939,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 80, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,980,998,1007,992,988,1013,1004,988,1000],
[1021,0,1034,1033,1016,1000,990,1031,1002,1024],
[1003,967,0,1010,1018,1001,1008,1031,994,1004],
[994,968,991,0,964,988,985,1009,980,962],
[1009,985,983,1037,0,985,1013,1033,994,1000],
[1013,1001,1000,1013,1016,0,1021,1001,979,1012],
[988,1011,993,1016,988,980,0,1002,975,1008],
[997,970,970,992,968,1000,999,0,942,976],
[1013,999,1007,1021,1007,1022,1026,1059,0,1017],
[1001,977,997,1039,1001,989,993,1025,984,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 81, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1012,999,1024,976,1050,980,995,977,996],
[989,0,1006,1001,1003,1010,1010,999,1033,1020],
[1002,995,0,1033,1014,1015,990,999,984,1047],
[977,1000,968,0,978,981,971,1005,937,1006],
[1025,998,987,1023,0,990,995,999,992,1012],
[951,991,986,1020,1011,0,969,1005,1018,1016],
[1021,991,1011,1030,1006,1032,0,1026,1042,1029],
[1006,1002,1002,996,1002,996,975,0,995,1023],
[1024,968,1017,1064,1009,983,959,1006,0,1029],
[1005,981,954,995,989,985,972,978,972,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 82, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1033,1032,997,1026,1003,1010,1014,1030,1056],
[968,0,1004,964,1036,1015,971,1032,1022,984],
[969,997,0,982,989,1013,996,1016,1035,1007],
[1004,1037,1019,0,1014,1041,974,1016,1038,994],
[975,965,1012,987,0,1001,953,987,969,1026],
[998,986,988,960,1000,0,988,1015,1004,1002],
[991,1030,1005,1027,1048,1013,0,1015,1044,1032],
[987,969,985,985,1014,986,986,0,1054,977],
[971,979,966,963,1032,997,957,947,0,1024],
[945,1017,994,1007,975,999,969,1024,977,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 83, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1033,1040,1012,991,1013,1018,1046,1036,1026],
[968,0,983,1000,996,960,979,999,1002,1012],
[961,1018,0,975,975,1008,998,1013,992,1017],
[989,1001,1026,0,1001,1008,1034,1036,1014,1019],
[1010,1005,1026,1000,0,995,1006,1045,1006,1013],
[988,1041,993,993,1006,0,1000,1042,1009,1026],
[983,1022,1003,967,995,1001,0,1024,997,1049],
[955,1002,988,965,956,959,977,0,992,1015],
[965,999,1009,987,995,992,1004,1009,0,1008],
[975,989,984,982,988,975,952,986,993,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 84, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,986,981,981,1008,1028,1021,982,1028,985],
[1015,0,1016,995,1008,1024,1000,1014,998,1019],
[1020,985,0,985,994,1042,1006,1000,1028,1006],
[1020,1006,1016,0,995,1018,1021,990,1022,1016],
[993,993,1007,1006,0,1043,1047,1040,1037,1019],
[973,977,959,983,958,0,984,970,999,987],
[980,1001,995,980,954,1017,0,1003,1018,1003],
[1019,987,1001,1011,961,1031,998,0,1042,996],
[973,1003,973,979,964,1002,983,959,0,991],
[1016,982,995,985,982,1014,998,1005,1010,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 85, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1014,969,1029,967,1020,979,1014,1025,961],
[987,0,986,1012,968,993,1003,1017,990,987],
[1032,1015,0,1014,998,1052,1020,1047,1033,992],
[972,989,987,0,986,1034,967,984,997,962],
[1034,1033,1003,1015,0,1066,1024,1009,1025,998],
[981,1008,949,967,935,0,979,972,967,958],
[1022,998,981,1034,977,1022,0,986,1019,989],
[987,984,954,1017,992,1029,1015,0,998,967],
[976,1011,968,1004,976,1034,982,1003,0,1005],
[1040,1014,1009,1039,1003,1043,1012,1034,996,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 86, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1009,1039,1032,1023,1038,1011,989,1000,1033],
[992,0,1052,1046,1045,1024,1027,1004,1055,1018],
[962,949,0,1043,1005,973,1000,969,1048,990],
[969,955,958,0,953,988,940,928,969,970],
[978,956,996,1048,0,989,1002,1009,1029,1017],
[963,977,1028,1013,1012,0,1018,995,1005,962],
[990,974,1001,1061,999,983,0,975,1021,988],
[1012,997,1032,1073,992,1006,1026,0,1047,1028],
[1001,946,953,1032,972,996,980,954,0,994],
[968,983,1011,1031,984,1039,1013,973,1007,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 87, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,984,1050,926,975,1000,1048,1005,955,978],
[1017,0,1031,948,948,1002,1002,946,1023,948],
[951,970,0,938,983,988,1000,897,969,952],
[1075,1053,1063,0,1039,1043,1057,994,1112,1016],
[1026,1053,1018,962,0,1092,964,1007,944,948],
[1001,999,1013,958,909,0,1009,949,966,1001],
[953,999,1001,944,1037,992,0,971,984,982],
[996,1055,1104,1007,994,1052,1030,0,968,931],
[1046,978,1032,889,1057,1035,1017,1033,0,1006],
[1023,1053,1049,985,1053,1000,1019,1070,995,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 88, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1013,1000,1000,985,978,1047,1060,924,955],
[988,0,1026,951,975,967,1041,1004,932,1022],
[1001,975,0,996,993,1003,1003,986,961,944],
[1001,1050,1005,0,1004,1014,1022,1027,944,937],
[1016,1026,1008,997,0,1039,1018,993,929,971],
[1023,1034,998,987,962,0,966,1031,1013,990],
[954,960,998,979,983,1035,0,1015,967,954],
[941,997,1015,974,1008,970,986,0,908,971],
[1077,1069,1040,1057,1072,988,1034,1093,0,1034],
[1046,979,1057,1064,1030,1011,1047,1030,967,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 89, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,950,965,965,962,990,978,957,989,937],
[1051,0,976,999,1029,987,1019,1007,989,987],
[1036,1025,0,1011,999,973,1022,981,994,1020],
[1036,1002,990,0,994,1002,983,983,989,1024],
[1039,972,1002,1007,0,993,996,959,974,998],
[1011,1014,1028,999,1008,0,998,977,978,1038],
[1023,982,979,1018,1005,1003,0,1009,972,1023],
[1044,994,1020,1018,1042,1024,992,0,1034,1032],
[1012,1012,1007,1012,1027,1023,1029,967,0,986],
[1064,1014,981,977,1003,963,978,969,1015,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 90, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1043,1037,1090,1030,1032,919,1014,1082,969],
[958,0,939,1002,1005,938,919,912,988,974],
[964,1062,0,1105,1005,1027,1020,987,1069,981],
[911,999,896,0,931,955,991,976,1036,912],
[971,996,996,1070,0,1023,962,1050,1011,953],
[969,1063,974,1046,978,0,975,976,1013,990],
[1082,1082,981,1010,1039,1026,0,1070,1106,1016],
[987,1089,1014,1025,951,1025,931,0,989,976],
[919,1013,932,965,990,988,895,1012,0,946],
[1032,1027,1020,1089,1048,1011,985,1025,1055,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 91, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1021,1030,1012,1001,966,1000,983,1002,988],
[980,0,1043,998,1029,987,985,977,976,1016],
[971,958,0,973,978,962,939,945,961,969],
[989,1003,1028,0,995,999,964,985,991,996],
[1000,972,1023,1006,0,1000,967,993,961,995],
[1035,1014,1039,1002,1001,0,983,996,1007,1002],
[1001,1016,1062,1037,1034,1018,0,998,1016,1049],
[1018,1024,1056,1016,1008,1005,1003,0,1000,1014],
[999,1025,1040,1010,1040,994,985,1001,0,1000],
[1013,985,1032,1005,1006,999,952,987,1001,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 92, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,999,1023,983,1003,1013,1056,1031,996,1017],
[1002,0,994,1007,982,1019,1034,1034,974,993],
[978,1007,0,1004,1030,991,1046,1046,991,1033],
[1018,994,997,0,1056,1019,1051,1033,1002,1050],
[998,1019,971,945,0,987,1019,1016,968,1026],
[988,982,1010,982,1014,0,985,1045,996,1003],
[945,967,955,950,982,1016,0,1023,956,981],
[970,967,955,968,985,956,978,0,952,1002],
[1005,1027,1010,999,1033,1005,1045,1049,0,1028],
[984,1008,968,951,975,998,1020,999,973,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 93, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,982,1008,960,1019,948,974,969,999,1001],
[1019,0,1011,1006,1056,1001,1020,1025,994,1009],
[993,990,0,1004,1032,1014,1043,993,1044,1028],
[1041,995,997,0,1044,1007,1002,1023,1025,1055],
[982,945,969,957,0,932,973,961,954,961],
[1053,1000,987,994,1069,0,1010,1019,1039,1015],
[1027,981,958,999,1028,991,0,956,988,978],
[1032,976,1008,978,1040,982,1045,0,1014,996],
[1002,1007,957,976,1047,962,1013,987,0,959],
[1000,992,973,946,1040,986,1023,1005,1042,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 94, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,944,982,973,971,969,989,981,990,995],
[1057,0,1020,1013,1002,992,1014,1009,1005,1016],
[1019,981,0,1006,988,1039,1024,988,1027,1013],
[1028,988,995,0,1012,1002,1007,1043,1003,1033],
[1030,999,1013,989,0,1007,1044,1014,1010,1007],
[1032,1009,962,999,994,0,1005,1012,993,1012],
[1012,987,977,994,957,996,0,1031,972,1009],
[1020,992,1013,958,987,989,970,0,977,998],
[1011,996,974,998,991,1008,1029,1024,0,1006],
[1006,985,988,968,994,989,992,1003,995,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 95, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,999,1028,1010,963,990,1030,955,1024,1011],
[1002,0,1013,954,981,972,1031,984,1056,993],
[973,988,0,974,964,1013,1002,1028,1034,963],
[991,1047,1027,0,1038,996,1020,1037,1064,1092],
[1038,1020,1037,963,0,1052,1072,1060,1061,1021],
[1011,1029,988,1005,949,0,1000,1014,1046,999],
[971,970,999,981,929,1001,0,987,980,1005],
[1046,1017,973,964,941,987,1014,0,1033,1027],
[977,945,967,937,940,955,1021,968,0,1059],
[990,1008,1038,909,980,1002,996,974,942,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 96, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1056,999,1019,1038,1022,1076,1032,1035,986],
[945,0,971,985,1021,965,974,1014,1012,948],
[1002,1030,0,1075,1108,1001,1116,1062,1029,983],
[982,1016,926,0,1020,976,1045,963,1027,988],
[963,980,893,981,0,958,1021,1019,1000,982],
[979,1036,1000,1025,1043,0,1021,1027,1026,995],
[925,1027,885,956,980,980,0,1047,937,885],
[969,987,939,1038,982,974,954,0,1011,1007],
[966,989,972,974,1001,975,1064,990,0,961],
[1015,1053,1018,1013,1019,1006,1116,994,1040,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 97, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1006,1007,1027,1028,1032,1017,1037,1000,991],
[995,0,1007,1021,1016,1038,976,1006,1027,1004],
[994,994,0,1045,1007,1041,1004,1008,1020,990],
[974,980,956,0,993,978,1005,1006,992,1014],
[973,985,994,1008,0,1003,982,998,981,999],
[969,963,960,1023,998,0,992,993,981,993],
[984,1025,997,996,1019,1009,0,1017,1025,992],
[964,995,993,995,1003,1008,984,0,1003,989],
[1001,974,981,1009,1020,1020,976,998,0,994],
[1010,997,1011,987,1002,1008,1009,1012,1007,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 98, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,991,967,1006,988,972,992,998,971,980],
[1010,0,969,986,946,961,993,975,983,963],
[1034,1032,0,1019,1007,1014,1021,982,1021,1037],
[995,1015,982,0,967,991,1002,975,991,959],
[1013,1055,994,1034,0,1004,987,977,1021,1007],
[1029,1040,987,1010,997,0,1024,1003,1007,1012],
[1009,1008,980,999,1014,977,0,955,1007,989],
[1003,1026,1019,1026,1024,998,1046,0,1025,1028],
[1030,1018,980,1010,980,994,994,976,0,1017],
[1021,1038,964,1042,994,989,1012,973,984,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 99, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1100,1031,1011,1017,1051,1024,1032,1030,996],
[901,0,964,1003,1016,1031,991,897,1018,930],
[970,1037,0,1080,1079,1023,992,1014,997,1036],
[990,998,921,0,1047,982,980,978,1017,956],
[984,985,922,954,0,998,1029,958,921,906],
[950,970,978,1019,1003,0,998,961,1008,970],
[977,1010,1009,1021,972,1003,0,1004,1049,959],
[969,1104,987,1023,1043,1040,997,0,1022,982],
[971,983,1004,984,1080,993,952,979,0,964],
[1005,1071,965,1045,1095,1031,1042,1019,1037,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 100, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1062,997,944,1147,1016,1052,1034,1039,1038],
[939,0,971,894,1006,952,909,966,902,1012],
[1004,1030,0,1023,1059,1011,1013,1050,972,1077],
[1057,1107,978,0,1133,1045,1107,1042,1071,1090],
[854,995,942,868,0,904,947,955,924,935],
[985,1049,990,956,1097,0,1013,1048,956,1046],
[949,1092,988,894,1054,988,0,1046,925,977],
[967,1035,951,959,1046,953,955,0,899,1024],
[962,1099,1029,930,1077,1045,1076,1102,0,1054],
[963,989,924,911,1066,955,1024,977,947,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 101, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1038,970,1024,965,1005,1000,1032,976,1028],
[963,0,954,976,935,957,984,960,964,975],
[1031,1047,0,1043,1021,1045,1012,1064,993,1014],
[977,1025,958,0,911,977,918,977,946,1005],
[1036,1066,980,1090,0,1040,1084,1064,1048,1006],
[996,1044,956,1024,961,0,1021,1015,1000,1010],
[1001,1017,989,1083,917,980,0,1002,949,1014],
[969,1041,937,1024,937,986,999,0,986,1019],
[1025,1037,1008,1055,953,1001,1052,1015,0,1030],
[973,1026,987,996,995,991,987,982,971,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 102, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,987,1009,1047,1136,1101,1030,1083,1042,1015],
[1014,0,1056,1116,1024,1054,1062,1047,1085,994],
[992,945,0,914,934,982,1021,947,975,976],
[954,885,1087,0,1026,1057,979,1002,1029,1024],
[865,977,1067,975,0,1095,1014,986,1056,1012],
[900,947,1019,944,906,0,966,928,1075,953],
[971,939,980,1022,987,1035,0,978,1019,885],
[918,954,1054,999,1015,1073,1023,0,1048,978],
[959,916,1026,972,945,926,982,953,0,919],
[986,1007,1025,977,989,1048,1116,1023,1082,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 103, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,991,1063,954,998,1022,1002,974,1006,1083],
[1010,0,1084,1041,1039,1025,1078,978,1050,1027],
[938,917,0,994,994,1017,998,1004,998,1020],
[1047,960,1007,0,1063,1030,994,997,1024,1047],
[1003,962,1007,938,0,989,1074,1053,989,1027],
[979,976,984,971,1012,0,1040,964,1021,1029],
[999,923,1003,1007,927,961,0,958,1003,1074],
[1027,1023,997,1004,948,1037,1043,0,1082,1048],
[995,951,1003,977,1012,980,998,919,0,967],
[918,974,981,954,974,972,927,953,1034,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 104, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1014,1017,1039,976,1014,999,976,993,1019],
[987,0,966,998,913,1024,957,915,1018,960],
[984,1035,0,943,915,986,963,923,917,916],
[962,1003,1058,0,965,1029,1003,947,991,982],
[1025,1088,1086,1036,0,1068,1033,1003,994,1033],
[987,977,1015,972,933,0,958,944,928,931],
[1002,1044,1038,998,968,1043,0,980,978,1022],
[1025,1086,1078,1054,998,1057,1021,0,1033,1014],
[1008,983,1084,1010,1007,1073,1023,968,0,1003],
[982,1041,1085,1019,968,1070,979,987,998,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 105, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,994,973,981,969,999,1027,986,977,995],
[1007,0,1009,993,982,992,979,987,987,1004],
[1028,992,0,992,1012,1024,978,985,994,1020],
[1020,1008,1009,0,1007,1032,972,977,1013,1023],
[1032,1019,989,994,0,1035,1033,1007,1021,1047],
[1002,1009,977,969,966,0,1003,969,966,1022],
[974,1022,1023,1029,968,998,0,982,994,1033],
[1015,1014,1016,1024,994,1032,1019,0,1014,1039],
[1024,1014,1007,988,980,1035,1007,987,0,1019],
[1006,997,981,978,954,979,968,962,982,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 106, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1006,1011,1072,995,1011,1022,1002,1023,995],
[995,0,1008,978,1045,973,1045,1009,951,978],
[990,993,0,1034,966,1055,1011,926,974,1005],
[929,1023,967,0,963,937,994,935,959,995],
[1006,956,1035,1038,0,1065,1012,979,962,1020],
[990,1028,946,1064,936,0,1011,977,954,1000],
[979,956,990,1007,989,990,0,946,972,1018],
[999,992,1075,1066,1022,1024,1055,0,1009,1046],
[978,1050,1027,1042,1039,1047,1029,992,0,1032],
[1006,1023,996,1006,981,1001,983,955,969,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 107, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,963,933,962,1002,961,964,950,985,999],
[1038,0,1007,1028,1072,990,976,977,1027,1037],
[1068,994,0,1015,1065,1035,1025,1043,1035,1015],
[1039,973,986,0,1034,987,949,964,1025,998],
[999,929,936,967,0,982,965,956,980,981],
[1040,1011,966,1014,1019,0,979,1022,1003,986],
[1037,1025,976,1052,1036,1022,0,1005,1030,1036],
[1051,1024,958,1037,1045,979,996,0,1031,999],
[1016,974,966,976,1021,998,971,970,0,992],
[1002,964,986,1003,1020,1015,965,1002,1009,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 108, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1015,965,929,1013,982,984,1016,1002,1003],
[986,0,967,990,989,950,975,1051,977,996],
[1036,1034,0,969,985,1074,967,1005,979,1012],
[1072,1011,1032,0,1011,1025,1039,997,1032,1043],
[988,1012,1016,990,0,1051,1033,1069,1011,988],
[1019,1051,927,976,950,0,1025,1025,997,1008],
[1017,1026,1034,962,968,976,0,1032,983,996],
[985,950,996,1004,932,976,969,0,1011,977],
[999,1024,1022,969,990,1004,1018,990,0,1005],
[998,1005,989,958,1013,993,1005,1024,996,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 109, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1020,987,1026,1021,1010,986,1007,1024,1000],
[981,0,999,993,995,1000,974,997,1028,972],
[1014,1002,0,1014,1016,1002,1014,1020,1038,992],
[975,1008,987,0,1016,1006,982,1006,1016,972],
[980,1006,985,985,0,988,973,1011,1006,988],
[991,1001,999,995,1013,0,974,1014,1013,981],
[1015,1027,987,1019,1028,1027,0,984,1017,1017],
[994,1004,981,995,990,987,1017,0,1016,983],
[977,973,963,985,995,988,984,985,0,971],
[1001,1029,1009,1029,1013,1020,984,1018,1030,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 110, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1034,1181,1061,900,1035,1058,1073,1179,1002],
[967,0,1117,1174,1053,1132,994,978,1062,1021],
[820,884,0,930,868,844,840,805,948,933],
[940,827,1071,0,980,881,986,941,1005,906],
[1101,948,1133,1021,0,996,1014,935,1109,1056],
[966,869,1157,1120,1005,0,998,878,1078,997],
[943,1007,1161,1015,987,1003,0,881,972,1012],
[928,1023,1196,1060,1066,1123,1120,0,1111,1056],
[822,939,1053,996,892,923,1029,890,0,930],
[999,980,1068,1095,945,1004,989,945,1071,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 111, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1010,1033,1027,1048,985,1023,1048,1081,988],
[991,0,994,1022,1059,1031,1079,986,1091,1027],
[968,1007,0,981,1015,985,972,1002,1029,948],
[974,979,1020,0,1016,963,985,1005,1002,983],
[953,942,986,985,0,998,965,1019,1040,958],
[1016,970,1016,1038,1003,0,987,1038,1017,996],
[978,922,1029,1016,1036,1014,0,1005,1066,1001],
[953,1015,999,996,982,963,996,0,1018,967],
[920,910,972,999,961,984,935,983,0,968],
[1013,974,1053,1018,1043,1005,1000,1034,1033,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 112, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1018,981,994,1008,1039,993,1013,996,1000],
[983,0,1015,957,1034,1025,960,1012,1016,994],
[1020,986,0,986,1026,1052,960,1027,1017,974],
[1007,1044,1015,0,1021,1053,1015,987,1005,1006],
[993,967,975,980,0,985,952,961,962,971],
[962,976,949,948,1016,0,965,1014,1001,984],
[1008,1041,1041,986,1049,1036,0,990,1026,1018],
[988,989,974,1014,1040,987,1011,0,992,997],
[1005,985,984,996,1039,1000,975,1009,0,974],
[1001,1007,1027,995,1030,1017,983,1004,1027,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 113, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1151,1058,1005,1006,1110,1072,867,1061,1049],
[850,0,849,1038,1015,929,1298,811,996,852],
[943,1152,0,1114,1124,1131,1175,849,1160,996],
[996,963,887,0,1073,894,1042,810,855,928],
[995,986,877,928,0,1166,984,884,993,883],
[891,1072,870,1107,835,0,972,724,926,882],
[929,703,826,959,1017,1029,0,816,726,734],
[1134,1190,1152,1191,1117,1277,1185,0,874,1094],
[940,1005,841,1146,1008,1075,1275,1127,0,985],
[952,1149,1005,1073,1118,1119,1267,907,1016,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 114, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,969,985,1005,1005,1015,989,985,985,1007],
[1032,0,1010,1018,1015,1046,1014,998,1030,1019],
[1016,991,0,1008,1019,1032,1032,1002,996,1027],
[996,983,993,0,1013,1026,1032,995,1042,986],
[996,986,982,988,0,1004,997,986,975,990],
[986,955,969,975,997,0,1037,953,991,996],
[1012,987,969,969,1004,964,0,960,1001,966],
[1016,1003,999,1006,1015,1048,1041,0,1004,1006],
[1016,971,1005,959,1026,1010,1000,997,0,992],
[994,982,974,1015,1011,1005,1035,995,1009,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 115, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,947,1056,980,1003,1000,946,995,992,1068],
[1054,0,1060,1028,998,1018,992,974,1001,1038],
[945,941,0,951,958,968,921,1009,972,1000],
[1021,973,1050,0,1004,976,1045,1025,1044,1080],
[998,1003,1043,997,0,1012,1008,1017,1010,1084],
[1001,983,1033,1025,989,0,980,1015,948,1037],
[1055,1009,1080,956,993,1021,0,1083,1031,1043],
[1006,1027,992,976,984,986,918,0,1005,1070],
[1009,1000,1029,957,991,1053,970,996,0,1077],
[933,963,1001,921,917,964,958,931,924,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 116, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,994,981,1003,971,966,990,1013,1018,998],
[1007,0,1009,1045,1007,996,1037,1032,1044,1010],
[1020,992,0,984,997,1003,965,1019,1022,991],
[998,956,1017,0,991,974,1007,1002,1037,986],
[1030,994,1004,1010,0,995,984,1026,1026,1023],
[1035,1005,998,1027,1006,0,1020,1025,1030,1012],
[1011,964,1036,994,1017,981,0,1022,1002,996],
[988,969,982,999,975,976,979,0,1012,970],
[983,957,979,964,975,971,999,989,0,999],
[1003,991,1010,1015,978,989,1005,1031,1002,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 117, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1027,983,989,977,996,1015,997,1009,1004],
[974,0,960,976,978,935,994,970,1003,964],
[1018,1041,0,983,999,991,1009,988,1005,995],
[1012,1025,1018,0,989,967,998,997,1005,992],
[1024,1023,1002,1012,0,1005,1014,999,1027,1012],
[1005,1066,1010,1034,996,0,999,1008,1003,1013],
[986,1007,992,1003,987,1002,0,983,1029,1008],
[1004,1031,1013,1004,1002,993,1018,0,1020,1017],
[992,998,996,996,974,998,972,981,0,994],
[997,1037,1006,1009,989,988,993,984,1007,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 118, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1016,987,990,994,981,994,996,1009,1017],
[985,0,972,1010,983,1010,1009,1002,1020,984],
[1014,1029,0,1030,1001,999,1006,1042,1015,998],
[1011,991,971,0,991,978,1012,997,994,996],
[1007,1018,1000,1010,0,1039,1008,1003,1012,997],
[1020,991,1002,1023,962,0,1026,979,989,1004],
[1007,992,995,989,993,975,0,990,1005,981],
[1005,999,959,1004,998,1022,1011,0,982,982],
[992,981,986,1007,989,1012,996,1019,0,974],
[984,1017,1003,1005,1004,997,1020,1019,1027,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 119, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,837,1415,972,932,932,556,816,346,953],
[1164,0,1069,788,586,748,956,1043,813,1164],
[586,932,0,1023,586,586,535,535,397,586],
[1029,1213,978,0,1213,1218,1167,816,743,1564],
[1069,1415,1415,788,0,1466,1604,1064,767,1812],
[1069,1253,1415,783,535,0,1323,1064,762,1720],
[1445,1045,1466,834,397,678,0,627,397,1445],
[1185,958,1466,1185,937,937,1374,0,1164,1374],
[1655,1188,1604,1258,1234,1239,1604,837,0,2001],
[1048,837,1415,437,189,281,556,627,0,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 120, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1029,1020,941,1007,1024,1086,951,942,947],
[972,0,994,954,974,992,1054,1008,946,978],
[981,1007,0,960,1003,1055,1068,929,932,996],
[1060,1047,1041,0,1140,1058,1091,988,1015,999],
[994,1027,998,861,0,1024,1053,987,984,975],
[977,1009,946,943,977,0,1085,990,990,963],
[915,947,933,910,948,916,0,908,942,952],
[1050,993,1072,1013,1014,1011,1093,0,1011,1067],
[1059,1055,1069,986,1017,1011,1059,990,0,957],
[1054,1023,1005,1002,1026,1038,1049,934,1044,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 121, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1023,1018,1014,999,981,1008,1014,991,1013],
[978,0,1003,994,989,980,1015,1010,998,1033],
[983,998,0,1000,993,982,972,1014,996,1005],
[987,1007,1001,0,1017,1004,986,993,975,1016],
[1002,1012,1008,984,0,1013,1004,1030,964,1037],
[1020,1021,1019,997,988,0,1023,1000,974,1016],
[993,986,1029,1015,997,978,0,988,987,1017],
[987,991,987,1008,971,1001,1013,0,1005,1027],
[1010,1003,1005,1026,1037,1027,1014,996,0,1028],
[988,968,996,985,964,985,984,974,973,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 122, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,992,980,950,995,954,1025,994,963,993],
[1009,0,948,1014,981,984,959,1005,986,1013],
[1021,1053,0,1014,998,1007,1063,1040,1035,1066],
[1051,987,987,0,1005,1019,1092,1033,1020,1056],
[1006,1020,1003,996,0,992,1014,1017,1009,1022],
[1047,1017,994,982,1009,0,1012,1023,1007,1049],
[976,1042,938,909,987,989,0,999,943,1026],
[1007,996,961,968,984,978,1002,0,998,1043],
[1038,1015,966,981,992,994,1058,1003,0,1011],
[1008,988,935,945,979,952,975,958,990,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 123, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,994,989,953,994,978,1028,987,975,990],
[1007,0,1010,974,1007,981,1014,975,985,995],
[1012,991,0,1000,1013,983,1044,990,1006,1016],
[1048,1027,1001,0,1037,988,1040,963,997,1021],
[1007,994,988,964,0,992,983,981,963,1009],
[1023,1020,1018,1013,1009,0,1032,991,982,1018],
[973,987,957,961,1018,969,0,949,948,981],
[1014,1026,1011,1038,1020,1010,1052,0,968,1018],
[1026,1016,995,1004,1038,1019,1053,1033,0,1026],
[1011,1006,985,980,992,983,1020,983,975,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 124, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1005,977,1027,1005,983,995,1019,1008,1034],
[996,0,1017,994,1028,1018,1032,1005,1040,1041],
[1024,984,0,970,1008,990,1026,993,988,1038],
[974,1007,1031,0,1062,989,986,981,975,1034],
[996,973,993,939,0,963,997,992,1010,962],
[1018,983,1011,1012,1038,0,1005,966,1048,994],
[1006,969,975,1015,1004,996,0,1029,999,952],
[982,996,1008,1020,1009,1035,972,0,994,1019],
[993,961,1013,1026,991,953,1002,1007,0,985],
[967,960,963,967,1039,1007,1049,982,1016,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 125, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,965,978,966,974,993,981,979,976,947],
[1036,0,967,987,986,1003,1003,1045,1075,1013],
[1023,1034,0,966,965,975,996,978,979,950],
[1035,1014,1035,0,1007,986,1012,1058,1033,991],
[1027,1015,1036,994,0,991,1007,1022,1005,996],
[1008,998,1026,1015,1010,0,1017,1007,984,989],
[1020,998,1005,989,994,984,0,1005,1000,1026],
[1022,956,1023,943,979,994,996,0,979,973],
[1025,926,1022,968,996,1017,1001,1022,0,969],
[1054,988,1051,1010,1005,1012,975,1028,1032,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 126, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1009,1030,1041,1058,1045,998,1032,1024,991],
[992,0,1005,1032,1006,1035,984,996,999,1031],
[971,996,0,983,1015,1007,1007,970,975,982],
[960,969,1018,0,1018,970,962,987,1011,975],
[943,995,986,983,0,1005,963,1016,995,992],
[956,966,994,1031,996,0,951,999,980,1004],
[1003,1017,994,1039,1038,1050,0,984,1022,986],
[969,1005,1031,1014,985,1002,1017,0,1016,1000],
[977,1002,1026,990,1006,1021,979,985,0,961],
[1010,970,1019,1026,1009,997,1015,1001,1040,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 127, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,984,1013,976,970,1063,976,1053,1011,1010],
[1017,0,1028,1025,995,1001,975,1014,1010,939],
[988,973,0,977,968,1003,950,1026,960,967],
[1025,976,1024,0,945,1047,926,1036,1001,968],
[1031,1006,1033,1056,0,1106,978,1100,1069,989],
[938,1000,998,954,895,0,918,1000,1012,951],
[1025,1026,1051,1075,1023,1083,0,1069,1044,994],
[948,987,975,965,901,1001,932,0,953,930],
[990,991,1041,1000,932,989,957,1048,0,963],
[991,1062,1034,1033,1012,1050,1007,1071,1038,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 128, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,834,1023,936,899,1011,922,813,925,981],
[1167,0,1081,1024,1022,1024,934,867,1032,1068],
[978,920,0,925,998,947,923,821,891,919],
[1065,977,1076,0,1001,1077,1020,988,979,1060],
[1102,979,1003,1000,0,1007,1037,912,1040,956],
[990,977,1054,924,994,0,1002,995,948,1042],
[1079,1067,1078,981,964,999,0,1004,1005,956],
[1188,1134,1180,1013,1089,1006,997,0,923,1045],
[1076,969,1110,1022,961,1053,996,1078,0,989],
[1020,933,1082,941,1045,959,1045,956,1012,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 129, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,958,1035,924,988,929,1002,979,1035,1019],
[1043,0,1018,997,1009,1018,1051,971,1089,1056],
[966,983,0,961,1006,942,987,910,984,1032],
[1077,1004,1040,0,1077,962,1033,994,1057,1052],
[1013,992,995,924,0,952,1002,947,990,998],
[1072,983,1059,1039,1049,0,1041,1027,1061,1060],
[999,950,1014,968,999,960,0,964,959,1046],
[1022,1030,1091,1007,1054,974,1037,0,1046,1087],
[966,912,1017,944,1011,940,1042,955,0,978],
[982,945,969,949,1003,941,955,914,1023,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 130, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1022,1030,967,969,1025,970,968,1022,971],
[979,0,1004,936,981,947,1012,940,1000,966],
[971,997,0,982,957,994,961,956,993,926],
[1034,1065,1019,0,986,985,981,1019,1013,1043],
[1032,1020,1044,1015,0,1040,1005,979,1051,1011],
[976,1054,1007,1016,961,0,1011,985,1001,1001],
[1031,989,1040,1020,996,990,0,966,1013,998],
[1033,1061,1045,982,1022,1016,1035,0,1033,1008],
[979,1001,1008,988,950,1000,988,968,0,960],
[1030,1035,1075,958,990,1000,1003,993,1041,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 131, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1005,1032,1035,990,1024,1041,1009,989,1006],
[996,0,987,982,951,994,998,981,947,988],
[969,1014,0,1047,976,1025,1015,1005,983,989],
[966,1019,954,0,947,941,1017,1014,983,992],
[1011,1050,1025,1054,0,1018,1051,1113,1020,1000],
[977,1007,976,1060,983,0,1032,1035,1003,1022],
[960,1003,986,984,950,969,0,998,945,983],
[992,1020,996,987,888,966,1003,0,953,971],
[1012,1054,1018,1018,981,998,1056,1048,0,979],
[995,1013,1012,1009,1001,979,1018,1030,1022,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 132, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,999,985,974,1019,951,1009,961,1027,1015],
[1002,0,957,946,992,963,1027,866,975,945],
[1016,1044,0,1001,982,1025,1053,1037,1050,1058],
[1027,1055,1000,0,1015,1027,1039,1024,1068,1058],
[982,1009,1019,986,0,1023,1031,996,1050,1004],
[1050,1038,976,974,978,0,1027,997,1013,979],
[992,974,948,962,970,974,0,982,977,905],
[1040,1135,964,977,1005,1004,1019,0,1067,975],
[974,1026,951,933,951,988,1024,934,0,1042],
[986,1056,943,943,997,1022,1096,1026,959,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 133, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,945,1028,980,958,997,972,938,993,988],
[1056,0,967,990,992,978,988,957,1007,978],
[973,1034,0,985,967,977,960,956,973,1009],
[1021,1011,1016,0,985,1002,1041,977,1011,999],
[1043,1009,1034,1016,0,1020,1001,1005,1002,948],
[1004,1023,1024,999,981,0,947,954,968,1010],
[1029,1013,1041,960,1000,1054,0,952,987,1012],
[1063,1044,1045,1024,996,1047,1049,0,1050,1054],
[1008,994,1028,990,999,1033,1014,951,0,1010],
[1013,1023,992,1002,1053,991,989,947,991,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 134, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,922,1089,1128,994,1008,1008,970,895,927],
[1079,0,1086,1181,997,964,1005,971,1033,1016],
[912,915,0,1057,1042,985,1000,935,972,935],
[873,820,944,0,840,847,858,868,908,861],
[1007,1004,959,1161,0,958,999,908,1048,1068],
[993,1037,1016,1154,1043,0,961,991,1010,932],
[993,996,1001,1143,1002,1040,0,1087,980,997],
[1031,1030,1066,1133,1093,1010,914,0,1090,1069],
[1106,968,1029,1093,953,991,1021,911,0,985],
[1074,985,1066,1140,933,1069,1004,932,1016,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 135, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1080,933,933,949,975,1132,937,988,955],
[921,0,926,880,959,1017,999,1011,1030,957],
[1068,1075,0,1114,1024,1150,1111,912,1122,1132],
[1068,1121,887,0,1020,1124,1025,980,1115,961],
[1052,1042,977,981,0,959,1029,930,1021,1156],
[1026,984,851,877,1042,0,1046,979,1119,1138],
[869,1002,890,976,972,955,0,919,892,918],
[1064,990,1089,1021,1071,1022,1082,0,1022,1067],
[1013,971,879,886,980,882,1109,979,0,889],
[1046,1044,869,1040,845,863,1083,934,1112,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 136, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1151,977,1144,1149,1070,1072,979,979,970],
[850,0,883,1017,1048,1058,1112,933,1022,1058],
[1024,1118,0,1150,1061,1054,998,1067,1034,907],
[857,984,851,0,1033,1067,949,904,969,864],
[852,953,940,968,0,953,937,844,1033,879],
[931,943,947,934,1048,0,999,1049,979,951],
[929,889,1003,1052,1064,1002,0,959,1066,841],
[1022,1068,934,1097,1157,952,1042,0,1044,939],
[1022,979,967,1032,968,1022,935,957,0,919],
[1031,943,1094,1137,1122,1050,1160,1062,1082,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 137, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1022,1018,989,971,990,1017,1059,1024,1049],
[979,0,996,963,986,1010,1001,1060,992,1013],
[983,1005,0,958,927,949,981,1022,963,1008],
[1012,1038,1043,0,1003,1000,1033,1050,992,1008],
[1030,1015,1074,998,0,983,1060,1090,1047,1049],
[1011,991,1052,1001,1018,0,1036,1043,1003,1020],
[984,1000,1020,968,941,965,0,999,1004,995],
[942,941,979,951,911,958,1002,0,936,955],
[977,1009,1038,1009,954,998,997,1065,0,1028],
[952,988,993,993,952,981,1006,1046,973,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 138, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,964,1022,979,978,1005,994,977,975,1021],
[1037,0,1022,992,1042,1021,1019,1010,1018,1022],
[979,979,0,992,986,1000,970,1001,982,991],
[1022,1009,1009,0,976,996,1033,1025,971,1033],
[1023,959,1015,1025,0,974,972,1038,1005,1001],
[996,980,1001,1005,1027,0,985,997,1039,1016],
[1007,982,1031,968,1029,1016,0,1003,1001,996],
[1024,991,1000,976,963,1004,998,0,1024,1014],
[1026,983,1019,1030,996,962,1000,977,0,998],
[980,979,1010,968,1000,985,1005,987,1003,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 139, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1013,984,1010,1033,1014,1041,1016,1015,996],
[988,0,1004,1003,1018,982,1002,987,961,970],
[1017,997,0,1035,1059,993,1033,978,988,1021],
[991,998,966,0,1011,969,1004,978,975,973],
[968,983,942,990,0,985,1010,974,962,972],
[987,1019,1008,1032,1016,0,1018,975,992,995],
[960,999,968,997,991,983,0,947,981,994],
[985,1014,1023,1023,1027,1026,1054,0,1000,1021],
[986,1040,1013,1026,1039,1009,1020,1001,0,1007],
[1005,1031,980,1028,1029,1006,1007,980,994,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 140, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,985,983,983,943,936,967,973,1017,1020],
[1016,0,997,1004,989,959,1012,1007,1046,1004],
[1018,1004,0,981,994,975,1005,1020,1050,1012],
[1018,997,1020,0,981,978,962,1025,1027,1057],
[1058,1012,1007,1020,0,1039,1005,998,1057,1010],
[1065,1042,1026,1023,962,0,1029,1003,1056,1006],
[1034,989,996,1039,996,972,0,988,1021,1012],
[1028,994,981,976,1003,998,1013,0,1051,1009],
[984,955,951,974,944,945,980,950,0,964],
[981,997,989,944,991,995,989,992,1037,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 141, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1054,1025,994,1026,1016,1021,1034,1004,1022],
[947,0,1010,1040,1022,1023,994,1010,1025,1037],
[976,991,0,1002,985,973,937,1007,993,987],
[1007,961,999,0,996,994,993,1037,1016,986],
[975,979,1016,1005,0,984,967,1010,987,972],
[985,978,1028,1007,1017,0,974,1055,995,1020],
[980,1007,1064,1008,1034,1027,0,1057,1005,1060],
[967,991,994,964,991,946,944,0,991,971],
[997,976,1008,985,1014,1006,996,1010,0,992],
[979,964,1014,1015,1029,981,941,1030,1009,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 142, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,989,978,1025,1024,1012,1008,991,995,991],
[1012,0,1023,988,1025,1045,1058,1003,1025,1031],
[1023,978,0,996,974,1006,1022,1010,1040,998],
[976,1013,1005,0,1025,1038,1025,1004,1042,990],
[977,976,1027,976,0,1032,972,1008,985,967],
[989,956,995,963,969,0,1026,1014,992,989],
[993,943,979,976,1029,975,0,1006,1047,973],
[1010,998,991,997,993,987,995,0,992,992],
[1006,976,961,959,1016,1009,954,1009,0,993],
[1010,970,1003,1011,1034,1012,1028,1009,1008,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 143, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,973,1016,980,972,1007,1027,1044,979,938],
[1028,0,1009,1004,969,986,983,1006,984,921],
[985,992,0,1000,978,1001,1048,1071,1043,1030],
[1021,997,1001,0,940,999,973,1031,994,970],
[1029,1032,1023,1061,0,1061,1036,1051,1050,984],
[994,1015,1000,1002,940,0,1012,999,964,959],
[974,1018,953,1028,965,989,0,1018,975,952],
[957,995,930,970,950,1002,983,0,958,920],
[1022,1017,958,1007,951,1037,1026,1043,0,960],
[1063,1080,971,1031,1017,1042,1049,1081,1041,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 144, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1002,1107,1046,1020,1046,1023,1032,993,989],
[999,0,1042,922,942,993,962,987,982,955],
[894,959,0,936,961,996,986,929,941,964],
[955,1079,1065,0,978,1025,974,1031,1002,1041],
[981,1059,1040,1023,0,1036,1010,1056,1036,1046],
[955,1008,1005,976,965,0,1002,997,991,1016],
[978,1039,1015,1027,991,999,0,992,986,988],
[969,1014,1072,970,945,1004,1009,0,934,992],
[1008,1019,1060,999,965,1010,1015,1067,0,984],
[1012,1046,1037,960,955,985,1013,1009,1017,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 145, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1004,1039,972,966,1029,1016,1048,1025,1044],
[997,0,1034,971,988,980,995,987,1023,1001],
[962,967,0,971,953,948,983,964,993,988],
[1029,1030,1030,0,993,991,999,1007,1014,1027],
[1035,1013,1048,1008,0,1009,1049,1069,993,1041],
[972,1021,1053,1010,992,0,1011,1027,1014,1028],
[985,1006,1018,1002,952,990,0,1010,1004,1029],
[953,1014,1037,994,932,974,991,0,1006,1012],
[976,978,1008,987,1008,987,997,995,0,1021],
[957,1000,1013,974,960,973,972,989,980,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 146, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1002,1036,959,1006,982,936,915,963,1069],
[999,0,1038,935,1021,1010,951,982,1061,1072],
[965,963,0,971,1025,980,1047,934,955,1045],
[1042,1066,1030,0,1065,1056,1021,950,997,1101],
[995,980,976,936,0,987,982,943,992,1069],
[1019,991,1021,945,1014,0,963,946,960,1065],
[1065,1050,954,980,1019,1038,0,932,967,1090],
[1086,1019,1067,1051,1058,1055,1069,0,959,1136],
[1038,940,1046,1004,1009,1041,1034,1042,0,1025],
[932,929,956,900,932,936,911,865,976,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 147, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,601,1022,562,658,813,795,764,696,874],
[1400,0,1199,1003,952,1201,1023,877,1201,1118],
[979,802,0,746,766,889,804,578,880,856],
[1439,998,1255,0,1012,1105,1260,1065,1097,1108],
[1343,1049,1235,989,0,1209,1066,1129,1146,1165],
[1188,800,1112,896,792,0,1091,1082,962,1110],
[1206,978,1197,741,935,910,0,942,942,1017],
[1237,1124,1423,936,872,919,1059,0,1186,1181],
[1305,800,1121,904,855,1039,1059,815,0,1020],
[1127,883,1145,893,836,891,984,820,981,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 148, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1390,1478,1128,1171,979,993,1143,1173,1329],
[611,0,914,908,682,856,904,428,842,1029],
[523,1087,0,837,937,1165,887,803,1033,1092],
[873,1093,1164,0,985,1161,1057,1194,1145,1267],
[830,1319,1064,1016,0,1204,1066,1093,874,1208],
[1022,1145,836,840,797,0,968,717,1366,1211],
[1008,1097,1114,944,935,1033,0,759,865,910],
[858,1573,1198,807,908,1284,1242,0,1093,931],
[828,1159,968,856,1127,635,1136,908,0,1110],
[672,972,909,734,793,790,1091,1070,891,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 149, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,973,957,1023,998,1027,978,946,982,999],
[1028,0,1005,1006,1002,1046,1004,1026,965,964],
[1044,996,0,1052,1009,1075,1016,1018,976,983],
[978,995,949,0,949,993,980,989,950,958],
[1003,999,992,1052,0,1039,992,991,986,1007],
[974,955,926,1008,962,0,981,973,950,961],
[1023,997,985,1021,1009,1020,0,993,994,967],
[1055,975,983,1012,1010,1028,1008,0,1011,1002],
[1019,1036,1025,1051,1015,1051,1007,990,0,986],
[1002,1037,1018,1043,994,1040,1034,999,1015,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 150, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1001,1026,993,1020,1046,946,974,1006,988],
[1000,0,1038,1021,1041,1013,988,972,987,1002],
[975,963,0,1007,1025,1005,949,956,963,1015],
[1008,980,994,0,1012,980,962,967,962,977],
[981,960,976,989,0,994,956,981,991,1004],
[955,988,996,1021,1007,0,940,961,974,1010],
[1055,1013,1052,1039,1045,1061,0,1005,996,1013],
[1027,1029,1045,1034,1020,1040,996,0,1017,1038],
[995,1014,1038,1039,1010,1027,1005,984,0,1006],
[1013,999,986,1024,997,991,988,963,995,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 151, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,979,1035,1041,1007,1009,975,944,1039,1025],
[1022,0,1020,995,980,970,927,955,1030,1015],
[966,981,0,947,956,994,907,946,962,939],
[960,1006,1054,0,985,1053,930,967,1094,1015],
[994,1021,1045,1016,0,999,1025,954,1032,1046],
[992,1031,1007,948,1002,0,970,965,1016,974],
[1026,1074,1094,1071,976,1031,0,1004,1042,1069],
[1057,1046,1055,1034,1047,1036,997,0,1018,1047],
[962,971,1039,907,969,985,959,983,0,1004],
[976,986,1062,986,955,1027,932,954,997,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 152, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,994,993,963,1050,1088,1079,1128,1021,1089],
[1007,0,1013,1032,1117,990,1032,1125,1061,1029],
[1008,988,0,1044,1058,1012,1081,1076,953,1074],
[1038,969,957,0,1025,1004,1001,1036,1011,1004],
[951,884,943,976,0,908,1002,1008,932,1000],
[913,1011,989,997,1093,0,1012,1056,944,1043],
[922,969,920,1000,999,989,0,1057,960,1066],
[873,876,925,965,993,945,944,0,947,996],
[980,940,1048,990,1069,1057,1041,1054,0,1043],
[912,972,927,997,1001,958,935,1005,958,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 153, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1018,992,990,977,984,986,1009,978,987],
[983,0,985,985,1001,1011,980,973,959,966],
[1009,1016,0,961,1038,1022,960,1011,992,995],
[1011,1016,1040,0,1001,1035,979,1020,1028,992],
[1024,1000,963,1000,0,983,944,997,999,951],
[1017,990,979,966,1018,0,964,996,994,1004],
[1015,1021,1041,1022,1057,1037,0,1064,1038,995],
[992,1028,990,981,1004,1005,937,0,1004,967],
[1023,1042,1009,973,1002,1007,963,997,0,996],
[1014,1035,1006,1009,1050,997,1006,1034,1005,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 154, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1015,969,1031,990,973,1041,975,984,1003],
[986,0,972,1018,1018,954,1008,985,1044,1006],
[1032,1029,0,1056,1072,1021,1091,1041,996,1065],
[970,983,945,0,1004,936,999,1014,995,1038],
[1011,983,929,997,0,1037,1020,977,1003,1016],
[1028,1047,980,1065,964,0,1037,1024,1034,1040],
[960,993,910,1002,981,964,0,977,974,1000],
[1026,1016,960,987,1024,977,1024,0,987,1041],
[1017,957,1005,1006,998,967,1027,1014,0,1041],
[998,995,936,963,985,961,1001,960,960,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 155, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1074,1049,1038,1033,1012,992,1031,1057,1019],
[927,0,1020,1045,1045,1045,950,1012,1041,954],
[952,981,0,903,989,923,979,949,973,907],
[963,956,1098,0,1063,1094,1053,996,977,1005],
[968,956,1012,938,0,949,991,967,960,974],
[989,956,1078,907,1052,0,983,932,1074,982],
[1009,1051,1022,948,1010,1018,0,1051,1061,1010],
[970,989,1052,1005,1034,1069,950,0,1000,997],
[944,960,1028,1024,1041,927,940,1001,0,956],
[982,1047,1094,996,1027,1019,991,1004,1045,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 156, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1030,996,1007,1014,1050,1020,979,1038,999],
[971,0,996,1042,1028,988,1022,967,1004,1006],
[1005,1005,0,1065,1056,1042,1030,1007,1005,983],
[994,959,936,0,980,976,1001,913,935,951],
[987,973,945,1021,0,1026,1021,948,959,985],
[951,1013,959,1025,975,0,1045,973,1036,982],
[981,979,971,1000,980,956,0,933,1008,954],
[1022,1034,994,1088,1053,1028,1068,0,1029,959],
[963,997,996,1066,1042,965,993,972,0,966],
[1002,995,1018,1050,1016,1019,1047,1042,1035,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 157, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,989,922,1015,1063,949,937,1005,921,957],
[1012,0,954,1057,1139,1025,977,1035,1011,1043],
[1079,1047,0,1043,1142,976,1062,1050,1065,1031],
[986,944,958,0,1026,948,961,936,977,963],
[938,862,859,975,0,902,918,1003,983,932],
[1052,976,1025,1053,1099,0,995,1047,1109,1023],
[1064,1024,939,1040,1083,1006,0,1038,1072,985],
[996,966,951,1065,998,954,963,0,973,987],
[1080,990,936,1024,1018,892,929,1028,0,953],
[1044,958,970,1038,1069,978,1016,1014,1048,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 158, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1052,1036,1068,1029,1000,1002,998,1017,1023],
[949,0,1011,956,990,981,974,954,995,1013],
[965,990,0,997,967,978,977,996,970,1010],
[933,1045,1004,0,1013,980,1000,984,1004,1007],
[972,1011,1034,988,0,1007,1020,989,995,1027],
[1001,1020,1023,1021,994,0,1038,979,1019,1020],
[999,1027,1024,1001,981,963,0,1022,1009,1059],
[1003,1047,1005,1017,1012,1022,979,0,1018,1047],
[984,1006,1031,997,1006,982,992,983,0,1019],
[978,988,991,994,974,981,942,954,982,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 159, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,999,1009,970,992,982,996,1031,1000,998],
[1002,0,1015,988,998,985,1025,1031,1010,1011],
[992,986,0,985,970,995,1008,1050,997,989],
[1031,1013,1016,0,1015,979,1021,1036,1002,979],
[1009,1003,1031,986,0,994,1013,1019,959,985],
[1019,1016,1006,1022,1007,0,1022,1038,994,1023],
[1005,976,993,980,988,979,0,1005,976,971],
[970,970,951,965,982,963,996,0,942,971],
[1001,991,1004,999,1042,1007,1025,1059,0,1011],
[1003,990,1012,1022,1016,978,1030,1030,990,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 160, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1007,907,858,991,877,1010,1051,833,917],
[994,0,912,812,885,863,891,799,761,873],
[1094,1089,0,888,1008,935,997,1043,1037,915],
[1143,1189,1113,0,995,1046,1089,1066,1038,957],
[1010,1116,993,1006,0,1035,940,1100,954,941],
[1124,1138,1066,955,966,0,964,1004,846,1008],
[991,1110,1004,912,1061,1037,0,1035,790,909],
[950,1202,958,935,901,997,966,0,993,1080],
[1168,1240,964,963,1047,1155,1211,1008,0,1039],
[1084,1128,1086,1044,1060,993,1092,921,962,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 161, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,960,970,941,983,958,972,969,1000,996],
[1041,0,996,1000,1014,1008,1020,1020,1065,1000],
[1031,1005,0,971,989,998,970,998,1005,972],
[1060,1001,1030,0,999,1012,1006,1046,1047,1013],
[1018,987,1012,1002,0,997,973,1007,1039,1000],
[1043,993,1003,989,1004,0,994,1009,997,993],
[1029,981,1031,995,1028,1007,0,1035,1012,1007],
[1032,981,1003,955,994,992,966,0,1008,1029],
[1001,936,996,954,962,1004,989,993,0,985],
[1005,1001,1029,988,1001,1008,994,972,1016,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 162, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,979,931,982,914,932,1016,939,860,866],
[1022,0,1044,1043,1020,968,1106,906,961,967],
[1070,957,0,959,928,950,1065,924,973,1002],
[1019,958,1042,0,957,904,1019,894,967,951],
[1087,981,1073,1044,0,1011,1091,966,1007,951],
[1069,1033,1051,1097,990,0,1181,1009,981,1040],
[985,895,936,982,910,820,0,840,923,903],
[1062,1095,1077,1107,1035,992,1161,0,1103,1028],
[1141,1040,1028,1034,994,1020,1078,898,0,958],
[1135,1034,999,1050,1050,961,1098,973,1043,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 163, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1004,1008,1010,991,1017,1013,994,1044,1052],
[997,0,1000,1064,996,980,967,1005,998,1002],
[993,1001,0,1030,974,1022,968,978,1020,1014],
[991,937,971,0,967,959,989,965,1020,977],
[1010,1005,1027,1034,0,1038,991,1001,1002,981],
[984,1021,979,1042,963,0,1004,998,1032,975],
[988,1034,1033,1012,1010,997,0,992,1025,1036],
[1007,996,1023,1036,1000,1003,1009,0,1011,995],
[957,1003,981,981,999,969,976,990,0,987],
[949,999,987,1024,1020,1026,965,1006,1014,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 164, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,944,927,939,937,846,973,913,855,901],
[1057,0,984,885,868,1049,1006,928,987,1019],
[1074,1017,0,970,1049,1068,1067,1014,952,1064],
[1062,1116,1031,0,928,1007,978,1095,923,1073],
[1064,1133,952,1073,0,1011,1046,1045,1037,937],
[1155,952,933,994,990,0,986,996,949,914],
[1028,995,934,1023,955,1015,0,1011,956,988],
[1088,1073,987,906,956,1005,990,0,1020,1063],
[1146,1014,1049,1078,964,1052,1045,981,0,1087],
[1100,982,937,928,1064,1087,1013,938,914,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 165, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,998,982,959,969,955,976,941,943,939],
[1003,0,1059,1022,980,1004,1002,978,982,952],
[1019,942,0,934,947,984,958,969,973,963],
[1042,979,1067,0,1007,1028,993,1023,980,983],
[1032,1021,1054,994,0,953,1007,972,946,969],
[1046,997,1017,973,1048,0,1017,981,944,985],
[1025,999,1043,1008,994,984,0,1003,970,1011],
[1060,1023,1032,978,1029,1020,998,0,967,1015],
[1058,1019,1028,1021,1055,1057,1031,1034,0,997],
[1062,1049,1038,1018,1032,1016,990,986,1004,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 166, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,927,966,860,989,1008,868,931,864,995],
[1074,0,1039,985,1064,1036,964,1013,935,1038],
[1035,962,0,1000,1058,1051,976,1040,986,973],
[1141,1016,1001,0,1059,1005,1010,997,987,1006],
[1012,937,943,942,0,947,910,1015,920,994],
[993,965,950,996,1054,0,980,948,1009,951],
[1133,1037,1025,991,1091,1021,0,1069,971,988],
[1070,988,961,1004,986,1053,932,0,916,941],
[1137,1066,1015,1014,1081,992,1030,1085,0,1029],
[1006,963,1028,995,1007,1050,1013,1060,972,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 167, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1017,974,1013,990,1046,951,969,960,967],
[984,0,1034,981,990,1067,993,1015,1005,990],
[1027,967,0,1024,996,1040,952,978,996,992],
[988,1020,977,0,1003,1066,987,979,1029,1032],
[1011,1011,1005,998,0,1032,1047,973,1000,977],
[955,934,961,935,969,0,963,983,937,986],
[1050,1008,1049,1014,954,1038,0,1012,1009,1054],
[1032,986,1023,1022,1028,1018,989,0,1033,1008],
[1041,996,1005,972,1001,1064,992,968,0,1005],
[1034,1011,1009,969,1024,1015,947,993,996,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 168, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,999,1021,1038,991,1017,1046,1001,1057,1014],
[1002,0,951,990,1012,1016,1047,961,1030,973],
[980,1050,0,1013,1007,1065,991,998,1022,1040],
[963,1011,988,0,1007,1013,1008,959,978,1006],
[1010,989,994,994,0,1012,1029,964,989,986],
[984,985,936,988,989,0,962,994,1003,986],
[955,954,1010,993,972,1039,0,951,974,997],
[1000,1040,1003,1042,1037,1007,1050,0,1015,1032],
[944,971,979,1023,1012,998,1027,986,0,1001],
[987,1028,961,995,1015,1015,1004,969,1000,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 169, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1033,1003,1052,1007,1018,976,1012,961,1001],
[968,0,994,1004,986,984,946,907,915,943],
[998,1007,0,1091,965,1049,981,1054,979,1007],
[949,997,910,0,953,978,932,955,922,972],
[994,1015,1036,1048,0,987,1000,986,955,974],
[983,1017,952,1023,1014,0,946,1016,988,978],
[1025,1055,1020,1069,1001,1055,0,980,1009,980],
[989,1094,947,1046,1015,985,1021,0,955,1019],
[1040,1086,1022,1079,1046,1013,992,1046,0,985],
[1000,1058,994,1029,1027,1023,1021,982,1016,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 170, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1008,1060,1002,986,886,988,1028,1048,1035],
[993,0,1098,1009,1022,987,1039,1061,1004,1017],
[941,903,0,890,956,876,972,1023,980,935],
[999,992,1111,0,1009,1038,1046,1048,1021,1027],
[1015,979,1045,992,0,1040,1066,1001,992,1031],
[1115,1014,1125,963,961,0,1009,1069,1042,994],
[1013,962,1029,955,935,992,0,1044,970,982],
[973,940,978,953,1000,932,957,0,984,962],
[953,997,1021,980,1009,959,1031,1017,0,943],
[966,984,1066,974,970,1007,1019,1039,1058,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 171, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1056,953,1007,1049,1025,1026,988,1065,1037],
[945,0,930,962,878,981,1015,922,974,928],
[1048,1071,0,1017,937,982,1030,1038,1133,989],
[994,1039,984,0,1033,1025,1074,965,1049,1066],
[952,1123,1064,968,0,1098,1094,987,1089,956],
[976,1020,1019,976,903,0,1025,912,1044,946],
[975,986,971,927,907,976,0,927,1037,981],
[1013,1079,963,1036,1014,1089,1074,0,1115,1021],
[936,1027,868,952,912,957,964,886,0,989],
[964,1073,1012,935,1045,1055,1020,980,1012,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 172, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1008,1039,1006,1026,987,1046,1049,1035,992],
[993,0,1017,973,1005,1004,1067,1037,1002,1001],
[962,984,0,973,1009,962,1039,1007,956,963],
[995,1028,1028,0,1033,1029,1059,1065,980,1000],
[975,996,992,968,0,992,1009,1035,954,983],
[1014,997,1039,972,1009,0,1054,1032,997,968],
[955,934,962,942,992,947,0,971,905,948],
[952,964,994,936,966,969,1030,0,998,961],
[966,999,1045,1021,1047,1004,1096,1003,0,1025],
[1009,1000,1038,1001,1018,1033,1053,1040,976,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 173, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,975,973,892,873,1032,954,957,1046,933],
[1026,0,998,936,1070,1134,1112,918,1047,961],
[1028,1003,0,835,900,1078,1006,940,1090,936],
[1109,1065,1166,0,1049,1107,1101,942,1167,1029],
[1128,931,1101,952,0,1096,1053,969,1082,903],
[969,867,923,894,905,0,987,890,983,931],
[1047,889,995,900,948,1014,0,977,1095,910],
[1044,1083,1061,1059,1032,1111,1024,0,1229,962],
[955,954,911,834,919,1018,906,772,0,876],
[1068,1040,1065,972,1098,1070,1091,1039,1125,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 174, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,954,997,1003,973,959,1058,1012,1025,989],
[1047,0,1049,1143,1059,999,1078,1216,1032,975],
[1004,952,0,1169,1100,1035,1154,1123,1131,1013],
[998,858,832,0,982,919,1001,983,1020,885],
[1028,942,901,1019,0,926,931,972,1045,883],
[1042,1002,966,1082,1075,0,985,1034,1051,970],
[943,923,847,1000,1070,1016,0,989,1024,1016],
[989,785,878,1018,1029,967,1012,0,957,947],
[976,969,870,981,956,950,977,1044,0,966],
[1012,1026,988,1116,1118,1031,985,1054,1035,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 175, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,994,1019,995,997,994,957,1003,1008,984],
[1007,0,1038,1006,1021,1020,982,996,1012,1008],
[982,963,0,975,992,985,948,983,996,959],
[1006,995,1026,0,1045,987,982,1001,1030,980],
[1004,980,1009,956,0,997,975,989,966,983],
[1007,981,1016,1014,1004,0,972,995,1000,1026],
[1044,1019,1053,1019,1026,1029,0,992,1011,1035],
[998,1005,1018,1000,1012,1006,1009,0,981,998],
[993,989,1005,971,1035,1001,990,1020,0,994],
[1017,993,1042,1021,1018,975,966,1003,1007,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 176, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1056,971,1008,1040,1032,1110,1007,1024,1049],
[945,0,930,969,1015,953,1002,943,967,1002],
[1030,1071,0,1000,1009,948,1094,1006,1016,1057],
[993,1032,1001,0,971,1002,1016,991,1031,1012],
[961,986,992,1030,0,965,1032,1009,1018,1034],
[969,1048,1053,999,1036,0,1029,947,991,995],
[891,999,907,985,969,972,0,916,965,1023],
[994,1058,995,1010,992,1054,1085,0,1019,1030],
[977,1034,985,970,983,1010,1036,982,0,986],
[952,999,944,989,967,1006,978,971,1015,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 177, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,997,1018,984,1013,1049,967,1001,982,944],
[1004,0,1001,995,989,1014,993,991,1014,1025],
[983,1000,0,994,1018,1042,1002,1029,979,1010],
[1017,1006,1007,0,1030,1037,1030,998,994,992],
[988,1012,983,971,0,1001,977,982,1011,991],
[952,987,959,964,1000,0,971,961,941,945],
[1034,1008,999,971,1024,1030,0,996,1014,991],
[1000,1010,972,1003,1019,1040,1005,0,973,992],
[1019,987,1022,1007,990,1060,987,1028,0,1021],
[1057,976,991,1009,1010,1056,1010,1009,980,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 178, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,974,1018,999,1082,1008,1024,975,1027,1031],
[1027,0,995,971,1068,1017,1028,1007,1058,1052],
[983,1006,0,978,1039,1031,1026,1025,1045,1024],
[1002,1030,1023,0,1058,1050,1033,994,1050,1050],
[919,933,962,943,0,970,960,924,952,931],
[993,984,970,951,1031,0,956,963,1019,988],
[977,973,975,968,1041,1045,0,981,1041,1003],
[1026,994,976,1007,1077,1038,1020,0,1051,1036],
[974,943,956,951,1049,982,960,950,0,972],
[970,949,977,951,1070,1013,998,965,1029,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 179, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1005,993,1027,1002,1033,996,1023,968,1049],
[996,0,979,1024,980,1015,982,1006,985,1020],
[1008,1022,0,1014,1001,1018,1000,991,1007,1016],
[974,977,987,0,986,1001,1004,959,953,998],
[999,1021,1000,1015,0,1017,1020,1001,966,1009],
[968,986,983,1000,984,0,963,976,982,1016],
[1005,1019,1001,997,981,1038,0,1035,964,1048],
[978,995,1010,1042,1000,1025,966,0,964,1030],
[1033,1016,994,1048,1035,1019,1037,1037,0,1062],
[952,981,985,1003,992,985,953,971,939,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 180, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1013,988,975,1034,1030,965,945,1023,1043],
[988,0,1032,977,1025,960,970,984,1029,983],
[1013,969,0,977,1031,1025,1029,976,1031,980],
[1026,1024,1024,0,1033,1023,1067,1011,1034,994],
[967,976,970,968,0,985,967,926,972,970],
[971,1041,976,978,1016,0,988,938,981,961],
[1036,1031,972,934,1034,1013,0,928,1020,1004],
[1056,1017,1025,990,1075,1063,1073,0,973,1035],
[978,972,970,967,1029,1020,981,1028,0,951],
[958,1018,1021,1007,1031,1040,997,966,1050,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 181, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,854,897,1042,1153,955,1062,1045,1034,855],
[1147,0,1106,984,1150,938,1031,1147,996,847],
[1104,895,0,1063,1227,1037,1141,1215,1012,1020],
[959,1017,938,0,974,921,934,979,1020,864],
[848,851,774,1027,0,1054,794,743,879,814],
[1046,1063,964,1080,947,0,934,815,1002,799],
[939,970,860,1067,1207,1067,0,925,907,808],
[956,854,786,1022,1258,1186,1076,0,1132,854],
[967,1005,989,981,1122,999,1094,869,0,873],
[1146,1154,981,1137,1187,1202,1193,1147,1128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 182, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1117,1096,1043,1048,1075,974,1061,1040,1066],
[884,0,1055,957,1007,980,930,972,1026,1016],
[905,946,0,953,1017,990,899,971,997,1022],
[958,1044,1048,0,1022,1061,934,1038,1028,1032],
[953,994,984,979,0,955,909,910,987,979],
[926,1021,1011,940,1046,0,925,981,1038,1007],
[1027,1071,1102,1067,1092,1076,0,998,1091,1001],
[940,1029,1030,963,1091,1020,1003,0,1087,1047],
[961,975,1004,973,1014,963,910,914,0,992],
[935,985,979,969,1022,994,1000,954,1009,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 183, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,993,1071,1082,1007,1035,1012,1032,1044,1036],
[1008,0,1020,1039,1040,1066,1032,1062,1000,1039],
[930,981,0,1027,1020,1017,976,998,997,990],
[919,962,974,0,1006,976,1006,988,1010,991],
[994,961,981,995,0,1018,978,957,983,980],
[966,935,984,1025,983,0,977,993,951,963],
[989,969,1025,995,1023,1024,0,1024,1043,1041],
[969,939,1003,1013,1044,1008,977,0,1040,1006],
[957,1001,1004,991,1018,1050,958,961,0,999],
[965,962,1011,1010,1021,1038,960,995,1002,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 184, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,970,1001,961,1007,1028,1010,1021,1022,1002],
[1031,0,1025,1014,993,1042,1028,1016,1032,1015],
[1000,976,0,969,1017,1037,1005,1036,988,1024],
[1040,987,1032,0,1039,1033,1037,1042,1041,1040],
[994,1008,984,962,0,1006,995,998,997,998],
[973,959,964,968,995,0,977,990,960,985],
[991,973,996,964,1006,1024,0,1000,997,965],
[980,985,965,959,1003,1011,1001,0,1010,1016],
[979,969,1013,960,1004,1041,1004,991,0,982],
[999,986,977,961,1003,1016,1036,985,1019,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 185, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1014,976,1059,1033,1041,1131,1005,1061,1077],
[987,0,1073,1047,1075,1048,1115,1043,1052,1085],
[1025,928,0,936,1014,984,1046,959,1039,1020],
[942,954,1065,0,983,1060,1062,961,1049,1051],
[968,926,987,1018,0,1000,1032,958,1011,1041],
[960,953,1017,941,1001,0,1067,945,1010,987],
[870,886,955,939,969,934,0,850,1007,966],
[996,958,1042,1040,1043,1056,1151,0,1069,1088],
[940,949,962,952,990,991,994,932,0,1035],
[924,916,981,950,960,1014,1035,913,966,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 186, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,992,1035,1037,1045,1039,1001,1016,994,1013],
[1009,0,1031,1027,1035,1022,1029,990,978,1024],
[966,970,0,1028,1012,988,997,986,994,1002],
[964,974,973,0,1001,976,962,959,957,963],
[956,966,989,1000,0,1018,978,978,962,982],
[962,979,1013,1025,983,0,993,977,966,1002],
[1000,972,1004,1039,1023,1008,0,1010,971,979],
[985,1011,1015,1042,1023,1024,991,0,991,1010],
[1007,1023,1007,1044,1039,1035,1030,1010,0,1000],
[988,977,999,1038,1019,999,1022,991,1001,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 187, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,999,1032,1004,1027,1008,1010,1023,995,998],
[1002,0,1023,998,1023,1011,1033,1022,979,989],
[969,978,0,964,992,1001,996,987,991,998],
[997,1003,1037,0,1006,989,1026,992,1015,1006],
[974,978,1009,995,0,998,975,987,971,968],
[993,990,1000,1012,1003,0,965,977,996,972],
[991,968,1005,975,1026,1036,0,1015,969,1001],
[978,979,1014,1009,1014,1024,986,0,982,973],
[1006,1022,1010,986,1030,1005,1032,1019,0,1007],
[1003,1012,1003,995,1033,1029,1000,1028,994,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 188, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1027,1060,961,1052,1033,985,1019,1040,993],
[974,0,1051,954,1020,1001,976,984,995,971],
[941,950,0,921,983,985,930,914,947,927],
[1040,1047,1080,0,1039,1059,1024,1007,1018,982],
[949,981,1018,962,0,987,959,1036,957,989],
[968,1000,1016,942,1014,0,958,943,1000,935],
[1016,1025,1071,977,1042,1043,0,999,997,983],
[982,1017,1087,994,965,1058,1002,0,1017,969],
[961,1006,1054,983,1044,1001,1004,984,0,1014],
[1008,1030,1074,1019,1012,1066,1018,1032,987,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 189, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,942,989,950,919,977,967,975,966,949],
[1059,0,1021,1033,1021,1028,993,985,1011,967],
[1012,980,0,986,945,998,975,972,994,962],
[1051,968,1015,0,977,993,1020,982,1016,958],
[1082,980,1056,1024,0,1016,1023,1014,1026,1006],
[1024,973,1003,1008,985,0,979,975,988,990],
[1034,1008,1026,981,978,1022,0,998,1007,991],
[1026,1016,1029,1019,987,1026,1003,0,1054,1024],
[1035,990,1007,985,975,1013,994,947,0,977],
[1052,1034,1039,1043,995,1011,1010,977,1024,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 190, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1021,1031,986,1063,1090,1121,1018,999,1067],
[980,0,1036,954,1028,1030,1095,1036,1078,1018],
[970,965,0,961,958,997,996,991,960,1033],
[1015,1047,1040,0,1054,1116,1134,1078,1000,1065],
[938,973,1043,947,0,1018,1152,1013,979,1017],
[911,971,1004,885,983,0,1031,963,968,1059],
[880,906,1005,867,849,970,0,954,900,917],
[983,965,1010,923,988,1038,1047,0,934,999],
[1002,923,1041,1001,1022,1033,1101,1067,0,1049],
[934,983,968,936,984,942,1084,1002,952,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 191, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1055,1010,996,977,1054,1033,1052,1025,1047],
[946,0,1065,1017,1044,1046,1079,1020,1004,1023],
[991,936,0,971,994,987,960,987,957,1007],
[1005,984,1030,0,1061,1112,1061,1041,982,981],
[1024,957,1007,940,0,1034,1000,944,998,1024],
[947,955,1014,889,967,0,974,1019,1002,1035],
[968,922,1041,940,1001,1027,0,948,969,1035],
[949,981,1014,960,1057,982,1053,0,1007,1008],
[976,997,1044,1019,1003,999,1032,994,0,1014],
[954,978,994,1020,977,966,966,993,987,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 192, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1020,975,1024,1000,1024,1021,1020,1000,1002],
[981,0,990,974,968,984,1009,1014,979,984],
[1026,1011,0,1024,977,1003,1033,1047,997,1033],
[977,1027,977,0,1005,1007,1000,1027,1006,1014],
[1001,1033,1024,996,0,1005,1021,1052,1030,1027],
[977,1017,998,994,996,0,976,1036,987,962],
[980,992,968,1001,980,1025,0,1007,973,977],
[981,987,954,974,949,965,994,0,974,1001],
[1001,1022,1004,995,971,1014,1028,1027,0,1027],
[999,1017,968,987,974,1039,1024,1000,974,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 193, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1033,999,1041,1084,1035,1052,1022,1004,1040],
[968,0,1036,1034,1042,1021,1069,1012,972,987],
[1002,965,0,1004,1016,988,1014,1011,970,1005],
[960,967,997,0,1019,979,981,943,937,982],
[917,959,985,982,0,969,992,949,941,972],
[966,980,1013,1022,1032,0,1023,951,956,950],
[949,932,987,1020,1009,978,0,956,963,1012],
[979,989,990,1058,1052,1050,1045,0,957,1027],
[997,1029,1031,1064,1060,1045,1038,1044,0,1008],
[961,1014,996,1019,1029,1051,989,974,993,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 194, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1023,888,1003,942,925,1072,892,1046,932],
[978,0,906,975,792,913,1036,935,937,879],
[1113,1095,0,1157,955,1002,1107,951,1052,1088],
[998,1026,844,0,895,935,1022,1053,989,999],
[1059,1209,1046,1106,0,997,1137,1094,1171,1019],
[1076,1088,999,1066,1004,0,1059,1082,1109,1007],
[929,965,894,979,864,942,0,857,973,856],
[1109,1066,1050,948,907,919,1144,0,1038,928],
[955,1064,949,1012,830,892,1028,963,0,947],
[1069,1122,913,1002,982,994,1145,1073,1054,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 195, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1011,1008,1029,1057,1079,994,1004,1003,913],
[990,0,1030,991,1030,1090,1028,975,1066,992],
[993,971,0,976,1057,1057,1038,1023,1021,957],
[972,1010,1025,0,1012,1055,967,997,987,988],
[944,971,944,989,0,1021,982,1012,1057,960],
[922,911,944,946,980,0,960,906,938,960],
[1007,973,963,1034,1019,1041,0,1003,1068,1020],
[997,1026,978,1004,989,1095,998,0,1042,945],
[998,935,980,1014,944,1063,933,959,0,953],
[1088,1009,1044,1013,1041,1041,981,1056,1048,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 196, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1004,1002,969,1030,1001,1031,1022,1039,1036],
[997,0,1042,1006,1047,997,1023,1007,1027,1038],
[999,959,0,973,1032,996,1021,1038,1012,1015],
[1032,995,1028,0,1049,1053,1044,1056,1050,1021],
[971,954,969,952,0,972,983,1006,1029,1001],
[1000,1004,1005,948,1029,0,1000,1019,1031,989],
[970,978,980,957,1018,1001,0,1012,1006,1005],
[979,994,963,945,995,982,989,0,1016,995],
[962,974,989,951,972,970,995,985,0,963],
[965,963,986,980,1000,1012,996,1006,1038,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 197, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1030,1010,1092,1025,1200,1009,1088,1157,993],
[971,0,909,888,1001,1031,912,1024,1059,969],
[991,1092,0,1092,1058,1071,949,1043,1114,1113],
[909,1113,909,0,962,1045,937,991,1093,1024],
[976,1000,943,1039,0,1113,981,1087,1114,1000],
[801,970,930,956,888,0,997,899,1029,1018],
[992,1089,1052,1064,1020,1004,0,1104,1174,1126],
[913,977,958,1010,914,1102,897,0,1085,986],
[844,942,887,908,887,972,827,916,0,951],
[1008,1032,888,977,1001,983,875,1015,1050,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 198, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1008,1031,995,1052,1026,1022,996,1003,1032],
[993,0,1002,1019,1016,1003,982,1003,1005,1009],
[970,999,0,1008,1041,1009,1028,1027,1008,1013],
[1006,982,993,0,1028,988,999,1016,1010,1006],
[949,985,960,973,0,993,981,993,999,992],
[975,998,992,1013,1008,0,1014,996,991,998],
[979,1019,973,1002,1020,987,0,1013,994,987],
[1005,998,974,985,1008,1005,988,0,1020,995],
[998,996,993,991,1002,1010,1007,981,0,1003],
[969,992,988,995,1009,1003,1014,1006,998,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 199, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,951,994,979,959,988,968,988,964,1011],
[1050,0,1040,1024,993,1025,1032,1006,997,1058],
[1007,961,0,956,958,990,975,975,1004,1005],
[1022,977,1045,0,965,1015,1004,990,1003,1035],
[1042,1008,1043,1036,0,1017,1030,998,1028,1033],
[1013,976,1011,986,984,0,1030,1005,991,1026],
[1033,969,1026,997,971,971,0,985,1030,1026],
[1013,995,1026,1011,1003,996,1016,0,1030,1026],
[1037,1004,997,998,973,1010,971,971,0,1020],
[990,943,996,966,968,975,975,975,981,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda6(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([10, 2001, 200, "ME-BBRCWd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/mebbrcwd/mebbrcwd_10_2001.csv", index=False, header=False)