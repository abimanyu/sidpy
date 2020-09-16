from django.shortcuts import render, get_object_or_404

from .models import Berita, Category

def Berita_Detail (request, category_slug, slug):
    berita = get_object_or_404(Berita, slug=slug)

    context = {
        'berita': berita
    }

    return render(request, 'berita_detail.html', context)

def Category_Detail (request, slug):
    category = get_object_or_404(Category, slug=slug)
    list_berita = category.all_berita.all()

    context = {
        'Category': category,
        'List_Berita': list_berita
    }

    return render(request, 'category_detail.html', context)

def qapuas_berita (request):
    list_berita = Berita.objects.all()
    context = {
        'list_berita': list_berita
    }
    return render(request, 'qapuas.html', context)