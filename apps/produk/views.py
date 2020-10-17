from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView

from .models import Item, Category
from .forms import ItemForm, CategoryForm


class ProdukListView(ListView):
    model = Item
    paginate_by = 5
    template_name = "produk/produk_list.html"
    ordering = ['-updated_at']    
    extra_context = {
        'page_title':'Produk',
    }

    def get_context_data(self, *args, **kwargs):
        self.kwargs.update(self.extra_context)
        kwargs = self.kwargs
        return super().get_context_data(*args, **kwargs)


class CategoryListView(ListView):
    model = Item
    paginate_by = 5
    template_name = "produk/by_cat_list.html"
    extra_context = {
        'page_title':'Produk',
    }

    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs.get('slug'))
        return Item.objects.filter(category=category).order_by('-created_at')


class ProdukDetailView(DetailView):
    model = Item
    template_name = "produk/produk_detail.html"


# ___________________________________
# DASHBOARD

@login_required
def qapuas_produk (request):
    produk = Item.objects.all()
    category = Category.objects.all()

    total_item = produk.count()
    total_category = category.count()

    context = {
        'produk': produk,
        'total_item': total_item, 'total_category': total_category
    }
    return render(request, 'produk/qapuas.html', context)

# ___________________________________

@login_required
def addProduk(request):
    form = ItemForm()
    nama_model = 'Tambah Produk Baru'

    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('qapuas_produk')

    context = {'form':form, 'nama_model':nama_model}
    return render(request, 'produk/q_add_modify.html', context)


@login_required
def updateProduk(request, pk):
    produk = Item.objects.get(id=pk)
    form = ItemForm(instance=produk)
    nama_model = 'Update Produk'

    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=produk)
        if form.is_valid():
            form.save()
        return redirect('qapuas_produk')

    context = {'form': form, 'nama_model':nama_model}
    return render(request, 'produk/q_add_modify.html', context)


@login_required
def deleteProduk(request, pk):
    produk = Item.objects.get(id=pk)
    nama_model = 'Delete Produk'

    if request.method == 'POST':
        produk.delete()
        return redirect('qapuas_produk')
    
    context = {'item':produk, 'nama_model':nama_model}
    return render(request, 'produk/q_delete.html', context)

# ___________________________________

@login_required
def addCategory(request):
    form = CategoryForm()
    nama_model = 'Tambah Kategori Produk'

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('qapuas_produk')

    context = {'form':form, 'nama_model':nama_model}
    return render(request, 'produk/q_add_modify.html', context)


@login_required
def updateCategory(request, pk):
    category = Category.objects.get(id=pk)
    form = CategoryForm(instance=category)
    nama_model = 'Update Kategori Produk'

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
        return redirect('qapuas_produk')

    context = {'form': form, 'nama_model':nama_model}
    return render(request, 'produk/q_add_modify.html', context)

@login_required
def deleteCategory(request, pk):
    category = Category.objects.get(id=pk)
    nama_model = 'Hapus Category Produk'

    if request.method == 'POST':
        category.delete()
        return redirect('qapuas_produk')
    
    context = {'item':category, 'nama_model':nama_model}
    return render(request, 'produk/q_delete.html', context)