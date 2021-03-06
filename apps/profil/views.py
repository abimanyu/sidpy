from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView

from .models import Pages, Category
from .forms import PagesForm


class CategoryPagesListView(ListView):
    model = Pages
    paginate_by = 10
    template_name = "profil/pages_list.html"
    extra_context = {
        'page_title':'Profil',
    }

    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs.get('slug'))
        return Pages.objects.filter(category=category).order_by('ordering')


class PagesDetailView(DetailView):
    model = Pages
    template_name = "profil/pages_detail.html"


def pages_list_by_category(request,category_id):
    page_list = Pages.objects.filter(category_id='1').order_by('ordering')
    return {'pages_list_by_category': page_list}


def pages_detail (request, category_slug, slug):
    pages = get_object_or_404(Pages, slug=slug)

    context = {
        'pages': pages
    }
    
    return render(request, 'profil/pages_detail.html', context)

def category_detail (request, slug):
    category = get_object_or_404(Category, slug=slug)
    list_pages = category.pages.all() #models.py = related_name

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

# ___________________________________

@login_required
def addPages(request):
    form = PagesForm()
    nama_model = 'Tambah Pages Baru'

    if request.method == 'POST':
        form = PagesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('qapuas_profil')

    context = {'form':form, 'nama_model':nama_model}

    return render(request, 'profil/q_add_modify.html', context)


@login_required
def updatePages(request, pk):
    pages = Pages.objects.get(id=pk)
    form = PagesForm(instance=pages)
    nama_model = 'Update Page'

    if request.method == 'POST':
        form = PagesForm(request.POST, instance=pages)
        if form.is_valid():
            form.save()
        return redirect('qapuas_profil')

    context = {'form': form, 'nama_model':nama_model}

    return render(request, 'profil/q_add_modify.html', context)

@login_required
def deletePages(request, pk):
    pages = Pages.objects.get(id=pk)
    nama_model = 'Delete Pages'

    if request.method == 'POST':
        pages.delete()
        return redirect('qapuas_profil')
    
    context = {'item':pages, 'nama_model':nama_model}
    
    return render(request, 'profil/q_delete.html', context)

# ___________________________________