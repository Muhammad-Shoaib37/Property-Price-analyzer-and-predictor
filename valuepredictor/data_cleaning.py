
import numpy as np
import pandas as pd

df = pd.read_csv('custom.csv')
# print(df.head())
print(df['County Winner'].dtype)
tcl = df['County Winner'].tolist()
# tl = df['County Winner'].tolist()
# print(tcl.unique())

print(df['County Winner'].unique())

rl = []
for i in tcl:
	if i == 'Trump':
		rl.append('Luxrious Houses')

	else:
		rl.append('Normal Houses')


df.drop(['County Winner'], axis = 1, inplace= True)
print(df.dtypes)

df['County Winner'] = rl



# this will replace "Boston Celtics" with "Omega Warrior" 
df.replace(to_replace ="Trump", 
                 value ="Luxrious Houses")
# this will replace "Boston Celtics" with "Omega Warrior" 
df.replace(to_replace ="Clinton", 
                 value ="Normal Houses")

print(df['County Winner'].head())

df.to_csv('customs.csv')


df = pd.read_csv('customs.csv')
print(df['County Winner'].head())