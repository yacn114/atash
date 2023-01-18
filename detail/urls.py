from django.urls import path
from .views import hashtag,allHashTags
app_name = "detail"
urlpatterns = [
    path("c/<str:tag>",hashtag),
    path("c/all",allHashTags,name="all"),
]
