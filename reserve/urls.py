from django.contrib import admin
from django.urls import path
from .import views
from reserve import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('book', views.book, name='book'),
    path('bookings', views.bookings, name='bookings'),



]
