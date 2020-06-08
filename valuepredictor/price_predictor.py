
# land area value (price) predictor using machine learning
# regression and its variants

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mpl_toolkits

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
# from sklearn.externals import joblib

class price_predictor:

# local data containers to hold data frames whcih
# at various  satges ...

	# Initial after loading
	hp_data = pd.DataFrame()
	
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


# Module object Intiating
	def __init__(self, predictor):
		print("Initiating machine learning model:", predictor)


# load data file and pass to local data container
	def loading_data(self):
		hdf = pd.read_csv("static/kc_house_data.csv",encoding = "utf-8")
		self.hp_data = hdf


# ....................................

# complete Eda done in other modules then rendering on Dashboard

# ...............................................



	def initiating_models(self):
		Linear_reg_model = LinearRegression()
		GradientBosting_reg_model = GradientBoostingRegressor(n_estimators=400, max_depth=5, min_samples_split=2, learning_rate=0.1, loss='ls')
		return (Linear_reg_model, GradientBosting_reg_model)

	def preparing_data(self):
		data = self.hp_data
		labels = data['price']
		conv_dates = [1 if values == 2014 else 0 for values in data.date]
		data['date'] = conv_dates
		processed_data = data.drop(['id', 'price'], axis=1)
		self.pr_Xdata = processed_data
		self.pr_Ydata = labels


	def splitting_data(self):
		xdata = self.pr_Xdata
		labels = self.pr_Ydata

		x_train, x_test, y_train, y_test = train_test_split(xdata, labels, test_size = 0.10, random_state = 2)
		self.tr_Xdata = x_train
		self.tr_Ydata = y_train
		self.ts_Xdata = x_test
		self.ts_Ydata = y_test

	def applying_models(self):
		x_train = self.tr_Xdata
		y_train = self.tr_Ydata
		Linear_reg_model, GradientBosting_reg_model = self.initiating_models()
		Linear_reg_model.fit(x_train, y_train)
		GradientBosting_reg_model.fit(x_train, y_train)

		# joblib.dump(Linear_reg_model, 'lr_model')
		# joblib.dump(GradientBosting_reg_model, 'gbr_model')

		return (Linear_reg_model, GradientBosting_reg_model)

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


	def getting_user_data(self):
		# Taking one sample from data:
		data = self.pr_Xdata
		us = data[19075:19076]
		print(type(us))
		print(us)
		# us = cs.drop(['id', 'price'], axis= 1)
		# conv_dates_ = [1 if values == 2014 else 0 for values in us.date]
		# us['date'] = conv_dates_
		# print(cs.price)
		return us


	def price_predition(self):
		lr_model, gbr_model =  self.applying_models()
		usX = self.getting_user_data()
		usY1 = lr_model.predict(usX)
		usY2 = gbr_model.predict(usX)
		print(usY1, usY2)

# ...................................................



# def main():
# 	p = price_predictor("Price Prediction")
# 	p.loading_data()
# 	p.preparing_data()
# 	p.initiating_models()
# 	p.splitting_data()
# 	p.applying_models()
# 	p.getting_models_accuray()

# 	p.getting_user_data()
# 	p.price_predition()


# if __name__ == '__main__':
# 	main()

