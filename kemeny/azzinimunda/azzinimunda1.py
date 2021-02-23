class AzziniMunda1: 
    
    import numpy as np
    import kemeny.scf.distance as dist
    
    def __init__(self, om):
        self.om = om
        self.n = om.shape[0]
        self.m = om[0,1]+om[1,0]
        # to_explore is a Boolean vector of length n. At the beginning all the 
        # elements must be explored thus it is an array of True values
        self.to_explore = self.np.ones(self.n, dtype=bool)
        # the solution array has length n and all the value set to 0
        self.solution = self.np.zeros(self.n, dtype=self.np.uint8)
        # create a copy of the outranking matrix to restore the values
        self.oom = self.np.ndarray.copy(om)
        # create an array to store all the possible solutions
        self.all_solutions = []
        # create a counter to store the number of tentative solutions
        self.ntentative = 0
        # half of the voters
        self.half = (self.np.arange(self.n)*(self.m//2))[::-1]

    def AM1(self, level):
        # Stop condition: matrix of dimension 2 x 2
        if self.to_explore.sum() == 2:
            # The remaining candidates are those that have not been explored yet
            remaining = self.np.asarray(self.np.where(self.to_explore == True)).flatten()
            # print("matrix 2x2 comparing: {} and {}".format(oom[remaining[0],remaining[1]],oom[remaining[1],remaining[0]]))
            # esto tiene un fallo, qué pasa si om[0,1] == om[1,0] ? da empate?
            if self.oom[remaining[0],remaining[1]] > self.oom[remaining[1],remaining[0]]:
                self.solution[remaining[0]] = level
                self.solution[remaining[1]] = level + 1
                # all_solutions = self.np.append(all_solutions, solution)
                # print("tentative solution: {}".format(solution))
                self.all_solutions.extend(self.solution)
            elif self.oom[remaining[0],remaining[1]] < self.oom[remaining[1],remaining[0]]:
                self.solution[remaining[1]] = level
                self.solution[remaining[0]] = level + 1
                # all_solutions = self.np.append(all_solutions, solution)
                # print("tentative solution: {}".format(solution))  
                self.all_solutions.extend(self.solution)
            else: # tied alternatives, add both
                self.solution[remaining[0]] = level
                self.solution[remaining[1]] = level + 1
                self.all_solutions.extend(self.solution)
                self.solution[remaining[1]] = level
                self.solution[remaining[0]] = level + 1
                self.all_solutions.extend(self.solution)
            return None

        # For the candidates that have not been explored yet:
        # Only the ones which rowsum is >= than their columsum will be kept
        keep = self.np.logical_and(self.to_explore, 
            (self.oom.sum(axis=1) >= self.half[level]))
        
        # Consider the elems that have rowsum >= colsum
        # and aren't part of the current solution yet
        for i in range(self.to_explore.size):
            if keep[i]:
                self.solution[i] = level # add the element to the solution ranking
                # Update the elements to explore so this one is not explored again in
                # the same solution
                self.to_explore[i] = False
                # Remove the candidate in the matrix provisional matrix
                self.oom[:, i] = 0
                self.oom[i,:] = 0
                # print("({}) (to_explore = {})".format(solution, to_explore))
                # all_solutions = self.np.append(all_solutions, azzini(to_explore, current_solution, all_solutions, om, oom, level+1))
                self.AM1(level+1) # recursive call
                # print("back i = {}! The matrix is now:".format(i))
                # In the next iteration this candidate must figure again available to explore
                self.to_explore[i] = True
                # Restore the matrix for the next iteration
                self.oom[:, i] = self.np.where(self.to_explore, self.om[:, i], 0) # om[:, i]
                self.oom[i, :] = self.np.where(self.to_explore, self.om[i, :], 0) # om[:, i]
        return None

    def execute(self):
        self.AM1(0)
        res = self.np.asarray(self.all_solutions, dtype=self.np.uint8)
        # reshape in the form of a matrix
        res = self.np.reshape(res, (res.size//self.n, self.n))
        # number of tentative solutions
        self.ntentative = res.shape[0]
        # Check the distance of each ranking to the profile of rankings
        dists = self.np.ndarray.flatten(self.np.apply_along_axis(self.dist.dRP, 1, res, self.om))
        #print(res)
        #print(dists)
        # Keep only the ones that are the closests to the profile
        dists_min = self.np.where(self.np.array(dists, copy=False) == self.np.amin(dists))[0]
        #print(dists_min)
        return res[dists_min,:]
