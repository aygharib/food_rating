from base.models import *

from django.shortcuts import render
from django.db.models.functions import Cast
from django.db.models import IntegerField

def city_list(request):
    cities = City.objects.all()
    context = {'cities': cities}

    return render(request, 'base/city_list.html', context)

def city_detail(request, pk):
    # restaurants, restaurantfoods, foods
    city = City.objects.filter(id=pk)
    restaurants = Restaurant.objects.filter(city_id=pk)
    restaurantfoods = RestaurantFood.objects.annotate(new_int_field=Cast('score', IntegerField())).order_by('-new_int_field', 'score')
    foods = Food.objects.all()
    
    context = {'pk': pk, 'city': city, 'restaurants': restaurants, 'restaurantfoods': restaurantfoods, 'foods': foods}
    
    return render(request, 'base/city_detail.html', context)