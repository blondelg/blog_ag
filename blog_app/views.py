from django.http import HttpResponse
from django.shortcuts import render
import datetime
from blog_app.models import Article
from blog_app.models import Images
from blog_app.models import Video
from django.db.models import Q
from django.core.paginator import Paginator

def videos(request):
    """ Display videos """

    # Load videos
    vid_grid = []
    row = []
    for vid in Video.objects.order_by('-vid_date'):
        row.append(str(vid.vid_link))
        if len(row) == 2:
            vid_grid.append(row)
            row = []
    if len(row) < 2 and len(row) > 0:
        vid_grid.append(row)

    # return render(request, 'accueil.html', {'derniers_articles': articles})
    return render(request, 'videos.html',{'vid_grid': vid_grid})


def images(request, art_id = -1):
    """ Display an image grid """

    # Load images

    ima_count = 1
    ima_grid = []
    row = []
    if art_id == -1:
        image_set = Images.objects.filter(ima_masquer=False).order_by('-ima_date')
        titre_page = "Toutes les images"
        url_retour = "/"
    else:
        article = Article.objects.get(id=art_id)
        image_set = Images.objects.filter(Q(ima_art_titre=article) & Q(ima_masquer=False)).order_by('-ima_date')
        titre_page = article.art_titre + " - Images"
        url_retour = "/article/" + str(art_id)

    for im in image_set:
        temp = []
        temp.append("photos/mini/" + str(im.ima_image).split("/")[-1])
        temp.append("photos/" + str(im.ima_image).split("/")[-1])
        temp.append(str(ima_count))
        temp.append(im.ima_description)

        ima_count += 1

        row.append(temp)
        if len(row) == 4:
            ima_grid.append(row)
            row = []
    if len(row) < 4 and len(row) > 0:
        ima_grid.append(row)

    return render(request, 'images.html',{'ima_grid': ima_grid, 'article_titre': titre_page, 'url_retour': url_retour})



def accueil(request):
    """ Display map, article list, video list and photos list """
    # articles = Article.objects.filter(art_masquer=False).order_by('-art_date')

    # Load articles
    art_grid = []
    row = []
    for art in Article.objects.filter(art_masquer=False).order_by('-art_date'):
        temp = []
        temp.append(art.art_titre)
        temp.append("photos/mini/" + str(art.art_ima_presentation).split("/")[-1])
        temp.append(str(art.art_ima_presentation))
        temp.append(art.id)
        row.append(temp)
        if len(row) == 4:
            art_grid.append(row)
            row = []
    if len(row) < 4 and len(row) > 0:
        art_grid.append(row)

    # Load videos
    vid_grid = []
    row = []
    for vid in Video.objects.order_by('-vid_date'):
        row.append(str(vid.vid_link))
        if len(row) == 2:
            vid_grid.append(row)
            row = []
    if len(row) < 2 and len(row) > 0:
        vid_grid.append(row)

    # Only select 2 first videos
    vid_grid = vid_grid[0:1]

    # Load images
    ima_count = 1
    ima_grid = []
    row = []

    # select 40 random images
    for im in Images.objects.filter(ima_masquer=False).order_by('?')[:20]:
        temp = []
        temp.append("photos/mini/" + str(im.ima_image).split("/")[-1])
        temp.append("photos/" + str(im.ima_image).split("/")[-1])
        temp.append(str(ima_count))
        temp.append(im.ima_description)

        ima_count += 1

        row.append(temp)
        if len(row) == 4:
            ima_grid.append(row)
            row = []
    if len(row) < 4 and len(row) > 0:
        ima_grid.append(row)

    # return render(request, 'accueil.html', {'derniers_articles': articles})
    return render(request, 'accueil.html',{'art_grid': art_grid, 'vid_grid': vid_grid, 'ima_grid': ima_grid, 'article': 'Toutes les photos'})


def lire(request, id):
    """ Display a specific article and content attached """

    # Load article
    article = Article.objects.get(id=id)

    # Load images
    ima_count = 1
    ima_grid = []
    row = []
    for im in Images.objects.filter(Q(ima_art_titre=article) & Q(ima_masquer=False)).order_by('?')[:20]:
        temp = []
        temp.append("photos/mini/" + str(im.ima_image).split("/")[-1])
        temp.append("photos/" + str(im.ima_image).split("/")[-1])
        temp.append(str(ima_count))
        temp.append(im.ima_description)

        ima_count += 1

        row.append(temp)
        if len(row) == 4:
            ima_grid.append(row)
            row = []
    if len(row) < 4 and len(row) > 0:
        ima_grid.append(row)

    return render(request, 'lire.html', {'ima_grid': ima_grid, 'article': article})

def display_image(request, image_id):
    """ Display a selected image """

    return render(request, 'display_image.html', {})
