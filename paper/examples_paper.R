r <- parse_profile_of_rankings("
3, C5 ≻ C4 ≻ C1 ≻ C3 ≻ C2,
2, C3 ≻ C4 ≻ C5 ≻ C2 ≻ C1,
2, C1 ≻ C4 ≻ C5 ≻ C2 ≻ C3,
3, C2 ≻ C5 ≻ C4 ≻ C3 ≻ C1")
votrix(r)
condorcet(r, seePoints = T)
kemeny(r)

r <- parse_profile_of_rankings("
3, C5 ≻ C4 ≻ C1 ≻ C3 ≻ C2,
2, C3 ≻ C4 ≻ C5 ≻ C2 ≻ C1,
2, C1 ≻ C4 ≻ C2 ≻ C5 ≻ C3,
3, C2 ≻ C5 ≻ C4 ≻ C3 ≻ C1")
votrix(r)
condorcet(r, seePoints = T)
kemeny(r)

r <- parse_profile_of_rankings("
3, C5 ≻ C4 ≻ C1 ≻ C3 ≻ C2,
2, C3 ≻ C4 ≻ C2 ≻ C5 ≻ C1,
2, C1 ≻ C4 ≻ C5 ≻ C2 ≻ C3,
3, C2 ≻ C5 ≻ C3 ≻ C4 ≻ C1")
votrix(r)
condorcet(r, seePoints = T)
kemeny(r)

r <- parse_profile_of_rankings("
3, C4 ≻ C5 ≻ C1 ≻ C3 ≻ C2,
2, C3 ≻ C4 ≻ C2 ≻ C5 ≻ C1,
2, C1 ≻ C5 ≻ C4 ≻ C2 ≻ C3,
3, C2 ≻ C5 ≻ C3 ≻ C4 ≻ C1")
votrix(r)
condorcet(r, seePoints = T)
kemeny(r)


###################

r <- parse_profile_of_rankings("
3, C2 ≻ C4 ≻ C1 ≻ C3 ≻ C6 ≻ C5,
2, C6 ≻ C2 ≻ C4 ≻ C5 ≻ C1 ≻ C3,
4, C1 ≻ C3 ≻ C6 ≻ C5 ≻ C4 ≻ C2,
1, C3 ≻ C6 ≻ C5 ≻ C1 ≻ C2 ≻ C4")
votrix(r)
condorcet(r, seePoints = T)
kemeny(r)

r <- parse_profile_of_rankings("
3, C2 ≻ C4 ≻ C1 ≻ C3 ≻ C6 ≻ C5,
2, C6 ≻ C2 ≻ C4 ≻ C5 ≻ C1 ≻ C3,
4, C1 ≻ C3 ≻ C6 ≻ C5 ≻ C4 ≻ C2,
1, C3 ≻ C6 ≻ C5 ≻ C1 ≻ C4 ≻ C2")
votrix(r)
condorcet(r, seePoints = T)
kemeny(r)

r <- parse_profile_of_rankings("
3, C2 ≻ C4 ≻ C1 ≻ C3 ≻ C6 ≻ C5,
2, C6 ≻ C2 ≻ C4 ≻ C5 ≻ C1 ≻ C3,
4, C2 ≻ C1 ≻ C3 ≻ C6 ≻ C5 ≻ C4,
1, C3 ≻ C6 ≻ C5 ≻ C1 ≻ C2 ≻ C4")
votrix(r)
condorcet(r, seePoints = T)
kemeny(r)
