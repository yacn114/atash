# Generated by Django 4.1.7 on 2023-03-22 22:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_posts_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='published',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]