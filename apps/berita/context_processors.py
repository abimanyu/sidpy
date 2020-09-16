from .models import Category

def menu_category(request):
    category = Category.objects.all()

    return {'menu_category': category}