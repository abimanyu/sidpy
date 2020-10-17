from django.urls import path
from django.views.generic import ListView, DetailView
from . import views

urlpatterns = [
    path('berita/', views.BeritaListView.as_view(), name='berita_list'),
    path('berita/<slug:slug>/', views.CategoryListView.as_view(), name='by_cat_list'),
    path('berita/by:<username>', views.UserListView.as_view(paginate_by=5), name='by_user_list'),
    path('berita/<slug:category_slug>/<slug:slug>/', views.BeritaDetailView.as_view(), name='Berita_Detail'),
    #path('berita/<slug:slug>', views.Berita_Detail, name='Category_Detail'),
    #path('berita/<slug:category_slug>/<slug:slug>', views.Berita_Detail, name='Berita_Detailvv'),
    # Dashboard
    path('berita/landing', views.qapuas_berita, name='qapuas_berita'),
        # Post
    path('berita/make', views.addBerita, name='addBerita'),
    path('berita/touch:<str:pk>', views.updateBerita, name='updateBerita'),
    path('berita/rm:<str:pk>', views.deleteBerita, name='deleteBerita'),
        # Category
    path('berita/cat/make', views.addCategory, name='addCategory'),
    path('berita/cat/touch=<str:pk>', views.updateCategory, name='updateCategory'),
    path('berita/cat/rm=<str:pk>', views.deleteCategory, name='deleteCategory'),
        # Tags
    path('berita/tag/make', views.addTag, name='addTag'),
    path('berita/tag/touch:<str:pk>', views.updateTag, name='updateTag'),
    path('berita/tag/rm:<str:pk>', views.deleteTag, name='deleteTag'),
]