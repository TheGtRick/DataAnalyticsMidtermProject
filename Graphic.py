import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import date
date_of = []
xiaomi_data = []
samsung_data = []
data = pd.read_csv('Xiaomi.csv')
for i in range(len(data["Price"])):
    datearr = data["Date"][i].split("/")
    date_of.append(date.fromisoformat(f'{datearr[2]}-{datearr[0]}-{datearr[1]}'))
    xiaomi_data.append(float(data["Price"][i]))
data = pd.read_csv('Samsung.csv')
for i in range(len(data["Price"])):
    samsung_data.append(float(data["Price"][i]))
xiaomi_data = (xiaomi_data - np.min(xiaomi_data)) / (np.max(xiaomi_data) - np.min(xiaomi_data))
samsung_data = (samsung_data - np.min(samsung_data)) / (np.max(samsung_data) - np.min(samsung_data))
plt.plot(date_of, xiaomi_data)
plt.plot(date_of, samsung_data)
plt.title('Samsung vs Xiaomi')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend(['Xiaomi', 'Samsung'])
plt.show()