n <- 5
m <- 50

i <- 0
eval <- 0
while(i < 10000) {
  i <- i + 1
  set.seed(i)
  r <- random_profile_of_rankings(ncandidates = n, nvoters = m)
  b <- as.numeric(borda(r))
  v <- votrix(r)
  if(length(unique(b)) == ncol(v)) {
    eval <- eval+1
    if (kemeny_distance(v, b) > (tr(n)*m)/2)
      stop(i)
  }
}
print(eval)

tr <- function(n) {
  return(n*(n-1)/2)
}

kemeny_distance <- function(om, ranking) {
  r <- match(1:ncol(om), ranking)
  om <- om[r,r]
  return(sum(om[lower.tri(om)]))
}

######

n <- 6
m <- 10

i <- 0
while(i < 20) {
  i <- i + 1
  set.seed(i)
  r <- random_profile_of_rankings(ncandidates = n, nvoters = m, distinct = 4)
  v <- votrix(r)
  if(!condorcet_winner(r)) {
    cat(to_python_om(v))
  }
}

to_python_om()
