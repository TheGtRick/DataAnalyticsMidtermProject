import matplotlib.pyplot as plt
import pandas as pd
from datetime import date
date_of = []
samsung_price = []
samsung_open = []
samsung_high = []
samsung_low = []
data = pd.read_csv('Samsung.csv')
for i in range(len(data["Price"])):
    datearr = data["Date"][i].split("/")
    date_of.append(date.fromisoformat(f'{datearr[2]}-{datearr[0]}-{datearr[1]}'))
    samsung_price.append(float(data["Price"][i]))
    samsung_open.append(float(data["Open"][i]))
    samsung_high.append(float(data["High"][i]))
    samsung_low.append(float(data["Low"][i]))
plt.plot(date_of, samsung_price, color='blue')
plt.plot(date_of, samsung_open, color='yellow', linestyle='-.')
plt.plot(date_of, samsung_high, color='green', linestyle='--')
plt.plot(date_of, samsung_low, color='red', linestyle='--')
plt.legend(['Close', 'Open', 'High', 'Low'])
plt.title('Samsung')
plt.xlabel('Date')
plt.ylabel('Price ($)')
plt.show()