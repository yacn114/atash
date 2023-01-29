from django.contrib import admin
from home.models import SiteInformation
# Register your models here.

class SiteInformationAdmin(admin.ModelAdmin):
    list_display = (['siteNamePersian','siteNameEnglish'])
