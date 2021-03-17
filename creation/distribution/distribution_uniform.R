voters <- seq(10, 100, 15)
# Uniform distribution
set.seed(123)
rpors10unif <- get_profiles_distribution(voters[1],5000,omit=F,distribution = "unif")
rpors25unif <- get_profiles_distribution(voters[2],5000,omit=F,distribution = "unif")
rpors40unif <- get_profiles_distribution(voters[3],5000,omit=F,distribution = "unif")
rpors55unif <- get_profiles_distribution(voters[4],5000,omit=F,distribution = "unif")
rpors70unif <- get_profiles_distribution(voters[5],5000,omit=F,distribution = "unif")
rpors85unif <- get_profiles_distribution(voters[6],5000,omit=F,distribution = "unif")
rpors100unif <- get_profiles_distribution(voters[7],5000,omit=F,distribution = "unif")
rpors125unif <- get_profiles_distribution(125,5000,omit=T,distribution = "unif")
rpors200unif <- get_profiles_distribution(200,5000,omit=T,distribution = "unif")
rpors225unif <- get_profiles_distribution(225,5000,omit=T,distribution = "unif")
save(rpors10unif, 
     rpors25unif, 
     rpors40unif, 
     rpors55unif, 
     rpors70unif, 
     rpors85unif, 
     rpors100unif,
     rpors125unif,
     rpors200unif,
     rpors225unif,
     file = "pors_uniform_distribution.RData")

