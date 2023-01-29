from django.contrib import admin
from .category import CategoryAdmin
from .Post import PostAdmin
from .site import SiteInformationAdmin
from home.models import Categories
from home.models import Posts
from home.models import SiteInformation
admin.site.register(Posts,PostAdmin)
admin.site.register(Categories,CategoryAdmin)
admin.site.register(SiteInformation,SiteInformationAdmin)
