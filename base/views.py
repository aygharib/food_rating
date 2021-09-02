from base.models import City, Restaurant

from django.views.generic.list import ListView

class CityList(ListView):
    model = City
    context_object_name = 'cities'
    template_name = 'base/city_list.html'

class CityDetail(ListView):
    model = Restaurant
    context_object_name = 'restaurants'
    template_name = 'base/city_detail.html'