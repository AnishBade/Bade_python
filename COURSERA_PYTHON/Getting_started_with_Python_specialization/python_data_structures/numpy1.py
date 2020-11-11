import numpy as np

A = [[1, 1, 1],
     [3, 2, 1],
     [2, 1, 2]]
B=np.array(A)
Ainv = np.linalg.inv(A) #to find the inverse
print(Ainv)
A_rank=np.linalg.matrix_rank(A)
print(A_rank)
print(B.T)#Finding Transpose
print(B.shape) #Finding order of matrix