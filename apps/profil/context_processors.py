from .models import Category, Pages

def menu_pages_category(request):
    category_list = Category.objects.all()
    return {'menu_pages_category': category_list}

def menu_pages(request):
    pages_umum = Pages.objects.filter(category_id='1')
    return {'menu_pages_umum': pages_umum}

def menu_pages_ppid(request):
    ppid_list = Pages.objects.filter(category_id='3')
    return {'menu_pages_ppid': ppid_list}