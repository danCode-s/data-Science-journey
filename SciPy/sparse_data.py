import numpy as np
from scipy.sparse import csr_matrix



# Sparse Data: is a data set where most of the item values are zero.
# Dense Array: is the opposite of a sparse array: most of the values are not zero.

# There are primarily two types of sparse matrices that we use:
# CSC - Compressed Sparse Column. For efficient arithmetic, fast column slicing.
# CSR - Compressed Sparse Row. For fast row slicing, faster matrix vector products


arr_1 = np.array([0, 0, 0, 0, 0, 1, 1, 0, 2])

print(csr_matrix(arr_1))

arr_2 = np.array([[0, 0, 0], [1, 0, 2], [0, 2, 0]])
print(csr_matrix(arr_2).data)
print(csr_matrix(arr_2).count_nonzero())

mat = csr_matrix(arr_2)
mat.eliminate_zeros()

print(mat)

# Convert from csr into csc
print('\n\n')
print(csr_matrix(arr_2))
print('\n\n')
newarr = csr_matrix(arr_2).tocsc()
print(newarr)
