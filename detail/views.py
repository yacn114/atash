from django.shortcuts import render
from home.models import Categories,Posts
# Create your views here.

def hashtag(request,tag):
   obj = Posts.objects.filter(Categories__title=tag)
   return render(request, 'home.html',{"obj":obj})
def allHashTags(request):
    pass
def detailPage(request,title):
   obj = Posts.objects.get(title=title)
   return render(request,"detailTemplates.html",{"obj":obj})