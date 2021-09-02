from base.models import Restaurant

from django.views.generic.list import ListView
from django.shortcuts import render

def city_list(request):
    return render(request, 'base/city_list.html')

def city_detail(request, pk):
    context = {'pk': pk}
    
    return render(request, 'base/city_detail.html', context)

# class CityList(ListView):
#     model = City
#     context_object_name = 'cities'
#     template_name = 'base/city_list.html'

# class CityDetail(ListView):
#     model = Restaurant
#     context_object_name = 'restaurants'
#     template_name = 'base/city_detail.html'