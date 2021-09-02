from django.urls import path

from base.views import *

urlpatterns = [
    path('', city_list, name='city-list'),
    path('city/<int:pk>/', city_detail, name='city'),
]