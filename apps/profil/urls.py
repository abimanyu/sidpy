from django.urls import path
# sitemap : https://github.com/agusmakmun/python.web.id/blob/master/app_blog/urls.py
from apps.profil.views import profil_detail, kategori_detail

urlpatterns = [
    path('p/<slug:slug>/', kategori_detail, name='kategori_detail'),
    path('p/<slug:kategori_slug>/<slug:slug>/', profil_detail, name='profil_detail'),
]