import pandas as pd
import numpy as np


def benefit(deposit, ec_prob, int_rate, delta_norm_pr):
    income = deposit*(1+int_rate)*(1+delta_norm_pr)
    return np.sum(income*ec_prob)

data = pd.DataFrame(
  {
    "bonds":{ 
        "economics_probability": [0.20, 0.15, 0.65],
        "interest_rate": [0.08, 0.06, 0.075],
        "delta_nominal_price": [0.10, 0.05, 0.0],
    },
    "fund":{
        "economics_probability": [0.20, 0.15, 0.65],
        "interest_rate": 0.01,
        "delta_nominal_price": [0.2, 0.2, 0.08],
    },
  }  
)

deposit = float(input("Enter deposit for investing: "))

e = np.array(data["bonds"]["economics_probability"])
ir = np.array(data["bonds"]["interest_rate"])
dnp = np.array(data["bonds"]["delta_nominal_price"])

bonds_benefit = benefit(deposit, e, ir, dnp)

e = np.array(data["fund"]["economics_probability"])
ir = np.array(data["fund"]["interest_rate"])
dnp = np.array(data["fund"]["delta_nominal_price"])

fund_benefit = benefit(deposit, e, ir, dnp)
if (fund_benefit > bonds_benefit):
    print("It is better to invest in a fund. Profit over bonds is: ", fund_benefit-bonds_benefit)
else:
    print("It is better to invest in a bonds. Profit over fund is: ", bonds_benefit-fund_benefit)
