from base.models import Restaurant

from django.views.generic.list import ListView
from django.shortcuts import render

def city_list(request):
    return render(request, 'base/city_list.html')

def city_detail(request, pk):
    restaurants = Restaurant.objects.all().filter(city_id=pk)
    context = {'pk': pk, 'restaurants': restaurants}
    
    return render(request, 'base/city_detail.html', context)