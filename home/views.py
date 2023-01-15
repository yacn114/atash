from django.shortcuts import render
from .models import Posts
# Create your views here.
def homePage(request):
    obj = Posts.objects.filter(status=True)
    return render(request, 'home.html',{"obj":obj})