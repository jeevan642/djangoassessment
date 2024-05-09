from django.db import models
from django.utils import timezone

# Create your models here.

class user(models.Model):
    email = models.TextField(max_length=30)

class country(models.Model):
    # my_user = models.ForeignKey(user,null=True,on_delete=models.CASCADE)
    name =  models.TextField()
    country_code = models.IntegerField()
    curr_symbol = models.TextField()
    phone_code = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

class state(models.Model):
    # country_code = models.ForeignKey(country,on_delete=models.CASCADE)
    name =  models.TextField()
    state_code = models.IntegerField()
    gst_code = models.TextField()
    phone_code = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

class city(models.Model):
    # country_code = models.ForeignKey(country,on_delete=models.CASCADE)
    # state_code = models.ForeignKey(state,on_delete=models.CASCADE,)
    name =  models.TextField()
    city_code = models.IntegerField()
    phone_code = models.TextField()
    population = models.BigIntegerField()
    avg_age = models.IntegerField()
    num_of_adult_males = models.BigIntegerField()
    num_of_adult_females = models.BigIntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
