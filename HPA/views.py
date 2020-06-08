from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect

from .PricePredictor import Collector
import folium
import pandas as pd
import pygeoj
import plotly.express as px
import json


def MapView(request):
	 
	# Make a data frame with dots to show on the map
	data = pd.DataFrame({
	   'lat':[33.67989, 33.6314859999999, 24.805045],
	   'lon':[73.01264, 72.926559, 67.064323],
	   'name':['Buenos Aires', 'Paris', 'melbourne'],
	   'value':[10.4,12.43,40.42]
	})
	
	 
	# Make an empty map
	m = folium.Map(location=[73.01,30.02], tiles="Mapbox Bright", zoom_start=8)
	 
	# I can add marker one by one on the map
	for i in range(0,len(data)):
	   folium.Circle(
	      location=[data.iloc[i]['lon'], data.iloc[i]['lat']],
	      popup=data.iloc[i]['name'],
	      radius=data.iloc[i]['value']*1000,
	      color='crimson',
	      fill=True,
	      fill_color='crimson'
	   ).add_to(m)
	 
	# Save it as html
	m.save('mymap.html')

	state_geo = pygeoj.load(filepath="HPA/static/pakistan.geojson")

	m = folium.Map([32, 73], zoom_start=9,tiles='cartodbpositron')
	c = Collector('Data Collector')
	r = c.get_ready()
	state_data = c.df
	state_data_ = c.df1


	choropleth = folium.Choropleth(
	    geo_data=state_geo,
	    name='choropleth',
	    data=state_data[:100],
	    columns=['latitude', 'longitude'],
	    key_on='feature.properties.districts',
	    fill_color='YlGn',
	    fill_opacity=0.7,
	    line_opacity=0.2,
	    legend_name='Property Prices',
	    highlight=True,
	    line_color='white'
	).add_to(m)

# I can add marker one by one on the map
	# for i in range(0,len(state_data[20595:20615])):
	#    folium.Circle(
	#       location=[state_data.iloc[i]['longitude'], state_data.iloc[i]['latitude']],
	#       popup=state_data.iloc[i][['longitude', 'latitude']],
	#       radius=state_data.iloc[i]['Area Size']*1000,
	#       color='crimson',
	#       fill=True,
	#       fill_color='crimson'
	#    ).add_to(m)
	for i in range(0,len(state_data[20915: 20915])):
		folium.Marker([state_data.iloc[i]['longitude'], state_data.iloc[i]['latitude']], popup=state_data.iloc[i]['location']).add_to(m)

	folium.LayerControl(collapsed=True).add_to(m)
	choropleth.geojson.add_child(
    folium.features.GeoJsonTooltip(['districts'],labels=False))
	m.save('pakistan.html')

	return render(request, 'HPA/pak-map.html')

cit = ""
loc = ""

ud = []

# info about cities and stats

def Predictor(request):
	global cit
	global loc
	global ud
	c = Collector('Data Collector')
	r = c.get_ready()
	dis, dl = c.get_dis_data()
		# print(dis)
		# ct = request.POST.get('city')
		# if request.method == 'POST':
	return render(request, 'HPA/dis_selection.html', {'dis': dis})
		# il, isl = c.get_is_data()
		# rp, rpl = c.get_rp_data()
		# lh, lhl = c.get_lh_data()
		# fd, fdl = c.get_fd_data()
		# kr, krl = c.get_kr_data()
		# br, brl = c.get_bedrooms_data()
		# bt, btl = c.get_baths_data()


		# ct = request.POST.get('city')
		# print(c.get_baths_data()[0])

		# # if ct != None:
		
		# context = {
		# 	'ct': ct,
		# 	'il': il,
		# 	'rp': rp,
		# 	'lh': lh,
		# 	'fd': fd,
		# 	'kr': kr,
		# 	'br': br,
		# 	'bt': bt,
		# }
		# # print(context)
		# return render(request, 'HPA/Predictor.html', context)


	# return render(request, 'HPA/predictor.html')

# ...................................

def isl_prediction(request):

	c = Collector('Data Collector')
	r = c.get_ready()
	prt, prt_ln = c.get_prt_data()
	cat, cat_ln = c.get_cat_data()
	loc, loc_ln = c.get_is_data()
	art, art_ln = c.get_art_data()
	prp, prp_ln = c.get_prp_data()

# province name is already hard code with city

	bed, bed_ln = c.get_bedrooms_data()
	bat, bat_ln = c.get_baths_data()
	ars, ars_ln = c.get_area_size_data()

	context = { 'loc': loc, 'prt': prt,
				'art': art, 'prp': prp,
				'cat': cat, 'bed': bed,
				'bat': bat, 'ars': ars,

			}


	if request.method == 'POST':
		prp_ = request.POST.get('purpose')
		prt_ = request.POST.get('type')
		loc_ = request.POST.get('location')
		cat_ = request.POST.get('category')
		art_ = request.POST.get('atype')
		ars_ = request.POST.get('size')
		bdr_ = request.POST.get('bedrooms')
		bat_ = request.POST.get('baths')

		dis_ = 1
		prn_ = 0
		# print(loc_, type(loc_))
		lon_, lat_ = c.get_lonlat_data(dis_, loc_)
		# print(lon_, lat_)
		# lon_, lat_ = lon_lat

		ui_ml_data = [prt_, loc_, dis_, prn_, prp_, art_, cat_, lon_, lat_, ars_, bdr_, bat_]

		print(ui_ml_data)
		
		r = c.get_price_predition(ui_ml_data)
		print(r, type(r))
		res = round(r[0], 0)
		if r[0] < 0:
			res = res * (-1)
		context = { 'loc': loc, 'prt': prt,
				'art': art, 'prp': prp,
				'cat': cat, 'bed': bed,
				'bat': bat, 'ars': ars,
				'ui' : ui_ml_data,
				'prediction': res,
				}

		return render(request, 'HPA/isl_predictor.html', context)

	return render(request, 'HPA/isl_predictor.html', context)


def rwp_prediction(request):
	c = Collector('Data Collector')
	r = c.get_ready()
	prt, prt_ln = c.get_prt_data()
	cat, cat_ln = c.get_cat_data()
	loc, loc_ln = c.get_rp_data()
	art, art_ln = c.get_art_data()
	prp, prp_ln = c.get_prp_data()

# province name is already hard code with city

	bed, bed_ln = c.get_bedrooms_data()
	bat, bat_ln = c.get_baths_data()
	ars, ars_ln = c.get_area_size_data()

	context = { 'loc': loc, 'prt': prt,
				'art': art, 'prp': prp,
				'cat': cat, 'bed': bed,
				'bat': bat, 'ars': ars,

			}


	if request.method == 'POST':
		prp_ = request.POST.get('purpose')
		prt_ = request.POST.get('type')
		loc_ = request.POST.get('location')
		cat_ = request.POST.get('category')
		art_ = request.POST.get('atype')
		ars_ = request.POST.get('size')
		bdr_ = request.POST.get('bedrooms')
		bat_ = request.POST.get('baths')

		dis_ = 4
		prn_ = 1
		# print(loc_, type(loc_))
		lon_, lat_ = c.get_lonlat_data(dis_, loc_)
		# print(lon_, lat_)
		# lon_, lat_ = lon_lat

		ui_ml_data = [prt_, loc_, dis_, prn_, prp_, art_, cat_, lon_, lat_, ars_, bdr_, bat_]

		print(ui_ml_data)
		
		r = c.get_price_predition(ui_ml_data)
		print(r, type(r))
		res = round(r[0], 0)
		if r[0] < 0:
			res = res * (-1)
		context = { 'loc': loc, 'prt': prt,
				'art': art, 'prp': prp,
				'cat': cat, 'bed': bed,
				'bat': bat, 'ars': ars,
				'ui' : ui_ml_data,
				'prediction': res,
				}

		return render(request, 'HPA/rwp_predictor.html', context)

	return render(request, 'HPA/rwp_predictor.html',  context)


def lhr_prediction(request):
	c = Collector('Data Collector')
	r = c.get_ready()
	prt, prt_ln = c.get_prt_data()
	cat, cat_ln = c.get_cat_data()
	loc, loc_ln = c.get_lh_data()
	art, art_ln = c.get_art_data()
	prp, prp_ln = c.get_prp_data()

# province name is already hard code with city

	bed, bed_ln = c.get_bedrooms_data()
	bat, bat_ln = c.get_baths_data()
	ars, ars_ln = c.get_area_size_data()

	context = { 'loc': loc, 'prt': prt,
				'art': art, 'prp': prp,
				'cat': cat, 'bed': bed,
				'bat': bat, 'ars': ars,

			}


	if request.method == 'POST':
		prp_ = request.POST.get('purpose')
		prt_ = request.POST.get('type')
		loc_ = request.POST.get('location')
		cat_ = request.POST.get('category')
		art_ = request.POST.get('atype')
		ars_ = request.POST.get('size')
		bdr_ = request.POST.get('bedrooms')
		bat_ = request.POST.get('baths')

		dis_ = 0
		prn_ = 1
		# print(loc_, type(loc_))
		lon_, lat_ = c.get_lonlat_data(dis_, loc_)
		# print(lon_, lat_)
		# lon_, lat_ = lon_lat

		ui_ml_data = [prt_, loc_, dis_, prn_, prp_, art_, cat_, lon_, lat_, ars_, bdr_, bat_]

		print(ui_ml_data)
		
		r = c.get_price_predition(ui_ml_data)
		print(r, type(r))
		res = round(r[0], 0)
		if r[0] < 0:
			res = res * (-1)
		context = { 'loc': loc, 'prt': prt,
				'art': art, 'prp': prp,
				'cat': cat, 'bed': bed,
				'bat': bat, 'ars': ars,
				'ui' : ui_ml_data,
				'prediction': res,
				}

		return render(request, 'HPA/lhr_predictor.html', context)

	return render(request, 'HPA/lhr_predictor.html',  context)

def fsd_prediction(request):

	c = Collector('Data Collector')
	r = c.get_ready()
	prt, prt_ln = c.get_prt_data()
	cat, cat_ln = c.get_cat_data()
	loc, loc_ln = c.get_fd_data()
	art, art_ln = c.get_art_data()
	prp, prp_ln = c.get_prp_data()

# province name is already hard code with city

	bed, bed_ln = c.get_bedrooms_data()
	bat, bat_ln = c.get_baths_data()
	ars, ars_ln = c.get_area_size_data()

	context = { 'loc': loc, 'prt': prt,
				'art': art, 'prp': prp,
				'cat': cat, 'bed': bed,
				'bat': bat, 'ars': ars,

			}


	if request.method == 'POST':
		prp_ = request.POST.get('purpose')
		prt_ = request.POST.get('type')
		loc_ = request.POST.get('location')
		cat_ = request.POST.get('category')
		art_ = request.POST.get('atype')
		ars_ = request.POST.get('size')
		bdr_ = request.POST.get('bedrooms')
		bat_ = request.POST.get('baths')

		dis_ = 1
		prn_ = 0
		# print(loc_, type(loc_))
		lon_, lat_ = c.get_lonlat_data(dis_, loc_)
		# print(lon_, lat_)
		# lon_, lat_ = lon_lat

		ui_ml_data = [prt_, loc_, dis_, prn_, prp_, art_, cat_, lon_, lat_, ars_, bdr_, bat_]

		print(ui_ml_data)
		
		r = c.get_price_predition(ui_ml_data)
		print(r, type(r))
		res = round(r[0], 0)
		if r[0] < 0:
			res = res * (-1)
		context = { 'loc': loc, 'prt': prt,
				'art': art, 'prp': prp,
				'cat': cat, 'bed': bed,
				'bat': bat, 'ars': ars,
				'ui' : ui_ml_data,
				'prediction': res,
				}

		return render(request, 'HPA/fsd_predictor.html', context)


	return render(request, 'HPA/fsd_predictor.html', context)

def krc_prediction(request):

	c = Collector('Data Collector')
	r = c.get_ready()
	prt, prt_ln = c.get_prt_data()
	cat, cat_ln = c.get_cat_data()
	loc, loc_ln = c.get_kr_data()
	art, art_ln = c.get_art_data()
	prp, prp_ln = c.get_prp_data()

# province name is already hard code with city

	bed, bed_ln = c.get_bedrooms_data()
	bat, bat_ln = c.get_baths_data()
	ars, ars_ln = c.get_area_size_data()

	context = { 'loc': loc, 'prt': prt,
				'art': art, 'prp': prp,
				'cat': cat, 'bed': bed,
				'bat': bat, 'ars': ars,

			}


	if request.method == 'POST':
		prp_ = request.POST.get('purpose')
		prt_ = request.POST.get('type')
		loc_ = request.POST.get('location')
		cat_ = request.POST.get('category')
		art_ = request.POST.get('atype')
		ars_ = request.POST.get('size')
		bdr_ = request.POST.get('bedrooms')
		bat_ = request.POST.get('baths')

		dis_ = 2
		prn_ = 2
		# print(loc_, type(loc_))
		lon_, lat_ = c.get_lonlat_data(dis_, loc_)
		# print(lon_, lat_)
		# lon_, lat_ = lon_lat

		ui_ml_data = [prt_, loc_, dis_, prn_, prp_, art_, cat_, lon_, lat_, ars_, bdr_, bat_]

		print(ui_ml_data)
		
		r = c.get_price_predition(ui_ml_data)
		print(r, type(r))
		res = round(r[0], 0)
		if r[0] < 0:
			res = res * (-1)
		context = { 'loc': loc, 'prt': prt,
				'art': art, 'prp': prp,
				'cat': cat, 'bed': bed,
				'bat': bat, 'ars': ars,
				'ui' : ui_ml_data,
				'prediction': res,
				}

		return render(request, 'HPA/krc_predictor.html', context)


	return render(request, 'HPA/krc_predictor.html',  context)

# ......................................



def test(request):
	context = {
		'info_1': "Number of Flats in Pakistan",
		'graph_file': "{% include 'HPA/PAK/pak-flat_counts.html' %}",
		'info_2': "Average Sale Price of Flats",
		
	}
	return render(request, 'HPA/test.html', context)

def Pak_Flats(request):
	context = {
		'info_1': "Number of Flats in Pakistan",
		"f1": "'{% include 'HPA/PAK/pak-flat_counts.html' %}'",
		'info_2': "Average Sale Price of Flats",
		
	}
	ct = request.POST.get('location')
	print(ct)
	# mapbox_access_token = 'pk.my_mapbox_access_token'
	c = {
		'city': ct,
		'info_1': "Number of Flats in ",
		'info_2': "Average Prices of Flats in ",
	}

	if request.method == 'POST':
	
		return render(request, 'HPA/Flats.html', c)


	

	return render(request, 'HPA/pak_flats.html', context)

def Pak_Rooms(request):
	context = {
		'info_1': "Number of Rooms in Pakistan",
		'f1': "HPA/PAK/pak-flat_counts.html",
		'info_2': "Average Sale Price of Rooms",
		'f2': "HPA/PAK/pak-flat.html",
	}

	ct = request.POST.get('location')
	print(ct)
	# mapbox_access_token = 'pk.my_mapbox_access_token'
	c = {
		'city': ct,
		'info_1': "Number of Rooms in ",
		'info_2': "Average Prices of Rooms in ",
	}

	if request.method == 'POST':
	
		return render(request, 'HPA/Rooms.html', c)


	return render(request, 'HPA/pak_rooms.html', context)

def Pak_UpperPortions(request):
	context = {
		'info_1': "Number of Upper Portions in Pakistan",
		'f1': "HPA/PAK/pak-flat_counts.html",
		'info_2': "Average Sale Price of Upper Portions",
		'f2': "HPA/PAK/pak-flat.html",
	}

	ct = request.POST.get('location')
	print(ct)
	# mapbox_access_token = 'pk.my_mapbox_access_token'
	c = {
		'city': ct,
		'info_1': "Number of Upper Portions in ",
		'info_2': "Average Prices of Upper Portions in ",
	}

	if request.method == 'POST':
	
		return render(request, 'HPA/UPortions.html', c)


	return render(request, 'HPA/pak_uportion.html', context)

def Pak_LowerPortions(request):
	context = {
		'info_1': "Number of Lower Portions in Pakistan",
		'f1': "HPA/PAK/pak-flat_counts.html",
		'info_2': "Average Sale Price of Lower Portions ",
		'f2': "HPA/PAK/pak-flat.html",
	}
	ct = request.POST.get('location')
	print(ct)
	c = {
		'city': ct,
		'info_1': "Number of Lower Portions in ",
		'info_2': "Average Prices of Lower Portions in ",
	}

	if request.method == 'POST':
	
		return render(request, 'HPA/LPortions.html', c)


	return render(request, 'HPA/pak_lportion.html', context)

def Pak_Houses(request):
	context = {
		'info_1': "Number of Houses in Pakistan",
		'f1': "HPA/PAK/pak-flat_counts.html",
		'info_2': "Average Sale Price of Houses",
		'f2': "HPA/PAK/pak-flat.html",
	}
	ct = request.POST.get('location')
	print(ct)
	c = {
		'city': ct,
		'info_1': "Number of Houses in ",
		'info_2': "Average Prices of Houses in ",
	}

	if request.method == 'POST':
	
		return render(request, 'HPA/Houses.html', c)

	return render(request, 'HPA/pak_houses.html', context)

def Pak_FarmHouses(request):
	context = {
		'info_1': "Number of Farm Houses in Pakistan",
		'f1': "HPA/PAK/pak-flat_counts.html",
		'info_2': "Average Sale Price of Farm Houses",
		'f2': "HPA/PAK/pak-flat.html",
	}
	ct = request.POST.get('location')
	print(ct)
	c = {
		'city': ct,
		'info_1': "Number of Farm Houses in ",
		'info_2': "Average Prices of Farm Houses in ",
	}

	if request.method == 'POST':
	
		return render(request, 'HPA/FHouses.html', c)

	return render(request, 'HPA/pak_fhouse.html', context)

def Pak_PentHouses(request):
	context = {
		'info_1': "Number of penthouses in Pakistan",
		'f1': "HPA/PAK/pak-flat_counts.html",
		'info_2': "Average Sale Price of penthouses",
		'f2': "HPA/PAK/pak-flat.html",
	}
	ct = request.POST.get('location')
	print(ct)
	c = {
		'city': ct,
		'info_1': "Number of Penthouses in ",
		'info_2': "Average Prices of Penthouses in ",
	}

	if request.method == 'POST':
	
		return render(request, 'HPA/PHouses.html', c)

	return render(request, 'HPA/pak_phouse.html', context)

# def crossmaps(request):
# 	return render(request, 'valuepredictor/coropleth map1.html')


# def maping(request):
# 	# map = folium.Map(location=[df['latitude'].mean(), 
# 	coords = [(40.7831, -73.9712), (40.6782, -73.9412), (40.7282, -73.7949)]

# 	# df['longitude'].mean()],tiles="cartodbpositron",zoom_start=12)
# 	map = folium.Map(location=[30.403978, 73.106812], zoom_start=12)

# 	map.save("map.html")

# 	# {'my_map': map} will output the object, which is what you are seeing
# 	# to rectify this we need to turn it into an iframe which 
# 	# the template can then render.
# 	context = {'my_map': map._repr_html_()} # change to {'my_map': map._repr_html_()}

# 	return render(request, 'valuepredictor/fmap.html', context)


# def scharts(request):
# 	hsales = pd.read_csv('static/nyc-rolling-sales.csv') 
# 	hsales.drop(['Unnamed: 0', 'EASE-MENT'],1, inplace=True)

# 	print('Column name')
# 	for col in hsales.columns:
# 		if hsales[col].dtype=='object':
# 			print(col, hsales[col].nunique())


# 	numer = ['LAND SQUARE FEET','GROSS SQUARE FEET', 'SALE PRICE', 'BOROUGH']
# 	for col in numer: # coerce for missing values
# 	    hsales[col] = pd.to_numeric(hsales[col], errors='coerce')

# 	categ = ['NEIGHBORHOOD', 'BUILDING CLASS CATEGORY', 'TAX CLASS AT PRESENT', 'BUILDING CLASS AT PRESENT', 'BUILDING CLASS AT TIME OF SALE', 'TAX CLASS AT TIME OF SALE']
# 	for col in categ:
# 	    hsales[col] = hsales[col].astype('category')

# 	hsales['SALE DATE'] = pd.to_datetime(hsales['SALE DATE'], errors='coerce')

# 	missing = hsales.isnull().sum()/len(hsales)*100

# 	print(pd.DataFrame([missing[missing>0],pd.Series(hsales.isnull().sum()[hsales.isnull().sum()>1000])], index=['percent missing','how many missing']))

# 	# let us check for outliers first
# 	hsales[['LAND SQUARE FEET','GROSS SQUARE FEET']].describe()

# 	print(hsales[(hsales['LAND SQUARE FEET'].isnull()) & (hsales['GROSS SQUARE FEET'].notnull())].shape)
# 	print(hsales[(hsales['LAND SQUARE FEET'].notnull()) & (hsales['GROSS SQUARE FEET'].isnull())].shape)

# 	hsales['LAND SQUARE FEET'] = hsales['LAND SQUARE FEET'].mask((hsales['LAND SQUARE FEET'].isnull()) & (hsales['GROSS SQUARE FEET'].notnull()), hsales['GROSS SQUARE FEET'])
# 	hsales['GROSS SQUARE FEET'] = hsales['GROSS SQUARE FEET'].mask((hsales['LAND SQUARE FEET'].notnull()) & (hsales['GROSS SQUARE FEET'].isnull()), hsales['LAND SQUARE FEET'])

# 	#  Check for duplicates before
# 	print(sum(hsales.duplicated()))
# 	hsales[hsales.duplicated(keep=False)].sort_values(['NEIGHBORHOOD', 'ADDRESS']).head(10)

# 	hsales.drop_duplicates(inplace=True)
# 	print(sum(hsales.duplicated()))

# 	missing = hsales.isnull().sum()/len(hsales)*100
# 	print(pd.DataFrame([missing[missing>0],pd.Series(hsales.isnull().sum()[hsales.isnull().sum()>1000])], index=['percent missing','how many missing']))

# 	print("The number of non-null prices for missing square feet observations:\n",((hsales['LAND SQUARE FEET'].isnull()) & (hsales['SALE PRICE'].notnull())).sum())

# 	# for visualization purposes, we replace borough numbering with their string names
# 	hsales['BOROUGH'] = hsales['BOROUGH'].astype(str)
# 	hsales['BOROUGH'] = hsales['BOROUGH'].str.replace("1", "Manhattan")
# 	hsales['BOROUGH'] = hsales['BOROUGH'].str.replace("2", "Bronx")
# 	hsales['BOROUGH'] = hsales['BOROUGH'].str.replace("3", "Brooklyn")
# 	hsales['BOROUGH'] = hsales['BOROUGH'].str.replace("4", "Queens")
# 	hsales['BOROUGH'] = hsales['BOROUGH'].str.replace("5", "Staten Island")

# 	dataset = hsales[(hsales['COMMERCIAL UNITS']<20) & (hsales['TOTAL UNITS']<50) & (hsales['SALE PRICE']<5000000) & (hsales['SALE PRICE']>100000) & (hsales['GROSS SQUARE FEET']>0)]

# 	return render('request, valuepredictor/rmap.html', context)

# def ind(request):

# 	form = InputFormModel()
# 	ct = request.POST.get('city')
	
# 	ar = request.POST.get('area')
# 	xp = request.POST.get('maxprice')
# 	np = request.POST.get('minprice')
# 	pt = request.POST.get('prtype')
# 	print(ct, ar, xp, np, pt)
# 	# mapbox_access_token = 'pk.my_mapbox_access_token'

# 	if request.method == 'POST':
# 		form = InputFormModel(request.POST)
# 		if form.is_valid():
# 			form.save(commit=True)
# 			return render(request, 'valuepredictor/vmap_.html', {'form': form})

# 	return render(request, 'valuepredictor/vmap_.html', {'form': form})


# # .......................................................

# # trevelx theme index page rending 

# def ind1(request):
# 	contents = {
# 	'Area_city': 'Lahore',
# 	'Property_type': 'Commercial',
# 	'land_price': 500000,
# 	}

	
# 	return render(request, 'valuepredictor/imap_.html')


