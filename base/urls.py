from django.urls import path

from base.views import *

urlpatterns = [
    path('login/', login_page, name='login'),

    path('', city_list, name='city-list'),
    path('city/<int:pk>/', city_detail, name='city'),
    path('city/<int:city_id>/<int:food_id>/', food_detail, name='food_detail'),
]