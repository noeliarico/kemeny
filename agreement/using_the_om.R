# Agreement among the voters of the profile -------------------------------

agreement_margin <- function(om, normalize = TRUE) {
  # For complete orders the outranking matrix has constant sum
  nvoters <- om[1,2] + om[2,1]
  # For each pair of elements
  elem <- sum(pmax(nvoters - om[upper.tri(om, diag = FALSE)], om[upper.tri(om, diag = FALSE)]))
  if(normalize) {
    # Number of alternatives in the outranking matrix
    n <- ncol(om)
    # Value if all the candidates are defeated by the max possible value
    max <- nvoters*((n*(n-1))/2)
    # Value if all the candidates are tied
    min <- (nvoters/2)*((n*(n-1))/2)
    return((elem-min)/(max-min))
  }
  else {
    return(elem)
  }
  
}

get_quartile <- function(ag) {
  if(ag < 0.25) {
    return(1)
  }
  else if(ag < 0.5) {
    return(2)
  }
  else if(ag < 0.75) {
    return(3)
  }
  else {
    return(4)
  }
}


# Alpha -------------------------------------------------------------------

get_alpha <- function(r) {
  v <- votrix(r)
  return(rowSums(v) >= colSums(v))
}

get_beta <- function(y) {
  v <- votrix(y)
  h <- (v[1,2]+v[2,1])/2
  sort(rowSums(v > h))
}


# Omega -------------------------------------------------------------------

get_omega <- function(por) {
  v <- votrix(por)
  w <- sum(rowSums(v) >= colSums(v))
  return(w)
}
