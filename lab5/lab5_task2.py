import numpy as np

matrix = np.array([
    [100, 15 ],
    [0  , 115],
    [50 , 45 ]
])


mean_cost = np.mean(matrix, axis=0)

print("Стратегія 0 - слід обрати маршрут А")
print("Стратегія 1 - слід обрати маршрут В")
print("Джеку слід дотримуватися стратегії", np.argmin(mean_cost))
