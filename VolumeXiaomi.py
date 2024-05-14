import matplotlib.pyplot as plt
import pandas as pd
from datetime import date
date_of = []
samsung_data = []
data = pd.read_csv('Samsung.csv')
for i in range(len(data["Price"])):
    datearr = data["Date"][i].split("/")
    date_of.append(date.fromisoformat(f'{datearr[2]}-{datearr[0]}-{datearr[1]}'))
    samsung_data.append(float(data["Vol"][i].replace('M', '')))
plt.bar(date_of, samsung_data, width=6)
plt.title('Samsung')
plt.xlabel('Date')
plt.ylabel('Volume (M)')
plt.show()