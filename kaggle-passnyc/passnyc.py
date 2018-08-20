import numpy as np 
import pandas as pd 

from matplotlib import cm
import matplotlib.pyplot as plt

import seaborn as sns

import warnings
warnings.filterwarnings("ignore", category=UserWarning)

df = pd.read_csv('C:\\Users\\yil1\\Documents\\GitHub\\kaggle\\data\\2016 School Explorer.csv')

example = df.tail(2).T[3:41]

print("original shape is {}".format(df.shape))

na_list = ['Adjusted Grade','New?','Other Location Code in LCGMS']
df = df.drop(na_list, axis=1)

print("Now the shape is {}".format(df.shape))

print("Items of school_explorer are {}".format(df.keys()))


def p2f(x):
    return float(x.strip('%'))/100

print("Process some data from percentage to float")
print("Before p2f example - Percent of Students Chronically Absent")
print(df['Percent of Students Chronically Absent'][0:5])

df['Percent of Students Chronically Absent']=df['Percent of Students Chronically Absent'].astype(str).apply(p2f)
df['Rigorous Instruction %'] = df['Rigorous Instruction %'].astype(str).apply(p2f)
df['Collaborative Teachers %'] = df['Collaborative Teachers %'].astype(str).apply(p2f)
df['Supportive Environment %'] = df['Supportive Environment %'].astype(str).apply(p2f)
df['Effective School Leadership %'] = df['Effective School Leadership %'].astype(str).apply(p2f)
df['Strong Family-Community Ties %'] = df['Strong Family-Community Ties %'].astype(str).apply(p2f)
df['Trust %'] = df['Trust %'].astype(str).apply(p2f)
df['Student Attendance Rate'] = df['Student Attendance Rate'].astype(str).apply(p2f)
print("After p2f example - Percent of Students Chronically Absent")
print(df['Percent of Students Chronically Absent'][0:5])


df['School Income Estimate'] = df['School Income Estimate'].str.replace(',', '')
df['School Income Estimate'] = df['School Income Estimate'].str.replace('$', '')
df['School Income Estimate'] = df['School Income Estimate'].str.replace(' ', '')
df['School Income Estimate'] = df['School Income Estimate'].astype(float)
df['School Income Estimate'] = df['School Income Estimate'].fillna(0)
df['Economic Need Index'] = df['Economic Need Index'].fillna(0)

df.plot(kind="scatter", x="Longitude", y="Latitude",
    s=df['School Income Estimate']/1000, c="Economic Need Index", cmap=plt.get_cmap("jet"),
        label='Schools', title='New York School Population Map,Scatter Size is "School Income Estimate"',colorbar=True, alpha=0.4, figsize=(15,7))


df['Percent Asian'] = df['Percent Asian'].apply(p2f)
df['Percent Black'] = df['Percent Black'].apply(p2f)
df['Percent Hispanic'] = df['Percent Hispanic'].apply(p2f)
df['Percent White'] = df['Percent White'].apply(p2f)
df['Percent Black / Hispanic'] = df['Percent Black / Hispanic'].apply(p2f)
df.plot(kind="scatter", x="Longitude", y="Latitude",
    s=df["School Income Estimate"]/1000, c="Percent Black", cmap=plt.get_cmap("jet"),
        label='Schools', title='New York Black Student Ratio Of School,Scatter Size is "School Income Estimate"',colorbar=True, alpha=0.4, figsize=(15,7))
df.plot(kind="scatter", x="Longitude", y="Latitude",
    s=df["School Income Estimate"]/1000, c="Percent Asian", cmap=plt.get_cmap("jet"),
        label='Schools', title='New York Asian Student Ratio Of School,Scatter Size is "School Income Estimate"',colorbar=True, alpha=0.4, figsize=(15,7))
df.plot(kind="scatter", x="Longitude", y="Latitude",
    s=df["School Income Estimate"]/1000, c="Percent Hispanic", cmap=plt.get_cmap("jet"),
        label='Schools', title='New York Hispanic Student Ratio Of School,Scatter Size is "School Income Estimate"',colorbar=True, alpha=0.4, figsize=(15,7))
df.plot(kind="scatter", x="Longitude", y="Latitude",
    s=df["School Income Estimate"]/1000, c="Percent White", cmap=plt.get_cmap("jet"),
        label='Schools', title='New York White Student Ratio Of School,Scatter Size is "School Income Estimate"',colorbar=True, alpha=0.4, figsize=(15,7))
plt.legend()
plt.show()