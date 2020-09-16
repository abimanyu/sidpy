from django.shortcuts import render, get_object_or_404

from .models import Profil, Kategori

def profil_detail (request, kategori_slug, slug):
    profil = get_object_or_404(Profil, slug=slug)

    context = {
        'profil': profil
    }
    
    return render(request, 'profil_detail.html', context)

def kategori_detail (request, slug):
    kategori = get_object_or_404(Kategori, slug=slug)
    list_profil = kategori.profil_all.all()

    context = {
        'kategori': kategori,
        'list_profil': list_profil
    }

    return render(request, 'kategori_detail.html', context)
