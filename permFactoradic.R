# To generate all the possible permutations of n alternatives ------------------
n <- 6
perms <- tibble(perm = 1:factorial(n))
for(i in n:1) {
  sequence <- as.numeric(t(replicate(factorial(i-1), 0:(i-1))))
  print(sequence)
  perms <- bind_cols(perms, i = rep(sequence, nrow(perms)/length(sequence)))
}
