from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
import uuid

# Create your models here.

class CustomUser(models.Model):
    username = models.EmailField(unique=True)
    created_at       = models.DateTimeField(auto_now_add=True )
    updated_at       = models.DateTimeField(auto_now_add=True )
    def __str__(self):
        return self.username

# class User(AbstractUser):
#     email = models.EmailField(unique=True)
#     def __str__(self):
#         return self.username

class Country(models.Model):

    #primary columns
    id               = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    name             = models.TextField(max_length=50,unique=True)
    country_code     = models.IntegerField(unique=True)
    curr_symbol      = models.CharField(max_length=15,unique=True)
    phone_code       = models.IntegerField(unique=True)

    #foreignKeys
    my_user          = models.ForeignKey(CustomUser,on_delete=models.CASCADE, default="test1@gmail.com")

    #audit columns
    created_at       = models.DateTimeField(auto_now_add=True)
    updated_at       = models.DateTimeField(auto_now_add=True )

    def __str__(self):
        return self.name

class State(models.Model):

    #primary columns
    id               = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    name             = models.TextField(max_length=50,unique=True)
    state_code       = models.IntegerField(unique=True)
    gst_code         = models.IntegerField(unique=True)

    #foreignKeys
    country_id       = models.ForeignKey(Country,on_delete=models.CASCADE,default=uuid.uuid4)

    #audit columns
    created_at       = models.DateTimeField(auto_now_add=True)
    updated_at       = models.DateTimeField(auto_now_add=True )

    def __str__(self):
        return self.name

class City (models.Model):

    #primary columns
    id                  = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    name                = models.TextField(max_length=50,unique=True)
    city_code           = models.IntegerField(unique=True)
    phone_code          = models.IntegerField(unique=True)
    population          = models.BigIntegerField()
    avg_age             = models.IntegerField()
    num_of_adult_males  = models.BigIntegerField()
    num_of_adult_females= models.BigIntegerField()

    #foreignKeys
    state_id       = models.ForeignKey(State,on_delete=models.CASCADE, default=uuid.uuid4)

    #audit columns
    created_at       = models.DateTimeField(auto_now_add=True)
    updated_at       = models.DateTimeField(auto_now_add=True )

    def __str__(self):
        return self.name
    
class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title