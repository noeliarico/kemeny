# Create the profiles of rankings ----------------------------------------------

# CREATE SCRIPTS FOR THE PROFILES ALREADY CREATED

names <- list.files(file.path(folder, "profiles_of_rankings")) %>% str_remove(".RData")
r <- 3
for(name in names) {
  info <- str_remove(name, "porsEJOR") %>% str_split("_", simplify = TRUE)
  n <- as.numeric(info[1,1])
  if(n<11) {
  i <- as.numeric(info[1,2])
  porsPredictTime <- get(name, envir = profiles_ejor)
  # write the python scripts to execute in python
  
  
  # scripts_me(porsPredictTime, n, i, "me",
  #            file.path(getwd(), folder, "scripts/me/"),
  #            file.path(getwd(), folder, "results/me"),
  #            rep=r)
  # 
  # scripts_mercw(porsPredictTime, n, i, "mercw",
  #            file.path(getwd(), folder, "scripts/mercw/"),
  #            file.path(getwd(), folder, "results/mercw"),
  #            rep=r)
  # 
  # scripts_mebb(porsPredictTime, n, i, "mebb",
  #            file.path(getwd(), folder, "scripts/mebb/"),
  #            file.path(getwd(), folder, "results/mebb"),
  #            rep=r)
  # 
  scripts_mebbd(porsPredictTime, n, i, "mebbd",
                file.path(getwd(), folder, "scripts/mebbd/"),
                file.path(getwd(), folder, "results/mebbd"),
                rep=r)
  
  # scripts_mebbrcw(porsPredictTime, n, i, "mebbrcw",
  #              file.path(getwd(), folder, "scripts/mebbrcw/"),
  #              file.path(getwd(), folder, "results/mebbrcw"),
  #              rep=r)
  # 
  scripts_mebbrcwd(porsPredictTime, n, i, "mebbrcwd",
               file.path(getwd(), folder, "scripts/mebbrcwd/"),
               file.path(getwd(), folder, "results/mebbrcwd"),
               rep=r)
 }
   
}
