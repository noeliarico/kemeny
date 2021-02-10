###########################################################################
# n = 8 -------------------------------------------------------------------
###########################################################################

n <- 8 # number of alternatives
nvotes <- 10
reps <- 2 # number of profiles of rankings with each characteristic


seeds <- profiles

for (number_of_explored_alternatives in 1:n) {
  
}

create_profiles <- function(n, nvotes, reps)  {

  # Create the list that contains all the profile of rankings
  profiles <- vector(mode = "list", length = (n-1))
  names(profiles) <- paste0("w",1:(n-1))
  # For each value of w, create in each quartile
  qu <- vector(mode = "list", length = 4)
  names(qu) <- paste0("q",1:4)
  # Empty spaces for each repetition
  profiles <- lapply(profiles, function(x) x <- qu)
  pr <- vector(mode = "list", length = reps)
  names(pr) <- paste0("pr",1:reps)
  profiles <- lapply(profiles, function(x) lapply(x, function(y) y <- pr))
  
  seed <- 1
  created <- 0
  while(created <  ((n-1)*4*reps) && seed < 1000) {
    
    print(paste(seed,"#################################################"))
    
    for(d in 2:nvotes) {
      set.seed(seed)
      r <- random_profile_of_rankings(n, nvotes, distinct = d)
      v <- votrix(r)
      w <- (sum(rowSums(v) >= colSums(v))) - 1 # -1 xq me salto el primero 
      
      if(w > 0 &&
         !condorcet(r) && 
         !condorcet_winner(r) && 
         !condorcet_loser(r)) {
        
        print(w)
        
        # Agreement among the voters of the profile of rankings
        ag <- agreement_margin(v)
        # Quartile
        q <- get_quartile(ag)
        # Get the index to insert the profile of rankings in
        i <- get_available_index(profiles[[w]][[q]])
        print(i)
        if(!is.null(i)) {
          print(paste("w =", w, "-- q =", q, "-- i =", i))
          profiles[[w]][[q]][[i]] <- r
          seeds[[w]][[q]][[i]] <- seed
          created <- created + 1
        }
      }
    }
  
    seed <- seed + 1
    
  }
  
  return(profiles)
  
}

get_summary <- function(profiles) {
  lapply(profiles, function(x) sapply(x, function(y) sum(sapply(y, is.por))))
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

