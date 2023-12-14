import numpy as np

payoff_matrix = np.array([
    [-3, 2, 9, 6],
    [-2, 5, 4, 6],
    [5, 3, 1, -5],
    [8, -2, 8, 4]
])


lower_prices = np.min(payoff_matrix, axis=1)

upper_prices = np.max(payoff_matrix, axis=0)

lower_price = np.max(lower_prices)
upper_price = np.min(upper_prices)

maxmin_indexes = np.where(lower_prices == lower_price)
minmax_indexes = np.where(upper_prices == upper_price)

print("Lower Price :", lower_price)
print("Upper Price :", upper_price)

if lower_price == upper_price:    
    pure_strategy_equilibria = np.argwhere(payoff_matrix == np.max(lower_prices))
    print("Pure Strategy Equilibria :", pure_strategy_equilibria)
