from base.models import *
from django.shortcuts import render
from django.http import HttpResponse

def city_list(request):
    cities = City.objects.raw('SELECT * FROM base_city ORDER BY name')
    context = {'cities': cities}

    return render(request, 'base/city_list.html', context)

def city_detail(request, pk):
    city = City.objects.raw('SELECT * FROM base_city WHERE id==' + str(pk))[0]

    restaurants_list = []
    for a in Restaurant.objects.raw('SELECT * FROM base_restaurant WHERE city_id==' + str(pk)):
        restaurants_list.append(a)
    
    restaurantfoods_list = []
    for a in RestaurantFood.objects.raw("SELECT * FROM base_restaurantfood WHERE restaurant_id IN (SELECT id FROM base_restaurant WHERE city_id==" + str(pk) + ") ORDER BY score DESC"):
        restaurantfoods_list.append(a)

    foods_list = []
    for a in Food.objects.raw("SELECT * FROM base_food WHERE id IN (SELECT food_id FROM base_restaurantfood WHERE restaurant_id IN (SELECT id FROM base_restaurant WHERE city_id==" + str(pk) + ")) ORDER BY name"):
        foods_list.append(a)

    context = {'pk': pk, 'city': city, 'restaurants_list': restaurants_list, 'restaurantfoods_list': restaurantfoods_list, 'foods_list': foods_list}
    
    return render(request, 'base/city_detail.html', context)

def food_detail(request, city_id, food_id):
    food = Food.objects.raw("SELECT * FROM base_food WHERE id ==" + str(food_id))[0]

    restaurants_list = []
    for a in Restaurant.objects.raw('SELECT * FROM base_restaurant WHERE id IN (SELECT restaurant_id FROM (SELECT * FROM base_restaurantfood WHERE restaurant_id IN (SELECT id FROM base_restaurant WHERE city_id==' + str(city_id) + ')) WHERE food_id==' + str(food_id) + ')'):
        restaurants_list.append(a)

    context = {'food': food, 'restaurants_list': restaurants_list}
    
    return render(request, 'base/food_detail.html', context)