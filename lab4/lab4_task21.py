import numpy as np

def normalize_max(arr):
    _max = arr.max()
    _min = arr.min()
    _dif = _max - _min
    for index, val in enumerate(arr):
        arr[index] = (val - _min) / _dif


def calculate():
    matrix = np.array([
        [9.0, 4.0, 5.0, 6.0],
        [7.0, 6.0, 5.0, 4.0],
        [3.0, 8.0, 6.0, 5.0],
        [4.0, 9.0, 4.0, 7.0],
        [6.0, 5.0, 7.0, 2.0],
    ])
    
    weights = np.array([7.0, 8.0, 6.0, 3.0])
    
    matrix = matrix.transpose()
    for index, val in enumerate(matrix):
        normalize_max(val)
    matrix = matrix.transpose()
    
    
    
    matrix = matrix * weights
    
    
    
    min_elements = np.min(matrix, axis=1)
    max_elements = np.max(matrix, axis=1)
    pessimism_criteria = min_elements
    optimism_criteria = max_elements
    lambda_val = 0.25
    hurwicz_criteria = lambda_val * min_elements + (1 - lambda_val) * max_elements
    laplace_criteria = np.mean(matrix, axis=1)
    bayes_laplace_criteria = np.array([0.1, 0.2, 0.3, 0.4])
    bayes_laplace_criteria_result = matrix @ bayes_laplace_criteria
    hodges_lehmann_criteria = lambda_val * bayes_laplace_criteria_result + (1 - lambda_val) * min_elements

    optimal_pessimism_strategy = np.argmax(pessimism_criteria)
    optimal_optimism_strategy = np.argmax(optimism_criteria)
    optimal_hurwicz_strategy = np.argmax(hurwicz_criteria)
    optimal_laplace_strategy = np.argmax(laplace_criteria)
    optimal_bayes_laplace_strategy = np.argmax(bayes_laplace_criteria_result)
    optimal_hodges_lehmann_strategy = np.argmax(hodges_lehmann_criteria)

    print(f"Критерій песимізму:\nОбираємо альтернативу A{optimal_pessimism_strategy + 1}, яка має найбільший прибуток при найгіршому сценарії :{np.max(pessimism_criteria)}")
    print(f"Критерій оптимізму:\n Обираємо альтернативу A{optimal_optimism_strategy + 1} з максимальним прибутком: {np.max(optimism_criteria)}")
    print(f"Критерій Гурвіца:\n Обираємо альтернативу A{optimal_hurwicz_strategy + 1} з максимальним значенням корисності: {np.max(hurwicz_criteria)}")
    print(f"Критерій Лапласа:\n Обираємо альтернативу A{optimal_laplace_strategy + 1}, з максимальним значенням корисності: {np.max(laplace_criteria)}")
    print(f"Критерій Байєса-Лапласа:\n Обираємо альтернативу A{optimal_bayes_laplace_strategy + 1}, з максимальним значенням корисності: {np.max(bayes_laplace_criteria_result)}")
    print(f"Критерій Ходжа-Лемана:\n Обираємо альтернативу A{optimal_hodges_lehmann_strategy + 1}, з максимальним значенням корисності: {np.max(hodges_lehmann_criteria)}")


calculate()
