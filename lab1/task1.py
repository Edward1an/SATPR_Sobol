import csv
import numpy as np
filename = "input1.csv"



rates = []
weights = []
with open(filename, "r", newline="", encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
       rates.append(list(map(int, row)))

weights = np.array(rates[-1])
rates = np.array(rates[:-1:])

print("rates:", rates, sep='\n')
print("weights:", weights, sep='\n')


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



