import numpy as np
import numpy.matlib
matrix1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
matrix2 = np.array([[9,8,7],[6,5,4],[3,2,1]])
divideans = np.matlib.divide(matrix1,matrix2)
print(divideans)