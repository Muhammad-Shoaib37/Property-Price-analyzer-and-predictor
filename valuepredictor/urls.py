from django.urls import path
from . import views

urlpatterns = [

path('init', views.init, name='init'),

path('maping', views.maping, name='maping'),

path('crossmaps', views.crossmaps, name = 'crossmaps'),

path('ind', views.ind, name='ind'),

path('ind1', views.ind1, name='ind1'),

path('blog', views.blog, name='blog'),

path('elements', views.elements, name='elements'),

path('offers', views.offers, name='offers'),


path('single_listing1', views.single_listing1, name='single_listing1'),


path('contact1', views.contact1, name='contact1'),

# path('visualizer', views.vis, name='vis'),
# path('help&support', views.help, name='help'),

# path('addup', views.add_data, name='add'),



]