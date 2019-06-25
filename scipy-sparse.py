import numpy as np

import scipy.sparse.linalg as ssl

from scipy.sparse import csr_matrix
from ssl import *


A = csr_matrix([[3, 0, 0], [1, -1, 0], [2, 0, 1]], dtype=float)
B = np.array([[2, 0], [-1, 0], [2, 0]], dtype=float)

x = ssl.spsolve_triangular(A, B)

#np.allclose(A.dot(x), B)
