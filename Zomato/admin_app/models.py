from django.db import models


class AdminLogin(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
    otp = models.IntegerField()


class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    country_name = models.CharField(unique=True, max_length=50)

    def __str__(self):
        return self.country_name


class State(models.Model):
    state_id = models.AutoField(primary_key=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state_name = models.CharField(unique=True, max_length=50)

    def __str__(self):
        return self.state_name


class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=50)

    def __str__(self):
        return self.city_name


class Region(models.Model):
    region_id = models.AutoField(primary_key=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    region_name = models.CharField(max_length=50)

    def __str__(self):
        return self.region_name


class RestaurantCategory(models.Model):
    resto_id = models.AutoField(primary_key=True)
    resto_type = models.CharField(unique=True, max_length=50)

    def __str__(self):
        return self.resto_type


