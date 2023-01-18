# Generated by Django 4.1.5 on 2023-01-18 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_posts_hot_alter_categories_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteinformation',
            name='email',
            field=models.CharField(default=None, max_length=20, verbose_name='ایمیل'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='siteinformation',
            name='phone',
            field=models.CharField(default=None, max_length=11, verbose_name='شماره'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='siteinformation',
            name='telegram',
            field=models.CharField(default=None, max_length=15, verbose_name='تلگرام'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='siteinformation',
            name='siteNameEnglish',
            field=models.CharField(max_length=20, verbose_name='اسم سایت انگلیسی'),
        ),
        migrations.AlterField(
            model_name='siteinformation',
            name='siteNamePersian',
            field=models.CharField(max_length=20, verbose_name='اسم سایت فارسی'),
        ),
    ]