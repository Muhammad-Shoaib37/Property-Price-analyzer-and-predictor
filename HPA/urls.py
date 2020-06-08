from django.urls import path
from . import views

urlpatterns = [

path('MapView', views.MapView, name='MapView'),

path('isl_prediction', views.isl_prediction, name='isl_prediction'),

path('rwp_prediction', views.rwp_prediction, name='rwp_prediction'),

path('lhr_prediction', views.lhr_prediction, name='lhr_prediction'),

path('fsd_prediction', views.fsd_prediction, name='fsd_prediction'),

path('krc_prediction', views.krc_prediction, name='krc_prediction'),



path('test', views.test, name='test'),

path('Property-Price-Predictor', views.Predictor, 
	 name = 'Predictor'),

path('Pak-flats', views.Pak_Flats, name='Pak_Flats'),

path('Pak-Rooms', views.Pak_Rooms, name='Pak_Rooms'),

path('Pak-Houses', views.Pak_Houses, name='Pak_Houses'),

path('Pak-LowerPortions', views.Pak_LowerPortions, name='Pak_LowerPortions'),

path('Pak-UpperPortions', views.Pak_UpperPortions, name='Pak_UpperPortions'),

path('Pak-FarmHouses', views.Pak_FarmHouses, name='Pak_FarmHouses'),

path('Pak-PentHouses', views.Pak_PentHouses, name='Pak_PentHouses'),


# path('maping', views.maping, name='maping'),

# path('crossmaps', views.crossmaps, name = 'crossmaps'),

]