import numpy as np
import pandas as pd
xmi = pd.read_csv('C:\\Users\\Rakon\\Desktop\\Midterm Project\\Xiaomi.csv')
print(f"Xiaomi: {xmi[xmi['Price'] == np.max(xmi['Price'])]['Date']}")
ssg = pd.read_csv('C:\\Users\\Rakon\\Desktop\\Midterm Project\\Samsung.csv')
print(f"Samsung: {ssg[ssg['Price'] == np.max(ssg['Price'])]['Date']}")