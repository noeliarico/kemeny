# este funciona!!!
# 2, a ≻ b ≻ d ≻ c,
# 4, b ≻ d ≻ c ≻ a,
# 4, c ≻ d ≻ a ≻ b
# 
# 1, c ≻ a ≻ b ≻ d,
# 1, a ≻ b ≻ d ≻ c,
# 4, b ≻ d ≻ c ≻ a,
# 4, c ≻ d ≻ a ≻ b

# el definitivo!!!!!!!!!! por fin
por <- parse_profile_of_rankings("
4, b ≻ c ≻ d ≻ a,
4, c ≻ d ≻ a ≻ b,
2, d ≻ a ≻ b ≻ c
")

#por <- random_profile_of_rankings(4,10,distinct=3,cnames = letters[1:4])
condorcet(por)
condorcet_winner(por)
condorcet_loser(por)
por

colSums(v)
k <- kemeny(por)
k
k$winnerDistance

v <- votrix(por)
v
sink("paraelpaper.txt")
cat(kemeny_to_tikz(por))
sink()

kemeny(por)



k
print(k, complete = T)

colSums(v[-1,-1])
colSums(v[-2,-2])
colSums(v[-3,-3])
colSums(v[-4,-4])

rowSums(v[-c(2,1),-c(2,1)])


rowSums(v[-c(3,4),-c(3,4)])
rowSums(v[-c(3,4),-c(3,4)])


# ejemplo de condorcet

por <- parse_profile_of_rankings("
1, C2 ≻ C3 ≻ C1 ≻ C4,
3, C1 ≻ C4 ≻ C2 ≻ C3,
4, C4 ≻ C1 ≻ C2 ≻ C3,
2, C1 ≻ C3 ≻ C2 ≻ C4
")
por <- set_candidates(por, paste0("a_", 1:4))
