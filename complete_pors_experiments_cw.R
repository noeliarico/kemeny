votrix(pors7nc$w1$pr1)

# n = 8 -------------------------------------------------------------------

## w = 1 faltan 3 ---------------------------------------------------------
pors8cw$w1

r <- parse_profile_of_rankings("
1, C8 ≻ C2 ≻ C3 ≻ C6 ≻ C1 ≻ C7 ≻ C5 ≻ C4,
3, C6 ≻ C3 ≻ C4 ≻ C7 ≻ C8 ≻ C1 ≻ C2 ≻ C5,
3, C6 ≻ C5 ≻ C7 ≻ C1 ≻ C2 ≻ C3 ≻ C4 ≻ C8,
2, C8 ≻ C6 ≻ C4 ≻ C2 ≻ C5 ≻ C1 ≻ C7 ≻ C3,
1, C1 ≻ C4 ≻ C5 ≻ C8 ≻ C7 ≻ C6 ≻ C3 ≻ C2")
get_omega(r)
get_alpha(r)
condorcet_winner(r)
pors8cw$w1[[3]] <- r

r <- parse_profile_of_rankings("
2, C4 ≻ C2 ≻ C8 ≻ C1 ≻ C3 ≻ C5 ≻ C7 ≻ C6,
4, C2 ≻ C1 ≻ C3 ≻ C8 ≻ C5 ≻ C6 ≻ C4 ≻ C7,
4, C7 ≻ C6 ≻ C2 ≻ C5 ≻ C4 ≻ C3 ≻ C8 ≻ C1")
get_omega(r)
get_alpha(r)
condorcet_winner(r)
pors8cw$w1[[4]] <- r

r <- parse_profile_of_rankings("
1, C5 ≻ C2 ≻ C1 ≻ C3 ≻ C6 ≻ C7 ≻ C8 ≻ C4,
3, C5 ≻ C6 ≻ C2 ≻ C4 ≻ C8 ≻ C1 ≻ C3 ≻ C7,
4, C5 ≻ C7 ≻ C8 ≻ C4 ≻ C3 ≻ C1 ≻ C2 ≻ C6,
1, C6 ≻ C3 ≻ C5 ≻ C8 ≻ C1 ≻ C7 ≻ C2 ≻ C4,
1, C3 ≻ C7 ≻ C6 ≻ C1 ≻ C2 ≻ C5 ≻ C4 ≻ C8")
get_omega(r)
get_alpha(r)
condorcet_winner(r)
pors8cw$w1[[5]] <- r

## w = 7 faltan 3 ---------------------------------------------------------
pors8cw$w7

r <- parse_profile_of_rankings("
3, C6 ≻ C4 ≻ C2 ≻ C3 ≻ C8 ≻ C5 ≻ C1 ≻ C7,
2, C7 ≻ C3 ≻ C5 ≻ C2 ≻ C1 ≻ C4 ≻ C8 ≻ C6,
3, C6 ≻ C4 ≻ C5 ≻ C1 ≻ C7 ≻ C3 ≻ C2 ≻ C8,
2, C1 ≻ C7 ≻ C2 ≻ C3 ≻ C6 ≻ C5 ≻ C8 ≻ C4")
get_omega(r)
get_alpha(r)
condorcet_winner(r)
pors8cw$w7[[3]] <- r

r <- parse_profile_of_rankings("
4, C4 ≻ C8 ≻ C2 ≻ C3 ≻ C5 ≻ C1 ≻ C7 ≻ C6,
2, C7 ≻ C5 ≻ C3 ≻ C2 ≻ C1 ≻ C4 ≻ C8 ≻ C6,
2, C4 ≻ C1 ≻ C5 ≻ C7 ≻ C8 ≻ C3 ≻ C2 ≻ C6,
2, C7 ≻ C1 ≻ C2 ≻ C3 ≻ C5 ≻ C8 ≻ C6 ≻ C4")
get_omega(r)
get_alpha(r)
condorcet_winner(r)
pors8cw$w7[[4]] <- r

r <- parse_profile_of_rankings("
3, C5 ≻ C1 ≻ C4 ≻ C6 ≻ C2 ≻ C7 ≻ C8 ≻ C3,
2, C4 ≻ C5 ≻ C2 ≻ C8 ≻ C7 ≻ C1 ≻ C6 ≻ C3,
3, C7 ≻ C6 ≻ C8 ≻ C5 ≻ C1 ≻ C4 ≻ C2 ≻ C3,
1, C2 ≻ C8 ≻ C5 ≻ C6 ≻ C1 ≻ C7 ≻ C3 ≻ C4,
1, C1 ≻ C2 ≻ C8 ≻ C3 ≻ C6 ≻ C4 ≻ C5 ≻ C7")
get_omega(r)
get_alpha(r)
condorcet_winner(r)
pors8cw$w7[[5]] <- r

# n = 9 -------------------------------------------------------------------

## w = 1 faltan 5 ---------------------------------------------------------
pors9cw$w1

r <- parse_profile_of_rankings("
1, C8 ≻ C2 ≻ C9 ≻ C3 ≻ C6 ≻ C1 ≻ C7 ≻ C5 ≻ C4,
3, C6 ≻ C3 ≻ C7 ≻ C9 ≻ C4 ≻ C8 ≻ C1 ≻ C2 ≻ C5,
3, C6 ≻ C5 ≻ C7 ≻ C1 ≻ C2 ≻ C3 ≻ C4 ≻ C9 ≻ C8,
2, C8 ≻ C6 ≻ C4 ≻ C2 ≻ C5 ≻ C9 ≻ C1 ≻ C3 ≻ C7,
1, C1 ≻ C4 ≻ C5 ≻ C8 ≻ C6 ≻ C2 ≻ C3 ≻ C9 ≻ C7")
get_omega(r)
get_alpha(r)
condorcet_winner(r)
pors9cw$w1[[1]] <- r

r <- parse_profile_of_rankings("
4, C4 ≻ C9 ≻ C8 ≻ C1  ≻ C5 ≻ C6 ≻ C7 ≻ C3 ≻ C2,
2, C9 ≻ C2 ≻ C1 ≻ C3 ≻ C5 ≻ C8 ≻ C4  ≻ C6 ≻ C7,
4, C9 ≻ C7 ≻ C6 ≻ C2 ≻ C3 ≻ C5 ≻ C8 ≻ C1 ≻ C4")
get_omega(r)
get_alpha(r)
condorcet_winner(r)
pors9cw$w1[[2]] <- r

r <- parse_profile_of_rankings("
3, C4 ≻ C3 ≻ C9 ≻ C7 ≻ C5 ≻ C2 ≻ C6 ≻ C1 ≻ C8,
3, C5 ≻ C3 ≻ C6 ≻ C8 ≻ C9 ≻ C4 ≻ C2 ≻ C7 ≻ C1,
4, C3 ≻ C1 ≻ C2 ≻ C7 ≻ C8 ≻ C6 ≻ C9 ≻ C4 ≻ C5")
get_omega(r)
get_alpha(r)
condorcet_winner(r)
pors9cw$w1[[3]] <- r

r <- parse_profile_of_rankings("
1, C2 ≻ C6 ≻ C4 ≻ C1 ≻ C8 ≻ C9 ≻ C3 ≻ C5 ≻ C7,
3, C6 ≻ C4 ≻ C7 ≻ C8 ≻ C1 ≻ C9 ≻ C3 ≻ C2 ≻ C5,
2, C4 ≻ C9 ≻ C5 ≻ C3 ≻ C7 ≻ C8 ≻ C6 ≻ C1 ≻ C2,
1, C1 ≻ C4 ≻ C5 ≻ C3 ≻ C8 ≻ C2 ≻ C7 ≻ C6 ≻ C9,
3, C2 ≻ C4 ≻ C5 ≻ C3 ≻ C9 ≻ C8 ≻ C1 ≻ C6 ≻ C7")
get_omega(r)
get_alpha(r)
condorcet_winner(r)
pors9cw$w1[[4]] <- r

r <- parse_profile_of_rankings("
1, C1 ≻ C5 ≻ C3 ≻ C8 ≻ C6 ≻ C2 ≻ C4 ≻ C7 ≻ C9,
3, C8 ≻ C5 ≻ C4 ≻ C9 ≻ C2 ≻ C1 ≻ C6 ≻ C7 ≻ C3,
2, C7 ≻ C3 ≻ C8 ≻ C1 ≻ C6 ≻ C2 ≻ C4 ≻ C9 ≻ C5,
2, C8 ≻ C4 ≻ C3 ≻ C7 ≻ C9 ≻ C6 ≻ C5 ≻ C1 ≻ C2,
2, C8 ≻ C6 ≻ C2 ≻ C1 ≻ C7 ≻ C9 ≻ C5 ≻ C3 ≻ C4")
get_omega(r)
get_alpha(r)
condorcet_winner(r)
pors9cw$w1[[5]] <- r

## w = 8 faltan 5 ---------------------------------------------------------

r <- parse_profile_of_rankings("
2, C9 ≻ C7 ≻ C6 ≻ C1 ≻ C8 ≻ C2 ≻ C4 ≻ C5 ≻ C3,
1, C6 ≻ C8 ≻ C1 ≻ C7 ≻ C4 ≻ C9 ≻ C3 ≻ C2 ≻ C5,
2, C4 ≻ C7 ≻ C9 ≻ C1 ≻ C6 ≻ C5 ≻ C8 ≻ C3 ≻ C2,
2, C1 ≻ C5 ≻ C8 ≻ C2 ≻ C4 ≻ C6 ≻ C7 ≻ C3 ≻ C9,
3, C2 ≻ C1 ≻ C5 ≻ C4 ≻ C9 ≻ C8 ≻ C6 ≻ C7 ≻ C3")
get_omega(r)
get_alpha(r)
condorcet_winner(r)
pors9cw$w8[[1]] <- r

r <- parse_profile_of_rankings("
3, C5 ≻ C8 ≻ C4 ≻ C2 ≻ C3 ≻ C7 ≻ C9 ≻ C6 ≻ C1,
2, C5 ≻ C2 ≻ C7 ≻ C6 ≻ C9 ≻ C4 ≻ C1 ≻ C8 ≻ C3,
1, C7 ≻ C5 ≻ C6 ≻ C4 ≻ C9 ≻ C8 ≻ C3 ≻ C1 ≻ C2,
3, C3 ≻ C2 ≻ C9 ≻ C6 ≻ C7 ≻ C8 ≻ C4 ≻ C5 ≻ C1,
1, C6 ≻ C8 ≻ C4 ≻ C3 ≻ C9 ≻ C2 ≻ C5 ≻ C1 ≻ C7")
get_omega(r)
get_alpha(r)
condorcet_winner(r)
pors9cw$w8[[2]] <- r

r <- parse_profile_of_rankings("
2, C1 ≻ C4 ≻ C7 ≻ C9 ≻ C5 ≻ C8 ≻ C2 ≻ C3 ≻ C6,
4, C2 ≻ C9 ≻ C6 ≻ C5 ≻ C8 ≻ C7 ≻ C1 ≻ C3 ≻ C4,
2, C4 ≻ C1 ≻ C8 ≻ C9 ≻ C7 ≻ C2 ≻ C5 ≻ C3 ≻ C6,
2, C6 ≻ C5 ≻ C2 ≻ C4 ≻ C7 ≻ C8 ≻ C3 ≻ C1 ≻ C9")
get_omega(r)
get_alpha(r)
condorcet_winner(r)
pors9cw$w8[[3]] <- r

r <- parse_profile_of_rankings("
3, C7 ≻ C9 ≻ C5 ≻ C1 ≻ C2 ≻ C6 ≻ C4 ≻ C8 ≻ C3,
2, C9 ≻ C2 ≻ C5 ≻ C4 ≻ C8 ≻ C7 ≻ C1 ≻ C6 ≻ C3,
3, C4 ≻ C6 ≻ C8 ≻ C5 ≻ C1 ≻ C9 ≻ C2 ≻ C7 ≻ C3,
1, C9 ≻ C2 ≻ C8 ≻ C5 ≻ C6 ≻ C1 ≻ C4 ≻ C7 ≻ C3,
1, C1 ≻ C2 ≻ C7 ≻ C8 ≻ C6 ≻ C9 ≻ C4 ≻ C5 ≻ C3")
get_omega(r)
get_alpha(r)
condorcet_winner(r)
pors9cw$w8[[4]] <- r

r <- parse_profile_of_rankings("
1, C2 ≻ C9 ≻ C6 ≻ C3 ≻ C1 ≻ C8 ≻ C7 ≻ C4 ≻ C5,
2, C9 ≻ C4 ≻ C6 ≻ C5 ≻ C2 ≻ C1 ≻ C7 ≻ C3 ≻ C8,
2, C7 ≻ C1 ≻ C8 ≻ C5 ≻ C9 ≻ C3 ≻ C4 ≻ C2 ≻ C6,
2, C3 ≻ C6 ≻ C1 ≻ C4 ≻ C7 ≻ C5 ≻ C8 ≻ C9 ≻ C2,
1, C2 ≻ C9 ≻ C5 ≻ C7 ≻ C3 ≻ C4 ≻ C1 ≻ C6 ≻ C8,
2, C2 ≻ C9 ≻ C6 ≻ C5 ≻ C4 ≻ C7 ≻ C3 ≻ C1 ≻ C8")
get_omega(r)
get_alpha(r)
condorcet_winner(r)
pors9cw$w8[[5]] <- r



# n = 10 -------------------------------------------------------------------

## w = 1 faltan 5 ----------------------------------------------------------

r <- parse_profile_of_rankings("
1, C1 ≻ C10 ≻ C5 ≻ C3 ≻ C8 ≻ C6 ≻ C2 ≻ C4 ≻ C7 ≻ C9,
3, C5 ≻ C10 ≻ C4 ≻ C9 ≻ C2 ≻ C1 ≻ C6 ≻ C8 ≻ C7 ≻ C3,
2, C7 ≻ C10 ≻ C3 ≻ C8 ≻ C1 ≻ C6 ≻ C2 ≻ C4 ≻ C9 ≻ C5,
2, C8 ≻ C4 ≻ C10 ≻ C3 ≻ C7 ≻ C9 ≻ C6 ≻ C5 ≻ C1 ≻ C2,
2, C2 ≻ C10 ≻ C6 ≻ C3 ≻ C1 ≻ C7 ≻ C9 ≻ C5 ≻ C8 ≻ C4")
get_omega(r)
get_alpha(r)
condorcet_winner(r)
pors10cw$w1[[1]] <- r

r <- parse_profile_of_rankings("
3, C4 ≻ C9 ≻ C10 ≻ C5 ≻ C7 ≻ C1 ≻ C6 ≻ C3 ≻ C8 ≻ C2,
1, C6 ≻ C1 ≻ C8 ≻ C5 ≻ C10 ≻ C3 ≻ C4 ≻ C9 ≻ C7 ≻ C2,
2, C1 ≻ C5 ≻ C6 ≻ C8 ≻ C4 ≻ C2 ≻ C3 ≻ C7 ≻ C10 ≻ C9,
4, C2 ≻ C1 ≻ C3 ≻ C7 ≻ C8 ≻ C9 ≻ C10 ≻ C6 ≻ C4 ≻ C5")
get_omega(r)
get_alpha(r)
condorcet_winner(r)
pors10cw$w1[[2]] <- r

r <- parse_profile_of_rankings("
3, C3 ≻ C4 ≻ C9 ≻ C10 ≻ C7 ≻ C5 ≻ C2 ≻ C6 ≻ C1 ≻ C8,
3, C5 ≻ C10 ≻ C3 ≻ C6 ≻ C8 ≻ C4 ≻ C9 ≻ C2 ≻ C7 ≻ C1,
4, C3 ≻ C1 ≻ C8 ≻ C2 ≻ C7 ≻ C6 ≻ C9 ≻ C4 ≻ C5 ≻ C10")
get_omega(r)
get_alpha(r)
condorcet_winner(r)
pors10cw$w1[[3]] <- r


r <- parse_profile_of_rankings("
1, C7 ≻ C10 ≻ C3 ≻ C8 ≻ C4 ≻ C2 ≻ C1 ≻ C5 ≻ C6,
2, C5 ≻ C8 ≻ C1 ≻ C6 ≻ C3 ≻ C7 ≻ C2 ≻ C10 ≻ C4,
2, C10 ≻ C4 ≻ C6 ≻ C8 ≻ C7 ≻ C5 ≻ C3 ≻ C1 ≻ C2,
2, C10 ≻ C7 ≻ C2 ≻ C1 ≻ C6 ≻ C8 ≻ C3 ≻ C4 ≻ C5,
2, C4 ≻ C10 ≻ C2 ≻ C3 ≻ C5 ≻ C6 ≻ C1 ≻ C8 ≻ C7,
1, C1 ≻ C5 ≻ C3 ≻ C10 ≻ C2 ≻ C4 ≻ C8 ≻ C7 ≻ C6")
get_omega(r)
get_alpha(r)
condorcet_winner(r)
pors10cw$w1[[4]] <- r


r <- parse_profile_of_rankings("
2, C4 ≻ C3 ≻ C6 ≻ C7 ≻ C5 ≻ C9 ≻ C1 ≻ C2 ≻ C10 ≻ C8,
2, C2 ≻ C6 ≻ C1 ≻ C3 ≻ C10 ≻ C5 ≻ C8 ≻ C4 ≻ C9 ≻ C7,
1, C7 ≻ C6 ≻ C3 ≻ C8 ≻ C2 ≻ C5 ≻ C4 ≻ C9 ≻ C1 ≻ C10,
1, C6 ≻ C2 ≻ C9 ≻ C5 ≻ C4 ≻ C8 ≻ C3 ≻ C1 ≻ C7 ≻ C10,
1, C10 ≻ C8 ≻ C9 ≻ C3 ≻ C1 ≻ C7 ≻ C6 ≻ C2 ≻ C5 ≻ C4,
2, C10 ≻ C8 ≻ C7 ≻ C6 ≻ C5 ≻ C1 ≻ C4 ≻ C9 ≻ C2 ≻ C3,
1, C6 ≻ C4 ≻ C1 ≻ C9 ≻ C10 ≻ C2 ≻ C8 ≻ C7 ≻ C5 ≻ C3")
get_omega(r)
get_alpha(r)
condorcet_winner(r)
pors10cw$w1[[5]] <- r


## w = 9 faltan 5 ----------------------------------------------------------

r <- parse_profile_of_rankings("
1, C9 ≻ C1 ≻ C5 ≻ C7 ≻ C2 ≻ C3 ≻ C6 ≻ C4 ≻ C8 ≻ C10,
3, C8 ≻ C5 ≻ C4 ≻ C2 ≻ C1 ≻ C3 ≻ C10 ≻ C9 ≻ C7 ≻ C6,
2, C9 ≻ C6 ≻ C7 ≻ C3 ≻ C8 ≻ C1 ≻ C4 ≻ C5 ≻ C2 ≻ C10,
2, C8 ≻ C7 ≻ C4 ≻ C2 ≻ C6 ≻ C3 ≻ C5 ≻ C10 ≻ C1 ≻ C9,
2, C8 ≻ C6 ≻ C9 ≻ C1 ≻ C3 ≻ C2 ≻ C7 ≻ C5 ≻ C4 ≻ C10")
get_omega(r)
get_alpha(r)
condorcet_winner(r)
pors10cw$w9[[1]] <- r

r <- parse_profile_of_rankings("
1, C7 ≻ C8 ≻ C5 ≻ C2 ≻ C4 ≻ C3 ≻ C1 ≻ C9 ≻ C6 ≻ C10,
1, C7 ≻ C5 ≻ C1 ≻ C4 ≻ C3 ≻ C9 ≻ C6 ≻ C10 ≻ C8 ≻ C2,
3, C2 ≻ C1 ≻ C5 ≻ C7 ≻ C3 ≻ C9 ≻ C6 ≻ C8 ≻ C4 ≻ C10,
2, C9 ≻ C3 ≻ C5 ≻ C6 ≻ C4 ≻ C1 ≻ C8 ≻ C2 ≻ C7 ≻ C10,
3, C6 ≻ C8 ≻ C4 ≻ C5 ≻ C7 ≻ C2 ≻ C9 ≻ C3 ≻ C1 ≻ C10")
get_omega(r)
get_alpha(r)
condorcet_winner(r)
pors10cw$w9[[2]] <- r

r <- parse_profile_of_rankings("
4, C6 ≻ C9 ≻ C5 ≻ C2 ≻ C8 ≻ C7 ≻ C1 ≻ C10 ≻ C4 ≻ C3,
4, C3 ≻ C1 ≻ C10 ≻ C8 ≻ C7 ≻ C5 ≻ C9 ≻ C2 ≻ C6 ≻ C4,
2, C3 ≻ C2 ≻ C10 ≻ C6 ≻ C7 ≻ C8 ≻ C1 ≻ C5 ≻ C9 ≻ C4")
get_omega(r)
get_alpha(r)
condorcet_winner(r)
pors10cw$w9[[3]] <- r

r <- parse_profile_of_rankings("
1, C6 ≻ C10 ≻ C2 ≻ C3 ≻ C9 ≻ C1 ≻ C7 ≻ C5 ≻ C8 ≻ C4,
2, C5 ≻ C10 ≻ C9 ≻ C1 ≻ C4 ≻ C6 ≻ C2 ≻ C3 ≻ C7 ≻ C8,
2, C7 ≻ C9 ≻ C10 ≻ C1 ≻ C5 ≻ C4 ≻ C2 ≻ C8 ≻ C6 ≻ C3,
2, C3 ≻ C10 ≻ C4 ≻ C6 ≻ C7 ≻ C1 ≻ C5 ≻ C8 ≻ C9 ≻ C2,
1, C2 ≻ C9 ≻ C5 ≻ C7 ≻ C10 ≻ C6 ≻ C3 ≻ C1 ≻ C4 ≻ C8,
2, C2 ≻ C3 ≻ C10 ≻ C4 ≻ C6 ≻ C1 ≻ C7 ≻ C9 ≻ C5 ≻ C8")
get_omega(r)
get_alpha(r)
condorcet_winner(r)
pors10cw$w9[[4]] <- r

r <- parse_profile_of_rankings("
1, C3 ≻ C1 ≻ C9 ≻ C7 ≻ C6 ≻ C10 ≻ C2 ≻ C5 ≻ C8 ≻ C4,
2, C9 ≻ C3 ≻ C5 ≻ C6 ≻ C8 ≻ C10 ≻ C7 ≻ C2 ≻ C4 ≻ C1,
1, C10 ≻ C3 ≻ C2 ≻ C1 ≻ C5 ≻ C6 ≻ C4 ≻ C7 ≻ C9 ≻ C8,
1, C2 ≻ C8 ≻ C7 ≻ C10 ≻ C5 ≻ C3 ≻ C4 ≻ C9 ≻ C6 ≻ C1,
2, C10 ≻ C3 ≻ C6 ≻ C5 ≻ C1 ≻ C9 ≻ C8 ≻ C7 ≻ C2 ≻ C4,
1, C1 ≻ C8 ≻ C6 ≻ C3 ≻ C7 ≻ C2 ≻ C5 ≻ C9 ≻ C10 ≻ C4,
2, C7 ≻ C2 ≻ C8 ≻ C1 ≻ C5 ≻ C9 ≻ C6 ≻ C3 ≻ C4 ≻ C10")
get_omega(r)
get_alpha(r)
condorcet_winner(r)
pors10cw$w9[[5]] <- r

# n = 10 -------------------------------------------------------------------

## w = 1 faltan 5 ----------------------------------------------------------

r <- parse_profile_of_rankings("
2, C3 ≻ C2 ≻ C10 ≻ C7 ≻ C6 ≻ C5 ≻ C9 ≻ C4 ≻ C8 ≻ C1 ≻ C11,
3, C10 ≻ C11 ≻ C8 ≻ C9 ≻ C6 ≻ C7 ≻ C5 ≻ C1 ≻ C4 ≻ C3 ≻ C2,
2, C10 ≻ C2 ≻ C1 ≻ C3 ≻ C7 ≻ C9 ≻ C5 ≻ C8 ≻ C4 ≻ C11 ≻ C6,
1, C4 ≻ C3 ≻ C5 ≻ C2 ≻ C10 ≻ C11 ≻ C8 ≻ C6 ≻ C1 ≻ C7 ≻ C9,
2, C10 ≻ C1 ≻ C4 ≻ C11 ≻ C6 ≻ C5 ≻ C9 ≻ C8 ≻ C7 ≻ C3 ≻ C2")
get_omega(r)
get_alpha(r)
votrix(r)
condorcet_winner(r)
pors11cw$w1[[1]] <- r

r <- parse_profile_of_rankings("
3, C4 ≻ C11 ≻ C10 ≻ C5 ≻ C7 ≻ C1 ≻ C9 ≻ C6 ≻ C3 ≻ C8 ≻ C2,
1, C11 ≻ C6 ≻ C5 ≻ C8 ≻ C1 ≻ C10 ≻ C3 ≻ C4 ≻ C9 ≻ C7 ≻ C2,
2, C5 ≻ C11 ≻ C6 ≻ C8 ≻ C1 ≻ C4 ≻ C2 ≻ C3 ≻ C7 ≻ C10 ≻ C9,
4, C11 ≻ C2 ≻ C9 ≻ C3 ≻ C7 ≻ C8 ≻ C1 ≻ C10 ≻ C6 ≻ C4 ≻ C5")
get_omega(r)
get_alpha(r)
votrix(r)
condorcet_winner(r)
pors11cw$w1[[2]] <- r

r <- parse_profile_of_rankings("
3, C3 ≻ C9 ≻ C4 ≻ C10 ≻ C7 ≻ C5 ≻ C2 ≻ C6 ≻ C1 ≻ C8 ≻ C11,
3, C5 ≻ C10 ≻ C3 ≻ C6 ≻ C8 ≻ C4 ≻ C11 ≻ C9 ≻ C2 ≻ C7 ≻ C1,
4, C3 ≻ C11 ≻ C1 ≻ C8 ≻ C2 ≻ C7 ≻ C6 ≻ C9 ≻ C4 ≻ C5 ≻ C10")
get_omega(r)
get_alpha(r)
votrix(r)
condorcet_winner(r)
pors11cw$w1[[3]] <- r

r <- parse_profile_of_rankings("
2, C4 ≻ C11 ≻ C3 ≻ C7 ≻ C5 ≻ C9 ≻ C1 ≻ C2 ≻ C10 ≻ C8 ≻ C6,
2, C2 ≻ C6 ≻ C11 ≻ C1 ≻ C3 ≻ C10 ≻ C5 ≻ C8 ≻ C9 ≻ C4 ≻ C7,
1, C7 ≻ C11 ≻ C6 ≻ C3 ≻ C8 ≻ C2 ≻ C5 ≻ C4 ≻ C9 ≻ C1 ≻ C10,
1, C11 ≻ C2 ≻ C9 ≻ C4 ≻ C5 ≻ C8 ≻ C6 ≻ C1 ≻ C3 ≻ C7 ≻ C10,
1, C11 ≻ C10 ≻ C8 ≻ C9 ≻ C3 ≻ C1 ≻ C7 ≻ C6 ≻ C2 ≻ C5 ≻ C4,
2, C10 ≻ C11 ≻ C8 ≻ C7 ≻ C6 ≻ C5 ≻ C1 ≻ C4 ≻ C9 ≻ C2 ≻ C3,
1, C11 ≻ C4 ≻ C1 ≻ C9 ≻ C10 ≻ C2 ≻ C8  ≻ C6 ≻ C7 ≻ C3 ≻ C5")
get_omega(r)
get_alpha(r)
votrix(r)
condorcet_winner(r)
pors11cw$w1[[4]] <- r


r <- parse_profile_of_rankings("
2, C4 ≻ C3 ≻ C6 ≻ C7 ≻ C5 ≻ C9 ≻ C1 ≻ C2 ≻ C10 ≻ C8,
2, C3 ≻ C10 ≻ C2 ≻ C1 ≻ C5 ≻ C6 ≻ C8 ≻ C4 ≻ C9 ≻ C7,
2, C7 ≻ C3 ≻ C8 ≻ C2 ≻ C4 ≻ C5 ≻ C9 ≻ C6 ≻ C1 ≻ C10,
2, C3 ≻ C6 ≻ C9 ≻ C5 ≻ C4 ≻ C8 ≻ C2 ≻ C1 ≻ C7 ≻ C10,
2, C1 ≻ C8 ≻ C9 ≻ C3 ≻ C10 ≻ C7 ≻ C2 ≻ C5 ≻ C6 ≻ C4")
get_omega(r)
get_alpha(r)
votrix(r)
condorcet_winner(r)
pors11cw$w1[[5]] <- r

## w = 9 faltan 5 ----------------------------------------------------------

r <- parse_profile_of_rankings("
3, C1 ≻ C11 ≻ C3 ≻ C9 ≻ C2 ≻ C6 ≻ C8 ≻ C5 ≻ C4 ≻ C7 ≻ C10,
2, C5 ≻ C9 ≻ C1 ≻ C7 ≻ C8 ≻ C3 ≻ C6 ≻ C11 ≻ C10 ≻ C4 ≻ C2,
1, C2 ≻ C7 ≻ C6 ≻ C9 ≻ C11 ≻ C3 ≻ C8 ≻ C4 ≻ C10 ≻ C1 ≻ C5,
1, C9 ≻ C6 ≻ C5 ≻ C2 ≻ C10 ≻ C8 ≻ C1 ≻ C4 ≻ C11 ≻ C7 ≻ C3,
1, C11 ≻ C3 ≻ C1 ≻ C7 ≻ C5 ≻ C10 ≻ C2 ≻ C9 ≻ C6 ≻ C8 ≻ C4,
2, C8 ≻ C9 ≻ C7 ≻ C3 ≻ C2 ≻ C6 ≻ C5 ≻ C1 ≻ C4 ≻ C11 ≻ C10")
get_omega(r)
get_alpha(r)
votrix(r)
condorcet_winner(r)
pors11cw$w9[[1]] <- r

r <- parse_profile_of_rankings("
1, C7 ≻ C11 ≻ C8 ≻ C3 ≻ C4 ≻ C2 ≻ C1 ≻ C9 ≻ C5 ≻ C6 ≻ C10,
1, C7 ≻ C6 ≻ C5 ≻ C1 ≻ C4 ≻ C3 ≻ C10 ≻ C9 ≻ C8 ≻ C11 ≻ C2,
3, C2 ≻ C5 ≻ C11 ≻ C1 ≻ C6 ≻ C7 ≻ C4 ≻ C9 ≻ C8 ≻ C10 ≻ C3,
2, C9 ≻ C3 ≻ C6 ≻ C2 ≻ C7 ≻ C1 ≻ C8 ≻ C4 ≻ C5 ≻ C11 ≻ C10,
3, C6 ≻ C8 ≻ C4 ≻ C3 ≻ C9 ≻ C11 ≻ C2 ≻ C5 ≻ C1 ≻ C7 ≻ C10")
get_omega(r)
get_alpha(r)
votrix(r)
condorcet_winner(r)
condorcet(r, seePoints = T)
pors11cw$w9[[2]] <- r

r <- parse_profile_of_rankings("
2, C5 ≻ C11 ≻ C2 ≻ C8 ≻ C7 ≻ C1 ≻ C4 ≻ C10 ≻ C6 ≻ C3 ≻ C9,
1, C4 ≻ C1 ≻ C5 ≻ C10 ≻ C9 ≻ C2 ≻ C3 ≻ C8 ≻ C11 ≻ C7 ≻ C6,
1, C3 ≻ C7 ≻ C4 ≻ C8 ≻ C11 ≻ C6 ≻ C10 ≻ C1 ≻ C2 ≻ C9 ≻ C5,
1, C3 ≻ C6 ≻ C11 ≻ C7 ≻ C2 ≻ C9 ≻ C10 ≻ C5 ≻ C8 ≻ C4 ≻ C1,
1, C2 ≻ C10 ≻ C1 ≻ C8 ≻ C6 ≻ C11 ≻ C3 ≻ C4 ≻ C9 ≻ C5 ≻ C7,
2, C2 ≻ C6 ≻ C1 ≻ C7 ≻ C11 ≻ C9 ≻ C8 ≻ C5 ≻ C3 ≻ C10 ≻ C4,
2, C4 ≻ C10 ≻ C3 ≻ C2 ≻ C5 ≻ C8 ≻ C7 ≻ C6 ≻ C1 ≻ C9 ≻ C11")
get_omega(r)
get_alpha(r)
votrix(r)
condorcet_winner(r)
condorcet(r, seePoints = T)
pors11cw$w9[[3]] <- r


r <- parse_profile_of_rankings("
1, C2 ≻ C9 ≻ C6 ≻ C3 ≻ C8 ≻ C7 ≻ C10 ≻ C11 ≻ C1 ≻ C4 ≻ C5,
2, C9 ≻ C11 ≻ C4 ≻ C5 ≻ C6 ≻ C10 ≻ C8 ≻ C2 ≻ C7 ≻ C1 ≻ C3,
2, C7 ≻ C10 ≻ C8 ≻ C9 ≻ C5 ≻ C3 ≻ C4 ≻ C11 ≻ C2 ≻ C1 ≻ C6,
2, C6 ≻ C3 ≻ C11 ≻ C10 ≻ C9 ≻ C4 ≻ C8 ≻ C7 ≻ C5 ≻ C2 ≻ C1,
1, C8 ≻ C11 ≻ C2 ≻ C5 ≻ C9 ≻ C7 ≻ C3 ≻ C10 ≻ C4 ≻ C1 ≻ C6,
2, C2 ≻ C3 ≻ C6 ≻ C5 ≻ C4 ≻ C7 ≻ C9 ≻ C10 ≻ C8 ≻ C11 ≻ C1")
get_omega(r)
get_alpha(r)
votrix(r)
condorcet_winner(r)
condorcet(r, seePoints = T)
pors11cw$w9[[4]] <- r

r <- parse_profile_of_rankings("
2, C2 ≻ C9 ≻ C6 ≻ C3 ≻ C8 ≻ C7 ≻ C10 ≻ C11 ≻ C4 ≻ C5 ≻ C1,
2, C5 ≻ C9 ≻ C4 ≻ C11 ≻ C6 ≻ C10 ≻ C8 ≻ C2 ≻ C7 ≻ C1 ≻ C3,
2, C7 ≻ C4 ≻ C10 ≻ C8 ≻ C9 ≻ C5 ≻ C3 ≻ C11 ≻ C2 ≻ C1 ≻ C6,
2, C6 ≻ C3 ≻ C11 ≻ C10 ≻ C9 ≻ C4 ≻ C8 ≻ C7 ≻ C5 ≻ C2 ≻ C1,
2, C2 ≻ C3 ≻ C6 ≻ C5 ≻ C11 ≻ C7 ≻ C9 ≻ C10 ≻ C8 ≻ C4 ≻ C1")
get_omega(r)
get_alpha(r)
votrix(r)
condorcet_winner(r)
condorcet(r, seePoints = T)
pors11cw$w9[[5]] <- r

## w = 10 faltan 5 ----------------------------------------------------------

r <- parse_profile_of_rankings("
3, C1 ≻ C11 ≻ C4 ≻ C9 ≻ C3 ≻ C2 ≻ C6 ≻ C8 ≻ C5 ≻ C7 ≻ C10,
2, C5 ≻ C9 ≻ C1 ≻ C7 ≻ C8 ≻ C6 ≻ C3 ≻ C11 ≻ C2 ≻ C4 ≻ C10,
1, C2 ≻ C7 ≻ C6 ≻ C9 ≻ C4 ≻ C3 ≻ C8 ≻ C5 ≻ C11 ≻ C1 ≻ C10,
1, C9 ≻ C4 ≻ C6 ≻ C5 ≻ C2 ≻ C8 ≻ C1 ≻ C11 ≻ C10 ≻ C7 ≻ C3,
1, C11 ≻ C3 ≻ C1 ≻ C7 ≻ C5 ≻ C4 ≻ C2 ≻ C9 ≻ C6 ≻ C8 ≻ C10,
2, C8 ≻ C9 ≻ C7 ≻ C3 ≻ C2 ≻ C6 ≻ C5 ≻ C1 ≻ C4 ≻ C11 ≻ C10")
get_omega(r)
get_alpha(r)
votrix(r)
condorcet_winner(r)
pors11cw$w10[[1]] <- r

r <- parse_profile_of_rankings("
1, C6 ≻ C3 ≻ C11 ≻ C1 ≻ C9 ≻ C2 ≻ C8 ≻ C5 ≻ C4 ≻ C10 ≻ C7,
4, C5 ≻ C10 ≻ C7 ≻ C11 ≻ C2 ≻ C8 ≻ C6 ≻ C1 ≻ C3 ≻ C4 ≻ C9,
3, C9 ≻ C7 ≻ C1 ≻ C11 ≻ C3 ≻ C8 ≻ C2 ≻ C10 ≻ C6 ≻ C5 ≻ C4,
2, C5 ≻ C6 ≻ C3 ≻ C9 ≻ C8 ≻ C2 ≻ C1 ≻ C10 ≻ C7 ≻ C4 ≻ C11")
get_omega(r)
get_alpha(r)
votrix(r)
condorcet_winner(r)
condorcet(r, seePoints = T)
pors11cw$w10[[2]] <- r

r <- parse_profile_of_rankings("
3, C1 ≻ C11 ≻ C3 ≻ C9 ≻ C2 ≻ C6 ≻ C8 ≻ C5 ≻ C4 ≻ C10 ≻ C7,
1, C5 ≻ C10 ≻ C7 ≻ C2 ≻ C9 ≻ C1 ≻ C8 ≻ C3 ≻ C6 ≻ C11 ≻ C4,
2, C9 ≻ C7 ≻ C6 ≻ C2 ≻ C11 ≻ C8 ≻ C3 ≻ C10 ≻ C5 ≻ C1 ≻ C4,
1, C5 ≻ C2 ≻ C6 ≻ C9 ≻ C8 ≻ C4 ≻ C1 ≻ C10 ≻ C7 ≻ C11 ≻ C3,
1, C10 ≻ C11 ≻ C7 ≻ C5 ≻ C1 ≻ C3 ≻ C2 ≻ C9 ≻ C4 ≻ C6 ≻ C8,
2, C10 ≻ C8 ≻ C9 ≻ C7 ≻ C3 ≻ C5 ≻ C6 ≻ C2 ≻ C1 ≻ C4 ≻ C11")
get_omega(r)
get_alpha(r)
votrix(r)
condorcet_winner(r)
condorcet(r, seePoints = T)
pors11cw$w10[[3]] <- r

r <- parse_profile_of_rankings("
2, C4 ≻ C7 ≻ C10 ≻ C9 ≻ C1 ≻ C5 ≻ C11 ≻ C6 ≻ C3 ≻ C2 ≻ C8,
2, C7 ≻ C6 ≻ C5 ≻ C4 ≻ C11 ≻ C9 ≻  C3 ≻ C2 ≻ C10 ≻ C8 ≻ C1,
3, C2 ≻ C3 ≻ C10 ≻ C4 ≻ C1 ≻ C5 ≻ C6 ≻ C11 ≻ C7 ≻ C9 ≻ C8,
1, C10 ≻ C3 ≻ C7 ≻ C5 ≻ C2 ≻ C1 ≻ C9 ≻ C11 ≻ C6 ≻ C8 ≻ C4,
2, C9 ≻ C11 ≻ C1 ≻ C4 ≻ C6 ≻ C2 ≻ C3 ≻ C7 ≻ C5 ≻ C8 ≻ C10")
get_omega(r)
get_alpha(r)
votrix(r)
condorcet_winner(r)
condorcet(r, seePoints = T)
pors11cw$w10[[4]] <- r

r <- parse_profile_of_rankings("
3, C11 ≻ C1 ≻ C3 ≻ C9 ≻ C7 ≻ C6 ≻ C8 ≻ C5 ≻ C2 ≻ C10 ≻ C4,
3, C10 ≻ C5 ≻ C1 ≻ C2 ≻ C11 ≻ C8 ≻ C3 ≻ C6 ≻ C7 ≻ C4 ≻ C9,
1, C9 ≻ C11 ≻ C6 ≻ C2 ≻ C10 ≻ C7 ≻ C3 ≻ C8 ≻ C1 ≻ C4 ≻ C5,
1, C6 ≻ C10 ≻ C5 ≻ C2 ≻ C9 ≻ C8 ≻ C1 ≻ C4 ≻ C11 ≻ C7 ≻ C3,
2, C7 ≻ C8 ≻ C11 ≻ C9 ≻ C3 ≻ C2 ≻ C6 ≻ C5 ≻ C1 ≻ C10 ≻ C4")
get_omega(r)
get_alpha(r)
votrix(r)
condorcet_winner(r)
condorcet(r, seePoints = T)
pors11cw$w10[[5]] <- r





