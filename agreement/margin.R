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
