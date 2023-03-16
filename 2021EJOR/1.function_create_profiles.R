# Function to create the profiles of rankings ----------------------------------

create_profiles_nc <- function(n, nvotes, total = 100, 
                               seed = NULL, 
                               max_distinct = NULL,
                               distribution = "norm")  {
  
  profiles <- vector(mode = "list", length = total)
  names(profiles) <- paste0("pr",1:total)
  
  created <- 1
  if(!is.null(seed)) set.seed(seed)
  if(is.null(max_distinct)) max_distinct <- nvotes
  if(max_distinct > nvotes) stop("max_distinct must be < than nvotes")
  
  while(created <= total) {
    
    d <- sample(1:max_distinct, 1)
    r <- random_profile_of_rankings(n, 
                                    nvotes, 
                                    seed = seed, 
                                    distinct = d, 
                                    distribution = distribution)
    
    if(!condorcet(r) && !condorcet_winner(r)) { 
      profiles[[created]] <- r
      created <- created + 1
    }
    
  }
  return(profiles)
}


