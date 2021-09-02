from django.contrib import admin

from base.models import *

admin.site.register(City)
admin.site.register(Restaurant)
admin.site.register(Food)
admin.site.register(RestaurantFood)