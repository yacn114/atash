from django.contrib import admin
from home.models import SiteInformation,Posts,Categories
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = (['title'])
