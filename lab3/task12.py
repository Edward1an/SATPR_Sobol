import pandas as pd
import numpy as np

def decor():
    print("-------------------------------------------------------------------")
def calc(data, term):
    cost = np.array([data["big_factory"]["cost"], data["small_factory"]["cost"]])
    comm = np.array(data["commodity"])
    
    big_income = np.array([data["big_factory"]["income"]])
    big_value = big_income*term-cost[0]
    big_value = np.sum(big_value*comm)
    
    small_income = np.array([data["small_factory"]["income"]])
    small_value = small_income*term-cost[1]
    small_value = np.sum(small_value*comm)

    if big_value >= small_value:
        return big_value, "великий"
    else:
        return small_value, "малий"
    
    
data = pd.DataFrame(
  {
    "not_wait":{
      "commodity": [0.7, 0.3],
      "big_factory":{
          "cost": 600_000,
          "income": [250_000, -50_000],
      },
      "small_factory":{
          "cost": 350_000,
          "income": [150_000, 25_000],
      },
    },
    
    "wait":{
      "forecats_probability": [0.8, 0.2],
      
      
      "positive_forecast":{
        "commodity": [0.9, 0.1],
        "big_factory":{
            "cost": 600_000,
            "income": [250_000, -50_000],
        },
        "small_factory":{
            "cost": 350_000,
            "income": [150_000, 25_000],
        },
        
      },
      
      "negative_forecast":{
        "commodity": [0.7, 0.3],
        "big_factory":{
            "cost": 600_000,
            "income": [250_000, -50_000],
        },
        "small_factory":{
            "cost": 350_000, 
            "income": [150_000, 25_000],
        },
        "no_factory":{
            "cost": 0,
            "income": 0,
        },
      },
    }
  }
)

term = 5.0
term = float(input("Введіть термін для інвестування: "))

not_wait_value, not_wait_fabric = calc(data["not_wait"], term)



positive_value, positive_fabric = calc(data["wait"]["positive_forecast"], term-1)
negative_value, negative_fabric = calc(data["wait"]["negative_forecast"], term-1)

if (negative_value<0):
    negative_value = 0
    negative_fabric = "ніякий"


print("Якщо не чекатимемо, то краще побудувати", not_wait_fabric, "завод. Значення функції за вказаний термін становить: ", not_wait_value)
print()
print("Якщо чекатимемо і будуть позитивні прогнози, то краще побудувати", positive_fabric, "завод. Значення функції за вказаний термін становить: ", positive_value)
print()
print("Якщо чекатимемо і будуть негативні прогнози, то краще побудувати", negative_fabric, "завод. Значення функції за вказаний термін становить: ", negative_value)
print()

if (positive_value < 0 and negative_value == 0):
    wait_value = 0
    wait_fabric = negative_fabric
else:
    prob = np.array(data["wait"]["forecats_probability"])
    wait_value = np.array([positive_value, negative_value])
    wait_value = np.sum(wait_value*prob)
    if positive_fabric == negative_fabric:
        wait_fabric = positive_fabric
    else:
        wait_fabric = "вирішимо на основі прогнозу"
    
if wait_value > not_wait_value:
    final_value = wait_value
    final_fabric = wait_fabric
else:
    final_value = not_wait_value
    final_fabric = not_wait_fabric
print("Отже, якщо чекатимемо, то значення функції буде становити: ", final_value) 
    
 
print("\n\nОСТАТОЧНЕ РІШЕННЯ!")



decor()
if wait_value > not_wait_value:
    print("Ми зачекаємо. Який побудувати завод? - ", final_fabric, ". Значення функції: ", final_value)
else:
    print("Будуємо ", final_fabric, " негайно! Значення функції ", final_value)
decor()



