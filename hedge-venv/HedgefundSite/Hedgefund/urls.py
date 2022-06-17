from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new', views.new, name='New Scrape'),
    path('icons', views.icons, name='Grab Icons'),
    path('test2', views.test2, name='Test Page'),
    path('test', views.test, name='Test Page')
]