get_condorcet_discrepancy <- function(por) {
  v <- votrix(por)
  half <- sum(por$numberOfVoters)/2
  v <- apply(v, 1:2, function(x) x > half)
  v <- rowSums(v, na.rm = TRUE)
  sd1 <- sd(0:(length(v)-1))
  sd2 <- sd(v)
  return(sd1-sd2)
}
