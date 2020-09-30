from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Pages, Category

def pages_detail (request, Category_slug, slug):
    pages = get_object_or_404(Pages, slug=slug)

    context = {
        'pages': pages
    }
    
    return render(request, 'profil/pages_detail.html', context)

def category_detail (request, slug):
    category = get_object_or_404(Category, slug=slug)
    list_pages = Category.objects.all()

    context = {
        'category': category,
        'list_pages': list_pages
    }

    return render(request, 'profil/category_detail.html', context)

# ___________________________________
# DASHBOARD

@login_required
def qapuas_pages (request):
    pages = Pages.objects.all()
    category = Category.objects.all()
    total_pages = pages.count()
    total_category = category.count()

    context = {
        'pages': pages,
        'total_pages': total_pages, 'total_category': total_category
    }
    return render(request, 'profil/qapuas.html', context)
