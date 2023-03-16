
tr <- function(n) {(n*(n-1))/2}



normalize <- function(data) {
  
  data <- data %>%
    mutate(n = (as.numeric(as.character(n))),
           m = (as.numeric(as.character(m))),
           
           #####################################################################
           # DEFINE THE BOUNDS OF THE INTERVALS FOR EACH MU --------------------
           #####################################################################
           
           # Average Kendall distance ------------------------------------------
           ub_mu1 = tr(n),
           # Related to the range of positions of the alternatives -------------
           ub_mu2 = n-1, # maximum
           ub_mu3 = n-1, # minimum
           ub_mu4 = n-1, # average
           # Bound of the distance ---------------------------------------------
           # (lower bound to the optimal distance)
           lb_mu5 = (m%%2)*tr(n),
           ub_mu5 = tr(n)*m,
           # ((trunc((m+1)/2)*tr(n)))
           # Number of intransitive cycles -------------------------------------
           ub_mu6 = factorial(n)/(factorial(3)*factorial(n-3)),
           # Related to the pairwise comparison of the alternatives ------------
           lb_mu7 = m%%2, # Mode
           ub_mu7 = m, # Mode
           lb_mu8 = 1, # Number of different margins
           ub_mu8 = tr(n), # Number of different margins
           ub_mu9 = tr(n), # frequency of the lowest margin
           
           # Distance from the borda ranking to the profile --------------------
           ub_mu10 = tr(n)*m,
           
           # Related to the rowsum of the outranking matrix --------------------
           lb_mu11 = 1,
           ub_mu11 = n, # n of alternatives with alpha = True
           ub_mu12 = m*tr(n), # standard deviation of the rowsum
           
           # Related to the Condorcet vector -----------------------------------
           ub_mu13 = tr(n),
           ub_mu14 = n-1,
           ub_mu15 = n-1,
           ub_mu16 = n-1,
           
           #####################################################################
           # NORMALIZE ---------------------------------------------------------
           #####################################################################
           
           # Average Kendall distance ------------------------------------------
           mu1 = mu1/ub_mu1, # average kendall distance
           
           # Related to the range of positions of the alternatives -------------
           mu2 = mu2/ub_mu2, # maximum 
           mu3 = mu3/ub_mu2, # minimum 
           mu4 = mu4/ub_mu2, # average 
           
           # Bound of the distance ---------------------------------------------
           # lower bound to the optimal distance
           mu5 = (mu5-lb_mu5)/(ub_mu5-lb_mu5),
           
           # Number of intransitive cycles -------------------------------------
           mu6 = mu6/ub_mu6,
           
           # Related to the pairwise comparison of the alternatives ------------
           mu7 = (mu7-lb_mu7)/(ub_mu7-lb_mu7), # Mode
           mu8 = (mu8-lb_mu8)/(ub_mu8-lb_mu8), # Number of different
           mu9 = mu9/ub_mu9, # frequency of the lowest margin
           
           # Distance from the borda ranking to the profile --------------------
           mu10 = mu10/ub_mu10, 
           
           # Related to the rowsum of the outranking matrix --------------------
           mu11 = (mu11-lb_mu11)/(ub_mu11-lb_mu11), # n of alternatives with alpha = True
           mu12 = mu12/ub_mu12, # standard deviation of the rowsum
           
           # Related to the Condorcet vector -----------------------------------
           mu13 = mu13/ub_mu13, # standard deviation
           mu14 = mu14/ub_mu14, # mean
           mu15 = mu15/ub_mu15, # median
           mu16 = mu16/ub_mu16, # relationship
            
           # Return back this numbers to factors -------------------------------
           n = as.factor(n),
           m = as.factor(m)
    )
  data
}

