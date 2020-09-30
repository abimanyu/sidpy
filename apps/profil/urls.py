from django.urls import path
from . import views

urlpatterns = [
    path('p/<slug:slug>/', views.category_detail, name='category_detail'),
    path('p/<slug:category_slug>/<slug:slug>/', views.pages_detail, name='pages_detail'),
    # Dashboard
    path('p/landing', views.qapuas_pages, name='qapuas_profil'),
]