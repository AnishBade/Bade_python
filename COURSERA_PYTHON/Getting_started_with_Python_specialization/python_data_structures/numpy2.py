import numpy as np
from numpy.linalg import norm, inv
from numpy import transpose
from readonly.bearNecessities import *
v=[[1,2,3],[1,0,1],[1,1,-1]]
V=np.array(v)
print(V)
E=np.gsBasis(V)