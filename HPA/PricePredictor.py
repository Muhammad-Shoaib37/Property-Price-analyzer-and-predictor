
# Property Price Predictor Module
# Using pakistan cities data and Regression Models

# import required packages

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mpl_toolkits

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor

import pickle
class Collector:


# Module object Intiating

	def __init__(self, a):
		print("Object of ", a, " Initilized")
	
	df = pd.DataFrame()
	df1 = pd.DataFrame()
	df2 = pd.DataFrame()
	df3 = pd.DataFrame()
	df4 = pd.DataFrame()
	df5 = pd.DataFrame()
	df6 = pd.DataFrame()
	df7 = pd.DataFrame()
	df8 = pd.DataFrame()
	df9 = pd.DataFrame()

	df0 = pd.DataFrame()
	dis = pd.DataFrame()
	mpd = pd.DataFrame()

	# Processed X data and Class labels Y after preprocessing (processed data)
	pr_Xdata = pd.DataFrame()
	pr_Ydata = pd.Series()

	
	# Training input (X) Data and calss (Y) labels (splitted Data)
	tr_Xdata = pd.DataFrame()
	tr_Ydata = pd.Series()

	# Testing input (X) Data and calss (Y) labels (splitted Data)
	tr_Xdata = pd.DataFrame()
	ts_Ydata = pd.Series()

	# User Sample Testing Data (After Deploying Model)
	us_Xdata = pd.Series() 


	def read_data(self):
		df = pd.read_csv("HPA/static/zameen-updated.csv")

		self.df = df
		# print(df.columns)

	def read_ml_data(self):
		df = pd.read_csv("HPA/static/mlData.csv")
		self.df1 = df
		# print(df.columns)

	def read_maped_data(self):
		df = pd.read_csv("HPA/static/prt_data.csv")
		self.df2 = df
		df = pd.read_csv("HPA/static/prp_data.csv")
		self.df3 = df
		df = pd.read_csv("HPA/static/prn_data.csv")
		self.df4 = df
		df = pd.read_csv("HPA/static/art_data.csv")
		self.df5 = df
		df = pd.read_csv("HPA/static/cat_data.csv")
		self.df6 = df

		df = pd.read_csv("HPA/static/dis_data.csv")
		self.dis = df

		df = pd.read_csv("HPA/static/maped_data.csv")
		self.mpd = df


		# self.df7 = self.df1['Area Size']
	
		# self.df8 = self.df1['bedrooms']
		
		# self.df9 = self.df1['baths']




# remaining data are: beds, baths, ars, lon and lat

	def get_ready(self):
		self.read_data()
		self.read_ml_data()
		self.read_maped_data()
		return True

# district values ............ step: [3]
	def get_dis_data(self):

		il = self.mpd['dis'].tolist()
		il_ = self.mpd['dis_'].values.tolist()
		il = [(i, j) for i, j in zip(il, il_)]
		il = list(set(il))
		return (il, len(il))


# district specific locations step: [2]

	def get_is_data(self):
		df1 = self.mpd.query('dis_ == "1"')
		il = df1['loc'].values.tolist()
		il_ = df1['loc_'].values.tolist()
		il = [(i, j) for i, j in zip(il, il_)]
		il = list(set(il))
		# print(il)
		return (il, len(il))

	def get_rp_data(self):
		df1 = self.mpd.query('dis_ == "4"')
		il = df1['loc'].values.tolist()
		il_ = df1['loc_'].values.tolist()
		il = [(i, j) for i, j in zip(il, il_)]
		il = list(set(il))
		return (il, len(il))

	def get_lh_data(self):
		df1 = self.mpd.query('dis_ == "3"')
		il = df1['loc'].values.tolist()
		il_ = df1['loc_'].values.tolist()
		il = [(i, j) for i, j in zip(il, il_)]
		il = list(set(il))
		return (il, len(il))

	def get_fd_data(self):
		df1 = self.mpd.query('dis_ == "0"')
		il = df1['loc'].values.tolist()
		il_ = df1['loc_'].values.tolist()
		il = [(i, j) for i, j in zip(il, il_)]
		il = list(set(il))
		return (il, len(il))

	def get_kr_data(self):
		df1 = self.mpd.query('dis_ == "2"')
		il = df1['loc'].values.tolist()
		il_ = df1['loc_'].values.tolist()
		il = [(i, j) for i, j in zip(il, il_)]
		il = list(set(il))
		return (il, len(il))

# ....................................
 
	def get_prt_data(self):
		df1 = self.mpd
		il = df1['prt'].values.tolist()
		il_ = df1['prt_'].values.tolist()
		il = [(i, j) for i, j in zip(il, il_)]
		il = list(set(il))
		# print(il)
		return (il, len(il))
		

	def get_prp_data(self):

		il = self.df3['prp'].values.tolist()
		il_ = self.df3['prp_'].values.tolist()
		il = [(i, j) for i, j in zip(il, il_)]
		il = list(set(il))
		return (il, len(il))

	def get_prn_data(self):

		il = self.df4['prn'].values.tolist()
		il_ = self.df4['prn_'].values.tolist()
		il = [(i, j) for i, j in zip(il, il_)]
		il = list(set(il))

		return (il, len(il))

	def get_art_data(self):

		il = self.df5['art'].values.tolist()
		il_ = self.df5['art_'].values.tolist()
		il = [(i, j) for i, j in zip(il, il_)]
		il = list(set(il))
		return (il, len(il))

	def get_cat_data(self):
		df1 = self.mpd
		il = df1['cat'].values.tolist()
		il_ = df1['cat_'].values.tolist()
		il = [(i, j) for i, j in zip(il, il_)]
		il = list(set(il))
		return (il, len(il))



# location spepcific........step: [3]

	def get_lonlat_data(self, cit, loc):

		if cit == 1:
			fidf = self.mpd.query('dis_ == "1"')
		elif cit == 2:
			fidf = self.mpd.query('dis_ == "2"')

		elif cit == 3:
			fidf = self.mpd.query('dis_ == "3"')

		elif cit == 4:
			fidf = self.mpd.query('dis_ == "4"')

		elif cit == 0:
			fidf = self.mpd.query('dis_ == "0"')

		lfdf = fidf.groupby(['loc_', 'lon_lat'])
		ul = []
		rg = lfdf.groups
		for i in list(rg.keys()):
			loc_, pts = i
			# print(loc_, i)

			if loc_ == float(loc):
				ul.append(pts)

		lonlat = ul.pop(0)

		d = lonlat.replace('(', '')
		d = d.replace(')', '')
		d = d.split(',')
		print(d, type(d))
		n = float(d[0])
		t = float(d[1])

		print(t, type(t))

		# print(type(lonlat), lonlat)
		# lon, lat = lonlat.unzip()

		return (n, t)

	def get_bedrooms_data(self):
		
		il = self.df1['bedrooms'].unique().tolist()
		il_ = []
		for i in il:
			il_.append(int(i))

		il = [(i, j) for i, j in zip(il, il_)]
		return (il, len(il))

	def get_baths_data(self):
		
		il = self.df1['baths'].unique().tolist()
		il_ = []
		for i in il:
			il_.append(int(i))

		il = [(i, j) for i, j in zip(il, il_)]

		return (il, len(il))


	def get_area_size_data(self):
		il = self.df1['Area Size'].unique().tolist()

		# il = [(i, j) for i, j in zip(il, il_)]
		return (il, len(il))

# .............................

# dist -> loc -> lonlat
	# def get maped_data(self):




# Start Macchine learning code



	def initiating_models(self):
		Linear_reg_model = LinearRegression()
		GradientBosting_reg_model = GradientBoostingRegressor(n_estimators=400, max_depth=5, min_samples_split=2, learning_rate=0.1, loss='ls')
		return (Linear_reg_model, GradientBosting_reg_model)

	def preparing_data(self):
		data = self.df1
		labels = data['price']

		processed_data = data.drop(['price'], axis=1)
		self.pr_Xdata = processed_data
		self.pr_Ydata = labels


	def splitting_data(self):
		xdata = self.pr_Xdata
		labels = self.pr_Ydata

		x_train, x_test, y_train, y_test = train_test_split(xdata, labels, test_size = 0.3, random_state = 40)
		self.tr_Xdata = x_train
		self.tr_Ydata = y_train
		self.ts_Xdata = x_test
		self.ts_Ydata = y_test

	def applying_models(self):
		x_train = self.tr_Xdata
		y_train = self.tr_Ydata
		Linear_reg_model, GradientBosting_reg_model = self.initiating_models()
		lr_model = Linear_reg_model.fit(x_train, y_train)
		gb_model = GradientBosting_reg_model.fit(x_train, y_train)

		LR_MOdel = "Pickle_LR_Model_R.pkl"  

		with open(LR_MOdel, 'wb') as file:  
		    pickle.dump(lr_model, file)

		GB_Model = "Pickle_GB_Model_R.pkl"  

		with open(GB_Model, 'wb') as file:  
		    pickle.dump(gb_model, file)

		return (lr_model, gb_model)

	def getting_models_accuray(self):
		# collect traing and testing data
		x_train = self.tr_Xdata
		y_train = self.tr_Ydata
		x_test = self.ts_Xdata
		y_test = self.ts_Ydata

		# collect trained models
		lr_model, gbr_model = self.applying_models()
		print(lr_model.score(x_train, y_train)*100)
		print(lr_model.score(x_test, y_test)*100)
		print(gbr_model.score(x_train, y_train)*100)
		print(gbr_model.score(x_test, y_test)*100)


# .............pass user data input

	def getting_user_data(self, ud):
		# Taking one sample from data:
		data = self.pr_Xdata
		udf = pd.DataFrame()

		us = data[19075:19076]
		ans = self.pr_Ydata
		
		print(us)
		print(ans)

		return us


	def get_price_predition(self, ud):
		# lr_model, gbr_model =  self.applying_models()
		Pkl_Filename = "HPA/Pickle_GB_Model_.pkl"

		with open(Pkl_Filename, 'rb') as file:
			GB_Model = pickle.load(file)

		# usX = self.getting_user_data()
		# usY1 = lr_model.predict(usX)
		usX = np.array([ud])
		usY1 = GB_Model.predict(usX)

		print(usY1)
		return usY1

# # ...................................................


# def main():
# 	p = Collector('Price Predictor')
# 	r = p.get_ready()
# 	p.preparing_data()
# 	p.initiating_models()
# 	p.splitting_data()
# 	p.applying_models()
# 	p.getting_models_accuray()

# 	p.getting_user_data()
# 	p.price_predition()


# # ..................................................



# if __name__ == '__main__':
# 	main()