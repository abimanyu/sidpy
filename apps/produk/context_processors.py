from .models import Category

def category_list_produk(request):
    category = Category.objects.all()

    return {'category_list_produk': category}