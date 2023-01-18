from .views import LoginUser
from django.urls import path
app_name = "account"
urlpatterns = [
    path('login',LoginUser,name="login"),
]
