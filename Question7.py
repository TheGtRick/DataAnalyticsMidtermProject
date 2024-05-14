import numpy as np
import pandas as pd
ssg = pd.read_csv('C:\\Users\\Rakon\\Desktop\\Midterm Project\\Table2.csv')
xmi = pd.read_csv('C:\\Users\\Rakon\\Desktop\\Midterm Project\\Table1.csv')
ssg['Price'] = [temp.replace('₸', '') for temp in ssg['Price']]
xmi['Price'] = [temp.replace('₸', '') for temp in xmi['Price']]
print(f"Samsung: {ssg['Price'].corr(ssg['Rating'])}")
print(f"Xiaomi: {xmi['Price'].corr(xmi['Rating'])}")