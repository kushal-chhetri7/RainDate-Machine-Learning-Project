from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    
    path('',views.index,name='index'),
    path('form/',views.form,name="form"),
    path('result/',views.result,name="result"),
    
]

