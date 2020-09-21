from django.shortcuts import render
from apps.profil.models import Profil, Kategori
from apps.berita.models import Berita, Category
from apps.qapuas.models import site_conf

def frontpage(request):
    list_profil = Profil.objects.all()
    list_kategori = Profil.objects.all()
    list_berita = Berita.objects.filter(is_featured=True)
    list_category = Category.objects.all()
    list_frontlink = site_conf.objects.filter(conf='frontlink')
    context = {
        'list_profil': list_profil,
        'list_kategori': list_kategori,
        'List_Berita': list_berita,
        'List_Category': list_category,
        'conf_frontlink': list_frontlink
    }
    return render(request, 'frontpage.html', context)

