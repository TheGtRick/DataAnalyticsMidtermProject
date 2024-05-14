import numpy as np
import pandas as pd
xmi = pd.read_csv('C:\\Users\\Rakon\\Desktop\\Midterm Project\\Table1.csv')
xmi_r = []
for r in xmi['Rating']:
    if not np.isnan(r):
        xmi_r.append(float(r))
print(f"Xiaomi: {round(np.average(xmi_r), 2)}")
ssg = pd.read_csv('C:\\Users\\Rakon\\Desktop\\Midterm Project\\Table2.csv')
ssg_r = []
for r in ssg['Rating']:
    if not np.isnan(r):
        ssg_r.append(float(r))
print(f"Samsung: {round(np.average(ssg_r), 2)}")