from django.urls import path
from django.views.generic import ListView, DetailView
from . import views

urlpatterns = [
    path('produk/', views.ProdukListView.as_view(), name='produk_list'),
    path('produk/<slug:slug>/', views.CategoryListView.as_view(), name='produk_by_cat_list'),
    path('produk/<slug:category_slug>/<slug:slug>/', views.ProdukDetailView.as_view(), name='Produk_Detail'),

    # Dashboard
    path('produk/landing', views.qapuas_produk, name='qapuas_produk'),

        # Post
    path('produk/make', views.addProduk, name='addProduk'),
    path('produk/touch:<str:pk>', views.updateProduk, name='updateProduk'),
    path('produk/rm:<str:pk>', views.deleteProduk, name='deleteProduk'),

        # Category
    path('produk/cat/make', views.addCategory, name='addCategory_produk'),
    path('produk/cat/touch=<str:pk>', views.updateCategory, name='updateCategory_produk'),
    path('produk/cat/rm=<str:pk>', views.deleteCategory, name='deleteCategory_produk'),
]