import numpy as np
import pandas as pd
ssg = pd.read_csv('C:\\Users\\Rakon\\Desktop\\Midterm Project\\Table2.csv')
xmi = pd.read_csv('C:\\Users\\Rakon\\Desktop\\Midterm Project\\Table1.csv')
ssg['Price'] = [int(temp.replace('₸', '')) for temp in ssg['Price']]
xmi['Price'] = [int(temp.replace('₸', '')) for temp in xmi['Price']]
print(f"Samsung: {round(np.average(ssg['Price']))}")
print(f"Xiaomi: {round(np.average(xmi['Price']))}")