por <- parse_profile_of_rankings("
4, c > a > b > d > e,
2, b > c > a > e > d,
2, a > b > c > e > d,
1, d > e > a > b > c,
1, e > d > b > a > c
")
por <- set_candidates(por, paste0("a",1:5))
votrix(por)
condorcet(por, seePoints = T)
kemeny(por)
get_alpha(por)
