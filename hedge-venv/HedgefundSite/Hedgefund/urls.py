from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new', views.new, name='New Scrape'),
    path('test', views.test, name='Test Page')
]