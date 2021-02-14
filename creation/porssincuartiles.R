###########################################################################
# n = 8 -------------------------------------------------------------------
###########################################################################

n <- 8 # number of alternatives
nvotes <- 10
reps <- 2 # number of profiles of rankings with each characteristic

create_profiles <- function(n, nvotes, reps, max_iter = Inf)  {
  
  # Create the list that contains all the profile of rankings
  # It is n-1 because for the case when the n alternatives have rowsum>=colsum
  # the uncertainty is max
  profiles <- vector(mode = "list", length = (n-1))
  names(profiles) <- paste0("w",1:(n-1))
  # Profiles of rankings
  pr <- vector(mode = "list", length = reps)
  names(pr) <- paste0("pr",1:reps)
  # Empty spaces for each repetition
  profiles <- lapply(profiles, function(x) x <- pr)
  
  seed <- 1
  created <- 0
  #while(created < ((n-1)*reps) && seed < 500) {
  
  #if(is.null(max_iter)) cond <- created < ((n-1)*reps)
  #else cond <- (created < ((n-1)*reps) && seed < max_iter)
  
  while(created < ((n-1)*reps) && seed < max_iter) {
    
    print(paste(seed,"#################################################"))
    
    for(d in 2:nvotes) {
      
      r <- random_profile_of_rankings(n, nvotes, seed = seed, distinct = d)
      v <- votrix(r)
      w <- sum(rowSums(v) >= colSums(v))
      
      if(w != n && !condorcet(r)) { 
        
        # Agreement among the voters of the profile of rankings
        ag <- agreement_margin(v)
        # Get the index to insert the profile of rankings in
        i <- get_available_index(profiles[[w]])
        
        if(!is.null(i)) {
          print(paste("w =", w, "-- i =", i))
          profiles[[w]][[i]] <- r
          created <- created + 1
        }
      }
    }
    
    seed <- seed + 1
    
  }
  
  return(profiles)
  
}

get_summary <- function(profiles) {
  sapply(profiles, function(x) sum(sapply(x, is.por)))
}


get_available_index <- function(the_list) {
  
  for(i in 1:length(the_list)) {
    if(is.null(the_list[[i]])) {
      return(i)
    }
  }
  return(NULL)
}

condorcet_winner(r)
i6(votrix(r))

