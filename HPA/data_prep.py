import pandas as pd

# df = pd.read_csv('zameen-features.csv')
# # print(df.dtypes)

# obj_df = df.select_dtypes(include=['object']).copy()
# int_df = df.select_dtypes(include=['int64']).copy()
# flt_df = df.select_dtypes(include=['float64']).copy()

# print(int_df.dtypes)
# print(flt_df.dtypes)
# # print(obj_df.dtypes)



# obj_df["property_type"] = obj_df["property_type"].astype('category')
# obj_df["districts"] = obj_df["districts"].astype('category')

# obj_df["province_name"] = obj_df["province_name"].astype('category')
# obj_df["purpose"] = obj_df["purpose"].astype('category')

# obj_df["Area Type"] = obj_df["Area Type"].astype('category')

# obj_df["Category"] = obj_df["Category"].astype('category')

# obj_df["location"] = obj_df["location"].astype('category')

# print(obj_df.dtypes)

# obj_df["Category"] = obj_df["Category"].cat.codes
# obj_df["Area Type"] = obj_df["Area Type"].cat.codes

# obj_df["purpose"] = obj_df["purpose"].cat.codes
# obj_df["province_name"] = obj_df["province_name"].cat.codes

# obj_df["districts"] = obj_df["districts"].cat.codes
# obj_df["location"] = obj_df["location"].cat.codes

# obj_df["property_type"] = obj_df["property_type"].cat.codes

# # print(obj_df.iloc[:2, :])

# cat_df = obj_df.copy()
# cat_df['longitude'] = flt_df['longitude']
# cat_df['latitude'] = flt_df['latitude']
# cat_df['Area Size'] = flt_df['Area Size']

# cat_df['bedrooms'] = int_df['bedrooms']
# cat_df['baths'] = int_df['baths']
# cat_df['price'] = int_df['price']

# ml_df = cat_df.copy()
# print(ml_df.iloc[:2, :])
# print(ml_df.dtypes)

# # ml_data = ml_df.to_csv('zameen-mlData.csv', index = False	)

# df4 = pd.read_csv('static/zameen-mlData.csv')
# print(df4.dtypes)


# obj_df =  df4.copy()



# obj_df["property_type"] = obj_df["property_type"].astype('float64')
# obj_df["location"] = obj_df["location"].astype('float64')

# obj_df["districts"] = obj_df["districts"].astype('float64')


# obj_df["province_name"] = obj_df["province_name"].astype('float64')
# obj_df["purpose"] = obj_df["purpose"].astype('float64')

# obj_df["Area Type"] = obj_df["Area Type"].astype('float64')

# obj_df["Category"] = obj_df["Category"].astype('float64')


# obj_df["bedrooms"] = obj_df["bedrooms"].astype('float64')

# obj_df["baths"] = obj_df["baths"].astype('float64')

# obj_df["price"] = obj_df["price"].astype('float64')

# ml_data = obj_df.to_csv('mlData.csv', index = False	)

import pickle

mldf = pd.read_csv('static/mlData.csv')

mdf = pd.read_csv('maped_data.csv')

idf = pd.read_csv('static/dis_data.csv')


rwdf = pd.read_csv('static/zameen-updated.csv')

rfdf = pd.read_csv('zameen-features.csv')


print(rwdf['Area Type'][:3])

print(rwdf['Area Category'][:3])

# print(obj_df.dtypes)

Pkl_Filename = "Pickle_GB_Model_.pkl"

# with open(Pkl_Filename, 'rb') as file:  
#     LR_Model = pickle.load(file)

ud = mldf.iloc[4000:4001, 0:12].values

import numpy as np

ls = [1,2,3]
ar = np.array([ls])
print(ar, type(ar))
print(type(ud), ud)
# Ypredict = LR_Model.predict(ud) 
# print(Ypredict)



prt = []; loc = []; dis = [];
prn = []; prp = []; art = [];
cat = []; lon = []; lat = [];

ars = []; bdr = []; bts = [];

prt = rwdf['property_type'].tolist()
loc = rwdf['location'].tolist()
dis = rwdf['districts'].tolist()

prn = rwdf['province_name'].tolist()
prp = rwdf['purpose'].tolist()
art = rwdf['Area Type'].tolist()

cat = rfdf['Category'].tolist()
lon = rwdf['longitude'].tolist()
lat = rwdf['latitude'].tolist()

ars = rwdf['Area Size'].tolist()
bdr = rwdf['bedrooms'].tolist()
bts = rwdf['baths'].tolist()

# ....................................

prt_ = []; loc_ = []; dis_ = [];
prn_ = []; prp_ = []; art_ = [];
cat_ = []; lon_ = []; lat_ = [];

ars_ = []; bdr_ = []; bts_ = [];


prt_ = mldf['property_type'].tolist()
loc_ = mldf['location'].tolist()
dis_ = mldf['districts'].tolist()

prn_ = mldf['province_name'].tolist()
prp_ = mldf['purpose'].tolist()
art_ = mldf['Area Type'].tolist()

cat_ = mldf['Category'].tolist()
lon_ = mldf['longitude'].tolist()
lat_ = mldf['latitude'].tolist()

ars_ = mldf['Area Size'].tolist()
bdr_ = mldf['bedrooms'].tolist()
bts_ = mldf['baths'].tolist()

prt_check1 = []
prt_check2 = []
loc_check1 = []
loc_check2 = []
dis_check1 = []
dis_check2 = []
prn_check1 = []
prn_check2 = []
prp_check1 = []
prp_check2 = []
art_check1 = []
art_check2 = []
cat_check1 = []
cat_check2 = []

# , loc, loc_, dis, dis_,
# 				   prn, prn_, prp, prp_, art, art_,
# 				   cat, cat_

f = 0

for c , c_, in zip(cat, cat_):


	if f==0:
		# prt_check1.append(c)
		# prt_check2.append(c_)

		# loc_check1.append(c)
		# loc_check2.append(c_)

		# dis_check1.append(c)
		# dis_check2.append(c_)

		# prn_check1.append(c)
		# prn_check2.append(c_)

		# prp_check1.append(c)
		# prp_check2.append(c_)

		# art_check1.append(c)
		# art_check2.append(c_)

		cat_check1.append(c)
		cat_check2.append(c_)

	if (c in cat_check1 and c_ in cat_check2):
		pass
	else:
		# prt_check1.append(c)
		# prt_check2.append(c_)

		# loc_check1.append(c)
		# loc_check2.append(c_)

		# dis_check1.append(c)
		# dis_check2.append(c_)

		# prn_check1.append(c)
		# prn_check2.append(c_)

		# prp_check1.append(c)
		# prp_check2.append(c_)

		# art_check1.append(c)
		# art_check2.append(c_)

		cat_check1.append(c)
		cat_check2.append(c_)

	f = 1

# print(prt_check1)
# print(prt_check2)


maped_data = {
	# 'prt': prt_check1,
	# 'prt_': prt_check2,

	# 'loc': loc_check1,
	# 'loc_': loc_check2,

	# 'dis': dis_check1,
	# 'dis_': dis_check2,

	# 'prn': prn_check1,
	# 'prn_': prn_check2,

	# 'prp': prp_check1,
	# 'prp_': prp_check2,

	# 'art': art_check1,
	# 'art_': art_check2,

	'cat': cat_check1,
	'cat_': cat_check2,

}

md = pd.DataFrame.from_dict(maped_data)

# print(nd.head())
# fd = nd.to_csv('maped_data.csv', index = False)
# md = pd.read_csv('maped_data.csv')
# md = md.drop(['cat', 'cat_'], axis = 1)

# md['art'] = art_check1
# md['art_'] = art_check2

# fd = md.to_csv('cat_data.csv', index = False)

# print(md.head())
# print(md.describe())

fidf = mdf.query('dis_ == "1"')

lfdf = fidf.groupby(['loc_', 'lon_lat'])

# print(len(ifdf['loc'].unique().tolist()))

# print(len(mldf['lon'].unique().tolist()))

# print(len(mldf['lat'].unique().tolist()))


# print(len(lfdf.index.tolist()))
# print(lfdf.index.tolist()[:3])

# v = lfdf.index.tolist()

# print(len(lfdf.values.tolist()))
# print(lfdf.values.tolist()[:3])
rg = lfdf.groups
# print(rg)
# print(len(list(rg.keys())), list(rg.keys())[:7])

ul = []
for i in list(rg.keys()):
	loc, pts = i
	if loc == 497.0:
		ul.append(pts)

n = ul.pop(0)
print(type(n), n)
print(ul)





# property_type      int64
# location           int64
# districts          int64
# province_name      int64
# purpose            int64
# Area Type          int64
# Category           int64
# longitude        float64
# latitude         float64
# Area Size        float64
# bedrooms           int64
# baths              int64

# print(mdf.columns)
# print(idf.describe())
# il = mdf['lon'].tolist()
# il_ = mdf['lat'].tolist()
# prd = [(i, j) for i, j in zip(il, il_)]
# print(prd)

# mdf['lon_lat'] = prd
# ics = mdf.to_csv('maped_data.csv', index = False)
# print(mdf['lon_lat'].tolist())

# my = rwdf['Area Category'].tolist()
# rm = []
# for i in my:
# 	t = str(i)
# 	if "Kanal" in t:
# 		s = t.replace("Kanal", '')
# 		rm.append(s)
# 	elif  "Marla" in t:
# 		s = t.replace("Marla", '')
# 		rm.append(s)
# print(rm)


# mldf = mldf.drop(['Category'], axis = 1)

# mldf["Category_"] = rm

# print(mldf["Category"].unique().tolist())
# mldf["Category"] = mldf["Category"].astype('category')

# print(obj_df.dtypes)

# mldf["Category"] = mldf["Category"].cat.codes

# print(mldf["Category_"].unique().tolist())


# mdf['lon'] = rwdf['longitude']
# mdf['lat'] = rwdf['latitude']
# ics = mdf.to_csv('maped_data.csv', index = False)

print(mdf.columns)