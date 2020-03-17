from django.contrib import admin
from .models import Article, Images, Video

# view of modes into django admin menu
class VideoAdmin(admin.ModelAdmin):
    list_display = ('vid_titre', 'vid_link', 'vid_date')

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('art_titre', 'art_auteur','art_date','art_masquer','art_ima_presentation')

class ImagesAdmin(admin.ModelAdmin):
    list_display = ('ima_art_titre','ima_masquer','ima_description','ima_image','id')
    list_filter = ('ima_art_titre',)
    search_fields = ('ima_description',)

# Register your models here.
admin.site.register(Video,VideoAdmin)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Images,ImagesAdmin)
