p1 <- parse_profile_of_rankings("2, F>G>D>A>B>C>E,
                                 2, F>G>E>A>B>C>D,
                                 1, F>G>C>D>E>A>B,
                                 2, G>F>D>A>B>C>E,
                                 2, G>F>E>A>B>C>D,
                                 1, G>F>C>D>E>A>B")


p <- random_profile_of_rankings(6, 10)
condorcet(p)
tideman(p)
kemeny(p)
votrix(p)


# 1              5 C4 ≻ C1 ≻ C3 ≻ C2
# 2              2 C4 ≻ C3 ≻ C2 ≻ C1
# 3              3 C3 ≻ C4 ≻ C1 ≻ C2
# C1 C2 C3 C4
#C1  0  8  5  0
# C2  2  0  0  0
# C3  5 10  0  3
# C4 10 10  7  0

p <- parse_profile_of_rankings(
  "7, C4 ≻ C3 ≻ C1 ≻ C2,
  2, C2 ≻ C4 ≻ C1 ≻ C3,
  1, C2 ≻ C3 ≻ C4 ≻ C1"
)


# El definitivo
1              3 C3 ≻ C1 ≻ C2 ≻ C4
2              3 C2 ≻ C4 ≻ C3 ≻ C1
3              4 C1 ≻ C2 ≻ C3 ≻ C4
C1 C2 C3 C4
C1  0  7  4  7
C2  3  0  7 10
C3  6  3  0  7
C4  3  0  3  0


# EL DEFINITIVO
p <- parse_profile_of_rankings(
"3, a_4 > a_2 > a_1 > a_3,
 4, a_3 > a_4 > a_2 > a_1,
 2, a_4 > a_1 > a_2 > a_3,
 1, a_1 > a_2 > a_3 > a_4"
)






