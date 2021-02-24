votrix(pors7nc$w1$pr1)

# n = 7 -------------------------------------------------------------------

## w = 1 faltan 4 ---------------------------------------------------------

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

r <- parse_profile_of_rankings("
4, C6 ≻ C4 ≻ C7 ≻ C2 ≻ C1 ≻ C5 ≻ C3,
2, C4 ≻ C3 ≻ C2 ≻ C1 ≻ C7 ≻ C5 ≻ C6,
3, C5 ≻ C3 ≻ C4 ≻ C1 ≻ C7 ≻ C2 ≻ C6,
1, C2 ≻ C6 ≻ C4 ≻ C5 ≻ C3 ≻ C1 ≻ C7")
get_omega(r)
votrix(r)
get_alpha(r)
agreement_margin(votrix(r))
condorcet_winner(r)

# n = 8 -------------------------------------------------------------------

## w = 1 faltan 5 ---------------------------------------------------------
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
pors8nc$w1[[1]] <- r

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
pors8nc$w1[[2]] <- r

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
pors8nc$w1[[3]] <- r

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
pors8nc$w1[[4]] <- r

r <- parse_profile_of_rankings("
3, C3 ≻ C8 ≻ C4 ≻ C5 ≻ C2 ≻ C1 ≻ C7 ≻ C6,
3, C6 ≻ C1 ≻ C3 ≻ C2 ≻ C5 ≻ C4 ≻ C7 ≻ C8,
2, C7 ≻ C6 ≻ C4 ≻ C8 ≻ C3 ≻ C1 ≻ C2 ≻ C5,
2, C7 ≻ C3 ≻ C5 ≻ C8 ≻ C1 ≻ C2 ≻ C4 ≻ C6")
get_omega(r)
votrix(r)
get_alpha(r)
agreement_margin(votrix(r))
condorcet_winner(r)
pors8nc$w1[[5]] <- r

# n = 9 -------------------------------------------------------------------

## w = 1 faltan 5 ---------------------------------------------------------
pors9nc$w1

r <- parse_profile_of_rankings("
1, C5 ≻ C9 ≻ C3 ≻ C2 ≻ C7 ≻ C6 ≻ C1 ≻ C8 ≻ C4,
1, C8 ≻ C9 ≻ C3 ≻ C4 ≻ C5 ≻ C6 ≻ C1 ≻ C7 ≻ C2,
1, C6 ≻ C3 ≻ C1 ≻ C9 ≻ C5 ≻ C7 ≻ C2 ≻ C8 ≻ C4,
2, C3 ≻ C7 ≻ C2 ≻ C5 ≻ C1 ≻ C9 ≻ C8 ≻ C4 ≻ C6,
1, C4 ≻ C6 ≻ C9 ≻ C3 ≻ C2 ≻ C5 ≻ C7 ≻ C1 ≻ C8,
1, C6 ≻ C5 ≻ C2 ≻ C1 ≻ C8 ≻ C3 ≻ C9 ≻ C4 ≻ C7,
2, C4 ≻ C8 ≻ C7 ≻ C2 ≻ C1 ≻ C6 ≻ C9 ≻ C3 ≻ C5,
1, C3 ≻ C4 ≻ C1 ≻ C8 ≻ C6 ≻ C7 ≻ C5 ≻ C9 ≻ C2")
get_omega(r)
votrix(r)
get_alpha(r)
agreement_margin(votrix(r))
condorcet_winner(r)
pors9nc$w1[[1]] <- r

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
pors9nc$w1[[2]] <- r

r <- parse_profile_of_rankings("
1, C8 ≻ C1 ≻ C4 ≻ C7 ≻ C9 ≻ C5 ≻ C3 ≻ C2 ≻ C6,
1, C3 ≻ C9 ≻ C1 ≻ C5 ≻ C8 ≻ C7 ≻ C2 ≻ C4 ≻ C6,
2, C1 ≻ C9 ≻ C3 ≻ C2 ≻ C4 ≻ C5 ≻ C7 ≻ C8 ≻ C6,
1, C9 ≻ C5 ≻ C2 ≻ C8 ≻ C3 ≻ C6 ≻ C7 ≻ C4 ≻ C1,
2, C5 ≻ C6 ≻ C9 ≻  C2 ≻ C4 ≻ C3 ≻ C7 ≻ C8 ≻ C1,
2, C6 ≻ C9 ≻ C7 ≻ C4 ≻ C2 ≻ C8 ≻ C3 ≻ C1 ≻ C5,
1, C8 ≻ C1 ≻ C6 ≻ C4 ≻ C9 ≻ C7 ≻ C2 ≻ C3 ≻ C5")
get_omega(r)
votrix(r)
get_alpha(r)
agreement_margin(votrix(r))
condorcet_winner(r)
pors9nc$w1[[3]] <- r

r <- parse_profile_of_rankings("
1, C1 ≻ C5 ≻ C3 ≻ C8 ≻ C6 ≻ C2 ≻ C4 ≻ C7 ≻ C9,
3, C8 ≻ C5 ≻ C4 ≻ C9 ≻ C2 ≻ C1 ≻ C6 ≻ C7 ≻ C3,
2, C7 ≻ C3 ≻ C8 ≻ C1 ≻ C6 ≻ C2 ≻ C4 ≻ C9 ≻ C5,
2, C9 ≻ C4 ≻ C3 ≻ C7 ≻ C8 ≻ C6 ≻ C5 ≻ C1 ≻ C2,
2, C8 ≻ C6 ≻ C2 ≻ C1 ≻ C7 ≻ C9 ≻ C5 ≻ C3 ≻ C4")
get_omega(r)
votrix(r)
get_alpha(r)
agreement_margin(votrix(r))
condorcet_winner(r)
pors9nc$w1[[4]] <- r

r <- parse_profile_of_rankings("
1, C6 ≻ C3 ≻ C1 ≻ C4 ≻ C8 ≻ C7 ≻ C9 ≻ C5 ≻ C2,
2, C3 ≻ C1 ≻ C8 ≻ C5 ≻ C2 ≻ C9 ≻ C6 ≻ C4 ≻ C7,
1, C1 ≻ C7 ≻ C9 ≻ C4 ≻ C5 ≻ C8 ≻ C6 ≻ C2 ≻ C3,
2, C2 ≻ C8 ≻ C9 ≻ C6 ≻ C3 ≻ C7 ≻ C4 ≻ C5 ≻ C1,
1, C6 ≻ C3 ≻ C7 ≻ C4 ≻ C2 ≻ C5 ≻ C9 ≻ C1 ≻ C8,
2, C6 ≻ C4 ≻ C7 ≻ C5 ≻ C2 ≻ C8 ≻ C9 ≻ C1 ≻  C3,
1, C5 ≻ C1 ≻ C9 ≻ C7 ≻ C4 ≻ C6 ≻ C2 ≻ C3 ≻ C8")
get_omega(r)
votrix(r)
get_alpha(r)
agreement_margin(votrix(r))
condorcet_winner(r)
pors9nc$w1[[5]] <- r

# n = 10 -------------------------------------------------------------------

## w = 1 faltan 5 ----------------------------------------------------------
pors10nc$w1

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
pors10nc$w1[[1]] <- r

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
pors10nc$w1[[2]] <- r

r <- parse_profile_of_rankings("
2, C7 ≻ C8 ≻ C3 ≻ C10 ≻ C4 ≻ C2 ≻ C1 ≻ C5 ≻ C6,
2, C5 ≻ C1 ≻ C6 ≻ C4 ≻ C7 ≻ C3 ≻ C8 ≻ C2 ≻ C10 ,
2, C4 ≻ C7 ≻ C8 ≻ C6 ≻ C10 ≻ C5 ≻ C3 ≻ C1 ≻ C2,
2, C7 ≻ C10 ≻ C2 ≻ C6 ≻ C1 ≻ C8 ≻ C3 ≻ C5 ≻ C4,
1, C4 ≻ C7 ≻ C2 ≻ C3 ≻ C5 ≻ C1 ≻ C6 ≻ C8 ≻ C10,
1, C1 ≻ C5 ≻ C3 ≻ C2 ≻ C6 ≻ C4 ≻ C7 ≻ C8 ≻ C10")
get_omega(r)
votrix(r)
get_alpha(r)
agreement_margin(votrix(r))
condorcet_winner(r)
pors10nc$w1[[3]] <- r

r <- parse_profile_of_rankings("
2, C4 ≻ C3 ≻ C7 ≻ C6 ≻ C5 ≻ C9 ≻ C1 ≻ C2 ≻ C10 ≻ C8,
2, C2 ≻ C6 ≻ C1 ≻ C3 ≻ C10 ≻ C5 ≻ C8 ≻ C9 ≻ C4 ≻ C7,
1, C7 ≻ C6 ≻ C3 ≻ C8 ≻ C2 ≻ C5 ≻ C4 ≻ C9 ≻ C1 ≻ C10,
1, C6 ≻ C2 ≻ C9 ≻ C4 ≻ C5 ≻ C8 ≻ C1 ≻ C3 ≻ C7 ≻ C10,
1, C10 ≻ C8 ≻ C9 ≻ C3 ≻ C1 ≻ C7 ≻ C6 ≻  C2 ≻ C5 ≻ C4,
2, C10 ≻ C8 ≻ C7 ≻ C6 ≻ C5 ≻ C1 ≻ C4 ≻ C9 ≻ C2 ≻ C3,
1, C4 ≻ C6 ≻ C1 ≻ C9 ≻ C10 ≻ C2 ≻ C8 ≻ C7 ≻ C3 ≻ C5")
get_omega(r)
votrix(r)
get_alpha(r)
agreement_margin(votrix(r))
condorcet_winner(r)
pors10nc$w1[[4]] <- r

r <- parse_profile_of_rankings("
1, C1 ≻ C5 ≻ C3 ≻ C8 ≻ C10 ≻ C6 ≻ C2 ≻ C4 ≻ C7 ≻ C9,
3, C8 ≻ C5 ≻ C4 ≻ C10 ≻ C2 ≻ C9 ≻ C1 ≻ C6 ≻ C7 ≻ C3 ,
2, C7 ≻ C3 ≻ C10 ≻ C8 ≻ C1 ≻ C6 ≻ C2 ≻ C9 ≻ C5 ≻ C4 ,
2, C9 ≻ C4 ≻ C3 ≻ C7 ≻ C8 ≻ C6 ≻ C10 ≻ C5 ≻ C1 ≻ C2 ,
2, C8 ≻ C6 ≻ C2 ≻ C1 ≻ C7 ≻ C9 ≻ C5 ≻ C3 ≻ C4 ≻ C10")
get_omega(r)
votrix(r)
get_alpha(r)
agreement_margin(votrix(r))
condorcet_winner(r)
pors10nc$w1[[5]] <- r

## w = 9 faltan 4 ----------------------------------------------------------
pors10nc$w9

r <- parse_profile_of_rankings("
5, C6 ≻ C9 ≻ C5 ≻ C2 ≻ C8 ≻ C7 ≻ C1 ≻ C10 ≻ C4 ≻ C3,
3, C3 ≻ C1 ≻ C10 ≻ C8 ≻ C7 ≻ C5 ≻ C9 ≻ C2 ≻ C4 ≻ C6,
2, C3 ≻ C2 ≻ C10 ≻ C6 ≻ C7 ≻ C8 ≻ C1 ≻ C4 ≻ C9 ≻ C5")
get_omega(r)
votrix(r)
get_alpha(r)
agreement_margin(votrix(r))
condorcet_winner(r)
pors10nc$w9[[2]] <- r

r <- parse_profile_of_rankings("
2, C10 ≻ C6 ≻ C4 ≻ C7 ≻ C9 ≻ C5 ≻ C3 ≻ C2 ≻ C8 ≻ C1,
1, C3 ≻ C7 ≻ C4 ≻ C5 ≻ C8 ≻ C6 ≻ C2 ≻ C9 ≻ C1 ≻ C10,
2, C2 ≻ C8 ≻ C9 ≻ C3 ≻ C6 ≻ C4 ≻ C7 ≻ C1 ≻ C10 ≻ C5,
1, C4 ≻ C5 ≻ C7 ≻ C8 ≻ C6 ≻ C3 ≻ C2 ≻ C10 ≻ C1 ≻ C9,
1, C5 ≻ C4 ≻ C8 ≻ C7 ≻ C10 ≻ C9 ≻ C2 ≻ C6 ≻ C3 ≻ C1,
1, C10 ≻ C7 ≻ C5 ≻ C9 ≻ C2 ≻ C1 ≻ C6 ≻ C4 ≻ C8 ≻ C3,
1, C10 ≻ C9 ≻ C8 ≻ C2 ≻ C3 ≻ C5 ≻ C6 ≻ C7 ≻ C1 ≻ C4,
1, C5 ≻ C3 ≻ C6 ≻ C1 ≻ C8 ≻ C10 ≻ C2 ≻ C7 ≻ C9 ≻ C4")
get_omega(r)
votrix(r)
get_alpha(r)
agreement_margin(votrix(r))
condorcet_winner(r)
pors10nc$w9[[3]] <- r


r <- parse_profile_of_rankings("
1, C2 ≻ C9 ≻ C6 ≻ C3 ≻ C8 ≻ C7 ≻ C10 ≻ C1 ≻ C4 ≻ C5,
2, C9 ≻ C4 ≻ C6 ≻ C5 ≻ C10 ≻ C8 ≻ C2 ≻ C7 ≻ C1 ≻ C3,
2, C7 ≻ C10 ≻ C8 ≻ C5 ≻ C9 ≻ C3 ≻ C4 ≻ C2 ≻ C1 ≻ C6,
2, C6 ≻ C3 ≻ C10 ≻ C9 ≻ C4 ≻ C8 ≻ C7 ≻ C5 ≻ C1 ≻ C2,
1, C8 ≻ C2 ≻ C5 ≻ C9 ≻ C7 ≻ C3 ≻ C10 ≻ C4 ≻ C1 ≻ C6,
2, C2 ≻ C3 ≻ C6 ≻ C5 ≻ C4 ≻ C7 ≻ C9 ≻ C10 ≻ C8 ≻ C1")
get_omega(r)
votrix(r)
get_alpha(r)
agreement_margin(votrix(r))
condorcet_winner(r)
pors10nc$w9[[4]] <- r


r <- parse_profile_of_rankings("
3, C8 ≻ C5 ≻ C4 ≻ C1 ≻ C2 ≻ C3 ≻ C9 ≻ C7 ≻ C6 ≻ C10,
2, C7 ≻ C5 ≻ C6 ≻ C1 ≻ C4 ≻ C9 ≻ C10 ≻ C8 ≻ C3 ≻ C2,
1, C2 ≻ C7 ≻ C6 ≻ C4 ≻ C8 ≻ C9 ≻ C1 ≻ C3 ≻ C10 ≻ C5,
3, C3 ≻ C2 ≻ C9 ≻ C6 ≻ C7 ≻ C1 ≻ C8 ≻ C4 ≻ C5 ≻ C10,
1, C6 ≻ C8 ≻ C4 ≻ C3 ≻ C9 ≻ C2 ≻ C5 ≻ C1 ≻ C10 ≻ C7")
get_omega(r)
votrix(r)
get_alpha(r)
agreement_margin(votrix(r))
condorcet_winner(r)


r <- parse_profile_of_rankings("
1, C7 ≻ C8 ≻ C3 ≻ C4 ≻ C2 ≻ C1 ≻ C9 ≻ C5 ≻ C6 ≻ C10,
1, C7 ≻ C5 ≻ C1 ≻ C6 ≻ C4 ≻ C3 ≻ C10 ≻ C9 ≻ C8 ≻ C2,
3, C2 ≻ C5 ≻ C1 ≻ C6 ≻ C7 ≻ C4 ≻ C9 ≻ C8 ≻ C10 ≻ C3,
2, C9 ≻ C3 ≻ C2 ≻ C6 ≻ C7 ≻ C1 ≻ C8 ≻ C4 ≻ C5 ≻ C10,
3, C6 ≻ C8 ≻ C4 ≻ C3 ≻ C9 ≻ C2 ≻ C5 ≻ C1 ≻ C7 ≻ C10")
get_omega(r)
votrix(r)
get_alpha(r)
agreement_margin(votrix(r))
condorcet_winner(r)
pors10nc$w9[[5]] <- r

# n = 11 -------------------------------------------------------------------

## w = 1 faltan 5 ----------------------------------------------------------
pors11nc$w1

r <- parse_profile_of_rankings("
2, C8 ≻ C11 ≻ C6 ≻ C10 ≻ C7 ≻ C3 ≻ C2 ≻ C4 ≻ C1 ≻ C5,
2, C5 ≻ C1 ≻ C2 ≻ C3 ≻ C11 ≻ C7 ≻ C4 ≻ C6 ≻ C8 ≻ C10 ,
2, C4 ≻ C8 ≻ C11 ≻ C7 ≻ C10 ≻ C6 ≻ C5 ≻ C3 ≻ C1 ≻ C2,
2, C11 ≻ C2 ≻ C10 ≻ C7 ≻ C6 ≻ C1 ≻ C5 ≻ C3 ≻ C8 ≻ C4,
1, C4 ≻ C10 ≻ C11 ≻ C3 ≻ C5 ≻ C1 ≻ C6 ≻ C2 ≻ C8 ≻ C7,
1, C1 ≻ C5 ≻ C3 ≻ C2 ≻ C6 ≻ C4 ≻ C8 ≻ C11 ≻ C7 ≻ C10  ")
get_omega(r)
votrix(r)
get_alpha(r)
agreement_margin(votrix(r))
condorcet_winner(r)
pors11nc$w1[[1]] <- r

r <- parse_profile_of_rankings("
2, C8 ≻ C11 ≻ C10 ≻ C7 ≻ C3 ≻ C2 ≻ C4 ≻ C1 ≻ C5 ≻ C6,
1, C11 ≻ C1 ≻ C2 ≻ C3 ≻ C5 ≻ C7 ≻ C4 ≻ C6 ≻ C8 ≻ C10 ,
2, C4 ≻ C8 ≻ C11 ≻ C7 ≻ C5 ≻ C6 ≻ C10 ≻ C3 ≻ C1 ≻ C2,
2, C11 ≻ C2 ≻ C10 ≻ C7 ≻ C6 ≻ C1 ≻ C5 ≻ C3 ≻ C8 ≻ C4,
1, C4 ≻ C10 ≻ C11 ≻ C3 ≻ C5 ≻ C1 ≻ C6 ≻ C2 ≻ C8 ≻ C7,
2, C1 ≻ C5 ≻ C3 ≻ C6 ≻ C2 ≻ C4 ≻ C8 ≻ C11 ≻ C7 ≻ C10  ")
get_omega(r)
votrix(r)
get_alpha(r)
agreement_margin(votrix(r))
condorcet_winner(r)
pors11nc$w1[[2]] <- r

r <- parse_profile_of_rankings("
1, C6 ≻ C8  ≻ C5 ≻ C11 ≻ C1 ≻ C10 ≻ C3 ≻ C4 ≻ C2 ≻ C7 ≻ C9, 
2, C4 ≻ C2  ≻ C8 ≻ C1 ≻ C11 ≻ C3 ≻ C10 ≻ C9 ≻ C6 ≻ C7 ≻ C5,
4, C5 ≻ C4 ≻ C9 ≻ C3 ≻ C7 ≻ C8 ≻ C2 ≻ C10 ≻ C6 ≻ C1 ≻ C11,
3, C11 ≻ C4 ≻ C10 ≻ C7 ≻ C1 ≻ C6 ≻ C2 ≻ C9 ≻ C3 ≻ C8 ≻ C5")
get_omega(r)
votrix(r)
get_alpha(r)
agreement_margin(votrix(r))
condorcet_winner(r)
pors11nc$w1[[3]] <- r


r <- parse_profile_of_rankings("
3, C9 ≻ C11 ≻ C3 ≻ C8 ≻ C10 ≻ C6 ≻ C5 ≻ C7 ≻ C2 ≻ C4 ≻ C1,
2, C2 ≻ C6 ≻ C3 ≻ C1 ≻ C9 ≻ C7 ≻ C5 ≻ C10 ≻ C4 ≻ C11 ≻ C8,
1, C3 ≻ C4 ≻ C7 ≻ C10 ≻ C6 ≻ C5 ≻ C9 ≻ C8 ≻ C2 ≻ C11 ≻ C1,
2, C4 ≻ C3 ≻ C1 ≻ C5 ≻ C2 ≻ C10 ≻ C8 ≻ C6 ≻ C11 ≻ C7 ≻ C9,
2, C7 ≻ C1 ≻ C8 ≻ C11 ≻ C4 ≻ C5 ≻ C2 ≻ C3 ≻ C6 ≻ C10 ≻ C9")
get_omega(r)
votrix(r)
get_alpha(r)
agreement_margin(votrix(r))
condorcet_winner(r)
pors11nc$w1[[4]] <- r

r <- parse_profile_of_rankings("
3, C10 ≻ C11 ≻ C8 ≻ C9 ≻ C6 ≻ C7 ≻ C5 ≻ C1 ≻ C4 ≻ C3 ≻ C2,
2, C2 ≻ C10 ≻ C1 ≻ C3 ≻ C9 ≻ C7 ≻ C5 ≻ C8 ≻ C4 ≻ C11 ≻ C6,
2, C3 ≻ C2 ≻ C10 ≻ C7 ≻ C6 ≻ C5 ≻ C9 ≻ C8 ≻ C4 ≻ C1 ≻ C11,
1, C4 ≻ C3 ≻ C5 ≻ C2 ≻ C11 ≻ C10 ≻ C8 ≻ C6 ≻ C1 ≻ C7 ≻ C9,
2, C10 ≻ C1 ≻ C4 ≻ C11 ≻ C6 ≻ C5 ≻ C9 ≻ C8 ≻ C7 ≻ C3 ≻ C2")
get_omega(r)
votrix(r)
get_alpha(r)
agreement_margin(votrix(r))
condorcet_winner(r)
pors11nc$w1[[5]] <- r

## w = 2 falta 1 ----------------------------------------------------------
pors11nc$w2

r <- parse_profile_of_rankings("
3, C11 ≻ C10 ≻ C8 ≻ C9 ≻ C6 ≻ C7 ≻ C5 ≻ C1 ≻ C4 ≻ C3 ≻ C2,
2, C2 ≻ C10 ≻ C1 ≻ C3 ≻ C9 ≻ C7 ≻ C5 ≻ C8 ≻ C4 ≻ C11 ≻ C6,
2, C3 ≻ C2 ≻ C10 ≻ C7 ≻ C6 ≻ C5 ≻ C9 ≻ C8 ≻ C4 ≻ C1 ≻ C11,
1, C4 ≻ C3 ≻ C5 ≻ C2 ≻ C11 ≻ C10 ≻ C8 ≻ C6 ≻ C1 ≻ C7 ≻ C9,
2, C10 ≻ C1 ≻ C4 ≻ C11 ≻ C6 ≻ C5 ≻ C9 ≻ C8 ≻ C7 ≻ C3 ≻ C2")
get_omega(r)
votrix(r)
get_alpha(r)
agreement_margin(votrix(r))
condorcet_winner(r)
pors11nc$w2[[5]] <- r

# n = 12 -------------------------------------------------------------------

## w = 1 faltan 5 ----------------------------------------------------------
pors12nc$w1

r <- parse_profile_of_rankings("
2, C4 ≻ C1 ≻ C8 ≻ C6 ≻ C3 ≻ C7 ≻ C11 ≻ C12 ≻ C2 ≻ C10 ≻ C5,
2, C5 ≻ C1 ≻ C2 ≻ C3 ≻ C11 ≻ C7 ≻ C12 ≻ C10 ≻ C6 ≻ C8 ≻ C4 ,
2, C8 ≻ C4 ≻ C1 ≻ C7 ≻ C10 ≻ C12 ≻ C6 ≻ C5 ≻ C11 ≻ C2 ≻ C3,
2, C1 ≻ C11 ≻ C2 ≻ C10 ≻ C12 ≻ C6 ≻ C7 ≻ C5 ≻ C3 ≻ C8 ≻ C4,
1, C10 ≻ C12 ≻ C3 ≻ C5 ≻ C2 ≻ C11 ≻ C4 ≻ C1 ≻ C6 ≻ C7  ≻ C8,
1, C5 ≻ C8 ≻ C6 ≻ C3 ≻ C4 ≻ C10 ≻ C1 ≻ C2 ≻    C7 ≻ C12 ≻ C11  ")
get_omega(r)
votrix(r)
get_alpha(r)
agreement_margin(votrix(r))
condorcet_winner(r)
pors12nc$w1[[1]] <- r

r <- parse_profile_of_rankings("
1, C6 ≻ C8  ≻ C11 ≻ C5 ≻ C9 ≻ C12 ≻ C10 ≻ C7 ≻ C3 ≻ C1 ≻ C4 ≻ C2,
4, C5 ≻ C9 ≻ C3 ≻ C7 ≻ C4 ≻ C8 ≻ C2 ≻ C10 ≻ C6 ≻ C1 ≻ C12 ≻ C11,
2, C12 ≻ C1  ≻ C2 ≻ C8 ≻ C9 ≻ C11 ≻ C4 ≻ C3 ≻ C6 ≻ C10 ≻ C5 ≻ C7,
3, C11 ≻ C9 ≻ C10 ≻ C1 ≻ C6 ≻ C7 ≻ C2 ≻ C4 ≻ C12 ≻ C3 ≻ C8 ≻ C5")
get_omega(r)
votrix(r)
get_alpha(r)
agreement_margin(votrix(r))
condorcet_winner(r)
pors12nc$w1[[2]] <- r

r <- parse_profile_of_rankings("
3, C4 ≻ C2 ≻ C9 ≻ C5 ≻ C11 ≻ C10 ≻ C7 ≻ C6 ≻ C12 ≻ C3 ≻ C1 ≻ C8,
2, C2 ≻ C6 ≻ C9 ≻ C12 ≻ C5 ≻ C7 ≻ C1 ≻ C3 ≻ C8 ≻ C10 ≻ C11 ≻ C4,
2, C8 ≻ C3 ≻ C9 ≻ C10 ≻ C12 ≻ C4 ≻ C5 ≻ C1 ≻ C6 ≻ C7 ≻ C11 ≻ C2,
1, C7 ≻ C1 ≻ C9 ≻ C10 ≻ C12 ≻ C5 ≻ C8 ≻ C6 ≻ C4 ≻ C3 ≻ C11 ≻ C2,
2, C11 ≻ C9 ≻ C8 ≻ C3 ≻ C1 ≻ C6 ≻ C7 ≻ C12 ≻ C4 ≻ C10 ≻ C2 ≻ C5")
get_omega(r)
votrix(r)
get_alpha(r)
agreement_margin(votrix(r))
condorcet_winner(r)
pors12nc$w1[[3]] <- r

r <- parse_profile_of_rankings("
1, C6 ≻ C5 ≻ C12 ≻ C8 ≻ C11 ≻ C1 ≻ C10 ≻ C4 ≻ C7 ≻ C2 ≻ C3 ≻ C9, 
2, C2 ≻ C12 ≻ C8 ≻ C1 ≻ C4 ≻ C10 ≻ C11 ≻ C3 ≻ C6 ≻ C9 ≻ C7 ≻ C5,
4, C5 ≻ C9 ≻ C10 ≻ C3 ≻ C1 ≻ C7 ≻ C8 ≻ C6 ≻ C2 ≻ C12 ≻ C4 ≻ C11 ,
3, C11 ≻ C4 ≻ C10 ≻ C7 ≻ C6 ≻ C2 ≻ C12 ≻ C3 ≻ C9 ≻ C8 ≻ C1 ≻ C5")
get_omega(r)
votrix(r)
get_alpha(r)
agreement_margin(votrix(r))
condorcet_winner(r)
pors12nc$w1[[4]] <- r

r <- parse_profile_of_rankings("
3, C10 ≻ C11 ≻ C8 ≻ C9 ≻ C6 ≻ C7 ≻ C5 ≻ C1 ≻ C4 ≻ C3 ≻ C2,
2, C2 ≻ C10 ≻ C1 ≻ C3 ≻ C9 ≻ C7 ≻ C5 ≻ C8 ≻ C4 ≻ C11 ≻ C6,
2, C3 ≻ C2 ≻ C10 ≻ C7 ≻ C6 ≻ C5 ≻ C9 ≻ C8 ≻ C4 ≻ C1 ≻ C11,
1, C4 ≻ C3 ≻ C5 ≻ C2 ≻ C11 ≻ C10 ≻ C8 ≻ C6 ≻ C1 ≻ C7 ≻ C9,
2, C10 ≻ C1 ≻ C4 ≻ C11 ≻ C6 ≻ C5 ≻ C9 ≻ C8 ≻ C7 ≻ C3 ≻ C2")
get_omega(r)
votrix(r)
get_alpha(r)
agreement_margin(votrix(r))
condorcet_winner(r)
pors12nc$w1[[5]] <- r

## w = 2 faltan 5 ----------------------------------------------------------
pors12nc$w2
r <- parse_profile_of_rankings("
1, C6 ≻ C5 ≻ C12 ≻ C8 ≻ C11 ≻ C1 ≻ C10 ≻ C4 ≻ C7 ≻ C2 ≻ C3 ≻ C9, 
2, C2 ≻ C12 ≻ C8 ≻ C1 ≻ C4 ≻ C10 ≻ C11 ≻ C3 ≻ C6 ≻ C9 ≻ C7 ≻ C5,
4, C5 ≻ C9 ≻ C10 ≻ C3 ≻ C1 ≻ C7 ≻ C8 ≻ C6 ≻ C2 ≻ C12 ≻ C4 ≻ C11 ,
3, C11 ≻ C4 ≻ C10 ≻ C7 ≻ C6 ≻ C12 ≻ C2 ≻ C3 ≻ C9 ≻ C8 ≻ C1 ≻ C5")
get_omega(r)
votrix(r)
get_alpha(r)
agreement_margin(votrix(r))
condorcet_winner(r)
pors12nc$w2[[1]] <- r

r <- parse_profile_of_rankings("
3, C10 ≻ C11 ≻ C8 ≻ C9 ≻ C6 ≻ C7 ≻ C1 ≻ C5 ≻ C4 ≻ C3 ≻ C2,
2, C2 ≻ C10 ≻ C1 ≻ C3 ≻ C9 ≻ C7 ≻ C5 ≻ C8 ≻ C4 ≻ C11 ≻ C6,
2, C3 ≻ C2 ≻ C10 ≻ C7 ≻ C6 ≻ C5 ≻ C9 ≻ C8 ≻ C4 ≻ C1 ≻ C11,
1, C4 ≻ C3 ≻ C5 ≻ C2 ≻ C11 ≻ C10 ≻ C8 ≻ C6 ≻ C1 ≻ C7 ≻ C9,
2, C10 ≻ C1 ≻ C4 ≻ C11 ≻ C6 ≻ C5 ≻ C9 ≻ C8 ≻ C7 ≻ C3 ≻ C2")
get_omega(r)
votrix(r)
get_alpha(r)
agreement_margin(votrix(r))
condorcet_winner(r)
pors12nc$w2[[2]] <- r

r <- parse_profile_of_rankings("
1, C6 ≻ C8  ≻ C11 ≻ C5 ≻ C9 ≻ C12 ≻ C10 ≻ C7 ≻ C3 ≻ C1 ≻ C4 ≻ C2,
4, C5 ≻ C9 ≻ C3 ≻ C7 ≻ C4 ≻ C8 ≻ C2 ≻ C10 ≻ C6 ≻ C1 ≻ C11 ≻ C12,
2, C12 ≻ C1  ≻ C2 ≻ C8 ≻ C9 ≻ C11 ≻ C4 ≻ C3 ≻ C6 ≻ C10 ≻ C5 ≻ C7,
3, C11 ≻ C9 ≻ C10 ≻ C1 ≻ C6 ≻ C7 ≻ C2 ≻ C4 ≻ C12 ≻ C3 ≻ C8 ≻ C5")
get_omega(r)
votrix(r)
get_alpha(r)
agreement_margin(votrix(r))
condorcet_winner(r)
pors13nc$w2[[3]] <- r

r <- parse_profile_of_rankings("
2, C4 ≻ C1 ≻ C8 ≻ C6 ≻ C3 ≻ C7 ≻ C11 ≻ C12 ≻ C2 ≻ C10 ≻ C5,
2, C5 ≻ C1 ≻ C2 ≻ C3 ≻ C11 ≻ C7 ≻ C12 ≻ C10 ≻ C6 ≻ C8 ≻ C4 ,
2, C8 ≻ C4 ≻ C1 ≻ C7 ≻ C10 ≻ C12 ≻ C6 ≻ C11 ≻ C5 ≻ C2 ≻ C3,
2, C1 ≻ C11 ≻ C2 ≻ C10 ≻ C12 ≻ C6 ≻ C7 ≻ C5 ≻ C3 ≻ C8 ≻ C4,
1, C10 ≻ C12 ≻ C3 ≻ C5 ≻ C2 ≻ C11 ≻ C4 ≻ C1 ≻ C6 ≻ C7  ≻ C8,
1, C5 ≻ C8 ≻ C6 ≻ C3 ≻ C4 ≻ C10 ≻ C1 ≻ C2 ≻ C7 ≻ C11 ≻ C12  ")
get_omega(r)
votrix(r)
get_alpha(r)
agreement_margin(votrix(r))
condorcet_winner(r)
pors12nc$w2[[4]] <- r

r <- parse_profile_of_rankings("
3, C9 ≻ C6 ≻ C11 ≻ C1 ≻ C10 ≻ C7 ≻ C12 ≻ C3 ≻ C8 ≻ C2 ≻ C4 ≻ C5,
2, C3 ≻ C1 ≻ C11 ≻ C12 ≻ C4 ≻ C8 ≻ C2 ≻ C7 ≻ C9 ≻ C5 ≻ C10 ≻ C6,
3, C5 ≻ C9 ≻ C11 ≻ C8 ≻ C2 ≻ C3 ≻ C7 ≻ C12 ≻ C6 ≻ C4 ≻ C1 ≻ C10,
2, C4 ≻ C10 ≻ C11 ≻ C2 ≻ C6 ≻ C7 ≻ C5 ≻ C8 ≻ C1 ≻ C12 ≻ C9 ≻ C3")
get_omega(r)
votrix(r)
get_alpha(r)
agreement_margin(votrix(r))
condorcet_winner(r)
pors12nc$w2[[5]] <- r

## w = 11 faltan 5 ---------------------------------------------------------
pors12nc$w11

r <- parse_profile_of_rankings("
1, C5 ≻ C1 ≻ C2 ≻ C11 ≻ C10 ≻ C12 ≻ C3 ≻ C7 ≻ C4 ≻ C9 ≻ C8 ≻ C6,
1, C3 ≻ C4 ≻ C1 ≻ C2 ≻ C8 ≻ C11 ≻ C10 ≻ C9 ≻ C12 ≻ C5 ≻ C6 ≻ C7,
1, C6 ≻ C10 ≻ C4 ≻ C12 ≻ C11 ≻ C3 ≻ C1 ≻ C5 ≻ C8 ≻ C2 ≻ C7 ≻ C9,
1, C2 ≻ C4 ≻ C12 ≻ C1 ≻ C5 ≻ C3 ≻ C10 ≻ C6 ≻ C9 ≻ C8 ≻ C11 ≻ C7,
2, C5 ≻ C6 ≻ C11 ≻ C8 ≻ C7 ≻ C2 ≻ C4 ≻ C12 ≻ C1 ≻ C10 ≻ C9 ≻ C3,
2, C7 ≻ C10 ≻ C3 ≻ C8 ≻ C11 ≻ C6 ≻ C12 ≻ C1 ≻ C9 ≻ C5 ≻ C4 ≻ C2,
1, C6 ≻ C12 ≻ C3 ≻ C5 ≻ C11 ≻ C4 ≻ C7 ≻ C8 ≻ C2 ≻ C9 ≻ C1 ≻ C10,
1, C2 ≻ C7 ≻ C1 ≻ C11 ≻ C8 ≻ C4 ≻ C10 ≻ C6 ≻ C9 ≻ C3 ≻ C12 ≻ C5")
get_omega(r)
get_alpha(r)
agreement_margin(votrix(r))
condorcet_winner(r)
pors12nc$w11[[1]] <- r

r <- parse_profile_of_rankings("
2, C9 ≻ C4 ≻ C7 ≻ C10 ≻ C5 ≻ C1 ≻ C11 ≻ C6 ≻ C3 ≻ C2 ≻ C12 ≻ C8,
2, C7 ≻ C6 ≻ C5 ≻ C11 ≻ C4 ≻ C12 ≻ C3 ≻ C9 ≻ C2 ≻ C10 ≻ C8 ≻ C1,
3, C12 ≻ C2 ≻ C3 ≻ C10 ≻ C1 ≻ C4 ≻ C5 ≻ C6 ≻ C9 ≻ C11 ≻ C7 ≻ C8,
1, C10 ≻ C3 ≻ C7 ≻ C5 ≻ C12 ≻ C2 ≻ C1 ≻ C9 ≻ C11 ≻ C6 ≻ C8 ≻ C4,
2, C11 ≻ C1 ≻ C4 ≻ C2 ≻ C6 ≻ C9 ≻ C3 ≻ C12 ≻ C7 ≻ C5 ≻ C8 ≻ C10")
get_omega(r)
get_alpha(r)
agreement_margin(votrix(r))
condorcet_winner(r)
pors12nc$w11[[2]] <- r

r <- parse_profile_of_rankings("
1, C12 ≻ C5 ≻ C2 ≻ C11 ≻ C3 ≻ C7 ≻ C9 ≻ C1 ≻ C8 ≻ C6 ≻ C4 ≻ C10,
2, C11 ≻ C1 ≻ C9 ≻ C5 ≻ C2 ≻ C3 ≻ C12 ≻ C7 ≻ C6 ≻ C4 ≻ C10 ≻ C8,
1, C7 ≻ C1 ≻ C6 ≻ C3 ≻ C5 ≻ C11 ≻ C8 ≻ C10 ≻ C9 ≻ C4 ≻ C12 ≻ C2,
2, C4 ≻ C2 ≻ C6 ≻ C11 ≻ C5 ≻ C8 ≻ C12 ≻ C9 ≻ C7 ≻ C3 ≻ C10 ≻ C1,
2, C8 ≻ C1 ≻ C7 ≻ C9 ≻ C2 ≻ C11 ≻ C6 ≻ C3 ≻ C4 ≻ C12 ≻ C5 ≻ C10,
2, C12 ≻ C4 ≻ C3 ≻ C7 ≻ C8 ≻ C5 ≻ C6 ≻ C9 ≻ C11 ≻ C2 ≻ C1 ≻ C10")
get_omega(r)
get_alpha(r)
agreement_margin(votrix(r))
condorcet_winner(r)
pors12nc$w11[[3]] <- r


r <- parse_profile_of_rankings("
3, C4 ≻ C7 ≻ C10 ≻ C5 ≻ C9 ≻ C1 ≻ C11 ≻ C6 ≻ C3 ≻ C2 ≻ C8 ≻ C12,
2, C7 ≻ C6 ≻ C5 ≻ C11 ≻ C4 ≻ C9 ≻ C3 ≻ C2 ≻ C8 ≻ C10 ≻ C12 ≻ C1,
2, C9 ≻ C2 ≻ C3 ≻ C10 ≻ C1 ≻ C4 ≻ C5 ≻ C6 ≻ C11 ≻ C7 ≻ C8 ≻ C12,
1, C10 ≻ C3 ≻ C7 ≻ C5 ≻ C8 ≻ C2 ≻ C1 ≻ C9 ≻ C11 ≻ C6 ≻ C12 ≻ C4,
2, C11 ≻ C1 ≻ C4 ≻ C2 ≻ C6 ≻ C8 ≻ C3 ≻ C12 ≻ C7 ≻ C5 ≻ C9 ≻ C10")
get_omega(r)
get_alpha(r)
agreement_margin(votrix(r))
condorcet_winner(r)
pors12nc$w11[[4]] <- r


r <- parse_profile_of_rankings("
1, C6 ≻ C10 ≻ C4 ≻ C12 ≻ C11 ≻ C3 ≻ C1 ≻ C5 ≻ C8 ≻ C2 ≻ C7 ≻ C9,
3, C2 ≻ C4 ≻ C12 ≻ C1 ≻ C3 ≻ C5 ≻ C10 ≻ C6 ≻ C9 ≻ C8 ≻ C11 ≻ C7,
1, C3 ≻ C6 ≻ C11 ≻ C8 ≻ C7 ≻ C2 ≻ C4 ≻ C12 ≻ C1 ≻ C9 ≻ C10 ≻ C5,
3, C7 ≻ C10 ≻ C8 ≻ C11 ≻ C6 ≻ C12 ≻ C1 ≻ C9 ≻ C3 ≻ C5 ≻ C4 ≻ C2,
1, C6 ≻ C9 ≻ C3 ≻ C12 ≻ C11 ≻ C4 ≻ C7 ≻ C8 ≻ C2 ≻ C1 ≻ C10 ≻ C5,
1, C2 ≻ C7 ≻ C1 ≻ C11 ≻ C8 ≻ C4 ≻ C10 ≻ C6 ≻ C9 ≻ C3 ≻ C12 ≻ C5")
get_omega(r)
get_alpha(r)
agreement_margin(votrix(r))
condorcet_winner(r)
pors12nc$w11[[5]] <- r

# n = 13 -------------------------------------------------------------------

## w = 1 faltan 5 ----------------------------------------------------------
pors13$w1

r <- parse_profile_of_rankings("
3, C4 ≻ C2 ≻ C10 ≻ C6 ≻ C11 ≻ C7 ≻ C9 ≻ C5 ≻ C12 ≻ C3 ≻ C13 ≻ C1 ≻ C8,
2, C2 ≻ C6 ≻ C5 ≻ C12 ≻ C9 ≻ C7 ≻ C13 ≻ C1 ≻ C3 ≻ C8 ≻ C10 ≻ C11 ≻ C4,
2, C8 ≻ C3 ≻ C6 ≻ C13 ≻ C1 ≻ C4 ≻ C5 ≻ C10 ≻ C12 ≻ C7 ≻ C11 ≻ C2 ≻ C9,
1, C6 ≻ C1 ≻ C9 ≻ C10 ≻ C12 ≻ C13 ≻ C7 ≻ C8 ≻ C5 ≻ C11 ≻ C3 ≻ C4 ≻ C2,
2, C11 ≻ C6 ≻ C8 ≻ C3 ≻ C1 ≻ C9 ≻ C7 ≻ C12 ≻ C4 ≻ C13 ≻ C10 ≻ C5 ≻ C2")
get_omega(r)
votrix(r)
get_alpha(r)
agreement_margin(votrix(r))
condorcet_winner(r)

r <- parse_profile_of_rankings("
3,  C1 ≻ C13 ≻ C11 ≻ C2 ≻ C3 ≻ C8 ≻ C12 ≻  C4 ≻ C7 ≻ C10 ≻ C6 ≻ C5 ≻ C9,
2, C13 ≻ C11 ≻ C7 ≻ C5  ≻ C3 ≻ C4  ≻ C8 ≻ C2 ≻ C9  ≻ C1 ≻ C10 ≻ C12 ≻ C6,
3, C11 ≻ C6 ≻ C10 ≻ C5 ≻ C9 ≻ C4 ≻ C12 ≻ C3 ≻ C7 ≻ C8  ≻ C1 ≻ C2 ≻ C13,
2, C9 ≻ C11 ≻ C6 ≻ C12 ≻ C10 ≻ C2  ≻ C7 ≻ C1 ≻ C8 ≻ C5 ≻ C3 ≻ C13 ≻ C4")
get_omega(r)
votrix(r)
get_alpha(r)
agreement_margin(votrix(r))
condorcet_winner(r)

r <- parse_profile_of_rankings("
1, C13 ≻ C3 ≻ C6 ≻ C2 ≻ C8 ≻ C11 ≻ C10 ≻ C4 ≻ C9 ≻ C7 ≻ C12 ≻ C5 ≻ C1,
1, C11 ≻ C13 ≻ C5 ≻ C6 ≻ C3 ≻ C2 ≻ C10 ≻ C9 ≻ C12 ≻ C7 ≻ C4 ≻ C1 ≻ C8,
1, C2 ≻ C10 ≻ C3 ≻ C8 ≻ C11 ≻ C9 ≻ C7 ≻ C4 ≻ C13 ≻ C6 ≻ C1 ≻ C12 ≻ C5,
2, C6 ≻ C7 ≻ C3 ≻ C9 ≻ C8 ≻ C1 ≻ C12 ≻ C4 ≻ C13 ≻ C5 ≻ C2 ≻ C10 ≻ C11,
1, C1 ≻ C5 ≻ C3 ≻ C12 ≻ C9 ≻ C10 ≻ C4 ≻ C2 ≻ C11 ≻ C7 ≻ C8 ≻ C13 ≻ C6,
2, C5 ≻ C3 ≻ C10 ≻ C1 ≻ C8 ≻ C2 ≻ C12 ≻ C13 ≻ C4 ≻ C9 ≻ C7 ≻ C11 ≻ C6,
1, C12 ≻ C4 ≻ C3 ≻ C1 ≻ C2 ≻ C7 ≻ C9 ≻ C10 ≻ C11 ≻ C13 ≻ C6 ≻ C5 ≻ C8,
1, C4 ≻ C7 ≻ C13 ≻ C6 ≻ C8 ≻ C12 ≻ C5 ≻ C3 ≻  C9 ≻ C1 ≻ C11 ≻ C10 ≻ C2")
get_omega(r)
votrix(r)
get_alpha(r)
agreement_margin(votrix(r))
condorcet_winner(r)


r <- parse_profile_of_rankings("
1, C8 ≻ C7 ≻ C3 ≻ C9 ≻ C4 ≻ C6 ≻ C10 ≻ C1 ≻ C13 ≻ C2 ≻ C11 ≻ C12 ≻ C5,
1, C12 ≻ C9 ≻ C13 ≻ C8 ≻ C6 ≻ C10 ≻ C1 ≻ C3 ≻ C7 ≻ C11 ≻ C2 ≻ C4 ≻ C5,
1, C11 ≻ C8 ≻ C5 ≻ C1 ≻ C6 ≻ C10 ≻ C9 ≻ C12 ≻ C2 ≻ C3 ≻ C13 ≻ C7 ≻ C4,
1, C10 ≻ C4 ≻ C8 ≻ C5 ≻ C9 ≻ C2 ≻ C1 ≻ C3 ≻ C13 ≻ C6 ≻ C7 ≻ C11 ≻ C12,
1, C12 ≻ C13 ≻ C5 ≻ C9 ≻ C11 ≻ C7 ≻ C3 ≻ C1 ≻ C6 ≻ C10 ≻ C4 ≻ C2 ≻ C8,
1, C4 ≻  C10 ≻ C8 ≻ C12 ≻ C9 ≻  C11 ≻ C13 ≻ C2 ≻ C3 ≻ C6 ≻ C7 ≻ C5 ≻ C1,
1, C9 ≻ C2 ≻ C7 ≻ C5 ≻ C1 ≻ C4 ≻ C6 ≻ C10 ≻ C13 ≻ C12 ≻ C8 ≻ C3 ≻ C11,
1, C11 ≻ C5 ≻ C9 ≻ C1 ≻ C3 ≻ C10 ≻ C2 ≻ C13 ≻ C4 ≻ C12 ≻ C6 ≻ C7 ≻ C8,
1, C9 ≻ C13 ≻ C11 ≻ C7 ≻ C4 ≻  C3 ≻ C1 ≻ C6 ≻ C12 ≻ C2 ≻ C8 ≻C10 ≻ C5,
1, C7 ≻ C2 ≻ C12 ≻ C5 ≻ C9 ≻ C6 ≻ C4 ≻ C1 ≻ C11 ≻ C8 ≻ C13 ≻ C3 ≻ C10")
get_omega(r)
votrix(r)
get_alpha(r)
agreement_margin(votrix(r))
condorcet_winner(r)

## w = 2 faltan 3 ---------------------------------------------------------
pors13$w2

r <- parse_profile_of_rankings("
3, C4 ≻ C2 ≻ C9 ≻ C5 ≻ C11 ≻ C10 ≻ C7 ≻ C6 ≻ C12 ≻ C3 ≻ C13 ≻ C1 ≻ C8,
2, C2 ≻ C6 ≻ C9 ≻ C12 ≻ C5 ≻ C7 ≻ C13 ≻ C1 ≻ C3 ≻ C8 ≻ C10 ≻ C11 ≻ C4,
2, C8 ≻ C3 ≻ C9 ≻ C13 ≻ C10 ≻ C6 ≻ C4 ≻ C5 ≻ C1 ≻ C12 ≻ C7 ≻ C11 ≻ C2,
1, C6 ≻ C1 ≻ C9 ≻ C10 ≻ C12 ≻ C13 ≻ C5 ≻ C8 ≻ C7 ≻ C4 ≻ C3 ≻ C11 ≻ C2,
2, C11 ≻ C9 ≻ C8 ≻ C3 ≻ C1 ≻ C6 ≻ C7 ≻ C12 ≻ C4 ≻ C13 ≻ C10 ≻ C2 ≻ C5")
get_omega(r)
votrix(r)
get_alpha(r)
agreement_margin(votrix(r))
condorcet_winner(r)
r <- parse_profile_of_rankings("
1, C9 ≻ C7 ≻ C3 ≻ C8 ≻ C4 ≻ C10 ≻ C6 ≻ C1 ≻ C13 ≻ C5 ≻ C12 ≻ C2 ≻ C11,
1, C12 ≻ C9 ≻ C5 ≻ C13 ≻ C8 ≻ C6 ≻ C10 ≻ C1 ≻ C3 ≻ C7 ≻ C11 ≻ C2 ≻ C4,
1, C5 ≻ C11 ≻ C8 ≻ C1 ≻ C6 ≻ C12 ≻ C9 ≻ C10 ≻ C2 ≻ C3 ≻ C13 ≻ C7 ≻ C4,
1, C4 ≻ C5 ≻ C10 ≻ C9 ≻ C8 ≻ C2 ≻ C1 ≻ C3 ≻ C13 ≻ C6 ≻ C7 ≻ C11 ≻ C12,
1, C12 ≻ C13 ≻ C5 ≻ C9 ≻ C11 ≻ C7 ≻ C3 ≻ C1 ≻ C10 ≻ C6 ≻ C4 ≻ C8 ≻ C2,
1, C4 ≻  C10 ≻ C8 ≻ C12 ≻ C9 ≻ C5 ≻ C11 ≻ C13 ≻ C6 ≻ C3 ≻ C2 ≻ C7 ≻ C1,
1, C9 ≻ C2 ≻ C5 ≻ C7 ≻ C1 ≻ C4 ≻ C6 ≻ C10 ≻ C13 ≻ C8 ≻ C12 ≻ C11 ≻ C3,
1, C11 ≻ C6 ≻ C9 ≻ C1 ≻ C3 ≻ C10 ≻ C2 ≻ C13 ≻ C4 ≻ C12 ≻ C5 ≻ C8 ≻ C7,
1, C9 ≻ C7 ≻ C13 ≻ C11 ≻ C4 ≻ C5 ≻ C3 ≻ C1 ≻ C6 ≻ C12 ≻ C2 ≻ C8 ≻ C10,
1, C7 ≻ C2 ≻ C5 ≻ C12 ≻ C8 ≻ C6 ≻ C1 ≻ C4 ≻ C9 ≻ C11 ≻ C13 ≻ C3 ≻ C10")
get_omega(r)
votrix(r)
get_alpha(r)
agreement_margin(votrix(r))
condorcet_winner(r)
