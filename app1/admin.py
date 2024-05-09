from django.contrib import admin

# Register your models here.
from .models import city, state, country

admin.site.register(city)
admin.site.register(state)
admin.site.register(country)