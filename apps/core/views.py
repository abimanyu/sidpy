from django.shortcuts import render
from apps.profil.models import Profil, Kategori
from apps.berita.models import Berita, Category

def frontpage(request):
    list_profil = Profil.objects.all()
    list_kategori = Profil.objects.all()
    list_berita = Berita.objects.filter(is_featured=True)
    list_category = Category.objects.all()
    context = {
        'list_profil': list_profil,
        'list_kategori': list_kategori,
        'List_Berita': list_berita,
        'List_Category': list_category
    }
    return render(request, 'frontpage.html', context)
