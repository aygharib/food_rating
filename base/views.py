from base.models import *
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from base.forms import CustomUserCreationForm

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('city-list')

    return render(request, 'base/login.html')

def logout_user(request):
    logout(request)

    return redirect('city-list')

def register_user(request):
    form = CustomUserCreationForm()
    
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            user = authenticate(request, username=user.username, password=request.POST['password1'])

            if user is not None:
                login(request, user)

                return redirect('city-list')

    context = {'form': form}
    return render(request, 'base/register.html', context)

def city_list(request):
    cities = City.objects.raw('SELECT * FROM base_city ORDER BY name')
    context = {'cities': cities}

    return render(request, 'base/city_list.html', context)

@login_required(login_url='login')
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

@login_required(login_url='login')
def food_detail(request, city_id, food_id):
    food = Food.objects.raw("SELECT * FROM base_food WHERE id ==" + str(food_id))[0]

    # This is theoretically useless, since we have restaurantfoods_list
    restaurants_list = []
    for a in Restaurant.objects.raw('SELECT * FROM base_restaurant WHERE id IN (SELECT restaurant_id FROM (SELECT * FROM base_restaurantfood WHERE restaurant_id IN (SELECT id FROM base_restaurant WHERE city_id==' + str(city_id) + ')) WHERE food_id==' + str(food_id) + ')'):
        restaurants_list.append(a)

    restaurantfoods_list = []
    for a in RestaurantFood.objects.raw('SELECT * FROM (SELECT * FROM base_restaurantfood WHERE restaurant_id IN (SELECT id FROM base_restaurant WHERE city_id==' + str(city_id) + ')) WHERE food_id==' + str(food_id)):
        restaurantfoods_list.append(a)

    context = {'food': food, 'restaurants_list': restaurants_list, 'restaurantfoods_list': restaurantfoods_list}
    
    return render(request, 'base/food_detail.html', context)