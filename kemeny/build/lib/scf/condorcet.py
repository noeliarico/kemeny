import numpy as np

def condorcet(om, see_points = False):
  n = om.shape[0]
  m = om[0,1]+om[1,0]
  ombool = (np.where(om > (m//2), 1, 0)).sum(axis=1)
  if see_points: 
    print(ombool)
  thereis = np.all(np.in1d(np.arange(n), ombool))
  return None if not thereis else n-1-ombool
      
def condorcet_winner(om):
  m = om[0,1]+om[1,0]
  n = om.shape[0]
  ombool = np.where(om > (m//2), 1, 0)
  i = np.where(ombool.sum(axis=1) == ((n)-1))[0]
  return None if i.size == 0 else i[0]
