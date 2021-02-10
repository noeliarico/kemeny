class DFS1: 
    
    import numpy as np
    import scf.distance as dist
    
    def __init__(self, om, d):
        self.om = om # outranking matrix
        self.n = om.shape[0] # number of alternatives
        
        # to_explore is a Boolean vector of length n. 
        # for each element, the value True indicates that the alternative
        # must be explored because it has not been explored yet
        self.to_explore = self.np.ones(self.n, dtype=bool)
        #self.to_explore = self.np.arange(self.n, dtype=np.dtype('u1'))

        
        # the solution array has length n and all the value set to 0
        self.solution = self.np.empty(0)
        
        # dist is the distance from solution to the profile of rankings
        self.dist = 0 # initially there is no solution so it is 0
        # the best distance found up to the moment, before the beginning of the
        # algorithm it is initialize to d, which is given in the constructor
        self.best_dist = d
        
        # to store all the solutions of the Kemeny method
        self.all_solutions = []
    
    def dfs1_rec(self, level):
      
      # Stop condition: the ranking gives a order for all the candidates
      if np.sum(self.to_explore) == 0: # no more elements to explore
        if self.dist < self.best_dist: # if it is best, overwritte
          print("{} NEW BEST! old distance = {}, best = {}".format(self.solution, self.best_dist, self.dist))
          self.all_solutions = solution # overwritte the previous solutions
          self.best_dist = self.dist # update the best distance
        elif selg.dist == self.best_dist: # if it is equal to the current, append
          self.all_solutions = self.np.append(self.all_solutions, self.solution)
          print("{} BEST AGAIN! old distance = {}, best = {}".format(self.solution, self.best_dist, self.dist))
        return None # go out of the recursive call

      # Recursive call
      for i in range(self.n):
        if self.to_explore[i]:
          # Add the next element to the solution
          self.solution[i] = level
          # Remove the added element from the list of nodes to explore
          self.to_explore[i] = False
    
          # Keep from the column of the element added in om only the rows that not
          # correspond to the elements that have been previously explroed
          keep = np.in1d(np.arange(self.n), self.to_explore)#, invert=True)
          add = np.sum(om[keep,to_explore[i]])
          self.dist += add

          if self.dist < self.best_dist:
            # Recursive call
            dfs1_rec(rec, level+1) 
    
      return None



    def execute(self):
      self.dfs1_rec(self, 0) 
      nrow = self.all_solutions.size // self.n
      return np.reshape(solution, (nrow, self.n))
    

np.random.seed(123)
n = 4
om = init.create_random_om(n, 10)
alg = DFS1(om, float('inf'))
alg.execute()
