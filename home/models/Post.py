from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from .Category import Categories
class Posts(models.Model):
    title = models.CharField(max_length=255)
    caption = models.TextField()
    image = models.ImageField(upload_to="post/")
    updated = models.DateTimeField(auto_now=True)
    published = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    Categories = models.ManyToManyField(Categories)
    status = models.BooleanField(default=False)
    hot = models.BooleanField(default=False)
    class Meta:
        verbose_name = "پست"
        verbose_name_plural = "پست ها"
    def __str__(self):
        return self.title
    @property
    def tpublished(self):
        return self.published