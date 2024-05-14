import numpy as np
import pandas as pd
ssg = pd.read_csv('C:\\Users\\Rakon\\Desktop\\Midterm Project\\Samsung.csv')
xmi = pd.read_csv('C:\\Users\\Rakon\\Desktop\\Midterm Project\\Xiaomi.csv')
print(f"Samsung std: {np.std(ssg['Price'])}")
print(f"Xiaomi std: {np.std(xmi['Price'])}")
print(f"Samsung max: {np.max(ssg['Price'])}")
print(f"Xiaomi max: {np.max(xmi['Price'])}")
print(f"Samsung min: {np.min(ssg['Price'])}")
print(f"Xiaomi min: {np.min(xmi['Price'])}")
print(f"Samsung var: {np.var(ssg['Price'])}")
print(f"Xiaomi var: {np.var(xmi['Price'])}")