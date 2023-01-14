from django.contrib import admin
from .models import SiteInformation,Posts,Categories
# Register your models here.
@admin.register(SiteInformation)
class SiteInformationAdmin(admin.ModelAdmin):
    list_display = (['siteNamePersian','siteNameEnglish'])
@admin.register(Posts)
class SiteInformationAdmin(admin.ModelAdmin):
    list_display = ('title','published','status')
@admin.register(Categories)
class SiteInformationAdmin(admin.ModelAdmin):
    list_display = (['title'])
def joincategory(Posts):
    
    