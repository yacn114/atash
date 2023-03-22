from django.shortcuts import render
from .models import Posts,Categories
from home.models import SiteInformation
from django.utils import timezone
# Create your views here.
def homePage(request):
    obj = Posts.objects.filter(status=True)
    cattrend = Categories.objects.all()
    timee = timezone.now()
    siteData = SiteInformation.objects.first()

    return render(request, 'home.html',{"obj":obj,"trendhash":cattrend,"timee":timee,"siteData":siteData})