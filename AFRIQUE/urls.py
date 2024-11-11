from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
     path('style/', views.style, name='style'),
   
    
]