import matplotlib.pyplot as plt
import pandas as pd
from datetime import date
date_of = []
samsung_data = []
data = pd.read_csv('Samsung.csv')
for i in range(len(data["Price"])):
    datearr = data["Date"][i].split("/")
    date_of.append(date.fromisoformat(f'{datearr[2]}-{datearr[0]}-{datearr[1]}'))
    samsung_data.append(float(data["Price"][i]))
plt.plot(date_of, samsung_data)
plt.title('Samsung')
plt.xlabel('Date')
plt.ylabel('Price ($)')
plt.show()