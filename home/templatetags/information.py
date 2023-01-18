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
        a = str(SiteInformation.objects.all()[0].logo)
        return "images/"+a
    if inp == "telegram":
        return SiteInformation.objects.all()[0].telegram
    if inp == "phone":
        return SiteInformation.objects.all()[0].phone
    if inp == "email":
        return SiteInformation.objects.all()[0].email