from .models import Kategori, Profil

def menu_kategori(request):
    kategori = Kategori.objects.all()
    return {'menu_kategori': kategori}

def menu_profil(request):
    profil = Profil.objects.filter(kategori_id='1')
    return {'menu_profil': profil}

def menu_profil_ppid(request):
    menu = Profil.objects.filter(kategori_id='3')
    return {'menu_profil_ppid': menu}