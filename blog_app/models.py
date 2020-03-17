from django.db import models
from django.utils import timezone
from django.db.models import Q
from django.core.files.base import ContentFile
from time import sleep

class Video(models.Model):
    vid_titre = models.CharField(max_length=30,verbose_name="Titre de la video")
    vid_desc = models.CharField(max_length=200,verbose_name="Description de la video")
    vid_link = models.CharField(max_length=100,verbose_name="Lien de la video")
    vid_date = models.DateTimeField(default=timezone.now, verbose_name="Date de la video")

    class Meta:
        verbose_name = "video"
        ordering = ['vid_date']

    def __str__(self):

        return self.vid_titre


class Article(models.Model):
    art_titre = models.CharField(max_length=100,verbose_name="Titre de l'article")
    art_auteur = models.CharField(max_length=42,verbose_name="Auteur de l'article")
    art_contenu = models.TextField(null=True,verbose_name="Contenu de l'article")
    art_date = models.DateTimeField(default=timezone.now, verbose_name="Date de parution")
    art_masquer = models.BooleanField(default=True, verbose_name="Article masqué")
    art_ima_presentation = models.ImageField(upload_to="photos/raw", null=True,verbose_name="Image presentation")

    class Meta:
        verbose_name = "article"
        ordering = ['art_date']

    def __str__(self):


        return self.art_titre


class Images(models.Model):
    ima_art_titre = models.ForeignKey('Article', on_delete=models.SET_NULL, blank=True, null=True,verbose_name="Titre de l'article associé à l'image")
    ima_date = models.DateTimeField(default=timezone.now, verbose_name="Date d'upload")
    ima_masquer = models.BooleanField(default=True, verbose_name="Image masquée")
    ima_image = models.ImageField(upload_to="photos/raw", null=True,verbose_name="Image")
    ima_description = models.CharField(max_length=100,verbose_name="description de l'image")

    class Meta:
        verbose_name = "images"
        ordering = ['-ima_date']

    def __str__(self):


        return self.ima_image.name
