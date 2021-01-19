initialize <- function(n, m = 100) {
  total <- 1
  total_condorcet <- 1
  total_condorcet_winner <- 1
  total_condorcet_loser <- 1
  total_other <- 1
  pors_condorcet <- vector(mode = "list", length = 10)
  pors_condorcet_winner <- vector(mode = "list", length = 10)
  pors_condorcet_loser <- vector(mode = "list", length = 10)
  pors_other <- vector(mode = "list", length = 10)
  while(total <= 40) {
    por <- random_profile_of_rankings(n, m)
    if((total_condorcet <= 10) && !is.null(condorcet(por))) {
      pors_condorcet[[total_condorcet]] <- por
      total_condorcet <- total_condorcet + 1
      total <- total + 1
    }
    else if((total_condorcet_winner <= 10) && !is.null(condorcet_winner(por))) {
      pors_condorcet_winner[[total_condorcet_winner]] <- por
      total_condorcet_winner <- total_condorcet_winner + 1
      total <- total + 1
    }
    else if((total_condorcet_loser <= 10) && !is.null(condorcet_loser(por))) {
      pors_condorcet_loser[[total_condorcet_loser]] <- por
      total_condorcet_loser <- total_condorcet_loser + 1
      total <- total + 1
    }
    else if((total_other <= 10)) {
      pors_other[[total_other]] <- por
      total_other <- total_other + 1
      total <- total + 1
    }
    
    
  }
  return(list(pors_condorcet, pors_condorcet_loser, pors_condorcet_winner, pors_other))
}

# Create the rankings

create_rankings_condorcet <- function(n, seed = 123) {
  set.seed(seed)
  r <- initialize(n, 10)
  omr <- unlist(lapply(r, function(x) lapply(x, votrix)), recursive = F)
  pom <- sapply(1:length(omr), function(x) to_python_om(omr[[x]], paste0("om", x)))
  sink(paste0("creation/om_to_python", n, ".txt"))
  cat(paste(pom, collapse = "\n"))
  sink()
}
lapply(4:12, create_rankings_condorcet)

