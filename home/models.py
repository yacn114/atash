from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class SiteInformation(models.Model):
    siteNamePersian = models.CharField(max_length=20,verbose_name="اسم سایت فارسی")
    logo = models.ImageField(upload_to='images/logo',verbose_name="لوگو سایت")
    siteNameEnglish = models.CharField(max_length=20,verbose_name="اسم سایت انگلیسی")
    telegram = models.CharField(max_length=15,verbose_name="تلگرام")
    phone = models.CharField(max_length=11,verbose_name="شماره")
    email = models.CharField(max_length=20,verbose_name="ایمیل")
    class Meta:
        verbose_name = 'اطلاعات سایت'
        verbose_name_plural = 'اطلاعات سایت'
    def _str__(self):
        return self.siteNameEnglish
class Categories(models.Model):
    title = models.CharField(max_length=20,verbose_name="اسم دسته بندی")
    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"
    def __str__(self):
        return self.title
    
class Posts(models.Model):
    title = models.CharField(max_length=255)
    caption = models.TextField()
    image = models.ImageField(upload_to="post/")
    updated = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    Categories = models.ManyToManyField(Categories)
    status = models.BooleanField(default=False)
    hot = models.BooleanField(default=False)
    class Meta:
        verbose_name = "پست"
        verbose_name_plural = "پست ها"
    def __str__(self):
        return self.title