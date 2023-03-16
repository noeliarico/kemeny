# Create scripts for the profiles already created

names <- list.files(file.path(folder, "profiles")) %>% str_remove(".RData")
r <- 3
for(name in names) {
  info <- str_remove(name, "porsAIHC_") %>% str_split("_", simplify = TRUE)
  n <- as.numeric(info[1,1])
  m <- as.numeric(info[1,2])
  print(paste0("name: ", name, " -- n: ", n, ", m: ", m))
  
  porsPredictTime <- get(name, envir = profiles_aihc)
  # write the python scripts to execute in python
  
  scripts_me(porsPredictTime, n, i, "me",
             file.path(getwd(), folder, "scripts/"),
             file.path(getwd(), folder, "results/"),
             rep=r)
   
}
