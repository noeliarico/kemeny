library(rlang)

profiles_jifs <- env()
files <- list.files(file.path(folder, "profiles"), full.names = T)
names <- list.files(file.path(folder, "profiles")) %>% str_remove(".RData")
for(i in 1:length(files)) {
  load(files[i], envir = profiles_jifs)
  assign(names[i], profiles_jifs$porsPredictTime, envir = profiles_jifs)
}
rm(porsPredictTime, envir = profiles_jifs)

