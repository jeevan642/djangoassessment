from django.db import models

# Create your models here.
class country(models.Model):
    id   =  models.UUIDField(primary_key=True,auto_created = True)
    name =  models.TextField()
    country_code = models.IntegerField()
    curr_symbol = models.TextField()
    phone_code = models.IntegerField()

class state(models.Model):
    id   =  models.UUIDField(primary_key=True, auto_created=True)
    name =  models.TextField()
    state_code = models.IntegerField()
    gst_code = models.TextField()
    phone_code = models.IntegerField()

class city(models.Model):
    id   =  models.UUIDField(primary_key=True, auto_created=True)
    name =  models.TextField()
    city_code = models.IntegerField()
    phone_code = models.TextField()
    population = models.BigIntegerField()
    avg_age = models.IntegerField()
    num_of_adult_males = models.BigIntegerField()
    num_of_adult_females = models.BigIntegerField()
