# Generated by Django 2.1.5 on 2019-11-03 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='art_titre',
            field=models.CharField(max_length=100, verbose_name="Titfrom blog_app.models import Imagesre de l'article"),
        ),
    ]
