from rest_framework import serializers
from .models import Blog,City, Country,CustomUser,State

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ["id","title","content","published_date"]


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id","username"]

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        # feilds = ["id","name","country_code","curr_symbol","phone_code"]
        fields = '__all__'

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        # feilds = ["id","name","country_code","curr_symbol","phone_code"]
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        # feilds = ["id","name","country_code","curr_symbol","phone_code"]
        fields = '__all__'