import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
ssg = pd.read_csv('C:\\Users\\Rakon\\Desktop\\Midterm Project\\Table2.csv')
ssg_fb = []
ssg_index = []
ssg_explode = []
i = 0
for fb in ssg['Feedback']:
    if fb != 'Нет отзывов':
        ssg_fb.append(int(fb.replace('(', '').split(' ')[0]))
        ssg_index.append(i)
        ssg_explode.append(0.1)
    i += 1
plt.pie(ssg_fb, labels=ssg.iloc[ssg_index, :]["Name"], explode=ssg_explode)
plt.title('Feedbacks')
plt.show()