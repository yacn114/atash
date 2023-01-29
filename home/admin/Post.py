from django.contrib import admin
from home.models import Posts
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','published','status')
