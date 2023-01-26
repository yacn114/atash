from django.db import models



class SiteInformation(models.Model):
    siteNamePersian = models.CharField("اسم سایت به فارسی",max_length=20)
    logo = models.ImageField("لوگو سایت",upload_to='images/logo')
    siteNameEnglish = models.CharField("اسم سایت انگلیسی",max_length=20)
    telegram = models.CharField("تلگرام",max_length=15)
    phone = models.CharField("شماره",max_length=11)
    email = models.CharField("ایمیل",max_length=20)
    class Meta:
        verbose_name = 'اطلاعات سایت'
        verbose_name_plural = 'اطلاعات سایت'
    def _str__(self):
        return self.siteNameEnglish