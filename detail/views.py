from django.shortcuts import render
from home.models import Categories,Posts
from django.utils import timezone
# Create your views here.

def hashtag(request,tag):
   cattrend = Categories.objects.all()
   timee = timezone.now()
   obj = Posts.objects.filter(Categories__title=tag)
   return render(request, 'home.html',{"obj":obj,"trendhash":cattrend,"timee":timee})
def allHashTags(request):
    pass
def detailPage(request,title):

   obj = Posts.objects.get(title=title)

   return render(request,"detailTemplates.html",{"obj":obj})