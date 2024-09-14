from django.contrib import admin
from django.urls import path, include


urlpatterns = [
   path('', include('app_ficha_policial.urls')),
]
