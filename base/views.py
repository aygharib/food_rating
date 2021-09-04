from base.models import *

from django.shortcuts import render

def city_list(request):
    cities = City.objects.all()
    context = {'cities': cities}

    return render(request, 'base/city_list.html', context)

def city_detail(request, pk):
    # city = City.objects.get(id=pk).name #get city
    # restaurants = Restaurant.objects.filter(city_id=pk) #restaurants in city
    # restaurantfoods = RestaurantFood.objects.filter(restaurant_id__in=restaurants) #restaurantfoods in city

    # restaurant_ids = Restaurant.objects.filter(city_id=pk).values('id') # city_id -> restaurant_id
    # food_ids = RestaurantFood.objects.filter(restaurant_id__in=restaurant_ids).values('food_id') # restaurant_id -> food_id
    # foods = Food.objects.filter(id__in=food_ids)

    # restaurants, restaurantfoods, foods
    restaurants = Restaurant.objects.filter(city_id=pk)
    restaurantfoods = RestaurantFood.objects.all()
    foods = Food.objects.all()

    # context = {'pk': pk, 'city': city, 'restaurants': restaurants, 'restaurantfoods': restaurantfoods, 'food_ids': food_ids}
    context = {'pk': pk, 'restaurants': restaurants, 'restaurantfoods': restaurantfoods, 'foods': foods}
    
    return render(request, 'base/city_detail.html', context)