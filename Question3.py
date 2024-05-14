import pandas as pd
ssg = pd.read_csv('C:\\Users\\Rakon\\Desktop\\Midterm Project\\Samsung.csv')
xmi = pd.read_csv('C:\\Users\\Rakon\\Desktop\\Midterm Project\\Xiaomi.csv')
ssg_vol = 0
xmi_vol = 0
for v in ssg['Vol']:
    if 'B' in v:
        ssg_vol += (float(v.repalce('B', '')) * 1000000000)
    elif 'M' in v:
        ssg_vol += (float(v.replace('M', '')) * 1000000)
for v in xmi['Vol']:
    if 'B' in v:
        xmi_vol += (float(v.replace('B', '')) * 1000000000)
    elif 'M' in v:
        xmi_vol += (float(v.replace('M', '')) * 1000000)
print(f"Samsung: {ssg_vol}")
print(f"Xiaomi: {xmi_vol}")