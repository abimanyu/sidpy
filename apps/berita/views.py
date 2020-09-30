from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import Berita, Category, Tag
from .forms import BeritaForm, CategoryForm, TagForm

def Berita_Detail (request, category_slug, slug):
    berita = get_object_or_404(Berita, slug=slug)

    context = {
        'berita': berita
    }

    return render(request, 'berita/berita_detail.html', context)

def Category_Detail (request, slug):
    category = get_object_or_404(Category, slug=slug)
    list_berita = category.all_berita.all()

    context = {
        'Category': category,
        'List_Berita': list_berita
    }

    return render(request, 'berita/category_detail.html', context)

# ___________________________________
# DASHBOARD

@login_required
def qapuas_berita (request):
    berita = Berita.objects.all()
    category = Category.objects.all()
    tag = Tag.objects.all()

    total_berita = berita.count()
    total_category = category.count()
    total_tag = tag.count()



    context = {
        'berita': berita,
        'total_berita': total_berita, 'total_category': total_category, 'total_tag': total_tag
    }
    return render(request, 'berita/qapuas.html', context)

# ___________________________________

@login_required
def addBerita(request):
    form = BeritaForm()
    nama_model = 'Tambah Berita Baru'

    if request.method == 'POST':
        form = BeritaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('qapuas_berita')

    context = {'form':form, 'nama_model':nama_model}
    return render(request, 'berita/q_add_modify.html', context)


@login_required
def updateBerita(request, pk):
    berita = Berita.objects.get(id=pk)
    form = BeritaForm(instance=berita)
    nama_model = 'Update Berita'

    if request.method == 'POST':
        form = BeritaForm(request.POST, request.FILES, instance=berita)
        if form.is_valid():
            form.save()
        return redirect('qapuas_berita')

    context = {'form': form, 'nama_model':nama_model}
    return render(request, 'berita/q_add_modify.html', context)


@login_required
def deleteBerita(request, pk):
    berita = Berita.objects.get(id=pk)
    nama_model = 'Delete Berita'

    if request.method == 'POST':
        berita.delete()
        return redirect('qapuas_berita')
    
    context = {'item':berita, 'nama_model':nama_model}
    return render(request, 'berita/q_delete.html', context)

# ___________________________________

@login_required
def addCategory(request):
    form = CategoryForm()
    nama_model = 'Tambah Kategori Berita'

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('qapuas_berita')

    context = {'form':form, 'nama_model':nama_model}
    return render(request, 'berita/q_add_modify.html', context)


@login_required
def updateCategory(request, pk):
    category = Category.objects.get(id=pk)
    form = CategoryForm(instance=category)
    nama_model = 'Update Kategori Berita'

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
        return redirect('qapuas_berita')

    context = {'form': form, 'nama_model':nama_model}
    return render(request, 'berita/q_add_modify.html', context)


@login_required
def deleteCategory(request, pk):
    category = Category.objects.get(id=pk)
    nama_model = 'Hapus Category Berita'

    if request.method == 'POST':
        category.delete()
        return redirect('qapuas_berita')
    
    context = {'item':category, 'nama_model':nama_model}
    return render(request, 'berita/q_delete.html', context)

# ___________________________________

@login_required
def addTag(request):
    form = TagForm()
    nama_model = 'Tambah Tag Berita'

    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('qapuas_berita')

    context = {'form':form, 'nama_model':nama_model}
    return render(request, 'berita/q_add_modify.html', context)


@login_required
def updateTag(request, pk):
    tag = Tag.objects.get(id=pk)
    form = TagForm(instance=tag)
    nama_model = 'Update Tag Berita'

    if request.method == 'POST':
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
        return redirect('qapuas_berita')

    context = {'form': form, 'nama_model':nama_model}
    return render(request, 'berita/q_add_modify.html', context)


@login_required
def deleteTag(request, pk):
    tag = Tag.objects.get(id=pk)
    nama_model = 'Hapus Tag Berita'

    if request.method == 'POST':
        tag.delete()
        return redirect('qapuas_berita')
    
    context = {'item':tag, 'nama_model':nama_model}
    return render(request, 'berita/q_delete.html', context)