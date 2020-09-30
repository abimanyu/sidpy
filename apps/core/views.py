from django.shortcuts import render
from apps.profil.models import Pages, Category as Pages_Category
from apps.berita.models import Berita, Category
from apps.qapuas.models import site_conf

def frontpage(request):
    list_pages = Pages.objects.all()
    list_pages_category = Pages_Category.objects.all()
    list_berita = Berita.objects.filter(featured=True)
    list_category = Category.objects.all()
    list_frontlink = site_conf.objects.filter(conf='frontlink')
    context = {
        'list_pages': list_pages,
        'list_pages_category': list_pages_category,
        'List_Berita': list_berita,
        'List_Category': list_category,
        'conf_frontlink': list_frontlink
    }
    return render(request, 'frontpage.html', context)

