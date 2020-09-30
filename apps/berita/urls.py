from django.urls import path
from . import views

urlpatterns = [
    path('berita/<slug:slug>/', views.Category_Detail, name='Category_Detail'),
    path('berita/<slug:category_slug>/<slug:slug>/', views.Berita_Detail, name='Berita_Detail'),
    # Dashboard
    path('berita/landing', views.qapuas_berita, name='qapuas_berita'),
    # Post
    path('berita/make', views.addBerita, name='addBerita'),
    path('berita/touch=<str:pk>', views.updateBerita, name='updateBerita'),
    path('berita/rm=<str:pk>', views.deleteBerita, name='deleteBerita'),
    # Category
    path('berita/cat/make', views.addCategory, name='addCategory'),
    path('berita/cat/touch=<str:pk>', views.updateCategory, name='updateCategory'),
    path('berita/cat/rm=<str:pk>', views.deleteCategory, name='deleteCategory'),
    # Tags
    path('berita/tag/make', views.addTag, name='addTag'),
    path('berita/tag/touch=<str:pk>', views.updateTag, name='updateTag'),
    path('berita/tag/rm=<str:pk>', views.deleteTag, name='deleteTag'),
]