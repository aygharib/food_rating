from base.models import *

from django.shortcuts import render

def city_list(request):
    cities = City.objects.all()
    context = {'cities': cities}

    return render(request, 'base/city_list.html', context)

def city_detail(request, pk):
    restaurants = Restaurant.objects.all().filter(city_id=pk)
    context = {'pk': pk, 'restaurants': restaurants}
    
    return render(request, 'base/city_detail.html', context)