from django.contrib import admin
from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:pk>/results/', views.results, name='result'),
    path('<str:pk>/vote/', views.vote, name='vote'),
    path('<str:pk>/', views.details, name='details'),

]
