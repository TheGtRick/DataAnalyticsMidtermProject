import numpy as np
import pandas as pd
ssg = pd.read_csv('C:\\Users\\Rakon\\Desktop\\Midterm Project\\Samsung.csv')
xmi = pd.read_csv('C:\\Users\\Rakon\\Desktop\\Midterm Project\\Xiaomi.csv')
ssg['Change'] = [float(temp.replace('%', '')) for temp in ssg['Change']]
xmi['Change'] = [float(temp.replace('%', '')) for temp in xmi['Change']]
print(f"Samsung:\n {ssg[ssg['Change'] == np.max(ssg['Change'])]}")
print(f"Xiaomi:\n {xmi[xmi['Change'] == np.max(xmi['Change'])]}")