from django.db import models


class Categories(models.Model):
    title = models.CharField(max_length=20,verbose_name="اسم دسته بندی")
    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"
    def __str__(self):
        return self.title
    
