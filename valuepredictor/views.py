from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from .forms import InputFormModel

import folium
import pandas as pd

def init(request):
	# return HttpResponse('Hello World')
	return render(request, 'valuepredictor/line chart3.html')



def crossmaps(request):
	return render(request, 'valuepredictor/coropleth map1.html')


def maping(request):
	# map = folium.Map(location=[df['latitude'].mean(), 
	coords = [(40.7831, -73.9712), (40.6782, -73.9412), (40.7282, -73.7949)]

	# df['longitude'].mean()],tiles="cartodbpositron",zoom_start=12)
	map = folium.Map(location=[30.403978, 73.106812], zoom_start=12)

	map.save("map.html")

	# {'my_map': map} will output the object, which is what you are seeing
	# to rectify this we need to turn it into an iframe which 
	# the template can then render.
	context = {'my_map': map._repr_html_()} # change to {'my_map': map._repr_html_()}

	return render(request, 'valuepredictor/fmap.html', context)


def scharts(request):
	hsales = pd.read_csv('static/nyc-rolling-sales.csv') 
	hsales.drop(['Unnamed: 0', 'EASE-MENT'],1, inplace=True)

	print('Column name')
	for col in hsales.columns:
		if hsales[col].dtype=='object':
			print(col, hsales[col].nunique())


	numer = ['LAND SQUARE FEET','GROSS SQUARE FEET', 'SALE PRICE', 'BOROUGH']
	for col in numer: # coerce for missing values
	    hsales[col] = pd.to_numeric(hsales[col], errors='coerce')

	categ = ['NEIGHBORHOOD', 'BUILDING CLASS CATEGORY', 'TAX CLASS AT PRESENT', 'BUILDING CLASS AT PRESENT', 'BUILDING CLASS AT TIME OF SALE', 'TAX CLASS AT TIME OF SALE']
	for col in categ:
	    hsales[col] = hsales[col].astype('category')

	hsales['SALE DATE'] = pd.to_datetime(hsales['SALE DATE'], errors='coerce')

	missing = hsales.isnull().sum()/len(hsales)*100

	print(pd.DataFrame([missing[missing>0],pd.Series(hsales.isnull().sum()[hsales.isnull().sum()>1000])], index=['percent missing','how many missing']))

	# let us check for outliers first
	hsales[['LAND SQUARE FEET','GROSS SQUARE FEET']].describe()

	print(hsales[(hsales['LAND SQUARE FEET'].isnull()) & (hsales['GROSS SQUARE FEET'].notnull())].shape)
	print(hsales[(hsales['LAND SQUARE FEET'].notnull()) & (hsales['GROSS SQUARE FEET'].isnull())].shape)

	hsales['LAND SQUARE FEET'] = hsales['LAND SQUARE FEET'].mask((hsales['LAND SQUARE FEET'].isnull()) & (hsales['GROSS SQUARE FEET'].notnull()), hsales['GROSS SQUARE FEET'])
	hsales['GROSS SQUARE FEET'] = hsales['GROSS SQUARE FEET'].mask((hsales['LAND SQUARE FEET'].notnull()) & (hsales['GROSS SQUARE FEET'].isnull()), hsales['LAND SQUARE FEET'])

	#  Check for duplicates before
	print(sum(hsales.duplicated()))
	hsales[hsales.duplicated(keep=False)].sort_values(['NEIGHBORHOOD', 'ADDRESS']).head(10)

	hsales.drop_duplicates(inplace=True)
	print(sum(hsales.duplicated()))

	missing = hsales.isnull().sum()/len(hsales)*100
	print(pd.DataFrame([missing[missing>0],pd.Series(hsales.isnull().sum()[hsales.isnull().sum()>1000])], index=['percent missing','how many missing']))

	print("The number of non-null prices for missing square feet observations:\n",((hsales['LAND SQUARE FEET'].isnull()) & (hsales['SALE PRICE'].notnull())).sum())

	# for visualization purposes, we replace borough numbering with their string names
	hsales['BOROUGH'] = hsales['BOROUGH'].astype(str)
	hsales['BOROUGH'] = hsales['BOROUGH'].str.replace("1", "Manhattan")
	hsales['BOROUGH'] = hsales['BOROUGH'].str.replace("2", "Bronx")
	hsales['BOROUGH'] = hsales['BOROUGH'].str.replace("3", "Brooklyn")
	hsales['BOROUGH'] = hsales['BOROUGH'].str.replace("4", "Queens")
	hsales['BOROUGH'] = hsales['BOROUGH'].str.replace("5", "Staten Island")

	dataset = hsales[(hsales['COMMERCIAL UNITS']<20) & (hsales['TOTAL UNITS']<50) & (hsales['SALE PRICE']<5000000) & (hsales['SALE PRICE']>100000) & (hsales['GROSS SQUARE FEET']>0)]

	return render('request, valuepredictor/rmap.html', context)

def ind(request):

	form = InputFormModel()
	ct = request.POST.get('city')
	
	ar = request.POST.get('area')
	xp = request.POST.get('maxprice')
	np = request.POST.get('minprice')
	pt = request.POST.get('prtype')
	print(ct, ar, xp, np, pt)
	# mapbox_access_token = 'pk.my_mapbox_access_token'

	if request.method == 'POST':
		form = InputFormModel(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return render(request, 'valuepredictor/vmap_.html', {'form': form})

	return render(request, 'valuepredictor/vmap_.html', {'form': form})


# .......................................................

# trevelx theme index page rending 

def ind1(request):
	contents = {
	'Area_city': 'Lahore',
	'Property_type': 'Commercial',
	'land_price': 500000,
	}

	
	return render(request, 'valuepredictor/imap_.html')


def blog(request):
	return render(request, 'valuepredictor/blog.html')


def offers(request):
	return render(request, 'valuepredictor/offers.html')

def single_listing1(request):
	return render(request, 'valuepredictor/single_listing.html')

def elements(request):
	return render(request, 'valuepredictor/elements.html')

def contact1(request):
	return render(request, 'valuepredictor/contact1.html')

