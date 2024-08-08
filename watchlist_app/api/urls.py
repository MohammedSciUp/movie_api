from django.contrib import admin
from django.urls import path

from .views import movie_list, movie_details  # Note the relative import
urlpatterns = [
    path('list/', movie_list ,name='list'), 
    path('<int:pk>/', movie_details, name='movie_detail'), 
]