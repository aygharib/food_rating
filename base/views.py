from base.models import *

from django.shortcuts import render
from django.db.models.functions import Cast
from django.db.models import IntegerField

def city_list(request):
    cities = City.objects.all()
    context = {'cities': cities}

    return render(request, 'base/city_list.html', context)

def city_detail(request, pk):
    city = City.objects.filter(id=pk)
    restaurants = Restaurant.objects.filter(city_id=pk)
    restaurantfoods = RestaurantFood.objects.annotate(new_int_field=Cast('score', IntegerField())).order_by('-new_int_field', 'score')
    foods = Food.objects.all()

    city = City.objects.raw('SELECT * FROM base_city WHERE id==' + str(pk))[0]

    restaurants_list = []
    for a in Restaurant.objects.raw('SELECT * FROM base_restaurant WHERE city_id==' + str(pk)):
        restaurants_list.append(a)
    
    restaurantfoods_list = []
    for a in RestaurantFood.objects.raw("SELECT * FROM base_restaurantfood WHERE restaurant_id IN (SELECT id FROM base_restaurant WHERE city_id==" + str(pk) + ")"):
        restaurantfoods_list.append(a)

    foods_list = []
    for a in Food.objects.raw("SELECT * FROM base_food WHERE id IN (SELECT food_id FROM base_restaurantfood WHERE restaurant_id IN (SELECT id FROM base_restaurant WHERE city_id==" + str(pk) + "))"):
        foods_list.append(a)

    context = {'pk': pk, 'city': city, 'restaurants': restaurants, 'restaurantfoods': restaurantfoods, 'foods': foods, 'city':city, 'restaurants_list':restaurants_list, 'restaurantfoods_list':restaurantfoods_list, 'foods_list':foods_list}
    
    return render(request, 'base/city_detail.html', context)