from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.home, name="home"),
   # path('',views.contact, name="contact"),
   path('contact', views.contact, name='contact'),
   path('aboutme', views.aboutme, name='aboutme'),
   path('', views.homepage, name='homepage'),
   
   
]