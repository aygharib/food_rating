from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100)
    # image = https://www.geeksforgeeks.org/imagefield-django-models/

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    postalcode = models.CharField(max_length=200)
    number = models.IntegerField(max_length=100)

    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Food(models.Model):
    name = models.CharField(max_length=100)
    
    restaurant = models.ManyToManyField(Restaurant, through='RestaurantFood')

    def __str__(self):
        return self.name

class RestaurantFood(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    score = models.CharField(max_length=100)

    def __str__(self):
        return self.score