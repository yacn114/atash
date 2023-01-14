from django.urls import path
from .views import homePage
app_name = "home"
urlpatterns = [
    path('',homePage,name="homePage")
]
