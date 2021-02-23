votrix(pors7nc$w1$pr1)


# n = 7 -------------------------------------------------------------------

r <- parse_profile_of_rankings("
1, C7 ≻ C4 ≻ C3 ≻ C5 ≻ C2 ≻ C1 ≻ C6,
1, C2 ≻ C5 ≻ C1 ≻ C6 ≻ C3 ≻ C4 ≻ C7,
3, C6 ≻ C2 ≻ C4 ≻ C1 ≻ C7 ≻ C3 ≻ C5,
1, C6 ≻ C2 ≻ C7 ≻ C1 ≻ C3 ≻ C4 ≻ C5,
3, C2 ≻ C5 ≻ C3 ≻ C7 ≻ C1 ≻ C4 ≻ C6,
1, C1 ≻ C5 ≻ C7 ≻ C3 ≻ C6 ≻ C4 ≻ C2")
get_omega(r)
votrix(r)
agreement_margin(votrix(r))
condorcet_winner(r)

r <- parse_profile_of_rankings("
1, C7 ≻ C4 ≻ C3 ≻ C5 ≻ C2 ≻ C1 ≻ C6,
1, C5 ≻ C2 ≻ C1 ≻ C6 ≻ C3 ≻ C4 ≻ C7,
3, C6 ≻ C2 ≻ C4 ≻ C1 ≻ C7 ≻ C3 ≻ C5,
1, C6 ≻ C2 ≻ C7 ≻ C1 ≻ C3 ≻ C4 ≻ C5,
3, C5 ≻ C2 ≻ C3 ≻ C7 ≻ C1 ≻ C4 ≻ C6,
1, C2 ≻ C1 ≻ C7 ≻ C3 ≻ C6 ≻ C4 ≻ C5")
get_omega(r)
agreement_margin(votrix(r))
condorcet_winner(r)

r <- parse_profile_of_rankings("
2, C7 ≻ C3 ≻ C6 ≻ C4 ≻ C2 ≻ C5 ≻ C1,
2, C1 ≻ C2 ≻ C5 ≻ C6 ≻ C3 ≻ C7 ≻ C4,
2, C6 ≻ C4 ≻ C2 ≻ C1 ≻ C7 ≻ C3 ≻ C5,
1, C2 ≻ C7 ≻ C3 ≻ C1 ≻ C5 ≻ C6 ≻ C4,
2, C5 ≻ C4 ≻ C2 ≻ C3 ≻ C7 ≻ C1 ≻ C6,
1, C1 ≻ C2 ≻ C5 ≻ C3 ≻ C6 ≻ C7 ≻ C4")
get_omega(r)
votrix(r)
get_alpha(r)
agreement_margin(votrix(r))
condorcet_winner(r)

# n = 8 -------------------------------------------------------------------

pors8nc$w1

r <- parse_profile_of_rankings("
1, C5 ≻ C3 ≻ C2 ≻ C7 ≻ C6 ≻ C1 ≻ C8 ≻ C4,
1, C8 ≻ C4 ≻ C1 ≻ C3 ≻ C5 ≻ C6 ≻ C7 ≻ C2,
1, C6 ≻ C3 ≻ C1 ≻ C5 ≻ C7 ≻ C2 ≻ C8 ≻ C4,
2, C3 ≻ C7 ≻ C2 ≻ C5 ≻ C1 ≻ C8 ≻ C6 ≻ C4,
1, C4 ≻ C6 ≻ C3 ≻ C2 ≻ C5 ≻ C7 ≻ C1 ≻ C8,
1, C6 ≻ C5 ≻ C2 ≻ C1 ≻ C8 ≻ C3 ≻ C4 ≻ C7,
2, C4 ≻ C8 ≻ C7 ≻ C2 ≻ C1 ≻ C6 ≻ C3 ≻ C5,
1, C3 ≻ C4 ≻ C1 ≻ C8 ≻ C6 ≻ C7 ≻ C5 ≻ C2")
get_omega(r)
votrix(r)
get_alpha(r)
agreement_margin(votrix(r))
condorcet_winner(r)

r <- parse_profile_of_rankings("
1, C8 ≻ C2 ≻ C3 ≻ C7 ≻ C6 ≻ C1 ≻ C5 ≻ C4,
1, C8 ≻ C4 ≻ C1 ≻ C3 ≻ C7 ≻ C6 ≻ C5 ≻ C2,
1, C6 ≻ C3 ≻ C1 ≻ C7 ≻ C8 ≻ C5 ≻ C4 ≻ C2,
2, C7 ≻ C5 ≻ C3 ≻ C2 ≻ C1 ≻ C8 ≻ C6 ≻ C4,
1, C4 ≻ C6 ≻ C2 ≻ C7 ≻ C5 ≻ C1 ≻ C8 ≻ C3,
1, C6 ≻ C2 ≻ C8 ≻ C5 ≻ C1 ≻ C3 ≻ C7 ≻ C4,
2, C4 ≻ C8 ≻ C5 ≻ C2 ≻ C1 ≻ C6 ≻ C7 ≻ C3,
1, C3 ≻ C4 ≻ C1 ≻ C8 ≻ C6 ≻ C7 ≻ C2 ≻ C5")
get_omega(r)
votrix(r)
get_alpha(r)
agreement_margin(votrix(r))
condorcet_winner(r)

r <- parse_profile_of_rankings("
2, C8 ≻ C7 ≻ C3 ≻ C6 ≻ C4 ≻ C5 ≻ C1 ≻ C2,
2, C2 ≻ C5 ≻ C8 ≻ C1 ≻ C6 ≻ C3 ≻ C7 ≻ C4,
2, C6 ≻ C4 ≻ C2 ≻ C1 ≻ C8 ≻ C7 ≻ C3 ≻ C5,
1, C2 ≻ C7 ≻ C3 ≻ C1 ≻ C6 ≻ C8 ≻ C4 ≻ C5,
2, C4 ≻ C5 ≻ C2 ≻ C3 ≻ C7 ≻ C1 ≻ C8 ≻ C6,
1, C1 ≻ C2 ≻ C5 ≻ C3 ≻ C6 ≻ C7 ≻ C4 ≻ C8")
get_omega(r)
votrix(r)
get_alpha(r)
agreement_margin(votrix(r))
condorcet_winner(r)

r <- parse_profile_of_rankings("
1, C7 ≻ C3 ≻ C8 ≻ C6 ≻ C4 ≻ C2 ≻ C1 ≻ C5,
2, C5 ≻ C8 ≻ C6 ≻ C1 ≻ C3 ≻ C7 ≻ C2 ≻ C4,
2, C6 ≻ C4 ≻ C8 ≻ C2 ≻ C7 ≻ C1 ≻ C5 ≻ C3,
2, C7 ≻ C2 ≻ C6 ≻ C1 ≻ C3 ≻ C8 ≻ C4 ≻ C5,
2, C4 ≻ C5 ≻ C2 ≻ C3 ≻ C1 ≻ C6 ≻ C8 ≻ C7,
1, C1 ≻ C5 ≻ C3 ≻ C6 ≻ C7 ≻ C4 ≻ C8 ≻ C2")
get_omega(r)
votrix(r)
get_alpha(r)
agreement_margin(votrix(r))
condorcet_winner(r)

# n = 9 -------------------------------------------------------------------

r <- parse_profile_of_rankings("
1, C5 ≻ C9 ≻ C3 ≻ C2 ≻ C7 ≻ C6 ≻ C1 ≻ C8 ≻ C4,
1, C8 ≻ C9 ≻ C3 ≻ C4 ≻ C5 ≻ C6 ≻ C1 ≻ C7 ≻ C2,
1, C6 ≻ C3 ≻ C1 ≻ C9 ≻ C5 ≻ C7 ≻ C2 ≻ C8 ≻ C4,
2, C3 ≻ C7 ≻ C2 ≻ C5 ≻ C1 ≻ C9 ≻ C8 ≻ C4 ≻ C6,
1, C4 ≻ C6 ≻ C9 ≻ C3 ≻ C2 ≻ C5 ≻ C7 ≻ C1 ≻ C8,
1, C6 ≻ C5 ≻ C2 ≻ C1 ≻ C8 ≻ C9 ≻ C3 ≻ C4 ≻ C7,
2, C4 ≻ C8 ≻ C7 ≻ C2 ≻ C1 ≻ C6 ≻ C9 ≻ C3 ≻ C5,
1, C3 ≻ C4 ≻ C1 ≻ C8 ≻ C6 ≻ C7 ≻ C5 ≻ C9 ≻ C2")
get_omega(r)
votrix(r)
get_alpha(r)
agreement_margin(votrix(r))
condorcet_winner(r)

r <- parse_profile_of_rankings("
3, C4 ≻ C9 ≻ C7 ≻ C5 ≻ C1 ≻ C6 ≻ C3 ≻ C8 ≻ C2,
1, C5 ≻ C6  ≻ C8  ≻ C1 ≻ C3 ≻ C4 ≻ C9 ≻ C7 ≻ C2, 
2, C5 ≻ C6  ≻ C8  ≻ C1 ≻ C4 ≻ C2 ≻ C3 ≻ C9 ≻ C7,
4, C2 ≻ C1 ≻ C3 ≻ C7 ≻ C8 ≻ C9 ≻ C6 ≻ C4 ≻ C5")
get_omega(r)
votrix(r)
get_alpha(r)
agreement_margin(votrix(r))
condorcet_winner(r)

# n = 10 -------------------------------------------------------------------

r <- parse_profile_of_rankings("
3, C4 ≻ C9 ≻ C10 ≻ C5 ≻ C7 ≻ C1 ≻ C6 ≻ C3 ≻ C8 ≻ C2,
1, C6 ≻ C5  ≻ C8 ≻ C1 ≻ C10 ≻ C3 ≻ C4 ≻ C9 ≻ C7 ≻ C2, 
2, C5 ≻ C6  ≻ C8 ≻ C1 ≻ C4 ≻ C2 ≻ C3 ≻ C7 ≻ C10 ≻ C9,
4, C2 ≻ C1 ≻ C3 ≻ C7 ≻ C8 ≻ C9 ≻ C10 ≻ C6 ≻ C4 ≻ C5")
get_omega(r)
votrix(r)
get_alpha(r)
agreement_margin(votrix(r))
condorcet_winner(r)

r <- parse_profile_of_rankings("
1, C7 ≻ C10 ≻ C3 ≻ C8 ≻ C4 ≻ C2 ≻ C1 ≻ C5 ≻ C6,
2, C5 ≻ C8 ≻ C1 ≻ C6 ≻ C3 ≻ C7 ≻ C2 ≻ C10 ≻ C4,
2, C10 ≻ C4 ≻ C6 ≻ C8 ≻ C7 ≻ C5 ≻ C3 ≻ C1 ≻ C2,
2, C7 ≻ C10 ≻ C2 ≻ C6 ≻ C1 ≻ C8 ≻ C3 ≻ C4 ≻ C5,
2, C4 ≻ C10 ≻ C2 ≻ C3 ≻ C5 ≻ C1 ≻ C6 ≻ C8 ≻ C7,
1, C1 ≻ C5 ≻ C3 ≻ C10 ≻ C2 ≻ C4 ≻ C8 ≻ C7  ≻ C6")
get_omega(r)
votrix(r)
get_alpha(r)
agreement_margin(votrix(r))
condorcet_winner(r)

r <- parse_profile_of_rankings("
2, C7 ≻ C8 ≻ C3 ≻ C10 ≻ C4 ≻ C2 ≻ C1 ≻ C5 ≻ C6,
2, C5 ≻ C1 ≻ C6 ≻ C4 ≻ C7 ≻ C3 ≻ C8 ≻ C2 ≻ C10 ,
2, C4 ≻ C7 ≻ C8 ≻ C6 ≻ C10 ≻ C5 ≻ C3 ≻ C1 ≻ C2,
2, C7 ≻ C10 ≻ C2 ≻ C6 ≻ C1 ≻ C8 ≻ C3 ≻ C5 ≻ C4,
1, C4 ≻ C7 ≻ C2 ≻ C3 ≻ C5 ≻ C1 ≻ C6 ≻ C8 ≻ C10,
1, C1 ≻ C5 ≻ C3 ≻ C2 ≻ C6 ≻ C4 ≻ C7 ≻ C8 ≻ C10  ")
get_omega(r)
votrix(r)
get_alpha(r)
agreement_margin(votrix(r))
condorcet_winner(r)

