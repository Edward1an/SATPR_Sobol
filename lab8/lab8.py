import numpy as np

costs = [[24, 50, 5, 27, 16],
         [50, 47, 23, 17, 21],
         [35, 59, 55, 27, 41]]
supply = [200, 350, 300]
demand = [270, 130, 190, 150, 110]

allocation = np.zeros((len(supply), len(demand)))

i, j = 0, 0

while i < len(supply) and j < len(demand):
    quantity = min(supply[i], demand[j])

    allocation[i, j] = quantity

    supply[i] -= quantity
    demand[j] -= quantity

    if supply[i] == 0:
        i += 1
    if demand[j] == 0:
        j += 1

print("Allocation Matrix:")
print(allocation)

from scipy.optimize import linear_sum_assignment
import numpy as np

supply = [310, 260, 280, 360, 220]
demand = [170, 200, 180, 210, 240, 180, 250]

cost_matrix = [
    [10, 15, 20, 5, 8, 22, 18],
    [12, 14, 10, 7, 13, 15, 11],
    [16, 11, 8, 9, 17, 20, 14],
    [19, 8, 14, 16, 10, 18, 12],
    [22, 10, 13, 12, 11, 17, 9]
]

cost_matrix_np = np.array(cost_matrix)
row_ind, col_ind = linear_sum_assignment(cost_matrix_np)

print("Оптимальний план перевезення:")
for i, j in zip(row_ind, col_ind):
    print(f"Завод {i + 1} -> Склад {j + 1}")
    
    :)