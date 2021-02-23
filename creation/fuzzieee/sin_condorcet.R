pors4cr <- create_profiles_condorcet(4,10,5,max_iter = 1000)
pors5cr <- create_profiles_condorcet(5,10,5,max_iter = 1000)
pors6cr <- create_profiles_condorcet(6,10,5,max_iter = 1000)
pors7cr <- create_profiles_condorcet(7,10,5,max_iter = 1000)
pors8cr <- create_profiles_condorcet(8,10,5,max_iter = 1000) 
pors9cr <- create_profiles_condorcet(9,10,5,max_iter = 1000) 
pors10cr <- create_profiles_condorcet(10,10,5,max_iter = 5000)
pors11cr <- create_profiles_condorcet(11,10,5,max_iter = 5000)
pors12cr <- create_profiles_condorcet(12,10,5,max_iter = 5000)
pors13cr <- create_profiles_condorcet(13,10,5,max_iter = 5000)
pors14cr <- create_profiles_condorcet(14,10,5,max_iter = 5000)

save(pors4cr,
     pors5cr,
     pors6cr,
     pors7cr,
     pors8cr,
     pors9cr,
     pors10cr,
     pors11cr,
     pors12cr,
     pors13cr,
     pors14cr,
     file = "creation/fuzzieeeCR.RData")

pors4cw <- create_profiles_condorcet_winner(4,10,5,max_iter = 5000)
pors5cw <- create_profiles_condorcet_winner(5,10,5,max_iter = 5000)
pors6cw <- create_profiles_condorcet_winner(6,10,5,max_iter = 5000)
pors7cw <- create_profiles_condorcet_winner(7,10,5,max_iter = 5000)
pors8cw <- create_profiles_condorcet_winner(8,10,5,max_iter = 5000) 
pors9cw <- create_profiles_condorcet_winner(9,10,5,max_iter = 5000) 
pors10cw <- create_profiles_condorcet_winner(10,10,5,max_iter = 5000)
pors11cw <- create_profiles_condorcet_winner(11,10,5,max_iter = 5000)
pors12cw <- create_profiles_condorcet_winner(12,10,5,max_iter = 5000)
pors13cw <- create_profiles_condorcet_winner(13,10,5,max_iter = 5000)
pors14cw <- create_profiles_condorcet_winner(14,10,5,max_iter = 5000)

save(pors4cw,
     pors5cw,
     pors6cw,
     pors7cw,
     pors8cw,
     pors9cw,
     pors10cw,
     pors11cw,
     pors12cw,
     pors13cw,
     pors14cw,
     file = "creation/fuzzieeeCW.RData")

pors4nc <- create_profiles_no_condorcet(4,10,5,max_iter = 5000)
pors5nc <- create_profiles_no_condorcet(5,10,5,max_iter = 5000)
pors6nc <- create_profiles_no_condorcet(6,10,5,max_iter = 5000)
pors7nc <- create_profiles_no_condorcet(7,10,5,max_iter = 5000)
pors8nc <- create_profiles_no_condorcet(8,10,5,max_iter = 5000) 
pors9nc <- create_profiles_no_condorcet(9,10,5,max_iter = 10000) 
pors10nc <- create_profiles_no_condorcet(10,10,5,max_iter = 10000)
pors11nc <- create_profiles_no_condorcet(11,10,5,max_iter = 10000)
pors12nc <- create_profiles_no_condorcet(12,10,5,max_iter = 10000)
pors13nc <- create_profiles_no_condorcet(13,10,5,max_iter = 10000)
pors14nc <- create_profiles_no_condorcet(14,10,5,max_iter = 10000)

save(pors4nc,
     pors5nc,
     pors6nc,
     pors7nc,
     pors8nc,
     pors9nc,
     pors10nc,
     pors11nc,
     pors12nc,
     pors13nc,
     pors14nc,
     file = "creation/fuzzieeeNC.RData")
