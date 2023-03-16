# n = 4, m = 10
p1 <- parse_profile_of_rankings("
1, C4 ≻ C2 ≻ C1 ≻ C3,
3, C1 ≻ C3 ≻ C4 ≻ C2,
2, C3 ≻ C2 ≻ C4 ≻ C1,
1, C2 ≻ C3 ≻ C4 ≻ C1,
3, C2 ≻ C3 ≻ C1 ≻ C4")

# n = 4, m = 15
p2 <- parse_profile_of_rankings("
2, C4 ≻ C2 ≻ C1 ≻ C3,
2, C3 ≻ C2 ≻ C4 ≻ C1,
2, C3 ≻ C2 ≻ C1 ≻ C4,
3, C1 ≻ C4 ≻ C3 ≻ C2,
2, C1 ≻ C2 ≻ C4 ≻ C3,
2, C1 ≻ C3 ≻ C2 ≻ C4,
2, C4 ≻ C2 ≻ C3 ≻ C1")

# n = 5, m = 10
p3 <- parse_profile_of_rankings("
1, C1 ≻ C4 ≻ C2 ≻ C3 ≻ C5,
1, C3 ≻ C4 ≻ C1 ≻ C2 ≻ C5,
1, C5 ≻ C2 ≻ C3 ≻ C1 ≻ C4,
2, C2 ≻ C3 ≻ C4 ≻ C1 ≻ C5,
1, C2 ≻ C3 ≻ C5 ≻ C4 ≻ C1,
1, C4 ≻ C5 ≻ C1 ≻ C2 ≻ C3,
3, C2 ≻ C4 ≻ C1 ≻ C3 ≻ C5")

p4 <- parse_profile_of_rankings("
1, C1 ≻ C4 ≻ C2 ≻ C3 ≻ C5,
1, C3 ≻ C4 ≻ C1 ≻ C2 ≻ C5,
1, C5 ≻ C2 ≻ C3 ≻ C1 ≻ C4,
2, C2 ≻ C3 ≻ C4 ≻ C1 ≻ C5,
1, C2 ≻ C3 ≻ C5 ≻ C4 ≻ C1,
1, C4 ≻ C5 ≻ C1 ≻ C2 ≻ C3,
3, C2 ≻ C4 ≻ C1 ≻ C3 ≻ C5")



