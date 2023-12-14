import numpy as np
from scipy.optimize import linear_sum_assignment

cost_matrix = np.array([
    [5, 6], 
    [2, 3], 
    [4, 7]
])

row_ind, col_ind = linear_sum_assignment(cost_matrix)

for i in range(len(row_ind)):
    print('Worker', row_ind[i]+1 , 'makes a work number', col_ind[i]+1)

suma = np.sum(cost_matrix[row_ind, col_ind])
print('Work will be gone in', suma, 'hours')