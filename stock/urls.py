from django.contrib import admin
from django.urls import path 

from stock import views

urlpatterns = [
    path("", views.index , name="index"),
    path("stock", views.stock, name = "stock"),
    path("results", views.results , name = "results"),
    path("list", views.lists, name = "list"),
    path("rck", views.rck)
    
]
    



