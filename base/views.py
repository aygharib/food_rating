from base.models import *

from django.shortcuts import render

def city_list(request):
    cities = City.objects.all()
    context = {'cities': cities}

    return render(request, 'base/city_list.html', context)

def city_detail(request, pk):
    city = City.objects.all().only('name').get(id=pk).name
    restaurants = Restaurant.objects.all().filter(city_id=pk)
    restaurantfoods = RestaurantFood.objects.all().filter(restaurant_id__in=restaurants)
    #foods = Food.objects.all().filter(food_id__in=restaurantfoods) # not working

    context = {'pk': pk, 'city': city, 'restaurants': restaurants, 'restaurantfoods': restaurantfoods}
    
    return render(request, 'base/city_detail.html', context)