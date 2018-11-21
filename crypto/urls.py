from django.contrib import admin
from django.urls import path,include
from crypto import views
urlpatterns = [
    path('',views.home,name='home'),
    path('prices/',views.prices,name='prices'),
]
