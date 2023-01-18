from django.shortcuts import render
from .models import Posts,Categories
# Create your views here.
def homePage(request):
    obj = Posts.objects.filter(status=True)
    cattrend = Categories.objects.all()
    return render(request, 'home.html',{"obj":obj,"trendhash":cattrend})