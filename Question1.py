import numpy as np
import pandas as pd
ssg = pd.read_csv('C:\\Users\\Rakon\\Desktop\\Midterm Project\\Samsung.csv')
xmi = pd.read_csv('C:\\Users\\Rakon\\Desktop\\Midterm Project\\Xiaomi.csv')
print(f"Samsung: {np.average(ssg['Price'])}")
print(f"Xiaomi: {np.average(xmi['Price'])}")