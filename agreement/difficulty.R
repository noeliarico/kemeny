npairs <- function(n) (n*(n-1))/2

d_abstract <- function(profileOfRankings = NULL, om = NULL) {
  if(is.null(profileOfRankings) && is.null(om)) {
    stop("Preferences are needed to compute the uncertainty.")
  }
  if(!is.null(profileOfRankings) && !is.null(om)) {
    warning("om will be ignored as a complete profile of rankings has been given.")
  }
  if(!is.null(profileOfRankings)) {
    om <- votrix(profileOfRankings)
    half <- sum(profileOfRankings$numberOfVoters)/2
  } else {
    half <- om[1,2]+om[2,1]
  }
  
  return(list(om = om, h = half))
}

tr <- function(n) {(n*(n-1))/2}

# Average kemeny distance between rankings in the profile  ----------------------

# lo que se supone que hace en el paper de average pairwise distance
# su magnitud no se ve afectada por el num de candidatos porque ya divide
# entre el num de candidatos al hacer la media
# su magnitud se ve afectada por el número de votantes porque la suma total
# cambia en función de cual sea el máximo que se puede obtener
d1 <- function(profileOfRankings = NULL, om = NULL, absolute = TRUE) {
  
  d <- d_abstract(profileOfRankings, om)
  om <- d$om
  half <- d$h
  
  v <- om * t(om) # o_{ij} * o_{ji}
  v <- v[upper.tri(v)] # symmetric matrix, keep only one pair
  
  m <- om[1,2] + om[2,1]
  
  # sum of the absolute majorities
  if(absolute) {
    return(sum(v)/tr(m))
  } else {
    return((sum(v)/tr(m))/tr(n))
  }
}

# Maximum range of positions of the alternatives -------------------------------

d2 <- function(profileOfRankings = NULL, absolute = TRUE) {
  if(! ("por" %in% class(profileOfRankings))) {
    stop("Rankings must be given")
  }
  
  s <- scorix(profileOfRankings)
  n <- ncol(s)
  s <- s != 0
  s <- t(1:ncol(s) * t(s)) 
  s <- ifelse(s==0, NA, s)
  
  minpos <- apply(s, 1, min, na.rm = TRUE)
  maxpos <- apply(s, 1, max, na.rm = TRUE)
  
  # sum of the absolute majorities
  if(absolute) return(max(maxpos-minpos))
  else return(max(maxpos-minpos)/(n-1))
}

# Minimum range of positions of the alternatives -------------------------------

d3 <- function(profileOfRankings = NULL, absolute = TRUE) {
  if(! ("por" %in% class(profileOfRankings))) {
    stop("Rankings must be given")
  }
  
  s <- scorix(profileOfRankings)
  n <- ncol(s)
  s <- s != 0
  s <- t(1:ncol(s) * t(s)) 
  s <- ifelse(s==0, NA, s)
  
  minpos <- apply(s, 1, min, na.rm = TRUE)
  maxpos <- apply(s, 1, max, na.rm = TRUE)
  
  # sum of the absolute majorities
  if(absolute) return(min(maxpos-minpos))
  else return(min(maxpos-minpos)/(n-1))
}

# Average range of positions of the alternatives -------------------------------

d4 <- function(profileOfRankings = NULL, absolute = TRUE) {
  if(! ("por" %in% class(profileOfRankings))) {
    stop("Rankings must be given")
  }
  
  s <- scorix(profileOfRankings)
  n <- ncol(s)
  s <- s != 0
  s <- t(1:ncol(s) * t(s)) 
  s <- ifelse(s==0, NA, s)
  
  # min position of each alternative
  minpos <- apply(s, 1, min, na.rm = TRUE)
  # max position of each alternative
  maxpos <- apply(s, 1, max, na.rm = TRUE)
  
  # average of the range of each alternative
  if(absolute) return(mean(maxpos-minpos))
  else return(mean(maxpos-minpos)/(n-1))
}

# Lower bound to the optimal cost ---------------------------------------------

d5 <- function(profileOfRankings = NULL, om = NULL, absolute = TRUE) {
  d <- d_abstract(profileOfRankings, om)
  om <- d$om
  half <- d$h
  m <- om[1,2]+om[2,1]
  n <- ncol(m)
  
  v1 <- om[upper.tri(om)]
  v2 <- t(om)
  v2 <- v2[upper.tri(v2)]
  mins <- pmin(v1, v2)
  
  # sum of the absolute majorities
  if(absolute) {
    return(sum(mins))
  } else {
    return(sum(mins)/((tr(n)*trunc(m/2))))
  }
}

# Upper bound to the optimal cost ----------------------------------------------

d6 <- function(profileOfRankings = NULL, om = NULL, absolute = TRUE) {
  d <- d_abstract(profileOfRankings, om)
  om <- d$om
  half <- d$h
  m <- om[1,2]+om[2,1]
  n <- ncol(om)
  
  v1 <- om[upper.tri(om)]
  v2 <- t(om)
  v2 <- v2[upper.tri(v2)]
  maxs <- pmax(v1, v2)
  s <- sum(maxs)
  
  # sum of the absolute majorities
  if(absolute) {
    return(s)
  } else {
    min_interval <- tr(n)*ceiling(m/2)
    return((s-min_interval)/((m*tr(n))-min_interval))
  }
}

# Range of possible distance to the profile defined by the bounds --------------

d7 <- function(profileOfRankings = NULL, om = NULL, absolute = TRUE) {
  d <- d_abstract(profileOfRankings, om)
  om <- d$om
  half <- d$h
  m <- om[1,2]+om[2,1]
  
  v1 <- om[upper.tri(om)]
  v2 <- t(om)
  v2 <- v2[upper.tri(v2)]
  maxs <- pmax(v1, v2)
  mins <- pmin(v1, v2)
  
  # sum of the absolute majorities
  if(absolute) {
    return(sum(maxs)-sum(mins))
  } else {
    return((sum(maxs)-sum(mins))/(m*tr(n)))
  }
}

# Average margin of votes between each pair ------------------------------------

d8 <- function(profileOfRankings = NULL, om = NULL, absolute = TRUE) {
  d <- d_abstract(profileOfRankings, om)
  om <- d$om
  half <- d$h
  m <- om[1,2]+om[2,1]
  
  v1 <- om[upper.tri(om)]
  v2 <- t(om)
  v2 <- v2[upper.tri(v2)]
  margins <- abs(v2-v1)
  
  # sum of the absolute majorities
  if(absolute) {
    return(mean(margins))
  } else {
    return(mean(margins)/m)
  }
}


# Most common margin of votes of the pairs -------------------------------------

d9 <- function(profileOfRankings = NULL, om = NULL, absolute = TRUE) {
  d <- d_abstract(profileOfRankings, om)
  om <- d$om
  half <- d$h
  
  # get marings
  v1 <- om[upper.tri(om)]
  v2 <- t(om)
  v2 <- v2[upper.tri(v2)]
  v <- abs(v1-v2)
  # get unique values
  uniqv <- unique(v)
  # count number of occurences of each value
  mode <- uniqv[which.max(tabulate(match(v, uniqv)))]
  
  # sum of the absolute majorities
  if(absolute) {
    return(mode)
  } else {
    return(mode)
  }
}

# Number of unique pairs in the matrix -----------------------------------------

d10 <- function(profileOfRankings = NULL, om = NULL, absolute = TRUE) {
  d <- d_abstract(profileOfRankings, om)
  om <- d$om
  half <- d$h
  
  # get margins
  v1 <- om[upper.tri(om)]
  v2 <- t(om)
  v2 <- v2[upper.tri(v2)]
  v <- abs(v1-v2)
  # count unique margins
  uniqv <- unique(v)
  
  # sum of the absolute majorities
  if(absolute) {
    return(length(uniqv))
  } else {
    return(length(uniqv)/tr(n))
  }
}

# Number of min margin ---------------------------------------------------------

d11 <- function(profileOfRankings = NULL, om = NULL, absolute = TRUE, trace = TRUE) {
  d <- d_abstract(profileOfRankings, om)
  om <- d$om
  m <- om[1,2]+om[2,1]
  half <- d$h
  n <- ncol(om)
  
  # If the number of voters is even, then
  # the min value is 0. If it is odd then
  # the min value is 1
  min_value <- m%%2
  # check the number of min values
  v1 <- om[upper.tri(om)]
  v2 <- t(om)
  v2 <- v2[upper.tri(v2)]
  v <- abs(v1-v2)
  v <- v == min_value
  v <- sum(v)
  if(absolute) {
    return(v)
  } else {
    return(v/tr(n))
  }
}

# Distance to the profile of rankings from the Borda consensus -----------------

# distance from the ranking to the profile of rankings
kemeny_distance_om <- function(r, om) {
  include <- rep(TRUE, length(r))
  dist <- 0
  for(i in 1:length(r)) {
    include[which(r == i)] <- FALSE
    # print(include)
    # print(i)
    # print(which(r == i))
    dist <- dist + sum(om[include, which(r == i)])
  }
  return(dist)
}

d12 <- function(profileOfRankings = NULL, om = NULL) {
  d <- d_abstract(profileOfRankings, om)
  om <- d$om
  half <- d$h
  
  v <- rowSums(om)
  v <- ranking(v, desc = TRUE)
  v <- ranking_to_linear(v)
  #print(as.numeric(v))
  
  dist <- kemeny_distance_om(v, om)
  
  return(dist)
}


# Omega ------------------------------------------------------------------------

d13 <- function(profileOfRankings = NULL, om = NULL) {
  d <- d_abstract(profileOfRankings, om)
  om <- d$om
  
  w <- sum(rowSums(om) >= colSums(om))
  
  return(w)
}

# Standard deviation of the rowsum ---------------------------------------------

d14 <- function(profileOfRankings = NULL, om = NULL) {
  d <- d_abstract(profileOfRankings, om)
  om <- d$om
  
  # get rowsum for each row
  v <- rowSums(om)
  # mean of the rowsums
  return(sd(v))
}

# Relacionadas con la distribución de condorcet


# sd beta -----------------------------------------------------------------

d15 <- function(profileOfRankings = NULL, om = NULL) {
  d <- d_abstract(profileOfRankings, om)
  om <- d$om
  half <- d$h
  
  # get beta for each alternative
  v <- om > half
  v <- rowSums(v)
  # mean value of beta
  return(sd(v))
}

# mean beta -----------------------------------------------------------------

d16 <- function(profileOfRankings = NULL, om = NULL) {
  d <- d_abstract(profileOfRankings, om)
  om <- d$om
  half <- d$h
  
  # get beta for each alternative
  v <- om > half
  v <- rowSums(v)
  
  # mean value of beta
  return(mean(v))
}

# median
d17 <- function(profileOfRankings = NULL, om = NULL) {
  d <- d_abstract(profileOfRankings, om)
  om <- d$om
  half <- d$h
  
  # get beta for each alternative
  v <- om > half
  v <- rowSums(v)
  
  # mean value of beta
  return(median(v))
}

# mean vs median 
d18 <- function(profileOfRankings = NULL, om = NULL) {
  d <- d_abstract(profileOfRankings, om)
  om <- d$om
  half <- d$h
  v <- om > half
  # difference between the median and the mean of beta
  v <- rowSums(v)
  # mean of the rowsums
  return(mean(v)-median(v))
}

# borda score of beta ranking because it ponderates the positions that are clear
# defined el problema es que creo que no es monótono

d19 <- function(profileOfRankings = NULL, om = NULL) {
  d <- d_abstract(profileOfRankings, om)
  om <- d$om
  half <- d$h
  n <- ncol(om)
  
  v <- om > half
  v <- rowSums(v)
  names(v) <- NULL
  v <- v + 1
  v <- factor(v, levels = 1:n)
  print(v)
  v <- table(v)
  print(v)
  v <- v * 1:n
  print(v)
  # difference between the median and the mean of beta
  #v <- rowSums(om)
  # mean of the rowsums
  #por <- parse_profile_of_rankings(paste0("1,",format(ranking(v, desc = TRUE))))
  #points <- mean(rowSums(votrix(por)))
  return(sum(v))
}

d19_viejo <- function(profileOfRankings = NULL, om = NULL) {
  d <- d_abstract(profileOfRankings, om)
  om <- d$om
  half <- d$h
  
  v <- om > half
  v <- rowSums(v)
  
  # difference between the median and the mean of beta
  #v <- rowSums(om)
  # mean of the rowsums
  #por <- parse_profile_of_rankings(paste0("1,",format(ranking(v, desc = TRUE))))
  #points <- mean(rowSums(votrix(por)))
  return(sum(v))
}

#############

# intransitive cyles
d20 <- function(profileOfRankings = NULL, om = NULL) {
  d <- d_abstract(profileOfRankings, om)
  om <- d$om
  half <- d$h
  #print(half)
  n <- ncol(om)
  #candidates <- colnames(om)
  # print(candidates)
  total <- 0
  for(i in 1:n) { 
    for(j in 1:n) {
      if(i!=j) {
        # now for each of the remaining candidates
        for(k in 1:n) {
          if(i!=k && j!=k) {
            # print(paste("i",i,"j",j,"k",k,om[i,j] > half,om[j,k] > half,om[k,i] > half))
            if(om[i,j] > half &&
               om[j,k] > half &&
               om[k,i] > half) {
              # print(paste(candidates[i], ">", candidates[j], ",",
              #             candidates[j], ">", candidates[k], ",",
              #             candidates[k], ">", candidates[i]
              #              ))
              total <- total + 1
            }
          }
        }
      }
    }
  }
  return(total/3)
}



# ejemplo de perfil con ciclos
por <- parse_profile_of_rankings("
4, a > b > c,
3, c > b > a,
1, c > a > b,
1, b > c > a
")
