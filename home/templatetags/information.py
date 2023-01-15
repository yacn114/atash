from home.models import SiteInformation
from django import template

register = template.Library()

@register.simple_tag
def information(inp):
    if inp == "name":
        return SiteInformation.objects.all()[0].siteNamePersian
    if inp == "nameE":
        return SiteInformation.objects.all()[0].siteNameEnglish
    if inp == "logo":
        return SiteInformation.objects.all()[0].logo