import numpy as np

def create_random_om(n, m):
    # Matrix of 0s of dimension n x n
    om = np.zeros(n*n).reshape(n, n)

    # Number of values over the diagonal
    triangular_number = ((n*(n+1))//2) - n

    # Generate random values in [0, m] for the upper diagonal
    values_upper_diag = np.random.randint(0, m, triangular_number)
    np.random.shuffle(values_upper_diag)

    # The values of the lower diagonal are m minus the symmetric value 
    # in the upper diagonal
    values_lower_diag = m - values_upper_diag

    # Modify the diagonals in the matrix
  
    index_lower_diag = np.triu_indices_from(om, k=1)
    om[index_lower_diag] = values_lower_diag
    om = om.T
    
    # Modify the upper diagonal
    index_upper_diag = np.triu_indices_from(om, k=1)
    om[index_upper_diag] = values_upper_diag

    om = om.astype(np.dtype('u1'))

    return om

def create_random_ranking(n):
  arr = np.arange(n, dtype = np.uint8)
  np.random.shuffle(arr)
  return arr
