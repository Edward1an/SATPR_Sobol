import csv
import numpy as np
filename = "input2.csv"

def normalize_max(arr):
    _max = arr.max()
    _min = arr.min()
    _dif = _max - _min
    for index, val in enumerate(arr):
        arr[index] = (val - _min) / _dif

def normalize_min(arr):
    _max = arr.max()
    _min = arr.min()
    _dif = _max - _min
    for index, val in enumerate(arr):
        arr[index] = (_max - val) / _dif





rates = []
weights = []
maximize = []

with open(filename, "r", newline="", encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
       rates.append(list(map(float, row)))

maximize = np.array(rates[-1])
weights = np.array(rates[-2])
rates = np.array(rates[:-2:])

print("rates:", rates, sep='\n')
print("weights:", weights, sep='\n')
print("maximize", maximize, sep='\n')

rates = rates.transpose()
print("transpose:", rates, sep='\n')
for index, val in enumerate(rates):
    if (maximize[index]==1):
        normalize_max(val)
    else:
        normalize_min(val)
rates = rates.transpose()


rates = rates * weights
print("rates:", rates, sep='\n')


total = np.zeros(len(rates))
for index, val in enumerate(rates):
    total[index] = val.sum()
print("total:", total, sep='\n')

biggest_rate = total.max()
biggest_position = 1+np.where(total == biggest_rate)[0]
print(biggest_rate)

print("Best alternative is {0} with total rates: {1}".format(biggest_position, biggest_rate))



