#' Create profiles Condorcet
#' 
#' Create profiles of rankings that have a Condorcet ranking
#'
#' @param n number of candidates
#' @param nvotes number of votes
#' @param reps number of profiles with the same characteristics
#' @param max_iter maximum iterations before breaking the loop if the list is not full
#'
#' @return
#' @export
#'
#' @examples
create_profiles_condorcet <- function(n, nvotes, reps, max_iter = Inf)  {
  
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
      
      if(w != n && any(condorcet(r))) { 
        
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

create_profiles_condorcet_winner <- function(n, nvotes, reps, max_iter = Inf)  {
  
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
      
      if(w != n && !condorcet(r) && condorcet_winner(r)) { 
        
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

create_profiles_no_condorcet <- function(n, nvotes, reps, max_iter = Inf)  {
  
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
      
      if(w != n && !condorcet(r) && !condorcet_winner(r)) { 
        
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


#' Get available index
#' 
#' Seeks the next available index in the list
#'
#' @param the_list 
#'
#' @return the first index available. NULL if the list is full
#' @export
#'
#' @examples
get_available_index <- function(the_list) {
  for(i in 1:length(the_list)) {
    if(is.null(the_list[[i]])) {
      return(i)
    }
  }
  return(NULL)
}

#' Summary of the profile of rankings
#' 
#' Checks the number of profiles of rankings that have been created 
#' for each value of omega
#'
#' @param profiles list of the profiles of rankings
#'
#' @return the number of profile for each value of alpha
#' @export
#'
#' @examples
get_summary <- function(profiles) {
  sapply(profiles, function(x) sum(sapply(x, is.por)))
}
