from django.urls import path
from . import views

urlpatterns =[
    path("blog",views.BlogListCreate.as_view(),name="blog"),
    path("user",views.CustomUserListCreate.as_view(),name="user"),
    path("country",views.CountryListCreate.as_view(),name="country"),
    path("state",views.StateListCreate.as_view(),name="state"),
    path("city",views.CityListCreate.as_view(),name="state")
]