from turtle import settiltangle
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new', views.new, name='New Scrape'),
    path('old', views.old, name='Test Page'),
    path('icons', views.icons, name='Grab Icons'),
    path('coins', views.getCoins, name='Grab Coins'),
    path('coin', views.getCoin, name='Grab Coins'),
    path('test', views.test, name='Test Page'),
    path('test2', views.test2, name='Test Page')
]

#urlpatterns += staticfiles_urlpatterns()