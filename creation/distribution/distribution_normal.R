voters <- seq(10, 100, 15)
# Normal distribution
set.seed(123)
rpors10norm <- get_profiles_distribution(voters[1],5000,omit=F)
rpors25norm <- get_profiles_distribution(voters[2],5000,omit=F)
rpors40norm <- get_profiles_distribution(voters[3],5000,omit=F)
rpors55norm <- get_profiles_distribution(voters[4],5000,omit=F)
rpors70norm <- get_profiles_distribution(voters[5],5000,omit=F)
rpors85norm <- get_profiles_distribution(voters[6],5000,omit=F)
rpors100norm <- get_profiles_distribution(voters[7],5000,omit=F)
rpors125norm <- get_profiles_distribution(125,5000,omit=T)
rpors200norm <- get_profiles_distribution(200,5000,omit=T)
rpors225norm <- get_profiles_distribution(225,5000,omit=T)
save(rpors10norm, 
     rpors25norm, 
     rpors40norm, 
     rpors55norm, 
     rpors70norm, 
     rpors85norm, 
     rpors100norm,
     rpors125norm,
     rpors200norm,
     rpors225norm,
     file = "pors_normal_distribution.RData")

