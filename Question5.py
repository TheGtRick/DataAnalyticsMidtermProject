import numpy as np
import pandas as pd
ssg = pd.read_csv('C:\\Users\\Rakon\\Desktop\\Midterm Project\\Samsung.csv')
xmi = pd.read_csv('C:\\Users\\Rakon\\Desktop\\Midterm Project\\Xiaomi.csv')
print(f"Samsung: {ssg['Price'][0] * 100 / ssg['Price'][len(ssg['Price']) - 1] - 100}")
print(f"Xiaomi: {xmi['Price'][0] * 100 / xmi['Price'][len(xmi['Price']) - 1] - 100}")