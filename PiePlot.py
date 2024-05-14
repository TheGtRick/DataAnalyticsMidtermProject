import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
ssg = pd.read_csv('C:\\Users\\Rakon\\Desktop\\Midterm Project\\Table2.csv')
xmi = pd.read_csv('C:\\Users\\Rakon\\Desktop\\Midterm Project\\Table1.csv')
ssg_fb = []
xmi_fb = []
for fb in ssg['Feedback']:
    if fb != 'Нет отзывов':
        ssg_fb.append(int(fb.replace('(', '').split(' ')[0]))
for fb in xmi['Feedback']:
    if fb != 'Нет отзывов':
        xmi_fb.append(int(fb.replace('(', '').split(' ')[0]))
plt.pie([np.sum(ssg_fb), np.sum(xmi_fb)], labels=['Samsung', 'Xiaomi'], colors = ['yellow', 'red'], explode = [0, 0.2], shadow = True)
plt.title('Feedbacks')
plt.show()