from django.urls import path
from . import views

from base.views import CityList, CityDetail

urlpatterns = [
    path('', CityList.as_view(), name='city-list'),
    path('city/<int:pk>/', CityDetail.as_view(), name='city'),
]