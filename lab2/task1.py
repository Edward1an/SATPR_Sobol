import pandas as pd
import numpy as np

def geomean(arr):
    # print(np.log(arr))
    # print(np.mean(np.log(arr)))
    return np.exp(np.mean(np.log(arr), axis=len(arr.shape)-1))

def normalize(arr):
    _sum = np.sum(arr, axis=len(arr.shape)-1)
    return arr/_sum

def criteria_sum(arr):
    return np.sum(arr, axis=0)

# Створення матриці парних порівнянь
comprassation1 = pd.DataFrame(
  {
  "matrix": [
    [1, 3, 5, 2, 3, 4, 6],
    [1/3, 1, 4, 1, 2, 3, 5],
    [1/5, 1/4, 1, 1/3, 1/2, 1, 3],
    [1/2, 1, 3, 1, 2, 3, 4],
    [1/3, 1/2, 2, 1/2, 1, 2, 3],
    [1/4, 1/3, 1, 1/3, 1/2, 1, 2],
    [1/6, 1/5, 1/3, 1/4, 1/3, 1/2, 1]
  ],
}
)

comprassation2 = pd.DataFrame(
   {
    "matrix": [
    [1, 4, 6, 2, 3, 5, 3],
    [1/4, 1, 3, 1, 2, 4, 2],
    [1/6, 1/3, 1, 1/3, 1/2, 1, 1],
    [1/2, 1, 3, 1, 2, 3, 2],
    [1/3, 1/2, 2, 1/2, 1, 2, 1],
    [1/5, 1/4, 1, 1/3, 1/2, 1, 1],
    [1/3, 1/2, 1, 1/2, 1, 2, 1]
  ]

  }
)

# Введення експертних оцінок для альтернатив
criteria1 = pd.DataFrame(
    {
        "price": [
  [1, 2, 3],
    [0.5, 1, 2],
  [0.3333, 0.5, 1]
]
,
        "quality":[
  [1, 3, 4],
        [0.25, 1, 2],
    [0.2, 0.5, 1]
]
,
        "brand": [
  [1, 4, 5],
  [0.2, 1, 3],
  [0.1667, 0.3333, 1],
],
        "functionality": [
  [1, 2, 5],
  [0.5, 1, 3],
  [0.2, 0.3333, 1]
]
,
        "ergonomics": [
  [1, 3, 4],
  [0.3333, 1, 2],
  [0.25, 0.5, 1]
]
,
        "reliability": [
  [1, 2, 3],
  [0.5, 1, 2],
  [0.3333, 0.5, 1]
]
,
        "safety": [
  [1, 4, 5],
  [0.2, 1, 3],
  [0.1667, 0.3333, 1]
]
      }
)

criteria2 = pd.DataFrame(
    {
      "price": [
  [1, 4, 5],
  [0.2, 1, 3],
  [0.1667, 0.3333, 1]
]
,
      "quality": [
  [1, 2, 3],
  [0.5, 1, 2],
  [0.3333, 0.5, 1]
]

,
      "brand": [
  [1, 3, 4],
  [0.3333, 1, 2],
  [0.25, 0.5, 1]
]
,
      "functionality": [
  [1, 3, 4],
  [0.25, 1, 2],
  [0.2, 0.5, 1]
]
,
      "ergonomics":[
  [1, 2, 3],
  [0.5, 1, 2],
  [0.3333, 0.5, 1]
]
,
      "reliability": [
  [1, 4, 5],
  [0.2, 1, 3],
  [0.1667, 0.3333, 1]
]
,
      "safety": [
  [1, 2, 5],
  [0.5, 1, 3],
  [0.2, 0.3333, 1]
]
    }
)


C1 = np.array([*comprassation1['matrix']])
C2 = np.array([*comprassation2['matrix']])

K1_1 = np.array([*criteria1['price']])
K1_2 = np.array([*criteria2['price']])

K2_1 = np.array([*criteria1['quality']])
K2_2 = np.array([*criteria2['quality']])

K3_1 = np.array([*criteria1['brand']])
K3_2 = np.array([*criteria2['brand']])

K4_1 = np.array([*criteria1['functionality']])
K4_2 = np.array([*criteria2['functionality']])

K5_1 = np.array([*criteria1['ergonomics']])
K5_2 = np.array([*criteria2['ergonomics']])

K6_1 = np.array([*criteria1['reliability']])
K6_2 = np.array([*criteria2['reliability']])

K7_1 = np.array([*criteria1['safety']])
K7_2 = np.array([*criteria2['safety']])


sum_1 = criteria_sum(C1)
sum_2 = criteria_sum(C2)

W_norm_C1 = normalize(geomean(C1))
W_norm_C2 = normalize(geomean(C2))

W_norm_K1_1 = normalize(geomean(K1_1))
W_norm_K1_2 = normalize(geomean(K1_2))

W_norm_K2_1 = normalize(geomean(K2_1))
W_norm_K2_2 = normalize(geomean(K2_2))

W_norm_K3_1 = normalize(geomean(K3_1))
W_norm_K3_2 = normalize(geomean(K3_2))

W_norm_K4_1 = normalize(geomean(K4_1))
W_norm_K4_2 = normalize(geomean(K4_2))

W_norm_K5_1 = normalize(geomean(K5_1))
W_norm_K5_2 = normalize(geomean(K5_2))

W_norm_K6_1 = normalize(geomean(K6_1))
W_norm_K6_2 = normalize(geomean(K6_2))

W_norm_K7_1 = normalize(geomean(K7_1))
W_norm_K7_2 = normalize(geomean(K7_2))


W_norm_all_1 = np.vstack([W_norm_K1_1, W_norm_K2_1, W_norm_K3_1, W_norm_K4_1, W_norm_K5_1, W_norm_K6_1, W_norm_K7_1])
W_norm_all_2 = np.vstack([W_norm_K1_2, W_norm_K2_2, W_norm_K3_2, W_norm_K4_2, W_norm_K5_2, W_norm_K6_2, W_norm_K7_2])

A1 = np.array([np.max([W_norm_all_1[i, 0], W_norm_all_2[i, 0]]) for i in range(7)])
A2 = np.array([np.max([W_norm_all_1[i, 1], W_norm_all_2[i, 1]]) for i in range(7)])
A3 = np.array([np.max([W_norm_all_1[i, 2], W_norm_all_2[i, 2]]) for i in range(7)])

MO = geomean(np.vstack([W_norm_C1, W_norm_C2]).T)

global_criteria = [np.sum(MO*A1),np.sum(MO*A2),np.sum(MO*A3)]

print("MO")
print(MO)

print("A1")
print(A1)

print("A2")
print(A2)

print("A3")
print(A3)

print("Global")
print(global_criteria)

print("Choose alternative with biggest global_criteria: ")
print("A", global_criteria.index(max(global_criteria))+1, " = ", max(global_criteria), sep="")

