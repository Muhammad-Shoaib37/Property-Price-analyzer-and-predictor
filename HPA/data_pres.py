
import pandas as pd

df = pd.read_csv('static/zameen-updated.csv')

df1 = df.drop(['date_added', 'area', 'agency', 'agent', 'property_id', 'page_url', 'location_id'], axis = 1)

# property_type     price     location 
# longitude  baths   purpose  bedrooms Area Type

print(df1.iloc[:3, 12:])

df2 = df1.copy()
print(df2.dtypes)

ac = df2['Area Category'].tolist()

rc = []
for i in ac:
	t = str(i)
	if "Kanal" in t:
		s = t.replace('Kanal', '')
		rc.append(s)
	elif "Marla" in t:
		s = t.replace('Marla', '')
		rc.append(s)

print(rc[:3])

df3 = df2.drop(['Area Category'], axis = 1)
df3['Category'] = rc
print(df3.iloc[:2, 5:])
print(df3.dtypes)

cs = df3.to_csv('zameen-features.csv', index = False)



