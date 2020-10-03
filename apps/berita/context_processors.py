from .models import Category

def category_list(request):
    category = Category.objects.all()

    return {'category_list': category}