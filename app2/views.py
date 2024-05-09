from django.shortcuts import render
from rest_framework import generics
from .models import Blog,CustomUser,City,Country,State
from .serializers import BlogSerializer,CountrySerializer,CustomUserSerializer,StateSerializer,CitySerializer
# Create your views here.

class BlogListCreate(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class CustomUserListCreate(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class CountryListCreate(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class StateListCreate(generics.ListCreateAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer

class CityListCreate(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer